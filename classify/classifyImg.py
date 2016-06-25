import os
import csv
import re
import sys
import enchant

epsilon = 0.5
engCount = 0
def countLines():
    # Get the length of whole .txt file and output it
    lines = [line.rstrip('\n') for line in open('/home/ubuntu/teamyogurt/classify/output_flattened.txt')]            # Make a list where each element is a line from the output_flattened.txt
    numLines = len(lines)                                                           # Get the number of lines in the .txt file
    # print("# of lines: " + str(numLines))                                           # Output it

    numChars = 0
    for line in lines:
        numChars += len(line)
    print("# of chars: " + str(numChars))

    # Get the length of the .txt without blank lines and output it
    linesCopy = lines                                                               # Copy the list holding the .txt file
    while '' in linesCopy:
        linesCopy.remove('')                                                        # Remove the blank lines
    numWOutEmpty = len(linesCopy)                                                   # Get the number of lines in the .txt file without blank lines

    print("Content of output_flattened.txt: ")

    return numLines

def countChars():
    # lines = [line.rstrip('\n') for line in open('output_flattened.txt')]
    delimiter = '-'
    lines = open('/home/ubuntu/teamyogurt/classify/output_flattened.txt').readlines()
    joinedLines = delimiter.join(lines)
    regPattern = re.compile('[A-Za-z]+')
    foundItems = regPattern.findall(joinedLines)

    charCount = 0
    engCount = 0
    d = enchant.Dict("en_US")
    for item in foundItems:
        if d.check(item) == True:
            engCount += 1                                                       # If the item is an English word, increment the counter
        charCount = charCount + len(item)

    print("Found " + str(charCount) + " characters")
    print("Found " + str(engCount) + " English words")

    linesNoN = [line.rstrip('\n') for line in lines]                            # Get rid of newlines before printing

    while '' in linesNoN:
        linesNoN.remove('')                                                     # Also remove lines with just empty strings

    for line in linesNoN:
        print(line)                                                             # Now print each line, now that whitespace has been removed

    # return numChars
    return charCount                                                            # Also return the charCount

def searchWords():
    divisions = 10
    charByDivision = []

    for percent in range(divisions):
        os.system("convert /home/ubuntu/teamyogurt/classify/images/pb_flash.jpg -resize " + str(percent * 10) + "% -flatten -type Grayscale input.tif")
        os.system("tesseract -l eng input.tif output_flattened")
        charByDivision.append(countChars())
        percentCharDict[percent] = countChars()
        percentEngDict[percent] = engCount                                      # Now that we know how many English words there are, add that to the dictionary

percentCharDict = {}                                                            # Key = percent, Value = # of chars obtained
percentEngDict = {}                                                             # Key = percent, Value = # of english words
searchWords()
print("percentCharDict (original): " + str(percentCharDict))
percentWithMax = max(percentCharDict, key=percentCharDict.get)                          # Get the key (percent) with max value (countChars())
print("Percent yielding max charCount: " + str(percentWithMax))

percentEngWithMax = max(percentEngDict, key=percentEngDict.get)
print("Percent yielding max engCount: " + str(percentEngWithMax))
