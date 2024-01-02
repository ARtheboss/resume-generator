from copy import deepcopy

PROJ_EXP = "PROJ_EXP"
EC = "EC"

#######################################
###  CONFIG MANIPULATION FUNCTIONS  ###
#######################################

'''
Find index of an id in a list
l: list of experiences, i: id
'''
def find_index(l, i):
	f = -1
	for ind, x in enumerate(l):
		if x["id"] == i:
			f = ind
			break
	return f

'''
Remove an id from list of experiences
and return that experience. Return None
if id does not exist.
l: list of experiences, i: id
'''
def remove_id(l, i):
	ind = find_index(l, i)
	if ind == -1:
		return None
	else:
		v = deepcopy(l[ind])
		del l[ind]
		return v

'''
In the list of experiences, order the exps
with the given ids in that order. Keep rest
at end in original order.
'''
def reorder(l, ids):
	nl = []
	for i in ids:
		v = remove_id(l, i)
		if not v:
			continue
		nl.append(v)
	nl += l
	return nl

def reorder_cat(conf, cat, ids):
	conf[cat] = reorder(conf[cat], ids)
	return conf

'''
Given full config, move id to first in 
either PROJ_EXP or EC.
'''
def move_id_to_first_conf(conf, i):
	if find_index(conf[PROJ_EXP], i) >= 0:
		return reorder_cat(conf, PROJ_EXP, [i])
	else:
		return reorder_cat(conf, EC, [i])

'''
Given full config, remove gien id
'''
def remove_id_conf(conf, i):
	if find_index(conf[PROJ_EXP], i) >= 0:
		remove_id(conf[PROJ_EXP], i)
	else:
		remove_id(conf[EC], i)
	return conf

'''
s: skills list which contains tuples
of (category, skill)
'''
def add_skills(conf, s):
	for t in s:
		conf["SKILLS"][t[0]].append(t[1])
	return conf

'''
In list of skills in given cat,
order skills (indexes in l)
as given, keep rest at end in 
original order.
'''
def reorder_skills(conf, cat, l):
	nl = []
	for i in l:
		nl.append(conf["SKILLS"][cat][i])
	for x in conf["SKILLS"][cat]:
		if x not in l:
			nl.append(x)
	conf["SKILLS"][cat] = nl
	return conf


def add_exp_at_pos(conf, cat, e, i):
	conf[cat].insert(i, e)
	return conf

def append_exp(conf, cat, e):
	conf[cat].append(e)
	return conf

def prepend_exp(conf, cat, e):
	return add_exp_at_pos(conf, cat, e, 0)

def add_coursework(conf, courses):
	conf["COURSEWORK"] += courses
	return conf


####################################
###  EXP MANIPULATION FUNCTIONS  ###
####################################

def replace_of_id(conf, i, n):
	x = find_index(conf[PROJ_EXP], i)
	y = -1
	if x == -1:
		y = find_index(conf[EC], i)

	if x != -1:
		conf[PROJ_EXP][x] = n
	if y != -1:
		conf[EC][y] = n
	return conf

'''
Change bullet completely based on params
i: exp id
b_l: bullet list, containing ways to change 
old bullet. Integers in list reference old bullets
and text represent new ones.
'''
def change_bullet(i, b_l):
	e = deepcopy(es[i])
	nbl = []
	for x in b_l:
		if type(x) == int:
			nbl.append(es[i]["bullets"][x])
		else:
			nbl.append(x)
	e["bullets"] = nbl
	return e

