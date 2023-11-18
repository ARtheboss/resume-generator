import os, shutil

import config
from main import generate_from_config

# output_path = "output"
output_path = "/Users/home/Documents/Work/Generated Resumes"

os.umask(0)

if not os.path.exists(output_path):
	os.mkdir(output_path)
else:
	for filename in os.listdir(output_path):
		if filename == ".DS_Store":
			continue
		file_path = os.path.join(output_path, filename)
		try:
			shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
	
for c, o in config.__dict__.items():
	if type(o) == type and o.RENDER and c != "BaseConfig":
		folder_path = output_path + "/" + c
		fn = folder_path + "/AdvayRatanResume.pdf"
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)
		generate_from_config(o, fn)
		print(f"Created: {fn}")