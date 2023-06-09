from fpdf import FPDF
from constants import *

class MyFPDF(FPDF):

	current_y = 0

	def _parse_complex_string(self, s, max_width=TEXT_SPACE):
		'''
		Can take in * (bold), _ (italic), • (indentation) and \n for newlines
		Returns (work order list
		 - 0 indicates newline
		 - 1.0 indicates start bold text
		 - 1.1 indicates end bold text
		 - 2.0 indicates start italic text
		 - 2.1 indicates end italic text
		 - 3.0 indicates starts indentation
		, lengh of each line)
		'''
		work_order = []
		curr_s = ""
		curr_line = ""
		bolded = ""
		italicized = ""
		indented = False
		line_lengths = []
		for i in range(len(s)):
			c = s[i]
			if c == "\n":
				work_order.append(curr_s)
				work_order.append(0)
				line_lengths.append(self.get_string_width(curr_line))
				if indented:
					curr_line = BULLET_STR
					work_order.append(curr_line)
				else:
					curr_line = ""
				curr_s = ""
			elif c == "*" and (i == 0 or s[i - 1] != "\\"):
				work_order.append(curr_s)
				curr_s = ""
				if bolded == "":
					work_order.append(1.0)
					bolded = " bold"
				else:
					work_order.append(1.1)
					bolded = ""
				self.set_font(f"body{bolded}{italicized}")
			elif c == "_" and (i == 0 or s[i - 1] != "\\"):
				work_order.append(curr_s)
				curr_s = ""
				if italicized == "":
					work_order.append(2.0)
					italicized = " italic"
				else:
					work_order.append(2.1)
					italicized = ""
				self.set_font(f"body{bolded}{italicized}")
			elif c == "•" and (i == 0 or s[i - 1] != "\\"):
				if len(work_order) == 0 or (work_order[len(work_order) - 1] != 0 and not indented):
					raise "Invalid indentation start. Indentation starts must follow a newline"
				if indented:
					indented = False
					# work_order.append(3.1)
				else:
					indented = True
					# work_order.append(3.0)
					work_order.append(BULLET_STR)
					curr_line = BULLET_STR
			elif self.get_string_width(curr_line) >= max_width:
				last_space = curr_line.rfind(" ")
				curr_s_ind = last_space - len(curr_line)
				if last_space != -1 and curr_s_ind != -1:
					if -curr_s_ind > len(curr_s):
						# last space occurred in last s

						# go into history of curr_s in work order to figure out new break
						wo_pos = len(work_order)
						ssum = 0
						while ssum < -curr_s_ind:
							wo_pos -= 1
							if type(work_order[wo_pos]) == str:
								ssum += len(work_order[wo_pos])

						# now the last_space being referenced is somewhere inside work_order[wo_pos]
						curr_s_ind += ssum - len(work_order[wo_pos])
						first_part = work_order[wo_pos][:curr_s_ind]
						second_part = work_order[wo_pos][curr_s_ind + 1:]

						# new order: first, new_line (where space was), second
						work_order[wo_pos] = first_part
						if indented:
							second_part = BULLET_GAP + second_part
						work_order.insert(wo_pos + 1, second_part)
						work_order.insert(wo_pos + 1, 0)

						# curr line is everything moved after new new_line
						curr_line = "".join([item for item in work_order[wo_pos + 2:] if type(item) == str])
						if indented:
							curr_line = BULLET_GAP + curr_line
						# but everything in curr_line has been handled (already in work_order)
						curr_s = c
					else:
						work_order.append(curr_s[:curr_s_ind])
						line_lengths.append(self.get_string_width(curr_line[:last_space]))
						work_order.append(0)
						curr_s = curr_s[curr_s_ind + 1:] + c
						curr_line = curr_line[last_space + 1:] + c
						if indented:
							curr_line = BULLET_GAP + curr_line
							work_order.append(BULLET_GAP)
				else:
					if c == " ":
						c = "" # don't start newline with space
					work_order.append(curr_s)
					line_lengths.append(self.get_string_width(curr_line))
					work_order.append(0)
					curr_s = c
					curr_line = c
					if indented:
						curr_line = BULLET_GAP + curr_line
						work_order.append(BULLET_GAP)
			else:
				curr_s += c
				curr_line += c
		line_lengths.append(self.get_string_width(curr_line))
		work_order.append(curr_s)
		return (work_order, line_lengths)
				



	def text(self, x, txt="EMPTY", adjust_y=False, line_height=BODY_LINE_HEIGHT, align=-1, max_width=TEXT_SPACE):
		'''
		cannot center align partly bolded text
		'''
		tmp_y = self.current_y
		work_order, line_lengths = self._parse_complex_string(txt, max_width=max_width)
		curr_x = x
		curr_line = 0
		bolded = ""
		italicized = ""
		if align == 1:
			curr_x -= line_lengths[curr_line]
		for t in work_order: 
			if t == 0:
				curr_x = x
				curr_line += 1
				if align == 1 and curr_line < len(line_lengths):
					curr_x -= line_lengths[curr_line]
				if adjust_y:
					self.current_y += line_height
				tmp_y += line_height
			elif t == 1.0:
				bolded = " bold"
				self.set_font(f"body{bolded}{italicized}")
			elif t == 1.1:
				bolded = ""
				self.set_font(f"body{bolded}{italicized}")
			elif t == 2.0:
				italicized = " italic"
				self.set_font(f"body{bolded}{italicized}")
			elif t == 2.1:
				italicized = ""
				self.set_font(f"body{bolded}{italicized}")
			else:
				w = self.get_string_width(t)
				if align == 1:
					FPDF.text(self, curr_x, tmp_y, txt=t)
				elif align == 0:
					FPDF.text(self, curr_x - w / 2, tmp_y, txt=t)
				else:
					FPDF.text(self, curr_x, tmp_y, txt=t)
				curr_x += w
		return max(line_lengths)
	
	def draw_seperator(self):
		self.current_y += BODY_LINE_HEIGHT / 2
		self.line(MARGIN - 2, self.current_y, PAGE_WIDTH - MARGIN + 2, self.current_y)
		self.current_y += BODY_LINE_HEIGHT

	def section_title(self, text):
		self.set_font("body bold")
		self.current_y += BODY_LINE_HEIGHT / 2
		self.text(MARGIN, txt=text)
		self.draw_seperator()

	def content(self, body="", meta=""):
		
		self.set_font_size(BODY_FONT_SIZE)
		right_width = self.text(PAGE_WIDTH - MARGIN, txt=meta, align=1)
		self.text(MARGIN, adjust_y=True, max_width=TEXT_SPACE-right_width, txt=body)

		self.current_y += BODY_LINE_HEIGHT

	def exp_content(self, position="", company="", bullets=[], dates="", location=""):
		if company == "":
			body = f"*_{position}_*\n•"
		else:
			body = f"*_{position}_ | {company}*\n•"
		body += "\n".join(bullets) + "•"
		meta = f"*{dates}*\n{location}" 
		self.content(body=body, meta=meta)
		self.current_y += BODY_LINE_HEIGHT / 4


if __name__ == "__main__":
	pdf = MyFPDF()
	pdf.add_page()
	pdf.set_margin(MARGIN)
	pdf.current_y += 100
	pdf.add_font(family="body", fname="assets/Times New Roman.ttf")
	pdf.add_font(family="body bold", fname="assets/Times New Roman Bold.ttf")
	pdf.add_font(family="body italic", fname="assets/Times New Roman Italic.ttf")
	pdf.add_font(family="body bold italic", fname="assets/Times New Roman Bold Italic.ttf")
	pdf.set_font("body", size=10)
	pdf.content(body="*Languages*: Python, Java, C, C++, Javascript, PHP, MATLAB; *Web Development*: HTML/CSS, JQuery, React, Webpack, Django, Ruby on Rails; *App Development*: Flutter/Dart; *Game Development*: HTML5 Canvas, Unity; *Competive Programming*: USACO Gold; *Software Engineering*: Git, Jira, GitHub, GitLab;")
	pdf.output("test.pdf")
