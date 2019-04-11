import os, re, csv
import pandas as pd

# This script creates an excel sheet with space data in tabular form. 
# Make sure a copy of this script and the CBECC-com file are in the same folder when running this script.
# This script will apply to all CBECC-com files in the folder.

# Find location of the python script and the CBECC-com file.
wkdir = os.getcwd()
directory = os.listdir(wkdir)
os.chdir(wkdir)

# Locate the CBECC-com file, find values.
for file in directory:
    if file.endswith("cibd16"):
        open_file=open(file,'r')
        read_file=open_file.read()
		
        #Find room names
        room = re.compile('Spc   "..*"')
        rooms = room.findall(read_file)
        for n, room in enumerate(rooms):
            rooms[n] = re.sub('Spc   |"', '',room)
        
        #Find Thermal Zones
        ThrmlZn = re.compile('ThrmlZnRef = "..*"')
        ThrmlZns = ThrmlZn.findall(read_file)
        for n, ThrmlZn in enumerate(ThrmlZns):
            ThrmlZns[n] = re.sub('ThrmlZnRef = |"', '',ThrmlZn)
		
        #Find Space Functions
        SpcFunc = re.compile('SpcFunc = "..*"')
        SpcFuncs = SpcFunc.findall(read_file)
        for n, SpcFunc in enumerate(SpcFuncs):
            SpcFuncs[n] = re.sub('SpcFunc = |"', '',SpcFunc)
           
        #Find LPDs
        LPD = re.compile('IntLPDReg = ..*')
        LPDs = LPD.findall(read_file)
        for n, LPD in enumerate(LPDs):
            LPDs[n] = re.sub('IntLPDReg = ', '',LPD)
        LPDs = [float(i) for i in LPDs]

        #Find plug loads
        Plug = re.compile('RecptPwrDens = ..*')
        Plugs = Plug.findall(read_file)
        for n, Plug in enumerate(Plugs):
            Plugs[n] = re.sub('RecptPwrDens = ', '',Plug)
        Plugs = [float(i) for i in Plugs]
        
        # Print results to an excel spreadsheet
        df = pd.DataFrame({'Space Name':rooms,'Thermal Zone':ThrmlZns,'Space Function':SpcFuncs,'Lighitng Power Density':LPDs,'Plug Loads':Plugs})
        writer = pd.ExcelWriter('SpaceData.xlsx', engine='xlsxwriter')
        df.to_excel(writer,sheet_name='General')
        writer.save()
        
        print("Space data generated")