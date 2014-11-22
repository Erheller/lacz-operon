# What my program can do:
    # parse and interpret lines of a specific format
    # solve simple IPOZY problems based on that format
# What I need it to do:
    # have a random generator
    # user inputs


# imports the regular expression library
import re

# opens the text file that contains the problems
fName = "geneReg.txt"
fHandle = open(fName)

problemIndex = 0
# parses each line
for line in fHandle:
    
    # '//' comments a line
    if re.search('//', line):
        continue
        
    # if it's not a commented line, check if it's in the supported format
    elif re.search('[0-2][0-1][1-2][0-1]{2}[0-2][1][1-2][0-1]{2}$', line):
    
        problemIndex += 1
        if problemIndex < 10:
            foo = 1
        elif problemIndex < 100:
            foo = 2
        elif problemIndex < 1000:
            foo = 3
        else:
            print "You're crazy! Take a break!"
            foo = 4
        print "\n\n              ------------" + "-" * foo + "\n              | Problem", problemIndex, "|"
        
        # grabs each number and sets it to a variable
        i = int(line[0:1])
        p = int(line[1:2])
        o = int(line[2:3])
        z = int(line[3:4])
        y = int(line[4:5])
        i2 = int(line[5:6])
        p2 = int(line[6:7])
        o2 = int(line[7:8])
        z2 = int(line[8:9])
        y2 = int(line[9:10])



        
        #print i, p, o, z, y
        
        
        # sets the raw data to strings and print the characteristics of the chromosome
        error = 0
        
        
        if i == 0:
            iFinal = '-'
        elif i == 1:
            iFinal = '+'
        elif i == 2:
            iFinal = 'S'
        else:
            print "Uh, something's not right with i."
            error = 1
        
        if p == 1:
            pFinal = '+'
        elif p == 0:
            pFinal = '-'
        else:
            print "Uh, something's not right with p."
            error = 1
        
        if o == 1:
            oFinal = '+'
        elif o == 2:
            oFinal = 'C'
        else:
            print "Uh, something's not right with o."
            error = 1
        
        if z == 0:
            zFinal = '-'
        elif z == 1:
            zFinal = '+'
        else:
            print "Uh, something's not right with z."
            error = 1

        if y == 0:
            yFinal = '-'
        elif y == 1:
            yFinal = '+'
        else:
            print "Uh, something's not right with y."
            error = 1

            
        if i2 == 0:
            i2Final = '-'
        elif i2 == 1:
            i2Final = '+'
        elif i2 == 2:
            i2Final = 'S'
        else:
            print "Uh, something's not right with i2."
            error = 1
        
        if p2 == 1:
            p2Final = '+'
        elif p2 == 0:
            p2Final = '-'
        else:
            print "Uh, something's not right with p2."
            error = 1
        
        if o2 == 1:
            o2Final = '+'
        elif o2 == 2:
            o2Final = 'C'
        else:
            print "Uh, something's not right with o2."
            error = 1
        
        if z2 == 0:
            z2Final = '-'
        elif z2 == 1:
            z2Final = '+'
        else:
            print "Uh, something's not right with z2."
            error = 1

        if y2 == 0:
            y2Final = '-'
        elif y2 == 1:
            y2Final = '+'
        else:
            print "Uh, something's not right with y2."
            error = 1
            
            
        
        # yay, an error message!
        if error == 1:
            print "Yeah, there was an error for that one. Oops."
            continue
        
        print "------------------------------------------\n|   I" + iFinal, "P" + pFinal, "O" + oFinal, "Z" + zFinal, "Y" + yFinal, "/", "F'", "I" + i2Final, "P" + p2Final, "O" + o2Final, "Z" + z2Final, "Y" + y2Final, "  |\n------------------------------------------"
        
        userInput = raw_input ( 'Type "hint", "skip", or just hit enter.\n> ' )
        
        if userInput == "hint":
            
            # prints the characteristics of chromosome 1
            print "\n\n\n--------------------------------------------------\nCharacteristics of chromosome 1:"
            
            if p == 1:
                print "    Genes can be transcribed (working promoter)"
                
                if o == 2:
                    print "    Operator is nonrepressible (mutant constitutive operator)"
                elif o == 1:
                    print "    Operator is repressible (wild-type operator)"
                    
                if z == 1:
                    print "    Z is activated"
                elif z == 0:
                    print "    Z is inactivated"
                    
                if y == 1:
                    print "    Y is activated"
                elif y == 0:
                    print "    Y in inactivated"
                
            elif p == 0: 
                print "    Genes cannot be transcribed (defective promoter)"
            
            
            
            
            # prints the characteristics of chromosome 2
            print "\nCharacteristics of chromosome 2:"
            
            if p2 == 1:
                print "    Genes can be transcribed (working promoter)"
                
                if o2 == 2:
                    print "    Operator is nonrepressible (mutant constitutive operator)"
                elif o2 == 1:
                    print "    Operator is repressible (wild-type operator)"
                    
                if z2 == 1:
                    print "    Z is activated"
                elif z2 == 0:
                    print "    Z is inactivated"
                    
                if y2 == 1:
                    print "    Y is activated"
                elif y2 == 0:
                    print "    Y in inactivated"
                
            elif p2 == 0: 
                print "    Genes cannot be transcribed (defective promoter)"
            
            
            # prints the status of the I gene
            print "\nStatus of repressor:"
            
            if i >= i2:
                ieffective = i
                print "    The highest level repressor is I" + iFinal
            
            elif i2 > i:
                ieffective = i2
                print "    The highest level repressor is I" + i2Final
                
            else:
                print "    Um, this is embarressing. Logic doesn't work anymore."
        
            print "--------------------------------------------------"
            userInput = raw_input ( "\n\n\nPress enter to see the answer...\n" )
        
        elif userInput == "skip":
            continue
            
        
        if i >= i2:
            ieffective = i
        
        elif i2 > i:
            ieffective = i2
            
        else:
            print "  Um, this is embarressing. Logic doesn't work anymore."








        # here's the solver
        
        # chromosome 1
        # no promoter, no transcription
        if p == 0:
            zinduced = 0
            znotinduced = 0
            yinduced = 0
            ynotinduced = 0
        # there's a promoter
        elif p == 1:
        
            # if both I genes are recessive then there's no inhibitor produced
            if ieffective == 0:
                if z == 1:
                    zinduced = 1
                    znotinduced = 1
                elif z == 0:
                    zinduced = 0
                    znotinduced = 0
                if y == 1: 
                    yinduced = 1
                    ynotinduced = 1
                elif y == 0:
                    yinduced = 0
                    ynotinduced = 0
            
            # if the dominant I gene is I+, then the regular inhibitor is produced
            if ieffective == 1:
            
                # if the operator is wild-type, then an inducer needs to be present for the protein to be expressed
                if o == 1:
                    if z == 1:
                        zinduced = 1
                        znotinduced = 0
                    elif z == 0:
                        zinduced = 0
                        znotinduced = 0
                    if y == 1: 
                        yinduced = 1
                        ynotinduced = 0
                    elif y == 0:
                        yinduced = 0
                        ynotinduced = 0
                
                # if the operator is mutant constitutive, then no inducer is needed for the protein to be expressed
                elif o == 2:
                    if z == 1:
                        zinduced = 1
                        znotinduced = 1
                    elif z == 0:
                        zinduced = 0
                        znotinduced = 0
                    if y == 1: 
                        yinduced = 1
                        ynotinduced = 1
                    elif y == 0:
                        yinduced = 0
                        ynotinduced = 0
            
            # if the dominant I gene is S, then a super inhibitor is produced
            if ieffective == 2:
            
                # if the operator is wild-type, then no protein is produced because the super inhibitor... inhibits it
                # I'm really great with words
                if o == 1:
                    zinduced = 0
                    znotinduced = 0
                    yinduced = 0
                    ynotinduced = 0

                
                # if the operator is mutant constitutive, then no inducer is needed for the protein to be expressed
                # it pretty much ignores the super inhibitor
                elif o == 2:
                    if z == 1:
                        zinduced = 1
                        znotinduced = 1
                    elif z == 0:
                        zinduced = 0
                        znotinduced = 0
                    if y == 1: 
                        yinduced = 1
                        ynotinduced = 1
                    elif y == 0:
                        yinduced = 0
                        ynotinduced = 0
        
        # let's print out the results here for the first chromosome
        # print "\n"
        # print "Z with inducer:", zinduced
        # print "Z without inducer:", znotinduced
        # print "Y with inducer:", yinduced
        # print "Y without inducer:", ynotinduced
        
        
        

        # chromosome 2
        # no promoter, no transcription
        if p2 == 0:
            z2induced = 0
            z2notinduced = 0
            y2induced = 0
            y2notinduced = 0
        # there's a promoter
        elif p2 == 1:
        
            # if both I genes are recessive then there's no inhibitor produced
            if ieffective == 0:
                if z2 == 1:
                    z2induced = 1
                    z2notinduced = 1
                elif z2 == 0:
                    z2induced = 0
                    z2notinduced = 0
                if y2 == 1: 
                    y2induced = 1
                    y2notinduced = 1
                elif y2 == 0:
                    y2induced = 0
                    y2notinduced = 0
            
            # if the dominant I gene is I+, then the regular inhibitor is produced
            if ieffective == 1:
            
                # if the operator is wild-type, then an inducer needs to be present for the protein to be expressed
                if o2 == 1:
                    if z2 == 1:
                        z2induced = 1
                        z2notinduced = 0
                    elif z2 == 0:
                        z2induced = 0
                        z2notinduced = 0
                    if y2 == 1: 
                        y2induced = 1
                        y2notinduced = 0
                    elif y2 == 0:
                        y2induced = 0
                        y2notinduced = 0
                
                # if the operator is mutant constitutive, then no inducer is needed for the protein to be expressed
                elif o2 == 2:
                    if z2 == 1:
                        z2induced = 1
                        z2notinduced = 1
                    elif z2 == 0:
                        z2induced = 0
                        z2notinduced = 0
                    if y2 == 1: 
                        y2induced = 1
                        y2notinduced = 1
                    elif y2 == 0:
                        y2induced = 0
                        y2notinduced = 0
            
            # if the dominant I gene is S, then a super inhibitor is produced
            if ieffective == 2:
            
                # if the operator is wild-type, then no protein is produced because the super inhibitor... inhibits it
                # I'm really great with words
                if o2 == 1:
                    z2induced = 0
                    z2notinduced = 0
                    y2induced = 0
                    y2notinduced = 0

                
                # if the operator is mutant constitutive, then no inducer is needed for the protein to be expressed
                # it pretty much ignores the super inhibitor
                elif o2 == 2:
                    if z2 == 1:
                        z2induced = 1
                        z2notinduced = 1
                    elif z2 == 0:
                        z2induced = 0
                        z2notinduced = 0
                    if y2 == 1: 
                        y2induced = 1
                        y2notinduced = 1
                    elif y == 0:
                        y2induced = 0
                        y2notinduced = 0
        
        # let's print out the results here for the second chromosome
        # print "\n"
        # print "Z with inducer:", z2induced
        # print "Z without inducer:", z2notinduced
        # print "Y with inducer:", y2induced
        # print "Y without inducer:", y2notinduced

        
        # if a protein is expressed in at least one of the two chromosomes, the stored variable will be at least 1.
        zFinalInduced = zinduced + z2induced
        zFinalNotInduced = znotinduced + z2notinduced
        yFinalInduced = yinduced + y2induced
        yFinalNotInduced = ynotinduced + y2notinduced


        
        print "\n\n--------------------------------------------------\nWhen an inducer is present:"
        
        if zFinalInduced >= 1:
            print "    Z is expressed"
        else:
            print "    Z is NOT expressed"
            
        if yFinalInduced >= 1:
            print "    Y is expressed"
        else:
            print "    Y is NOT expressed"


            
        print "\nWhen NO inducer is present:"
        
        if zFinalNotInduced >= 1:
            print "    Z is expressed"
        else:
            print "    Z is NOT expressed"
            
        if yFinalNotInduced >= 1:
            print "    Y is expressed"
        else:
            print "    Y is NOT expressed"        

        print "--------------------------------------------------"    
            
            
        userInput = raw_input ( "\n\nPress enter to go on to the next question...\n" )
            
print "Could not find any more problems. Terminating."