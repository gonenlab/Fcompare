#! /usr/bin/env python

### compare structure factors from MTZdumped mtzfile to MTZdumped file
### prepare the mtz dump file using the following shell command
###     phenix.mtz.dump -f s -c [filename] > [output_filename]

#########################################################
## User variables 
dumpfile = "mosflm_stills.txt"
dumpfile2 = "mosflm_rot.txt"
output = open("MTZ-MTZ.csv","w")
fcol1 = 10          # which column contains F 1st column in number 0 1st file
fcol2 = 3           # which column contains F 1st column in number 0 2nd file
#########################################################

## open MTZdumped cif file and make dictionaries


dumpdatadic = {}
with open(dumpfile) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split(',')
        if single[fcol1] == "":
            single[fcol1] = "0"
        dumpdatadic[(single[0],single[1],single[2])] = single[fcol1]
        

for i in dumpdatadic:
    print "%s\t%s" % (i,dumpdatadic[i]) 

## open 2nd MTZdumped data file and make dictionaries

dumpdatadosdic = {}
with open(dumpfile2) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split(',')
        if single[fcol2] == "":
            single[fcol2] = "0"
        dumpdatadosdic[(single[0],single[1],single[2])] = single[fcol2]
        
output.write("h,k,l,%s,%s,ratio\n"% (dumpfile2,dumpfile))
for i in dumpdatadosdic:
    if dumpdatadosdic[i] != "?" and dumpdatadosdic[i] != "F":
        if i in dumpdatadic:
            if dumpdatadic[i] != "?" and dumpdatadic[i] != "F":
                if float(dumpdatadic[i]) != 0:
                    print (i, dumpdatadosdic[i],dumpdatadic[i], float(dumpdatadosdic[i])/float(dumpdatadic[i]))
                    output.write("%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(dumpdatadosdic[i]),float(dumpdatadic[i]),float(dumpdatadosdic[i])/float(dumpdatadic[i])))