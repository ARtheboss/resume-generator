class BaseConfig:

	RENDER = True # special case, baseconfig never renders

	OUTPUT_FILE_NAME = "AdvayRatanResume.pdf"

	CONTACT_INFO = ["(628) 255-0206", "advayratan@berkeley.edu", "advayratan.com", "linkedin.com/in/advay-ratan/", "github.com/ARtheboss/"]

	GPA = "4.0"

	GRAD_TERM = "May 2026"

	COURSEWORK = ["Algorithms & Datastructures (Java)", "Computer Architecture (C)", "Databases", "Graphics (C++)", "Machine Learning"]

	SKILLS = {
				"Languages": ["Python","Java","C","C++","Javascript","PHP", "MATLAB"],
				"Web Development": ["HTML/CSS", "JQuery", "React", "Webpack", "Django", "Ruby on Rails"],
				"App Development": ["Flutter/Dart"],
				"Game Development": ["HTML5 Canvas", "Unity"],
				"Competive Programming": ["USACO Gold"],
				"Software Engineering": ["Git","Jira","GitHub","GitLab"],
			  }

	PROJ_EXP = [
		{
			"position": "Project Intern",
			"company": "Fractal Analytics",
			"bullets": [
				"Working with cloud and data technology team to develop a Python machine learning data classifier.",
				"Creating an API to expose classifier endpoints to client-facing webapp.",
				],
			"dates": "June 2023 - Present",
			"location": "Bengaluru, India"
		},
		{
			"position": "Software Engineering Intern",
			"company": "GlobeSisters",
			"bullets": [
				"Developed from early stages and helped launched app in a small team.",
				"Translated UI/UX requirements from Figma to frontend Flutter/Dart user interface.",
				"Handled Firebase backend, including Cloud Firestore, Firestore Rules, Firebase Functions etc.",
				"Led creation of CI pipelines on GitLab to set up unit, widget and integration testing."
				],
			"dates": "Sep 2022 - Jan 2023",
			"location": "Berkeley, CA"
		},
		{
			"position": "Data Engineering Intern",
			"company": "Nugit",
			"bullets": [
				"Led creation of a new data pipeline (extract, transform, load) optimizing core tech for all clients using Apache Airflow/Python. Wrote integrations for various APIs such as GoogleAdwords, Facebooks Ads etc. and handled MongoDB server for transformed data storage.",
				"Followed AGILE framework/Jira roadmaps to work effectively with team of twelve engineers"
				],
			"dates": "May 2021 - Jul 2021",
			"location": "Singapore"
		},
		{
			"position": "CS 61A Academic Intern",
			"company": "UC Berkeley EECS",
			"bullets": [
				"Weekly Office Hour assistant for introductory Python programming course at UC Berkeley."
				],
			"dates": "Jan 2023 - May 2023",
		},
		{
			"position": "EECS 16A Junior Mentor",
			"company": "Computer Science Mentors",
			"bullets": [
				"Ran weekly 1.5 hour mini-lecture/tutoring sessions on circuits and linear algebra."
				],
			"dates": "Jan 2023 - May 2023"
		},
		{
			"position": "Creator",
			"company": "Time Trial Racing",
			"bullets": [
				"Independently published game to Chrome Webstore (6000+ users) and developed car physics with Javascript, rendered with HTML5. Currently in 7th major version with 3000+ lines of code.",
				"Managing Ruby on Rails web server hosted via Heroku to handle thousands of requests a day.",
				"Worked with Node and Webpack to optimize code performance, reliability and ease-of-development."
				],
			"dates": "Oct 2017 - Present"
		},
		{
			"position": "Delivery Route Optimization",
			"bullets": [
				"Created tool to solve for the quickest delivery route plan for multiple vehicles given a city plan and a list of orders.",
				"Employed Java to create a modified version of Dijkstra's and employed a greedy approach to increase efficiency.",
				],
			"dates": "Apr 2023"
		},
	]

	EC = [
		{
			"position": "Vehicle Dynamics Member",
			"company": "Berkeley Formula Racing",
			"bullets": [
				"Member of Vehicle Dynamics for UC Berkeley's internal combustion Formula SAE team.",
				"In charge of suspension kinematics design, static and dynamic car testing, and overall design direction of the car to maximize performance.",
				],
			"dates": "Oct 2022 - Present"
		},
		{
			"position": "Unit 1 Representative",
			"company": "Berkeley Residence Hall Assembly",
			"bullets": [
				"Awarded Finance Comittee Member of the year and won school of the year against 60+ RHAs.",
				"Organized general activities for 1600 residents in residence hall, managed a $100k+ budget.",
				"Liaised for Residence Hall Assembly, collated and represented resident’s voice to initiate positive change in my residence hall.",
				],
			"dates": "Aug 2022 - May 2023"
		},
	]
'''
class SpaceRelated(BaseConfig):
	EC = BaseConfig.EC + [{
			"position": "Experiment Lead",
			"company": "SpaceLab",
			"bullets": [
				"Selected on a team of ten people to design and build an experiment to be sent to the International Space Station."
				"Wrote software to be run by the experimental module aboard the ISS using PBasic."
				],
			"dates": "May 2020 - May 2021"
		}]

'''
class USA2026Standard(BaseConfig):
	pass

class USA2025Standard(BaseConfig):
	GRAD_TERM = "May 2025"

class SG2026Standard(BaseConfig):
	CONTACT_INFO = ["+65 9169 9871"] + BaseConfig.CONTACT_INFO[1:]

class SG2025Standard(USA2025Standard, SG2026Standard):
	pass




