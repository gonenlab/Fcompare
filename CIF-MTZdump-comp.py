#! /usr/bin/env python

### compare structure factors from MTZdumped mtzfiles to CIF intensity file
### prepare the mtz dump file using the following shell command
###     phenix.mtz.dump -f s -c [filename] > [output_filename]
### The column that contains F will vary (WTF stupid program!)
### so you must enter which program contains the F value into the variables section


################################
## user edited variables 
ciffile = "4axt-sf.cif"        # cif file to use
dumpfile = "mosflm_rot.txt"    # MTZdump file to use
fcol = 3                       # which column in MTZdump file contains F values 1st column = 0
output = open("EM-CIF.csv","w")
################################



## open MTZdumped cif file and make dictionaries 

dumpdatadic = {}
with open(dumpfile) as reffile:
    reflines = reffile.read().splitlines()
    for i in reflines:
        single = i.split(',')
        if single[fcol] == "":
            single[fcol] = "0"
        dumpdatadic[(single[0],single[1],single[2])] = single[fcol]
        


## open EM data file and make dictionaries

cifdatadic = {}
with open(ciffile) as expfile:
    explines = expfile.read().splitlines()
    for i in explines:
        single = i.split()
        cifdatadic[(single[3],single[4],single[5])] = single[7]


output.write("h,k,l,%s,%s,ratio\n"% (ciffile,dumpfile))
for i in cifdatadic:
    if cifdatadic[i] != "?":
        if i in dumpdatadic:
            if dumpdatadic[i] != "?":
                if float(dumpdatadic[i]) != 0:
                    print (i, cifdatadic[i],dumpdatadic[i], float(cifdatadic[i])/float(dumpdatadic[i]))
                    output.write("%s,%s,%s,%s,%s,%s\n" % (i[0],i[1],i[2],float(cifdatadic[i]),float(dumpdatadic[i]),float(cifdatadic[i])/float(dumpdatadic[i])))