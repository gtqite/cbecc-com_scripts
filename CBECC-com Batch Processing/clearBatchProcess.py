import os
import shutil
import re

# Define all directories, files, and remove existing .cibd files
wkdir = os.getcwd()

dest = os.path.join(wkdir,'BatchProcess')
src = os.listdir(dest)
for file in src:
	if file.endswith(".cibd16"):
		os.remove(os.path.join(dest,file))
