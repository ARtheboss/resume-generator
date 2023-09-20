import os

import config
from main import generate_from_config

# output_path = "output"
output_path = "/Users/home/Documents/Work/Generated Resumes"

if not os.path.exists(output_path):
	os.mkdir(output_path)
	
for c, o in config.__dict__.items():
	if type(o) == type and o.RENDER and c != "BaseConfig":
		folder_path = output_path + "/" + c
		fn = folder_path + "/AdvayRatanResume.pdf"
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)
		generate_from_config(o, fn)
		print(f"Created: {fn}")