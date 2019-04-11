import os, re

# This script resets various room data information from IES. 
# Make sure a copy of this script and the CBECC-com file are in the same folder when running this script.
# This script will apply to all CBECC-com files in the folder.

# WARNING: This script will reset most information to defaults in the rooms. Take care when specific hard-coded information.

# Find location of the python script and the CBECC-com file.
wkdir = os.getcwd()
directory = os.listdir(wkdir)
os.chdir(wkdir)

# Locate the CBECC-com file, find and delete the hard-coded values.
for file in directory:
    if file.endswith("cibd16"):
        open_file=open(file,'r')
        read_file=open_file.read()

        #Reset plenum
        plenum = re.compile('SupPlenumSpcRef = ..*\n..*\n   ')
        read_file = plenum.sub('', read_file)
        
        #Reset floor height and volume    
        geom = re.compile('FlrToCeilingHgt = ..*\n..*\n   ')
        read_file = geom.sub('', read_file)
        
        #Reset occupancy status
        occ = re.compile('OccFrac = ..*\n..*\n   ')
        read_file = occ.sub('', read_file)

        #Reset new
        new = re.compile('EnvStatus = ..*\n..*\n   ')
        read_file = new.sub('', read_file)

        #Reset lighting fraction
        frac = re.compile('IntLtgRegHtGnSpcFrac = ..*\n..*\n   ')
        read_file = frac.sub('', read_file)

        #Reset daylighitng control
        dl = re.compile('DayltgCtrlType = ..*\n..*\n..*\n..*\n..*\n   ')
        read_file = dl.sub('', read_file)
        
        #Reset Skylights
        sky = re.compile('SkyltReqExcpt = ..*\n..*\n   ')
        read_file = sky.sub('', read_file)

        #Reset process loads
        proc = re.compile('ElevCnt = ..*\n..*\n..*\n..*\n..*\n..*\n   ')
        read_file = proc.sub('', read_file)
        
        #Reset dwelling
        dwell = re.compile('DwellingUnitTypeCnt = ..*\n..*\n   ')
        read_file = dwell.sub('', read_file)

        write_file = open(file,'w')
        write_file.write(read_file)
        open_file.close()
        write_file.close()