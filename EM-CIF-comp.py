#! /usr/bin/env python

import math

### compare structure factors from x-ray structure to those from expeirmental data

output = open("xraycom.csv","w")

#######################################
#### files to work on
emfile = "microED_dataset.txt"      # microED file
ciffile = "inhouse_lysozyme.cif"    # cif file
#######################################

## open xray sructure cif file and make dictionaries 

xrayspotsdic = {}
with open(ciffile) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split()
        xrayspotsdic[(single[3],single[4],single[5])] = single[7]


## open experimental data file and make dictionaries

expdatadic = {}
with open(emfile) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split()
        expdatadic[(single[0],single[1],single[2])] = single[3]

emdataformean = []
xraydataformean = []
goodindices = []

for i in expdatadic:
    if i in xrayspotsdic:
        if xrayspotsdic[i] != "?":
            if float(xrayspotsdic[i]) != 0:
                print (i, expdatadic[i],xrayspotsdic[i], float(expdatadic[i])/float(xrayspotsdic[i]))
                output.write("%s,%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(expdatadic[i]),float(xrayspotsdic[i]),float(i[0])+float(i[1]),float(expdatadic[i])/float(xrayspotsdic[i])))
                emdataformean.append(float(expdatadic[i]))
                xraydataformean.append(float(xrayspotsdic[i]))
                goodindices.append(i)
                
#### do some statistics
ssem = 0
ssxray = 0
ssxy = 0



emmean = sum(emdataformean)/len(emdataformean)
xraymean = sum(xraydataformean)/len(xraydataformean)
for i in goodindices:
    ssem = ssem+(float(expdatadic[i])-emmean)**2
    ssxray = ssxray+(float(xrayspotsdic[i])-xraymean)**2
    ssxy = ssxy + (float(expdatadic[i])-emmean)*(float(xrayspotsdic[i])-xraymean)
r= ssxy/math.sqrt(ssem*ssxray)

print "Correlation coeff: %s" % r