from copy import deepcopy
from constants import PROJ_EXP, EC

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

'''
To a config, add an experience 
for a certain category at a specific
position
'''
def add_exp_at_pos(conf, cat, e, i):
	conf[cat].insert(i, e)
	return conf

'''
To a config, append an experience 
for a certain category to the end
'''
def append_exp(conf, cat, e):
	conf[cat].append(e)
	return conf

'''
To a config, prepend an experience 
for a certain category to the start
'''
def prepend_exp(conf, cat, e):
	return add_exp_at_pos(conf, cat, e, 0)

'''
To a config, add a list of courses
to the coursework section
'''
def add_coursework(conf, courses):
	conf["COURSEWORK"] += courses
	return conf


'''
Replace an experience of given id 'i' with 'n'
'''
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


####################################
###  EXP MANIPULATION FUNCTIONS  ###
####################################

'''
Change bullet completely based on params
e: experience
b_l: bullet list, containing ways to change 
old bullet. Integers in list reference indexes
in old bullet list and text represent new ones.
'''
def change_bullet(e, b_l):
	e = deepcopy(e)
	nbl = []
	for x in b_l:
		if type(x) == int:
			nbl.append(e["bullets"][x])
		else:
			nbl.append(x)
	e["bullets"] = nbl
	return e