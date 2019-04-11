# CBECC-com XML file parser
#
# This script parses the CBECC-com xml file and outputs an excel document with information about the spaces, thermal zones, and HVAC system
# The file type must be .cibdx or .xml in order for this script to work properly.
# Save this script in the same folder as the CBECC-com file location.

### Paste the name of the file including the extension here:
file = ('Presidio Knolls 100CD_No ERV.cibd16x')

from lxml import etree as ET
import pandas as pd

filename = file.split('.')[0]

tree = ET.parse(file)
root = tree.getroot()

### Space Variables
spcname = []
spcstory = []
spccond = []
spcthm = []
spcfunc = []
spcstory = []
spclight = []
spcequip = []

### Thermal Zone Variables
thmname = []
thmcond = []
thmventsrc = []
thmventctrl =[]
thmventspec = []
thmprimsys = []
thmsecsys = []
thmventsys = []

### Air System Variables

### Zone System Variables
znsysname = []
znsystype = []
znsysfanctrl = []

znsyscoolname = []
znsyscooltype = []
znsyscoolwin = []
znsyscoolwout = []
znsysnetcoolcap = []
znsysgrscoolcap = []
znsyscoolEER = []
znsyscoolSEER = []

znsysheatname = []
znsysheattype = []
znsysheatwin = []
znsysheatwout = []
znsysnetheatcap = []
znsysgrsheatcap = []

znsysfanflow = []
znsysfanname = []


### Parse Space Variables
for space in root.iter('Spc'):
    spcname.append(space.find('Name').text)
    spccond.append(space.find('CondgType').text)
    spcthm.append(space.find('ThrmlZnRef').text)
    spcfunc.append(space.find('SpcFunc').text)
    spcstory.append(space.getparent().find('Name').text)
    try:
        spclight.append(float(space.find('IntLPDReg').text))
    except AttributeError:
        spclight.append('- default -')
    try:
        spcequip.append(float(space.find('RecptPwrDens').text))
    except AttributeError:
        spcequip.append('- default -')

### Parse Thermal Zone Variables
for thmlzn in root.iter('ThrmlZn'): 
    thmname.append(thmlzn.find('Name').text)
    try:
        thmcond.append(thmlzn.find('Type').text)
    except AttributeError:
        thmcond.append('- default -')
    try:
        thmventsrc.append(thmlzn.find('VentSrc').text)
    except AttributeError:
        thmventsrc.append('- default -')
    try:
        thmventctrl.append(thmlzn.find('VentCtrlMthd').text)
    except AttributeError:
        if thmlzn.find('VentSrc').text == 'None':
            thmventctrl.append('- none -')
        else:
            thmventctrl.append('- default -')
    try:
        thmventspec.append(thmlzn.find('VentSpecMthd').text)
    except AttributeError:
        if thmlzn.find('VentSrc').text == 'None':
            thmventspec.append('- none -')
        else:
            thmventspec.append('- default -')
    try:
        thmprimsys.append(thmlzn.find('.//PriAirCondgSysRef[@index="0"]').text)
    except AttributeError:
        thmprimsys.append('- none -')
    try:
        thmsecsys.append(thmlzn.find('.//PriAirCondgSysRef[@index="1"]').text)
    except AttributeError:
        thmsecsys.append('- none -')
    try:
        thmventsys.append(thmlzn.find('VentSysRef').text)
    except AttributeError:
        thmventsys.append('- none -')

### Parse Air System Variables
# TBD

### Parse Zone System Variables
for znsys in root.iter('ZnSys'):
    znsysname.append(znsys.find('Name').text)
    znsystype.append(znsys.find('Type').text)
    znsysfanctrl.append(znsys.find('FanCtrl').text)

