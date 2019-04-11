import os, re

wkdir = os.getcwd()
directory = os.listdir(wkdir)
os.chdir(wkdir)

for file in directory:
	if file.endswith("cibd16"):
		open_file=open(file,'r')
		read_file=open_file.read()
		regex = re.compile('TotStaticPress = 4')
		read_file = regex.sub('TotStaticPress = 6.25', read_file)
		write_file = open(file,'w')
		write_file.write(read_file)
		open_file.close()
		write_file.close()