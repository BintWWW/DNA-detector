"""
==========================================================
Programmer:  Bintao Wang
Summary:     This program will print the DNA strings and find the numbers of cag repeated in the file, it can find the percentages of c and g in DNA.

INPUT:     The files' names and the option you pick, please do the first one first, or the file will not be read.
        
OUTPUT:   DNA, numbers of cag repeat, and the percentage of c and g.

Date Last Modified:
 10/12/2016:  (mdl) Starter Kit created
 10/19/2016:  (mdl) Journal
 
========================================================== 
"""

import os

# ------ CONSTANTS for entire file ----------

# menu options
READFILE  = 1
FINDCAG   = 2
GCPERCENT = 3
EXIT      = 4
ERROR     = -1

# definition of the snip of DNA of interest
REPEAT    = "cag"

# constants for Classification Status


# ---------------------------

def getDNA(dnaFile):
    """ignoring header line, returns all DNA in file as one lowercase string; returns empty string if bad file"""

    DNA = ""
    if not os.path.exists(dnaFile):
        print("\nSORRY, the file", dnaFile, "does not exist.")
        print("Try another filename ...")

    else:
        File = open(dnaFile,'r')
        print("using data file: ",dnaFile,"\n")
        headerline = File.readline()
        headerline = headerline.strip()        
        for nextline in File:
            nextline = nextline.strip()
            nextline = nextline.lower()
            nextvalue = nextline
            DNA = DNA + nextvalue
            
        print("the DNA is: ",DNA)
        
        
        
        
    # end else

    return DNA
# ---------------------------------------------------------

def findCAGs(DNA):
    #report on all 'cag' repeats (lowercase) in a string of DNA

    #start looking in the string DNA at start(0) for cag-repeats
    print(DNA)
    first=("")
    where = DNA.find("cag",0)
    #n is number of reapeat
    n = 0
    where1= 0
    while(where!=-1):
        first=where
        print("*"*25)
        print("found first cag at: ",first)
        where1= DNA.find("cag",where+1)
        while(where1-where==3):
            #print(n,"[location:",where,"]:",DNA[where:])
            print("found another cag at: ",where1)  
            where1= DNA.find("cag",where1+3)
            where = DNA.find("cag",where+3)
            n+=1
        where=DNA.find("cag",where1)
        print("*"*25)
    
    print("cag Repeats found at bp location: ",first)
    if(first !=""):
        n+=1
    
    print("cag Repeat string is: ", "cag"*n)
    print("Length of cag string: ",n*3)
           
           
    
# ---------------------------------------------------------

def getGCpercentage(DNA):
    #return the GC percentage of a strand of DNA
    g=DNA.count("g")
    c=DNA.count("c")
    percent = ((g+c)/len(DNA))*100
    print("g and c percent is: %.2f"%percent,"%")
    

        
# ---------------------------------------------------------

def main():

    gotDNA = False   # flag to tell if we've already loaded some DNA
    DNA = ""         # string of DNA held here

    choice = -1  # bogus setting to get us started

    while (choice != EXIT):
        print ("------------------------------")
        print ("  1  -  Read DNA file")
        print ("  2  -  Find", REPEAT, "repeat");
        print ("  3  -  Report percent GC");
        print ("  4  -  EXIT");
        print ("---------------------------")
        choice = input("ENTER: ")

        # trap bad user input
        if ( (str(READFILE) <= choice) and (choice <= str(EXIT)) ):
            # force to an integer, for example "1" to 1
            choice = eval(choice)
        else:
            badInput = choice
            # force to an integer to test below
            choice = ERROR;

        # ============ 1: READ DNA FILE =============================
        if ( choice == READFILE):
            dnaFile = input("Enter DNA filename: ")
            #dnaFile = ("gene3.fna")
            DNA = getDNA(dnaFile)

            if (DNA != ""):
                gotDNA = True
                print ("First 10 nucleotides in DNA file in one string is:\n", DNA[:10])
            # end if

        # ============ 2: FIND CAG Repeats =============================
        elif (choice == FINDCAG):

            if (gotDNA):
                #start looking in the string DNA at start(0) for cag-repeats
                findCAGs(DNA)
            # end if gotDNA

            else:
                print ("You cannot search for CAGs at this time.")
                print ("Please open a file of DNA to search first.")
            # end else no file open yet


        # ============ 3: COMPUTE GC % =============================
        elif (choice == GCPERCENT):

            if (gotDNA):
                getGCpercentage(DNA)
            # end if gotDNA
            
            else:
                print ("You cannot compute GC % at this time.")
                print ("Please open a file of DNA to search first.")
            # end else no file open yet

        # ============ 4: EXIT =====================================
        elif (choice == EXIT):
            print ("Goodbye ...")

        # ============ ? HUH ? =====================================
        else:  # invalid input
            print ("ERROR: ", badInput, "is an invalid input. Try again.")

    # end WHILE input is not EXIT

    print ("\n\nDone.\n")
# end main


#-----------------------------------------------------

if __name__ == '__main__':
    main()

#-----------------------------------------------------
