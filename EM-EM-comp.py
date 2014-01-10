#! /usr/bin/env python

import math

### compare structure factors from 2 micoED suite merged intensity files

output = open("ememcomp.csv","w")

###########################################
#### files to work on
emfile = "123usf_merged.txt"    # microED file 1
emfile2 = "f_mergedint_BGS.txt" # microED file 2
##########################################

## open xray sructure cif file and make dictionaries 

file1dic = {}
with open(emfile) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split()
        file1dic[(single[0],single[1],single[2])] = single[3]



## open experimental data file and make dictionaries

expdatadic = {}
with open(emfile2) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split()
        expdatadic[(single[0],single[1],single[2])] = single[3]

## write the output
output.write("h,k,l,%s,%s,ratio\n"% (emfile,dumpfile))
expdataformean = []
file1dataformean = []
goodindices = []
for i in expdatadic:
    if i in file1dic:
        if file1dic[i] != "?":
            if float(file1dic[i]) != 0:
                print (i, expdatadic[i],file1dic[i], float(expdatadic[i])/float(file1dic[i]))
                output.write("%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(expdatadic[i]),float(file1dic[i]),float(expdatadic[i])/float(file1dic[i])))
                expdataformean.append(float(expdatadic[i]))
                file1dataformean.append(float(file1dic[i]))
                goodindices.append(i) 

#### do some statistics
ssexp = 0
ssfile1 = 0
ssxy = 0

file1mean = sum(file1dataformean)/len(file1dataformean)
expmean = sum(expdataformean)/len(expdataformean)
for i in goodindices:
    ssexp = ssexp+(float(expdatadic[i])-expmean)**2
    ssfile1 = ssfile1+(float(file1dic[i])-file1mean)**2
    ssxy = ssxy + (float(expdatadic[i])-expmean)*(float(file1dic[i])-file1mean)
r= ssxy/math.sqrt(ssexp*ssfile1)

print "Correlation coeff: %s" % r