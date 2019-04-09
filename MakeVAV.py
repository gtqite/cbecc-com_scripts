AHU = 'AHU-1/2'
HWS = 'HWS'
HWR = 'HWR'

file = open('VAV_box.txt','w')

VAV_list = []
for i in range(101,124):
    VAV_list.append('        <TrmlUnit>\n          <Name>VAV {0}</Name>\n          <Type>VAVReheatBox</Type>\n          <PriAirSegRef>{1}</PriAirSegRef>\n          <CoilHtg>\n            <Name>VAV {0} RHC</Name>\n            <Type>HotWater</Type>\n            <FluidSegInRef>{2}</FluidSegInRef>\n            <FluidSegOutRef>{3}</FluidSegOutRef>\n          </CoilHtg>\n        </TrmlUnit>'.format(i, AHU, HWS, HWR))

VAV_string = '\n'.join(VAV_list)
file.write(VAV_string)
file.close()
