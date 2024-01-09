from fpdf import FPDF
import constants

class MyFPDF(FPDF):

	current_y = 0 # y_counter to append to bottom
	line_count = 0 # total # of 'lines', used to scale total length of resume

	def change_y(self, amount):
		self.current_y += amount
		self.line_count += amount / constants.BODY_LINE_HEIGHT

	def _parse_complex_string(self, s, max_width=constants.TEXT_SPACE):
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
					curr_line = constants.BULLET_STR
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
					work_order.append(constants.BULLET_STR)
					curr_line = constants.BULLET_STR
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
							second_part = constants.BULLET_GAP + second_part
						work_order.insert(wo_pos + 1, second_part)
						work_order.insert(wo_pos + 1, 0)

						# curr line is everything moved after new new_line
						curr_line = "".join([item for item in work_order[wo_pos + 2:] if type(item) == str])
						if indented:
							curr_line = constants.BULLET_GAP + curr_line
						# but everything in curr_line has been handled (already in work_order)
						curr_s = c
					else:
						work_order.append(curr_s[:curr_s_ind])
						line_lengths.append(self.get_string_width(curr_line[:last_space]))
						work_order.append(0)
						curr_s = curr_s[curr_s_ind + 1:] + c
						curr_line = curr_line[last_space + 1:] + c
						if indented:
							curr_line = constants.BULLET_GAP + curr_line
							work_order.append(constants.BULLET_GAP)
				else:
					if c == " ":
						c = "" # don't start newline with space
					work_order.append(curr_s)
					line_lengths.append(self.get_string_width(curr_line))
					work_order.append(0)
					curr_s = c
					curr_line = c
					if indented:
						curr_line = constants.BULLET_GAP + curr_line
						work_order.append(constants.BULLET_GAP)
			else:
				curr_s += c
				curr_line += c
		line_lengths.append(self.get_string_width(curr_line))
		work_order.append(curr_s)
		return (work_order, line_lengths)
				



	def text(self, x, txt="EMPTY", adjust_y=False, line_height=None, align=-1, max_width=constants.TEXT_SPACE, link=False):
		'''
		cannot center align partly bolded text
		'''
		line_height = line_height or constants.BODY_LINE_HEIGHT
		start_y = self.current_y
		tmp_y = self.current_y
		work_order, line_lengths = self._parse_complex_string(txt, max_width=max_width)
		curr_x = x
		curr_line = 0
		bolded = ""
		italicized = ""
		if align == 1:
			curr_x -= line_lengths[curr_line]
		if link:
			FPDF.set_font(self, style="U")
		else:
			FPDF.set_font(self, style="")
		for t in work_order: 
			if t == 0:
				curr_x = x
				curr_line += 1
				if align == 1 and curr_line < len(line_lengths):
					curr_x -= line_lengths[curr_line]
				if adjust_y:
					self.change_y(line_height)
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

		if link:
			FPDF.link(self, x, start_y, max(line_lengths), tmp_y - start_y, link=txt)
			FPDF.set_text_color(self, 0, 0, 0)

		return max(line_lengths)
	
	def draw_seperator(self, space_after=True):
		'''
		long black line from left to right margin
		'''
		self.change_y(constants.BODY_LINE_HEIGHT / 2)
		self.line(constants.MARGIN - 2, self.current_y, constants.PAGE_WIDTH - constants.MARGIN + 2, self.current_y)
		self.change_y(constants.BODY_LINE_HEIGHT if space_after else 0)

	def section_title(self, text):
		'''
		Eg. WORK EXPERIENCE with seperator underneath
		'''
		self.set_font("body bold")
		self.change_y(constants.BODY_LINE_HEIGHT / 2)
		self.text(constants.MARGIN, txt=text)
		self.draw_seperator()

	def content(self, body="", meta="", right_space=0):
		'''
		fill in body with margins in mind 
		'''
		self.set_font("body")
		self.set_font_size(constants.BODY_FONT_SIZE)
		right_width = self.text(constants.PAGE_WIDTH - constants.MARGIN, txt=meta, align=1)
		self.text(constants.MARGIN, adjust_y=True, max_width=(constants.TEXT_SPACE-right_width if right_space == 0 else constants.TEXT_SPACE-right_space), txt=body)

		self.change_y(constants.BODY_LINE_HEIGHT)

	def exp_content(self, **kw):
		'''
		takes an experience object and adapts it to be used with content function
		'''
		if not kw.get("company"):
			body = f"*_{kw['position']}_*\n•"
		else:
			body = f"*_{kw['position']}_ | {kw['company']}*\n•"
		body += "\n".join(kw['bullets']) + "•"
		meta = f"{kw.get('dates', '')}\n{kw.get('location', '')}" 
		self.content(body=body, meta=meta, right_space=constants.TEXT_SPACE / 5.8)
		self.change_y(constants.BODY_LINE_HEIGHT / 4)

	def post_gen_height_analysis(self):
		'''
		Detect overflows or too short
		return -1 = overflow
		return 0 = just right
		return >0 = new body line height to make fill just right
		'''
		if self.current_y >= constants.PAGE_HEIGHT:
			return -1
		elif self.current_y >= constants.PAGE_HEIGHT * constants.MINIMUM_FILL_FACTOR:
			return 0
		else:
			return (constants.PAGE_HEIGHT * constants.MINIMUM_FILL_FACTOR - self.current_y) / self.line_count + constants.BODY_LINE_HEIGHT


