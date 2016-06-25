import os
import csv

epsilon = 0.5

def countLines():
    # Get the length of whole .txt file and output it
    lines = [line.rstrip('\n') for line in open('output_flattened.txt')]            # Make a list where each element is a line from the output_flattened.txt
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

    for line in lines:
        print(line)                                                                 # Print the contents of the .txt file

    return numChars

# def binarySearch(percent, top, bottom, count):
#     if abs(percent - top) < epsilon:
#         print("Final output: ")
#         os.system("convert pb_flash.JPG -resize " + str(percent) + "% -flatten -type Grayscale input.tif")
#         os.system("tesseract -l eng input.tif output_flattened")
#         print(str(countLines()))
#         return percent
#
#     num_lines = []
#     for value in [percent, top, bottom]:
#         os.system("convert pb_flash.JPG -resize " + str(value) + "% -flatten -type Grayscale input.tif")
#         os.system("tesseract -l eng input.tif output_flattened")
#         num_lines.append(countLines())
#
#     curr_count, top_count, bot_count = num_lines
#     print("What's curr_count " + str(curr_count))
#     print("What's top_count " + str(top_count))
#
#     if curr_count < top_count:
#         print("Top: " + str(top) + " Percent: " + str((percent + top) / 2.0) + " Bottom: " + str(percent))
#         return binarySearch((percent + top) / 2.0, top, percent, top_count)
#     else:
#         print("Top: " + str(percent) + " Percent: " + str((percent + bottom) / 2.0) + " Bottom: " + str(bottom))
#         return binarySearch((percent + bottom) / 2.0, percent, bottom, bot_count)
#
#     # if num == count:
#     #     return midPercent
#     # elif num > count:
#     #     return midPercent + binarySearch(midPercent, num)
#     # elif num < count:
#     #     return binarySearch(midPercent, num)
#     # else:
#     #     print("Error")

def binarySearch(percent, top, bottom, count):
    for i in range(0,10):
        print("Iteration #" + str(i))
        if abs(percent - top) < epsilon:
            print("Final output: ")
            os.system("convert pb_flash.JPG -resize " + str(percent) + "% -flatten -type Grayscale input.tif")
            os.system("tesseract -l eng input.tif output_flattened")
            print(str(countLines()))
            return percent

        num_lines = []
        
        for value in [percent, top, bottom]:
            os.system("convert pb_flash.JPG -resize " + str(value) + "% -flatten -type Grayscale input.tif")
            os.system("tesseract -l eng input.tif output_flattened")
            num_lines.append(countLines())

        curr_count, top_count, bot_count = num_lines
        print("What's curr_count " + str(curr_count))
        print("What's top_count " + str(top_count))

binarySearch(50, 100, 0, 0)