for zncoolcoil in root.findall('./Proj/Bldg/ZnSys/CoilClg'):
    znsyscoolname.append(zncoolcoil.find('Name').text)
    znsyscooltype.append(zncoolcoil.find('Type').text)
    try:
        znsyscoolwin.append(zncoolcoil.find('FluidSegInRef').text)
    except AttributeError:
        znsyscoolwin.append('- none -')
    try:
        znsyscoolwout.append(zncoolcoil.find('FluidSegOutRef').text)
    except AttributeError:
        znsyscoolwout.append('- none -')
    try:
        znsyscoolEER.append(float(zncoolcoil.find('DXEER').text))
    except AttributeError:
        znsyscoolEER.append('- none -')
    try:
        znsyscoolSEER.append(float(zncoolcoil.find('DXSEER').text))
    except AttributeError:
        znsyscoolSEER.append('- none -')
    try:
        znsysnetcoolcap.append(float(zncoolcoil.find('CapTotNetRtd').text))
    except AttributeError:
        znsysnetcoolcap.append('- none -')
    try:
        znsysgrscoolcap.append(float(zncoolcoil.find('CapTotGrossRtd').text))
    except AttributeError:
        znsysgrscoolcap.append('- none -')

for znheatcoil in root.findall('./Proj/Bldg/ZnSys/CoilHtg'):
    znsysheatname.append(znheatcoil.find('Name').text)
    znsysheattype.append(znheatcoil.find('Type').text)
    try:
        znsysheatwin.append(znheatcoil.find('FluidSegInRef').text)
    except AttributeError:
        znsysheatwin.append('- none -')
    try:
        znsysheatwout.append(znheatcoil.find('FluidSegOutRef').text)
    except AttributeError:
        znsysheatwout.append('- none -')
    try:
        znsysnetheatcap.append(float(znheatcoil.find('CapTotNetRtd').text))
    except AttributeError:
        znsysnetheatcap.append('- none -')
    try:
        znsysgrsheatcap.append(float(znheatcoil.find('CapTotGrossRtd').text))
    except AttributeError:
        znsysgrsheatcap.append('- none -')
    
for fan in root.findall('./Proj/Bldg/ZnSys/Fan'):
    znsysfanname.append(fan.find('Name').text)
    znsysfanflow.append(float(fan.find('FlowCap').text))


# Create Dataframes and output results to excel
spcdf = pd.DataFrame({'Space Name':spcname,'Story':spcstory,'Conditioning':spccond,'Thermal Zone':spcthm,'Space Function':spcfunc,'Lighting Power Densiy':spclight,'Equipment Power Density':spcequip})
thmdf = pd.DataFrame({'Zone Name':thmname,'Conditioning':thmcond,'Ventrilation Source':thmventsrc,'Ventilation Control Method':thmventctrl,'Ventilation Specification':thmventspec,'Primary System':thmprimsys,'Secondary System':thmsecsys,'Ventilation System':thmventsys})
znsysdf = pd.DataFrame({'Zone System Name':znsysname,'Zone System Type':znsystype,'Zone Fan Control':znsysfanctrl,'Cooling Coil':znsyscoolname,'Cooling Coil Type':znsyscooltype,'Cooling Coil Fluid In':znsyscoolwin,'Cooling Coil Fluid out':znsyscoolwout,'DX Coil EER':znsyscoolEER,'DX Coil SEER':znsyscoolSEER,'Cooling Net Capacity':znsysnetcoolcap,'Cooling Gross Capacity':znsysgrscoolcap,'Heating Coil':znsysheatname,'Heating Coil Type':znsysheattype,'Hetaing Coil Fluid In':znsysheatwin,'Heating Coil Fluid out':znsysheatwout,'Heating Capacity':znsysnetheatcap,'Heating Gross Capacity':znsysgrsheatcap,'Fan':znsysfanname,'Fan Flow':znsysfanflow})
writer = pd.ExcelWriter(filename + ' - SpaceData.xlsx', engine='xlsxwriter')
spcdf.to_excel(writer,sheet_name='Space Data')
thmdf.to_excel(writer,sheet_name='Thermal Zones')
znsysdf.to_excel(writer,sheet_name='Zone System')
writer.save()