from copy import deepcopy as dc
from config_helpers import *
from constants import PROJ_EXP, EC

'''
Map containing all your base experiences (work/ec/leadership) to make
it easier to mix and match as well as use change_bullet function
to manipulate them.
Example is given.
'''
exps = {
	"[ARBITRARY_ID]": {
		"id": "[ARBITRARY_ID]", # mandatory
		"position": "[WHAT YOUR ROLE WAS CALLED]", # mandatory
		"company": "[WHAT THE COMPANY YOU WORKED AT WAS CALLED]", # optional
		"bullets": [
			"[BULLET 1]",
			"...",
			"[BULLET N]"
			],
		"dates": "Jun 2023 - Aug 2023", # mandatory
		"location": "Bengaluru, India" # optional
	},
}

change_bullet_demonstration = change_bullet(exps["[ARBITRARY_ID]"], [0, "BULLET 2", "BULLET 3", 2, "FINAL BULLET"])

'''
The format for every config object.
I recommend you start with a base one true for every resume
you have, and then build out more variations in a functional way.
Remember to use the deepcopy (dc) function as appropriate.
'''
base_config = {
	"NAME": "[your name]",
	"UNIVERSITY": "[university you attend]",
	"DEGREE": "[B.S. in Making Resumes]",
	"OUTPUT_FILE_NAME": "MyResume.pdf", # standardized name, probably FirstnameLastnameResume.pdf
	"CONTACT_INFO": ["[phone number]", "[email]", "[location]", "[etc]"],
	"GPA": "[x.y]",
	"GRAD_TERM": "[Month] [Year]",
	"COURSEWORK": ["[class 1]", "[class 2]"], # optional
	"CERTIFICATIONS": [], # optional
	"SKILLS": { # of the format str: list[str]. Each key is a bolded subheader for skills on a new line
				"Languages": [], 
				"Frameworks": [],
				"Tools": [],
			  },
	PROJ_EXP: [
		# title of this section is WORK EXPERIENCE & PROJECTS. Can be changed in main.py
		exps["[ARBITRARY_ID]"],
	],
	EC: [
		# title of this section is LEADERSHIP & EXTRACURRICULARS. Can be changed in main.py
	]
}

def base():
	return dc(base_config)

# generate_variations.py will iterate through items in this map
configs = {
	"example": base(),
}
