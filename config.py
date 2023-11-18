class BaseConfig:

	SUMMARY = "Passionate about finding efficient and reliable solutions to complex problems"

	RENDER = True # special case, baseconfig never renders

	OUTPUT_FILE_NAME = "AdvayRatanResume.pdf"

	CONTACT_INFO = ["(628) 255-0206", "advayratan@berkeley.edu", "advayratan.com", "linkedin.com/in/advay-ratan/"]

	GPA = "4.0"

	GRAD_TERM = "May 2026"

	COURSEWORK = ["Algorithms & Datastructures (Java)", "Computer Architecture (C)", "Databases (SQL, Java)", "Discrete Math & Probability", "Circuits", "Physics"]

	SKILLS = {
				"Languages": ["Python", "C++", "Java", "Javascript", "Typescript", "SQL", "GoLang", "HTML", "CSS"],
				"Frameworks": ["JQuery", "ReactJS", "Django", "Node.js", "Ruby on Rails", "Flutter", "Microservices"],
				"Tools": ["Apache Airflow", "Figma", "PostgreSQL", "Microsoft Azure", "AWS", "Firebase", "Git"]
			  }

	# Python, C++ , Java, C, Javascript, SQL, GoLang, PHP, MATLAB, HTML, CSS, Typescript, JQuery, React, Webpack, Django, Node.js, Ruby on Rails, Flutter, Dart, Git, Jira, Github, Gitlab, Unix, Linux, Apache Airflow, Figma, Firebase, Heroku, Distributed Systems, REST APIs

	PROJ_EXP = [
		{
			"position": "Project Intern",
			"company": "Fractal Analytics",
			"bullets": [
				"Worked with cloud and data technology team to develop a Python ML model to auto-tag 10MiB+ datasets in milliseconds, automating a tedious process to boost efficiency",
				"Exposed model via REST API hosted on Microsoft Azure, accessed by 5+ projects within company",
				],
			"dates": "Jun 2023 - Aug 2023",
			"location": "Bengaluru, India"
		},
		{
			"position": "Software Engineering Intern",
			"company": "GlobeSisters",
			"bullets": [
				"Developed from early stages to app launch w/ 500+ MAU on Play Store and App Store",
				"Translated UI/UX from Figma to Flutter/Dart, Firebase and entirely created two of four main pages: a social-media style home and direct-messaging",
				"Led creation of CI pipelines on GitLab to set up automated testing and improve code reliability" 
				],
			"dates": "Sep 2022 - Jan 2023",
			"location": "Berkeley, CA"
		},
		{
			"position": "Data Engineering Intern",
			"company": "Nugit",
			"bullets": [
				"Led creation of new ETL data pipeline using Apache Airflow/Python, boosting reliability of core tech for all 10+ large corporate clients", 
				"Wrote integrations for 5 APIs including GoogleAdwords and Twitter Ads and utilized MongoDB for transformed data storage",
				"Followed AGILE framework/Jira roadmaps to collaborate with team of twelve engineers" 
				],
			"dates": "May 2021 - Jul 2021",
			"location": "Singapore"
		},
		{
			"position": "Creator",
			"company": "Time Trial Racing",
			"bullets": [
				"Independently published game to Chrome Webstore (6000+ users) and developed car physics with Javascript/Webpack w/ HTML5 rendering. Currently in 7th major version with 3000+ lines of code",
				"Managing Ruby on Rails web server hosted via Heroku to handle thousands of requests a day",
				"Followed 12-Factor App principles to optimize performance, reliability and ease-of-development"
				],
			"dates": "Oct 2017 - Present"
		},
	]

	EC = [
		{
			"position": "EECS 16A Lab Assistant",
			"company": "UC Berkeley EECS",
			"bullets": [
				"Working 8 hours a week to help ~100 students in two sections with circuits/control labs"
				],
			"dates": "Aug 2023 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "CS61C Junior Mentor",
			"company": "Computer Science Mentors",
			"bullets": [
				"Running weekly tutoring session for group of 5 students in computer architectures class"
				],
			"dates": "Aug 2023 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "Vehicle Dynamics Subteam Member",
			"company": "Berkeley Formula Racing",
			"bullets": [
				"Using intersection of cars and CS to help build racecar for 120+ university competition",
				"Improved performance of simulations by 50% and upgraded aero model to inform mechanical design of 7 subteams",
				],
			"dates": "Oct 2022 - Present",
			"location": "Berkeley, CA",
		},
		{
			"position": "Unit 1 Representative",
			"company": "Berkeley Residence Hall Assembly",
			"bullets": [
				"Awarded Finance Comittee Member of the year and won school of the year against 60+ RHAs",
				"Organized general activities for 1600 residents in residence hall, managed a $100k+ budget",
				],
			"dates": "Aug 2022 - May 2023",
			"location": "Berkeley, CA"
		},
	]


