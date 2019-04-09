# Import Libraries
import os
import shutil
import re
import csv

# Define working directory
wkdir = os.getcwd()

# Define folder lists
BaseList = ['BaseModel','BatchProcess']
StageList = ['Stage1','Stage2','Stage3','Stage4']
CZList = ['CZ01','CZ02','CZ03','CZ04','CZ05','CZ06','CZ07','CZ08','CZ09','CZ10','CZ11','CZ12','CZ13','CZ14','CZ15','CZ16']

# Make temporary directories
BaseFolder = []
for folder in BaseList:
	BaseFolder.append(os.path.join(wkdir,folder))
StageFolder = []
for folder in StageList:
	os.mkdir(os.path.join(wkdir,folder))
	StageFolder.append(os.path.join(wkdir,folder))
CZFolder = []
for folder in CZList:
	os.mkdir(os.path.join(wkdir,folder))
	CZFolder.append(os.path.join(wkdir,folder))
print("Temporary folders created")

# From Base directory of python script, copy BaseModels to Stage1
os.chdir(BaseFolder[0])
src = os.listdir(BaseFolder[0])
for file in src:
	if file.endswith(".cibd16"):
		shutil.copy(file,StageFolder[0])

# From Stage1, rename to CZ01_N_ and file name to Stage2, 3, 4, and CZ01
os.chdir(StageFolder[0])
src = os.listdir(StageFolder[0])
for file in src:
	os.rename(file, file.replace(file, 'CZ01_N_' + file))
src = os.listdir(StageFolder[0])
for file in src:
	if file.endswith(".cibd16"):
		shutil.copy(file,StageFolder[1])
		shutil.copy(file,StageFolder[2])
		shutil.copy(file,StageFolder[3])
		shutil.copy(file,CZFolder[0])
		
# From Stage2, 3, and 4, rename, change orientation in CBECC-com file, and paste to CZ01
# Define list for orientation and azimuth
OriList = ['_N_','_S_','_E_','_W_']
AziList = ['BldgAz = 0','BldgAz = 180','BldgAz = 90','BldgAz = 270',]

# Skip North orientation since the base model should already be in the north orientation.
for folder,ori,azi in zip(StageFolder,OriList,AziList):
	# Skip North
	if folder == StageFolder[0]:
		pass
	else:
		# Rename the '_N_' to new orientation
		os.chdir(folder)
		[os.rename(f, f.replace('_N_', ori)) for f in os.listdir('.') if not f.startswith('.')]
		# Replace building azimuth to corresponding orientation
		src = os.listdir(folder)
		for file in src:
			if file.endswith(".cibd16"):
				open_file=open(file,'r')
				read_file=open_file.read()
				regex = re.compile('BldgAz = 0')
				read_file = regex.sub(azi, read_file)
				write_file = open(file,'w')
				write_file.write(read_file)
				shutil.copy(file,CZFolder[0])
print("Stage files copied")

# From CZ01, paste to CZ02-CZ16 and BatchProcess. Replace CZ01 to BatchProcess.
os.chdir(CZFolder[0])
src = os.listdir(CZFolder[0])
for file in src:
	for folder in CZFolder:
		if folder == CZFolder[0]:
			folder = BaseFolder[1]
		shutil.copy(file,folder)	

# Define climate zone and city 
replaceclim = ['"ClimateZone1"','"ClimateZone2"','"ClimateZone3"','"ClimateZone4"','"ClimateZone5"','"ClimateZone6"','"ClimateZone7"','"ClimateZone8"','"ClimateZone9"','"ClimateZone10"','"ClimateZone11"','"ClimateZone12"','"ClimateZone13"','"ClimateZone14"','"ClimateZone15"','"ClimateZone16"']
replacecity = ['ARCATA_725945','SANTA-ROSA_724957','OAKLAND_724930','SAN-JOSE-INTL_724945','SANTA-MARIA_723940','TORRANCE_722955','SAN-DIEGO-LINDBERGH_722900','FULLERTON_722976','BURBANK-GLENDALE_722880','RIVERSIDE_722869','RED-BLUFF_725910','SACRAMENTO-EXECUTIVE_724830','FRESNO_723890','PALMDALE_723820','PALM-SPRINGS-INTL_722868','BLUE-CANYON_725845']

# Rename and set climate zone and city to corresponding climate zone
for CZ,clim,city,folder in zip(CZList,replaceclim,replacecity,CZFolder):
	# Skip CZ01
	if CZ == CZList[0]:
		pass
	else:
		# Rename CZ01 to new climate zone
		os.chdir(folder)
		[os.rename(f, f.replace('CZ01', CZ)) for f in os.listdir('.') if not f.startswith('.')]
		# Replace the Climate Zone and City in CBECC-com to corresponding climate zone
		src = os.listdir(folder)
		for file in src:
			if file.endswith(".cibd16"):
				open_file=open(file,'r')
				read_file=open_file.read()
				regex = re.compile('"ClimateZone1"')
				read_file = regex.sub(clim, read_file)
				regex = re.compile('ARCATA_725945')
				read_file = regex.sub(city, read_file)	
				write_file = open(file,'w')
				write_file.write(read_file)
				shutil.copy(file,BaseFolder[1])
				open_file.close()
				write_file.close()
print("Files for all other climate zones created")
				
# Create .csv with all file names in BatchProcess
os.chdir(BaseFolder[1])
src = os.listdir(BaseFolder[1])
with open(os.path.join(BaseFolder[1],'_filelist.csv'), "w", newline='') as csv_file:
	for line in src:
		if line.endswith(".cibd16"):
			line = line.replace('.cibd16','')
			csv_file.write('{}\n'.format(line))
print("File list CSV created")
			
# Clear temporary directories	
for folder in StageFolder:
	shutil.rmtree(folder)
for folder in CZFolder:
	shutil.rmtree(folder)
print("Temporary folders cleared")