es = {
	"fractal": {
		"id": "fractal",
		"position": "Project Intern",
		"company": "Fractal Analytics",
		"bullets": [
			"Worked with cloud and data technology team to develop a Python ML model to auto-tag 10MiB+ datasets in milliseconds, automating a tedious process to boost efficiency",
			"Exposed model via REST API hosted on Microsoft Azure, accessed by 5+ projects within company",
			],
		"dates": "Jun 2023 - Aug 2023",
		"location": "Bengaluru, India"
	},
	"globesisters": {
		"id": "globesisters",
		"position": "Software Engineering Intern",
		"company": "GlobeSisters",
		"bullets": [
			"Developed from early stages to app launch w/ 1 500+ MAU on Play Store and App Store",
			"Translated UI/UX from Figma to Flutter/Dart, Firebase and entirely created two of four main pages: a social-media style home and direct-messaging",
			"Led creation of CI pipelines on GitLab to set up automated testing and improve code reliability" 
			],
		"dates": "Sep 2022 - Jan 2023",
		"location": "Berkeley, CA"
	},
	"nugit": {
		"id": "nugit",
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
	"timetrialracing": {
		"id": "timetrialracing",
		"position": "Creator",
		"company": "Time Trial Racing",
		"bullets": [
			"Independently published game to Chrome Webstore (6000+ users) and developed car physics with Javascript/Webpack w/ HTML5 rendering. Currently in 7th major version with 3000+ lines of code",
			"Managing Ruby on Rails web server hosted via Heroku to handle thousands of requests a day",
			"Followed 12-Factor App principles to optimize performance, reliability and ease-of-development"
			],
		"dates": "Oct 2017 - Present"
	},
	"coursestaff16a": {
		"id": "coursestaff16a",
		"position": "EECS 16A Lab Assistant",
		"company": "UC Berkeley EECS",
		"bullets": [
			"Working 8 hours a week to help ~100 students in two sections with circuits/control labs",
			"Debugged Arduino code to improve accuracy of single-pixel camera lab by 15%"
			],
		"dates": "Aug 2023 - Present",
		"location": "Berkeley, CA",
	},
	"csm61c": {
		"id": "csm61c",
		"position": "CS61C Junior Mentor",
		"company": "Computer Science Mentors",
		"bullets": [
			"Running weekly tutoring session for group of 5 students in computer architectures class"
			],
		"dates": "Aug 2023 - Present",
		"location": "Berkeley, CA",
	},
	"bfr": {
		"id": "bfr",
		"position": "Vehicle Dynamics Subteam Member",
		"company": "Berkeley Formula Racing",
		"bullets": [
			"Using intersection of cars and CS to help build racecar for 120+ university competition",
			"Improved performance of simulations by 50% and upgraded aero model to inform mechanical design of 7 subteams",
			],
		"dates": "Oct 2022 - Present",
		"location": "Berkeley, CA",
	},
	"rha": {
		"id": "rha",
		"position": "Unit 1 Representative",
		"company": "Berkeley Residence Hall Assembly",
		"bullets": [
			"Awarded Finance Comittee Member of the year and won school of the year against 60+ RHAs",
			"Organized general activities for 1600 residents in residence hall, managed a $100k+ budget",
			],
		"dates": "Aug 2022 - May 2023",
		"location": "Berkeley, CA"
	},
	"guitarpedalsim": {
		"id": "guitarpedalsim",
		"position": "Guitar Pedal Simulator",
		"bullets": [
			"Created a program that manipulates realtime microphone inputs to replicate guitar effects (such as delay and reverb) and emit realtime audio output with C",
			"Used LT Spice to simulate circuit configurations for guitar pedals to apply effects on my playing",
			],
		"dates": "Apr 2023"
	},
	"berkeleytime": {
		"id": "berkeleytime",
		"position": "Backend Developer",
		"company": "Berkeleytime",
		"location": "Berkeley, CA",
		"bullets": [
			"Working with ~15 student team to maintain Berkeley's leading open source course discovery/research platform, used by ~30k students",
			"Updating legacy Django code to Express/Typescript for increased performance with GraphQL and MongoDB, using Kubernetes for deployment",
			"Boosted endpoint performance by 10x with custom Redis caching"
			],
		"dates": "Sep 2023 - Present"
	},
	"sc": {
		"id": "sc",
		"position": "Administrative Co-ordinator",
		"company": "Residential Life Safety Program",
		"bullets": [
			"Collaborating in team of 8 to manage 150+ student employees with nightly shifts"
			],
		"dates": "Aug 2023 - Present"
	},
	"fantasyautoroster": {
		"id": "fantasyautoroster",
		"position": "Fantasy Basketball Auto-Roster",
		"bullets": [
			"Created program with Python to optimally roster players for ESPN's fantasy basketball to automate tedious process",
			"Employed Selenium to interact with ESPN Web UI for rapid performance",
			],
		"dates": "Jan 2021"
	},
	"rookiedb": {
		"id": "rookiedb",
		"position": "RookieDB",
		"bullets": [
			"Created simple DBMS with Java for class project including B+ tree indices, efficient join algorithms, query optimization, and multigranularity locking to allow concurrent execution of transactions, and ARIES database recovery while preserving ACID properties",
			],
		"dates": "Nov 2023"
	},
	"familytree": {
		"id": "familytree",
		"position": "Family Tree Webapp",
		"bullets": [
			"Creating social-media style webapp to stay updated, connected, and aware in large families",
			"Used a Go/PostgreSQL backend to implement JWT token authentication and MVC structure from scratch, paired with React/Typescript/Sass frontend",
			],
		"dates": "Jul 2023 - Present"
	},
	"3d": {
		"id": "3d",
		"position": "3D Rendering Engine",
		"bullets": [
			"Created a basic Javascript 3D .STL file renderer for Post-Euclidean Geometry Class",
			"Implemented projection and quaternion logic from ground up, enabling movement with 6 D.O.F."
			],
		"dates": "Nov 2021"
	},
	"c": {
		"id": "c",
		"position": "Convolution Optimization",
		"bullets": [
			"Optimized matrix convolution algorithm in C with SIMD, OpenMP, OpenMPI, loop unrolling, cache blocking etc. for class project",
			"Solution ranked 2nd fastest out of 500 submissions"
		],
		"dates": "Apr 2023",
	}
}

safetycoordinator_automation = change_bullet("sc", [0, "Built spreadsheet automations such as ingestion from Shiftboard API to cut admin work by 80%"])
safetycoordinator_data = change_bullet("sc", [0, "Implemented standardized spreadsheet data collection to automate employee performance analysis"])

fractal_frontend = change_bullet("fractal", [0, "Exposed model via Streamlit UI on Microsoft Azure, accessed by 5+ projects within company",])

berkeleytime_data = change_bullet("berkeleytime", [0, "Updating legacy Django code to Express/Typescript for increased performance with GraphQL, using Kubernetes for deployment", "Wrote MongoDB backup & API data ingestion scripts, outperforming PostgreSQL version by 3x"])
berkeleytime_infra = change_bullet("berkeleytime", [0, 1, "Provisioned MinIO S3 Docker volumes replicating prod CloudFlare R2 to facilitate development"])

globesisters_infra = change_bullet("globesisters", [0, "Rewrote components to separate logic and UI for reliability and facilitating unit testing", "Led creation of first CI pipelines on GitLab, boosting development speed and eliminating merging of faulty code"])

base_config = {
		"OUTPUT_FILE_NAME": "AdvayRatanResume.pdf",
		"CONTACT_INFO": ["(628) 255-0206", "advayratan@berkeley.edu", "advayratan.com", "linkedin.com/in/advay-ratan/", "Berkeley, CA"],
		"GPA": "4.0",
		"GRAD_TERM": "May 2026",
		"COURSEWORK": ["Algorithms & Datastructures (Java)", "Computer Architecture (C)", "Discrete Math & Probability"],
		"SKILLS": {
					"Languages": ["Python", "C++", "C", "Java", "SQL", "HTML", "CSS"],
					"Frameworks": [],
					"Tools": ["Linux", "Microsoft Azure", "AWS", "Git"],
				  },
		PROJ_EXP: [
			es["fractal"],
			es["globesisters"],
			es["nugit"],
			es["timetrialracing"],
		],
		EC: [
			es["coursestaff16a"],
			es["csm61c"],
			es["bfr"],
			es["rha"],
		]
	}

def base():
	return deepcopy(base_config)

def g2025(config):
	config["GRAD_TERM"] = "May 2025"
	return config

def sg(config):
	config["CONTACT_INFO"] = ["+65 9169 9871"] + config["CONTACT_INFO"][1:-1]
	return config

def software(config):
	return add_skills(
		add_coursework(config, ["Databases (SQL, Java)"]),[
		("Languages", "Javascript"),
		("Languages", "Typescript"),
		("Languages", "Go"),
		("Frameworks", "Django"),
		("Frameworks", "Node.js"),
		("Frameworks", "Ruby on Rails"),
		("Frameworks", "Flutter"),
		("Frameworks", "S3"),
		("Frameworks", "JQuery"),
		("Frameworks", "ReactJS"),
		("Tools", "PostgreSQL"),
		("Tools", "MongoDB"),
		("Tools", "Firebase"),
	])

def berkeleytime(config):
	return add_skills(
		prepend_exp(config, PROJ_EXP, es["berkeleytime"]),[
		("Languages", "GraphQL"),
		("Frameworks", "Express"),
		("Tools", "Kubernetes"),
		("Tools", "Docker"),
		("Tools", "Redis"),
	])

def main2026(config):
	return remove_id_conf(berkeleytime(prepend_exp(software(config), EC, safetycoordinator_automation)), "csm61c")

def main(config):
	return g2025(main2026(config))

def infra(config):
	return replace_of_id(replace_of_id(main(config), "globesisters", globesisters_infra), "berkeleytime", berkeleytime_infra)

def frontend(config):
	return replace_of_id(
		add_skills(
			remove_id_conf(
				prepend_exp(
					software(config), EC, safetycoordinator_automation
				), "csm61c"),
			[
				("Tools", "Figma"),
				("Tools", "Webpack"),
				("Languages", "Sass")
			]),
		"fractal",
		fractal_frontend
		)

def data_engineering(config):
	return add_skills(
		replace_of_id(
			remove_id_conf(
				append_exp(
					replace_of_id(main(config), "sc", safetycoordinator_data), 
					PROJ_EXP, 
					es["rookiedb"]
				), 
				"globesisters"), 
			"berkeleytime", 
			berkeleytime_data
			),
		[("Tools", "Apache Airflow"),]
		)

def backend(config):
	return remove_id_conf(main(config), "globesisters")

def automation(config):
	config["PROJ_EXP"].append(es["fantasyautoroster"])
	return config

def java(config):
	# move java to front of list
	return reorder_skills(append_exp(backend(config), PROJ_EXP, es["rookiedb"]), "Languages", [3])

def go(config):
	# move go to front of list
	return reorder_skills(append_exp(backend(config), PROJ_EXP, es["familytree"]), "Languages", [9])

def graphics(config):
	return add_coursework(
			prepend_exp(
				main(config),
				PROJ_EXP,
				es["3d"]
			),	
			["Linear Algebra"],
		)

def gaming(config):
	return move_id_to_first_conf(graphics(config), "timetrialracing")

def ee105(config):
	return add_coursework(
			add_skills(
				config,
				[
					("Tools", "Cadence Virtuoso"),
					("Tools", "LTSpice"),
				]
			),
			["Microelectronic Devices"],
		)

def c(config):
	return prepend_exp(config, PROJ_EXP, es["c"])

def computer_architecture(config):
	return ee105(c(
		move_id_to_first_conf(
			prepend_exp(
				remove_id_conf(config, "nugit"), 
				PROJ_EXP, 
				es["berkeleytime"]), 
			"csm61c"
		)
	))


configs = {
	"main": main(base()),
	"main2026": main2026(base()),
	"frontend": frontend(base()),
	"app_dev": move_id_to_first_conf(main(base()), "globesisters"),
	"data_engineering": data_engineering(base()),
	"databases": move_id_to_first_conf(data_engineering(base()), "rookiedb"),
	"java": java(base()),
	"go": go(base()),
	"infra": infra(base()),
	"graphics": graphics(base()),
	"gaming": gaming(base()),
	"computer_architecture": computer_architecture(base()),
}