class USA2026Standard(BaseConfig):
	CONTACT_INFO = BaseConfig.CONTACT_INFO + ["Berkeley, CA"]

class USA2025Standard(USA2026Standard):
	GRAD_TERM = "May 2025"

class SG2026Standard(BaseConfig):
	CONTACT_INFO = ["+65 9169 9871"] + BaseConfig.CONTACT_INFO[1:]

class SG2025Standard(USA2025Standard, SG2026Standard):
	pass

class CircuitSim(BaseConfig):
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append(
		{
			"position": "Guitar Pedal Simulator",
			"bullets": [
				"Created a program that manipulates realtime microphone inputs to replicate guitar effects (such as delay and reverb) and emit realtime audio output with C",
				"Used LT Spice to simulate circuit configurations for guitar pedals to apply effects on my playing",
				],
			"dates": "Apr 2023"
		})

class Cadence(USA2025Standard, CircuitSim):
	RENDER = True
	COURSEWORK = BaseConfig.COURSEWORK[:]
	COURSEWORK.append("_Digital Design (Plan to take in Spring 2024)_")
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Languages"] = ["Python", "C++", "C", "Java", "Javascript", "Typescript", "SQL", "GoLang"]
	

class BerkeleyTime(BaseConfig):
	RENDER = False
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Frameworks"].append("Express")
	SKILLS["Tools"].append("Kubernetes")
	SKILLS["Tools"].append("Docker")
	SKILLS["Tools"].append("Redis")
	SKILLS["Languages"].append("GraphQL")
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.insert(0,
		{
			"position": "Backend Developer",
			"company": "Berkeleytime",
			"location": "Berkeley, CA",
			"bullets": [
				"Working with ~15 student team to maintain Berkeley's leading open source course discovery/research platform, used by ~30k students",
				"Updating legacy Django code to Express/Typescript for increased performance use with GraphQL and MongoDB, using Kubernetes for deployment",
				"Boosted endpoint performance by 10x with custom Redis caching"
				],
			"dates": "Sep 2023 - Present"
		})

class SafetyCoordinator(BaseConfig):
	RENDER = False
	EC = BaseConfig.EC[:]
	EC = [{
			"position": "Co-ordinator",
			"company": "Residential Life Safety Program",
			"bullets": [
				"Collaborating in team of 8 to manage 150+ student employees with nightly shifts"
				],
			"dates": "Aug 2023 - Present"
		}] + BaseConfig.EC

class TentativeMain(USA2025Standard, BerkeleyTime):
	RENDER = True
	EC = SafetyCoordinator.EC[:]
	EC.pop(2)

class CircuitSimR(CircuitSim, TentativeMain):
	RENDER = True
	PROJ_EXP = TentativeMain.PROJ_EXP + [CircuitSim.PROJ_EXP[-1]]

class TentativeMain2026(USA2026Standard, BerkeleyTime):
	RENDER = True
	EC = SafetyCoordinator.EC[:]
	EC.pop(2)

class AppDev(TentativeMain):
	PROJ_EXP = TentativeMain.PROJ_EXP[:]
	PROJ_EXP = [PROJ_EXP[2]] + PROJ_EXP[0:2] + PROJ_EXP[3:]


class SpaceRelated(USA2025Standard):
	RENDER = False
	EC = BaseConfig.EC + [{
			"position": "Experiment Lead",
			"company": "SpaceLab",
			"bullets": [
				"Selected on a team of ten people to design and build an experiment to be sent to the International Space Station"
				"Wrote software to be run by the experimental module aboard the ISS using PBasic"
				],
			"dates": "May 2020 - May 2021"
		}]

