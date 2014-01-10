#! /usr/bin/env python

### compare structure factors from MTZdumped mtzfiles to MicroED suite intensity file
### prepare the mtz dump file using the following shell command
###     phenix.mtz.dump -f s -c [filename] > [output_filename]

###################################################
## User edited variables
emfile = "microED_dataset.txt"
dumpfile = "mosflm_rot.txt"
fcol = 3    # which column in MTZdump file contains F values 1st column = 0
output = open("EM-MTZ.csv","w")
###################################################


## open MTZdumped cif file and make dictionaries 

dumpdatadic = {}
with open(dumpfile) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split(',')
        if single[fcol] == "":
            single[fcol] = "0"
        dumpdatadic[(single[0],single[1],single[2])] = single[fcol]
        

for i in dumpdatadic:
    print "%s\t%s" % (i,dumpdatadic[i]) 

## open EM data file and make dictionaries

emdatadic = {}
with open(emfile) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split()
        emdatadic[(single[0],single[1],single[2])] = single[3]
        
output.write("h,k,l,%s,%s,ratio\n"% (emfile,dumpfile))
for i in emdatadic:
    if emdatadic[i] != "?":
        if i in dumpdatadic:
            if dumpdatadic[i] != "?":
                if float(dumpdatadic[i]) != 0:
                    print (i, emdatadic[i],dumpdatadic[i], float(emdatadic[i])/float(dumpdatadic[i]))
                    output.write("%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(emdatadic[i]),float(dumpdatadic[i]),float(emdatadic[i])/float(dumpdatadic[i])))