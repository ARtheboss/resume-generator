class BaseConfig:

	SUMMARY = "Passionate about finding efficient and reliable solutions to complex problems"

	RENDER = True # special case, baseconfig never renders

	OUTPUT_FILE_NAME = "AdvayRatanResume.pdf"

	CONTACT_INFO = ["(628) 255-0206", "advayratan@berkeley.edu", "advayratan.com", "linkedin.com/in/advay-ratan/"]

	GPA = "4.0"

	GRAD_TERM = "May 2026"

	COURSEWORK = ["Algorithms & Datastructures (Java)", "Computer Architecture (C)", "Databases (SQL, Java)", "Discrete Math & Probability", "Circuits", "Physics"]

	SKILLS = {
				"Languages": ["Python","C++","Java","C","Javascript","SQL", "GoLang","PHP","MATLAB"],
				"Web Development": ["HTML", "CSS", "Sass", "Typescript", "JQuery", "React", "Webpack", "Django", "Node.js", "Ruby on Rails"],
				"App Development": ["Flutter/Dart"],
				"Software Engineering": ["Git","Jira","Unix/Linux"],
				"Technologies": ["Apache Airflow", "Figma", "Firebase", "Heroku", "Postgres"],
				"Frameworks": ["Distributed Systems", "REST APIs"],
			  }

	# Python, C++ , Java, C, Javascript, SQL, GoLang, PHP, MATLAB, HTML, CSS, Typescript, JQuery, React, Webpack, Django, Node.js, Ruby on Rails, Flutter, Dart, Git, Jira, Github, Gitlab, Unix, Linux, Apache Airflow, Figma, Firebase, Heroku, Distributed Systems, REST APIs

	PROJ_EXP = [
		{
			"position": "Project Intern",
			"company": "Fractal Analytics",
			"bullets": [
				"Worked with cloud and data technology team to develop an ML model w/ Python to auto-tag dataframe headers, automating a tedious process and boosting efficiency.",
				"Exposed model with API hosted with Microsoft Azure, accessed by 5+ projects within company.",
				],
			"dates": "Jun 2023 - Aug 2023",
			"location": "Bengaluru, India"
		},
		{
			"position": "Software Engineering Intern",
			"company": "GlobeSisters",
			"bullets": [
				"Developed from early stages to app launch on Google Play Store and App Store.",
				"Translated UI/UX from Figma to Flutter/Dart frontend and Firebase backend and created two of four main pages: a social-media style home and direct-messaging.",
				"Led creation of CI pipelines on GitLab to set up unit, widget and integration testing to drastically improve code reliability." 
				],
			"dates": "Sep 2022 - Jan 2023",
			"location": "Berkeley, CA"
		},
		{
			"position": "Data Engineering Intern",
			"company": "Nugit",
			"bullets": [
				"Led creation of a new ETL data pipeline using Apache Airflow/Python to substantially boost reliability of core tech for all sensitive client data.", 
				"Wrote integrations for 5 APIs such as GoogleAdwords, Facebooks Ads, Twitter Ads and utilized MongoDB for transformed data storage.",
				"Followed AGILE framework/Jira roadmaps to collaborate effectively with team of twelve engineers and ship cohesive microservices products." 
				],
			"dates": "May 2021 - Jul 2021",
			"location": "Singapore"
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
	]

	EC = [
		{
			"position": "EECS 16A Lab Assistant",
			"company": "UC Berkeley EECS",
			"bullets": [
				"Working 8 hours a week to help  almost 100 students in two sections with circuits/control labs."
				],
			"dates": "Aug 2023 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "CS61C Junior Mentor",
			"company": "Computer Science Mentors",
			"bullets": [
				"Running weekly 1 hour tutoring for group of 5 students in computer architectures class."
				],
			"dates": "Aug 2023 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "Vehicle Dynamics Member",
			"company": "Berkeley Formula Racing",
			"bullets": [
				"Exploring the intersection of passions: physics, cars, and CS.",
				"Writing simulations to predict laptimes and orchestrating real-life tests for validation to dictate overall car design direction to maximize performance against 120+ universities yearly.",
				],
			"dates": "Oct 2022 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "Unit 1 Representative",
			"company": "Berkeley Residence Hall Assembly",
			"bullets": [
				"Awarded Finance Comittee Member of the year and won school of the year against 60+ RHAs.",
				"Organized general activities for 1600 residents in residence hall, managed a $100k+ budget.",
				"Liaised for Residence Hall Assembly, collated and represented resident’s voice to initiate positive change in my residence hall.",
				],
			"dates": "Aug 2022 - May 2023",
			"location": "Berkeley, CA"
		},
	]

class SpaceRelated(BaseConfig):
	RENDER = False
	EC = BaseConfig.EC + [{
			"position": "Experiment Lead",
			"company": "SpaceLab",
			"bullets": [
				"Selected on a team of ten people to design and build an experiment to be sent to the International Space Station."
				"Wrote software to be run by the experimental module aboard the ISS using PBasic."
				],
			"dates": "May 2020 - May 2021"
		}]


class USA2026Standard(BaseConfig):
	pass

class USA2025Standard(BaseConfig):
	GRAD_TERM = "May 2025"

class SG2026Standard(BaseConfig):
	CONTACT_INFO = ["+65 9169 9871"] + BaseConfig.CONTACT_INFO[1:]

class SG2025Standard(USA2025Standard, SG2026Standard):
	pass

class Automation(USA2025Standard):
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Technologies"].append("Selenium")
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append({
			"position": "Fantasy Basketball Auto-Roster",
			"bullets": [
				"Created program with Python to optimally roster players for ESPN's fantasy basketball to automate tedious process.",
				"Employed Selenium to interact with ESPN Web UI for rapid performance.",
				],
			"dates": "Jan 2021"
		})

class Java(USA2025Standard):
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append(
		{
			"position": "Delivery Route Optimization",
			"bullets": [
				"Created tool to solving for the optimized multi-vehicle delivery given a city plan and order list.",
				"Employed Java to implement a modified Dijkstra's with a greedy approach to increase efficiency.",
				],
			"dates": "Apr 2023"
		})

class GoLang(USA2025Standard):
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append(
		{
			"position": "Family Tree Webapp",
			"bullets": [
				"Creating social-media style webapp to stay updated, connected, and aware in large families.",
				"Used a GoLang/Postgres backend to implement JWT token authentication and MVC structure from scratch, paired with React/Typescript/Sass frontend.",
				],
			"dates": "Jul 2023 - Present"
		})

class USA2025Cloud(GoLang):
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Technologies"].append("Microsoft Azure")
	SKILLS["Technologies"].append("AWS")

class USA2025Car(USA2025Standard):
	SUMMARY = "Passionate about creating efficient and reliable solutions for cars and software"
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS.update({"MechE": ["Solidworks"]})

class USA2025SomeEE(USA2025Standard):
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS.update({"Others": ["Electrical lab equipment"]})

class USA2025AppDev(USA2025Standard):
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	s = PROJ_EXP[1]
	PROJ_EXP[1] = PROJ_EXP[0]
	PROJ_EXP[0] = s

class USA2025PayPal(USA2025Standard):
	RENDER = False
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Web Development"].append("AJAX")
	SKILLS.update({"Others": ["SaaS Technology"]})

"""
{
			"position": "CS 61A Academic Intern",
			"company": "UC Berkeley EECS",
			"bullets": [
				"Weekly Office Hour assistant for introductory Python programming course with ~1500 students."
				],
			"dates": "Jan 2023 - May 2023",
			"location": "Berkeley, CA",
		},
		{
			"position": "EECS 16A Junior Mentor",
			"company": "Computer Science Mentors",
			"bullets": [
				"Ran weekly 1.5 hour mini-lecture/tutoring sessions on circuits and linear algebra for three students."
				],
			"dates": "Jan 2023 - May 2023",
			"location": "Berkeley, CA",
		},
		"""

class Cambly(USA2025Standard):
	RENDER = False
	SUMMARY = "Imagining technology to connect the globe"
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append({
			"position": "CS 61A Academic Intern",
			"company": "UC Berkeley EECS",
			"bullets": [
				"Weekly Office Hour assistant for introductory Python programming course with ~1500 students."
				],
			"dates": "Jan 2023 - May 2023",
			"location": "Berkeley, CA",
		})
	PROJ_EXP.append(
		{
			"position": "EECS 16A Junior Mentor",
			"company": "Computer Science Mentors",
			"bullets": [
				"Ran weekly 1.5 hour mini-lecture/tutoring sessions on circuits and linear algebra for three students."
				],
			"dates": "Jan 2023 - May 2023",
			"location": "Berkeley, CA",
		})

class EpicGamesPhysics(USA2025Standard):
	SUMMARY = "Passionate about recreating real life in beautiful and efficient simulations"
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP = [PROJ_EXP[3]] + PROJ_EXP[:3]
	EC = BaseConfig.EC[:]
	EC = [EC[2]] + EC[:2] + [EC[3]]
