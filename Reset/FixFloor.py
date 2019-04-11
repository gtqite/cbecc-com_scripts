import os, re

# This script replaces all exterior floors with slab on grade floors. 

# You will need to set the name of the MassFloor Construction here:
MassFloor = re.compile("MassFloorU269")

# Make sure a copy of this script and the CBECC-com file are in the same folder when running this script.
# This script will apply to all CBECC-com files in the folder.

# WARNING: This script will replace ALL exterior floors to underground floors.

# Find location of the python script and the CBECC-com file.
wkdir = os.getcwd()
directory = os.listdir(wkdir)
os.chdir(wkdir)

# Locate the CBECC-com file, find and replace the floors.
for file in directory:
    if file.endswith("cibd16"):
        open_file=open(file,'r')
        read_file=open_file.read()

        # Add uninsulated floor construction to the end of the CBECC-com file
        EndOfFile = re.compile('END_OF_FILE')
        read_file = EndOfFile.sub('ConsAssm   "UninsulatedSlab F-073"\n   CompatibleSurfType = "UndergroundFloor"\n   ..\n\nEND_OF_FILE', read_file)
    
        # Replace exterior floor with underground floor
        Floor = re.compile('ExtFlr')
        read_file = Floor.sub('UndgrFlr', read_file)
        
        # Replace MassFloor contruction 
        read_file = MassFloor.sub('UninsulatedSlab F-073',read_file)        
        
        write_file = open(file,'w')
        write_file.write(read_file)
        open_file.close()
        write_file.close()