import sys
import re
import os
from argparse import ArgumentParser

def readFileToString(shaderName):
    fileContent = ""
    try:
        shaderFile = open(shaderName, "r")  # Open the file to read
        for x in shaderFile:
            fileContent += x
        shaderFile.close()  # close the file
        return fileContent
    except (OSError, IOError) as e:
        print(">>>> ERROR! - An error occured: ", e)
        return fileContent

def writeStringToFile(fileName, stringToWrite):
    try:
        outputFile = open(fileName, "w")
        outputFile.write(stringToWrite)
        outputFile.close()
    except (OSError, IOError) as e:
        print(">>>> ERROR! - An error occured: ", e)

def executeIncludes(fileText):
    includeToken = "#include"
    linesOfText = re.split("(\n)", fileText)
    for index, line in enumerate(linesOfText):
        indexTokenStartsAt = line.find(includeToken)
        if indexTokenStartsAt != -1:
            # get the file to includes name using the index of the token, length of token and length of line.
            nameOfFileToInclude = line[(indexTokenStartsAt + len(includeToken)):len(line)]
            nameOfFileToInclude = nameOfFileToInclude.strip()  # Remove the leading or trailing spaces
            print(">>>>", includeToken, "found replacing with contents of file:", nameOfFileToInclude)
            fileTextToInclude = readFileToString(nameOfFileToInclude)
            linesOfText[index] = fileTextToInclude
    outputText = "".join(linesOfText)
    return outputText

def main():
    print("---------------------------\nIvaldi, The Shader Smith\n---------------------------")
    outputDirectoryName = "output"
    # Create the output directory to output our file to
    try:
        os.makedirs(outputDirectoryName)
        print(">> Creating the output directory")
    except FileExistsError:
        pass

    # Register the program's command line arguments
    parser = ArgumentParser(description='A lightweight GLSL preprocessor')
    parser.add_argument("-i", "--input", dest='input', help='GLSL source file to compile', default='', type=str)
    parser.add_argument("-o", "--output", dest='output', help='Where to output the compiled shader to', default='', type=str)
    arguments = parser.parse_args()

    # Program runtime
    if arguments.input != "":
        print(">> Building shader:", arguments.input)
        mainShaderSource = readFileToString(arguments.input)  # Read the shader main
        if mainShaderSource != "":
            builtShaderSource = executeIncludes(mainShaderSource)  # Compile the shader file, compiling down the includes/requires
            if (arguments.output != ""):
                writeStringToFile(outputDirectoryName + "/" + arguments.output, builtShaderSource)  # Write the compiled shader string to our target file
                print(">> Shader source saved to:", outputDirectoryName + "/" + arguments.output)
            else:
                fileName = arguments.input.split("\\")[-1]                  # trims the second parameter down to its last sub-string, which SHOULD be the file name
                writeStringToFile(outputDirectoryName + "/" + fileName, builtShaderSource)  # Write the compiled shader string to our target file
                print(">> Shader source saved to:", outputDirectoryName + "/" + fileName)
        else:
            print(">>>> ERROR! - unable to open main source file, please check the entered name")
    else:
        print(">>>> ERROR! - No input source file supplied!")

if __name__ == '__main__':
    main()