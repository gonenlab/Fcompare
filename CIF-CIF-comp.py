#! /usr/bin/env python

### compare structure factors from x-ray structures cif file to cif file


###########################
##files
file1 = "1.cif"
file2 = "4axt-sf.cif"
############################


output = open("CIF-CIF.csv","w")

## open xray sructure cif file and make dictionaries 

xrayspotsdic = {}
with open(file1) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split()
        xrayspotsdic[(single[3],single[4],single[5])] = single[7]


## open experimental data file and make dictionaries

expdatadic = {}
with open(file2) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split()
        expdatadic[(single[3],single[4],single[5])] = single[7]
        
for i in expdatadic:
    if expdatadic[i] != "?":
        if i in xrayspotsdic:
            if xrayspotsdic[i] != "?":
                if float(xrayspotsdic[i]) != 0:
                    print (i, expdatadic[i],xrayspotsdic[i], float(expdatadic[i])/float(xrayspotsdic[i]))
                    output.write("%s,%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(expdatadic[i]),float(xrayspotsdic[i]),float(i[0])+float(i[1]),float(expdatadic[i])/float(xrayspotsdic[i])))