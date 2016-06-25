import os
import csv
import re

epsilon = 0.5

def countLines():
    # Get the length of whole .txt file and output it
    lines = [line.rstrip('\n') for line in open('output_flattened.txt')]            # Make a list where each element is a line from the output_flattened.txt
    numLines = len(lines)                                                           # Get the number of lines in the .txt file
    print("# of lines: " + str(numLines))                                           # Output it

    # Get the length of the .txt without blank lines and output it
    linesCopy = lines                                                               # Copy the list holding the .txt file
    while '' in linesCopy:
        linesCopy.remove('')                                                        # Remove the blank lines
    numWOutEmpty = len(linesCopy)                                                   # Get the number of lines in the .txt file without blank lines

    return numLines

def countChars():
    # lines = [line.rstrip('\n') for line in open('output_flattened.txt')]
    delimiter = '-'
    lines = open('output_flattened.txt').readlines()
    joinedLines = delimiter.join(lines)
    regPattern = re.compile('[A-Za-z]+')
    foundItems = regPattern.findall(joinedLines)

    charCount = 0
    for item in foundItems:
        charCount = charCount + len(item)

    print("Found " + str(charCount) + " characters")
    for line in lines:
        print(line)

    return charCount

def searchWords():
    divisions = 10
    charByDivision = []

    for percent in range(divisions):
        os.system("convert pb_flash.JPG -resize " + str(percent * 10) + "% -flatten -type Grayscale input.tif")
        os.system("tesseract -l eng input.tif output_flattened")
        charByDivision.append(countChars())



searchWords()

# def binarySearch(percent, top, bottom, count):
#     if abs(percent - top) < epsilon:
#         countLinesPrinted()
#         return percent
#     num_lines = []
#     for value in [percent, top, bottom]:
#         os.system("convert pb_flash.JPG -resize " + str(value) + "% -flatten -type Grayscale input.tif")
#         os.system("tesseract -l eng input.tif output_flattened")
#         num_lines.append(countLines())

#     curr_count, top_count, bot_count = num_lines

#     if curr_count < top_count:
#         print("Top: " + str(top) + " Percent: " + str(percent) + " Bottom: " + str(bottom))
#         return binarySearch((percent + top) / 2.0, top, percent, top_count)
#     else:
#         print("Top: " + str(top) + " Percent: " + str(percent) + " Bottom: " + str(bottom))
#         return binarySearch((percent + bottom) / 2.0, percent, bottom, bot_count)

#     if num == count:
#         return midPercent
#     elif num > count:
#         return midPercent + binarySearch(midPercent, num)
#     elif num < count:
#         return binarySearch(midPercent, num)
#     else:
#         print("Error")

# binarySearch(50, 100, 0, 0)
