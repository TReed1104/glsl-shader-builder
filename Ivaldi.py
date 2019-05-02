import sys
import re
import os
from argparse import ArgumentParser

def readFileToString(shaderName):
    fileContent = ""
    try:
        shaderFile = open(shaderName, "r")
        for x in shaderFile:
            fileContent += x
        shaderFile.close()
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
            nameOfFileToInclude = line[(indexTokenStartsAt + len(includeToken)) : len(line)].strip()        # Get the substring containing the file to include's name, and remove the leading or trailing spaces
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
    inputMutualExclusionGroup.add_argument("-i", "--input", dest="input", help="Specify the GLSL source file to compile.", type=str)
    inputMutualExclusionGroup.add_argument("-a", "--all", nargs="?", dest="input_directory", help="Compile all shaders found in the specified directory. The default value for this argument is 'shaders'. Files compiled by this mode use their source file names.", type=str, const="shaders")
    # Output arguments
    parser.add_argument("-o", "--output", dest="output", help="Where to output the compiled shader to. If --all is used, this argument will be ignored.", type=str)
    arguments = parser.parse_args()

    # Program runtime
    print("---------------------------\nIvaldi, The Shader Smith\n---------------------------")
    outputDirectoryName = "output"
    try:
        os.makedirs(outputDirectoryName)
        print(">> Creating the output directory")
    except FileExistsError:
        pass

    # Execute the supplied flags input flags
    if arguments.input is not None:
        # If the --input flag been supplied with an input, compile it
        print(">> Building shader:", arguments.input)
        mainShaderSource = readFileToString(arguments.input)
        if mainShaderSource != "":
            builtShaderSource = executeIncludes(mainShaderSource)
            if (arguments.output is not None):
                writeStringToFile(outputDirectoryName + "/" + arguments.output, builtShaderSource)
                print(">> Shader source saved to:", outputDirectoryName + "/" + arguments.output)
            else:
                fileName = os.path.basename(arguments.input)    # Trim the input string to just the file name to reuse
                writeStringToFile(outputDirectoryName + "/" + fileName, builtShaderSource)
                print(">> Shader source saved to:", outputDirectoryName + "/" + fileName)
        else:
            print(">>>> ERROR! - unable to open main source file, please check the entered name")
    elif arguments.input_directory is not None:
        # If the --all flag is set, compile all the files in the supplied directory
        for fileToCompile in os.listdir(arguments.input_directory):
            print(">> Building shader:", fileToCompile)
            mainShaderSource = readFileToString(os.path.join(arguments.input_directory, fileToCompile))
            if mainShaderSource != "":
                builtShaderSource = executeIncludes(mainShaderSource)
                writeStringToFile(outputDirectoryName + "/" + fileToCompile, builtShaderSource)
                print(">> Shader source saved to:", outputDirectoryName + "/" + fileToCompile)
            else:
                print(">>>> ERROR! - unable to open main source file, please check the entered name")

if __name__ == '__main__':
    main()