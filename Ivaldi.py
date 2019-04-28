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
    # Register the program's command line arguments
    parser = ArgumentParser(description='A lightweight GLSL preprocessor')
    # Inputs arguments, these are mutually exclusive
    inputMutualExclusionGroup = parser.add_mutually_exclusive_group(required=True)
    inputMutualExclusionGroup.add_argument("-i", "--input", dest='input', help='GLSL source file to compile', type=str)
    inputMutualExclusionGroup.add_argument("-a", "--all", dest='input_directory', help='Compile all shaders found in the supplied directory', type=str)
    # Output arguments
    parser.add_argument("-o", "--output", dest='output', help='Where to output the compiled shader to. If --all is used, this argument will be ignored', type=str)
    # Parse the arguments to a usable form
    arguments = parser.parse_args()

    
    # Program runtime
    print("---------------------------\nIvaldi, The Shader Smith\n---------------------------")
    outputDirectoryName = "output"  # the directory to compile the shaders into
    
    # Create the output directory to output our file to
    try:
        os.makedirs(outputDirectoryName)
        print(">> Creating the output directory")
    except FileExistsError:
        pass

    # Execute the supplied flags
    if arguments.input != "":
        # If we've been supplied with an input, compile it
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
        # TODO: Check for a compile all flag, if no compile all flag, close.

        # If there is no input, output an error
        print(">>>> ERROR! - No valid flags supplied")

if __name__ == '__main__':
    main()