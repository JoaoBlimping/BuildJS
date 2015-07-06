import sys
import os

specialChar = "$"

loadedFiles = []

#does all the stuff
def writeFile(filename,outputFile):
    inputFile = open(filename)

    content = inputFile.readlines()

    for line in content:
        specialIndex = line.find(specialChar)

        if (specialIndex != -1):
            specialPart = line[specialIndex + 1:line.find(specialChar,specialIndex + 1)]
            specialValues = specialPart.split(" ")


            if (specialValues[0] == "include"):
                if (loadedFiles.count(specialValues[1]) == 0):
                    print "including " + specialValues[1]
                    writeFile(specialValues[1],outputFile)


            if (specialValues[0] == "insert"):
                print "inserting " + specialValues[1]
                writeFileInline(line,specialValues[1],outputFile)


        else:
            outputFile.write(line)
    inputFile.close()

    #record that this file has been loaded
    loadedFiles.append(filename)


def writeFileInline(line,filename,outputFile):
    firstSpecial = line.find(specialChar)
    secondSpecial = line.find(specialChar,firstSpecial + 1)

    writtenLine = line[:firstSpecial]
    inputFile = open(filename)

    content = inputFile.readlines()

    for l in content:
        writtenLine += l[:-1] + "_"

    writtenLine += line[secondSpecial + 1:] + "\n"

    outputFile.write(writtenLine)



def main():
    #test if the program is already over
    if (len(sys.argv) != 3):
        print "arguments wrong"
        sys.exit();

    #otherwise it's time to go
    outputFile = open(sys.argv[2],"w")

    #go to directory of the main file
    if (sys.argv[1].rfind('/') != -1):
        os.chdir(sys.argv[1][0:sys.argv[1].rfind('/')])

    writeFile(sys.argv[1][sys.argv[1].rfind('/')+1:],outputFile)
    outputFile.close()

main()
