import os
import csv
import re
import sys
import enchant

epsilon = 0.5
engCount = 0

def countChars(percent):
    # lines = [line.rstrip('\n') for line in open('output_flattened.txt')]
    delimiter = '-'
    lines = open('/home/ubuntu/teamyogurt/classify/output' + str(percent) + '.txt').readlines()
    joinedLines = delimiter.join(lines)
    regPattern = re.compile('[A-Za-z]+')
    foundItems = regPattern.findall(joinedLines)

    charCount = 0
    engCount = 0
    outputText = ""
    d = enchant.Dict("en_US")
    for item in foundItems:
        if d.check(item) == True:
            engCount += 1
	    outputText = outputText + " " + item                                                       # If the item is an English word, increment the counter
        charCount = charCount + len(item)

#    print("Found " + str(charCount) + " characters")
#    print("Found " + str(engCount) + " English words")

    linesNoN = [line.rstrip('\n') for line in lines]                            # Get rid of newlines before printing

    while '' in linesNoN:
        linesNoN.remove('')                                                     # Also remove lines with just empty strings

#    for line in linesNoN:
#        print(line)                                                             # Now print each line, now that whitespace has been removed

    # return numChars
    return (charCount, outputText)                                                           # Also return the charCount

def searchWords():
    divisions = 10
  
    os.chdir('/home/ubuntu/teamyogurt/classify') 
    for percent in range(divisions):
        os.system("convert /home/ubuntu/teamyogurt/classify/images/pb_flash.jpg -resize " + str(percent * 10) + "% -flatten -type Grayscale input" + str(percent) + ".tif")
       	os.system("tesseract -l eng input" + str(percent) + ".tif output" + str(percent))
        percentCharDict[percent] = countChars(percent)
#        percentEngDict[percent] = engCount                                      # Now that we know how many English words there are, add that to the dictionary

percentCharDict = {}                                                            # Key = percent, Value = # of chars obtained
percentEngDict = {}                                                             # Key = percent, Value = # of english words
searchWords()
#print("percentCharDict (original): " + str(percentCharDict))
#percentWithMax = max(percentCharDict, key=percentCharDict.get)                          # Get the key (percent) with max value (countChars())
#print("Percent yielding max charCount: " + str(percentWithMax))
#percentEngWithMax = max(percentEngDict, key=percentEngDict.get)
#print("Percent yielding max engCount: " + str(percentEngWithMax))

outChar = 0
outText = ""
for key in percentCharDict:
    tupData = percentCharDict[key]
    if tupData[0] > outChar:
	outText = tupData[1]
	outChar = tupData[0]

output = {}
output['textClassification'] = outText
print(output)




