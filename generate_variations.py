import os, shutil

from config import configs
from main import generate_from_config
from constants import BODY_LINE_HEIGHT

output_path = "output" # Change this load into specific folder on your computer

os.umask(0)

YELLOW = "\033[93m"
RED = "\033[91m"
ENDC = "\033[0m"

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
			print(f"{RED}Failed to delete {file_path}. Reason: {e}{ENDC}")
	
for n, c in configs.items():
	folder_path = output_path + "/" + n
	fn = folder_path + "/" + c["OUTPUT_FILE_NAME"]
	if not os.path.exists(folder_path):
		os.mkdir(folder_path)
	stat = generate_from_config(c, fn)
	if stat == -1:
		print(f"Created {YELLOW}(overflowing){ENDC}: {n}")
	else:
		if stat > BODY_LINE_HEIGHT * 2:
			print(f"Created {YELLOW}(add more content){ENDC}: {n}")
		else:
			print(f"Created: {n}")