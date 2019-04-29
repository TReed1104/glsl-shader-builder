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
    inputMutualExclusionGroup.add_argument("-i", "--input", dest='input', help='Specify the GLSL source file to be compile.', type=str)
    inputMutualExclusionGroup.add_argument("-a", "--all", dest='input_directory', help='Compile all shaders found in the supplied directory, using their source file names as their output file names.', type=str)
    # Output arguments
    parser.add_argument("-o", "--output", dest='output', help='Where to output the compiled shader to. If --all is used, this argument will be ignored.', type=str)
    # Parse the arguments to a usable form
    arguments = parser.parse_args()

    # Program runtime
    print("---------------------------\nIvaldi, The Shader Smith\n---------------------------")
    outputDirectoryName = "output"
    
    # Create the output directory to output our file to
    try:
        os.makedirs(outputDirectoryName)
        print(">> Creating the output directory")
    except FileExistsError:
        pass

    # Execute the supplied flags input flags
    if arguments.input is not None:                                                                         # If the --input flag been supplied with an input, compile it
        print(">> Building shader:", arguments.input)
        mainShaderSource = readFileToString(arguments.input)                                                # Read the shader source file
        if mainShaderSource != "":
            builtShaderSource = executeIncludes(mainShaderSource)                                           # Compile the shader file, compiling down the includes/requires
            if (arguments.output is not None):
                writeStringToFile(outputDirectoryName + "/" + arguments.output, builtShaderSource)          # Write the compiled shader string to our target file
                print(">> Shader source saved to:", outputDirectoryName + "/" + arguments.output)
            else:
                # TODO: fix this to work with \ or / directories
                fileName = arguments.input.split("\\")[-1]                                                  # Trims the input file name down to its last sub-string, which SHOULD be the file name
                writeStringToFile(outputDirectoryName + "/" + fileName, builtShaderSource)                  # Write the compiled shader string to our target file
                print(">> Shader source saved to:", outputDirectoryName + "/" + fileName)
        else:
            print(">>>> ERROR! - unable to open main source file, please check the entered name")
    elif arguments.input_directory is not None:                                                             # If the --all flag is set, compile all the files in the supplied directory
        print(">> Building shader:", arguments.input)
        for fileToCompile in os.listdir(arguments.input_directory):
            mainShaderSource = readFileToString(os.path.join(arguments.input_directory, fileToCompile))     # Read the shader source file
            if mainShaderSource != "":
                builtShaderSource = executeIncludes(mainShaderSource)                                       # Compile the shader file, compiling down the includes/requires
                writeStringToFile(outputDirectoryName + "/" + fileToCompile, builtShaderSource)             # Write the compiled shader string to our target file
                print(">> Shader source saved to:", outputDirectoryName + "/" + fileToCompile)
            else:
                print(">>>> ERROR! - unable to open main source file, please check the entered name")

if __name__ == '__main__':
    main()