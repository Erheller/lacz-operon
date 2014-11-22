# imports the rng module
import random

# opens the file
fname = "geneReg.txt"
fh = open(fname, 'w')

# prompts the user for the number of problems generated
userInput = raw_input ( "How many example problems do you want to generate?.\n> " )
foo = int(userInput)


#setup for the loop
bar = 0
numbers = [0,0,0,0,0,0,0,0,0,0]

while bar < foo:
    print "Generating problem", bar + 1
    numbers[0] = str(random.randint(0,2))
    numbers[1] = str(random.randint(0,1))
    numbers[2] = str(random.randint(1,2))
    numbers[3] = str(random.randint(0,1))
    numbers[4] = str(random.randint(0,1))
    numbers[5] = str(random.randint(0,2))
    numbers[6] = str(random.randint(0,1))
    numbers[7] = str(random.randint(1,2))
    numbers[8] = str(random.randint(0,1))
    numbers[9] = str(random.randint(0,1))
    
    hello = 0
    finalNumber = ""
    
    while hello < 10:
        finalNumber = finalNumber + numbers[hello]
        #print finalNumber
        hello +=1
        
    #print finalNumber
    
    fh.write ( finalNumber + "\n" )
    
    print "Finished writing problem to file."
    
    bar += 1
    
fh.close()

print "\nFinished generating problems. Terminating."