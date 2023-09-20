from myfpdf import MyFPDF
from constants import *
import config

def generate_from_config(conf, output_file_name):

	pdf = MyFPDF()
	pdf.add_page()
	pdf.set_margin(MARGIN)
	pdf.add_font(family="body", fname="assets/Times New Roman.ttf")
	pdf.add_font(family="body bold", fname="assets/Times New Roman Bold.ttf")
	pdf.add_font(family="body italic", fname="assets/Times New Roman Italic.ttf")
	pdf.add_font(family="body bold italic", fname="assets/Times New Roman Bold Italic.ttf")

	# TITLE

	pdf.current_y += 15
	pdf.set_font("body", size=30)
	width = pdf.get_string_width("Advay Ratan")
	pdf.text(PAGE_WIDTH / 2, txt="Advay Ratan", align=0)
	pdf.current_y += 8


	pdf.set_font("body italic", size=15)
	pdf.text(PAGE_WIDTH / 2, txt=conf.SUMMARY, align=0)
	pdf.current_y += 8

	# CONTACT INFO
	pdf.set_font("body", size=10)
	widths = [pdf.get_string_width(ci) for ci in conf.CONTACT_INFO]
	gaps = (PAGE_WIDTH - (MARGIN - 2) * 2 - sum(widths)) / (len(conf.CONTACT_INFO) - 1)
	for i, ci in enumerate(conf.CONTACT_INFO):
		pdf.text(MARGIN - 2 + gaps * i + sum(widths[:i]), txt=ci, link=("." in ci))
	pdf.set_font_size(BODY_FONT_SIZE)

	# EDUCATION
	pdf.current_y += BODY_LINE_HEIGHT
	pdf.section_title("EDUCATION")

	coursework_s = ", ".join(conf.COURSEWORK)
	pdf.content(
		body=f"*University of California, Berkeley*\nB.S. in Electrical Engineering and Computer Science\n*Relevant Coursework:* {coursework_s}", 
		meta=f"*Aug 2022 - {conf.GRAD_TERM}*\nBerkeley, CA\nGPA: {conf.GPA}", 
	)

	# SKILLS
	pdf.section_title("SKILLS")


	cont = ""
	for k, l in conf.SKILLS.items():
		s = ", ".join(l)
		cont += f"*{k}*: {s}; "

	pdf.content(
		body=cont[:-2] + ".",
		)

	# projects
	pdf.section_title("HIGHLIGHTED PROJECTS & EXPERIENCE")

	for p in conf.PROJ_EXP:
		pdf.exp_content(**p)

	# leadership
	pdf.section_title("LEADERSHIP & EXTRACURRICULAR ACTIVITIES")

	for e in conf.EC:
		pdf.exp_content(**e)

	pdf.output(output_file_name)

if __name__ == "__main__":
	generate_from_config(config.BaseConfig, "AdvayRatanResume.pdf")