class Automation(USA2025Standard):
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Tools"].append("Selenium")
	PROJ_EXP = BaseConfig.PROJ_EXP[:]
	PROJ_EXP.append({
			"position": "Fantasy Basketball Auto-Roster",
			"bullets": [
				"Created program with Python to optimally roster players for ESPN's fantasy basketball to automate tedious process",
				"Employed Selenium to interact with ESPN Web UI for rapid performance",
				],
			"dates": "Jan 2021"
		})

class Java(USA2025Standard):
	SKILLS = {key: value[:] for key, value in BerkeleyTime.SKILLS.items()}
	PROJ_EXP = BerkeleyTime.PROJ_EXP[:]
	PROJ_EXP.append(
		{
			"position": "Delivery Route Optimization",
			"bullets": [
				"Created tool to solving for the optimized multi-vehicle delivery given a city plan and order list",
				"Employed Java to implement a modified Dijkstra's with a greedy approach to increase efficiency",
				],
			"dates": "Apr 2023"
		})
	EC = [BaseConfig.EC[0]] + BaseConfig.EC[2:]

class GoLang(USA2025Standard):
	SKILLS = {key: value[:] for key, value in BerkeleyTime.SKILLS.items()}
	PROJ_EXP = BerkeleyTime.PROJ_EXP[:]
	PROJ_EXP.append(
		{
			"position": "Family Tree Webapp",
			"bullets": [
				"Creating social-media style webapp to stay updated, connected, and aware in large families",
				"Used a GoLang/Postgres backend to implement JWT token authentication and MVC structure from scratch, paired with React/Typescript/Sass frontend",
				],
			"dates": "Jul 2023 - Present"
		})
	EC = [BaseConfig.EC[0]] + BaseConfig.EC[2:]

class WebDev(BerkeleyTime):
	RENDER = True
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Tools"].append("Webpack")
	SKILLS["Languages"].append("Sass")

class USA2025Car(USA2025Standard):
	SUMMARY = "Passionate about creating efficient and reliable solutions for cars and software"
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS["Tools"].append("Solidworks")
	SKILLS["Languages"].append("MATLAB")

class USA2025CAD(TentativeMain):
	SKILLS = {key: value[:] for key, value in TentativeMain.SKILLS.items()}
	SKILLS["Tools"].append("Solidworks")
	SKILLS["Languages"].append("MATLAB")

class USA2025SomeEE(CircuitSim):
	PROJ_EXP = CircuitSim.PROJ_EXP[:]
	SKILLS = {key: value[:] for key, value in BaseConfig.SKILLS.items()}
	SKILLS.update({"Others": ["Electrical lab equipment"]})


class Gaming(TentativeMain):
	RENDER = True
	PROJ_EXP = TentativeMain.PROJ_EXP[:]
	PROJ_EXP = [PROJ_EXP[4]] + [{
		"position": "3D Rendering Engine",
		"bullets": [
			"Created a basic Javascript 3D .STL file renderer for Post-Euclidean Geometry Class",
			"Implemented projection and quaternion logic from ground up, enabling movement with 6 D.O.F."
			],
		"dates": "Nov 2021"
	}] + PROJ_EXP[:4] + PROJ_EXP[5:]
	COURSEWORK = BaseConfig.COURSEWORK[:]
	COURSEWORK.append("Linear Algebra")

class Databases(TentativeMain):
	RENDER = True
	PROJ_EXP = TentativeMain.PROJ_EXP[:]
	PROJ_EXP = [{
		"position": "RookieDB",
		"bullets": [
			"Created simple DBMS with Java for class project including B+ tree indices, efficient join algorithms, query optimization, and multigranularity locking to allow concurrent execution of transactions, and ARIES database recovery while preserving ACID properties",
			],
		"dates": "Nov 2023"
	}] + PROJ_EXP
	COURSEWORK = BaseConfig.COURSEWORK[:]
	COURSEWORK.append("Linear Algebra")
