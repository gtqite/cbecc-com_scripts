import os, re

# This script removes the hard-coded ventilation rates from IES and resets them to the default (blank). 
# Make sure a copy of this script and the CBECC-com file are in the same folder when running this script.
# This script will apply to all CBECC-com files in the folder.

# WARNING: This script will reset ALL ventilation rates in the rooms. Take care when specific hard-coded ventilation rates are required.

# Find location of the python script and the CBECC-com file.
wkdir = os.getcwd()
directory = os.listdir(wkdir)
os.chdir(wkdir)

# Locate the CBECC-com file, find and delete the ventilation values.
for file in directory:
	if file.endswith("cibd16"):
		open_file=open(file,'r')
		read_file=open_file.read()
		vent = re.compile('VentPerPerson = ..*\n..*\n..*\n..*\n   ')
		read_file = vent.sub('', read_file)
		exh = re.compile('ExhPerArea ..*\n..*\n..*\n   ')
		read_file = exh.sub('', read_file)
		write_file = open(file,'w')
		write_file.write(read_file)
		open_file.close()
		write_file.close()