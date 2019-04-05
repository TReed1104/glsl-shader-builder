import sys
import re
import os

def readFileToString(shaderName):
    fileContent = ""
    try:
        shaderFile = open(shaderName, "r")    # Open the file to read
        for x in shaderFile:
            fileContent += x
        shaderFile.close()  # close the file
        return fileContent
    except (OSError, IOError) as e:
        print(">> ERROR! - An error occured: ", e)
        return fileContent

def writeStringToFile(fileName, stringToWrite):
    try:
        outputFile = open(fileName, "w")
        outputFile.write(stringToWrite)
        outputFile.close()
    except (OSError, IOError) as e:
        print(">> ERROR! - An error occured: ", e)

def executeIncludes(fileText):
    includeToken = "#include "
    linesOfText = re.split("(\n)", fileText)
    for index, line in enumerate(linesOfText):
        indexTokenStartsAt = line.find(includeToken)
        if indexTokenStartsAt != -1:
            # get the file to includes name using the index of the token, length of token and length of line.
            nameOfFileToInclude = line[(indexTokenStartsAt + len(includeToken)) : len(line)]
            nameOfFileToInclude = nameOfFileToInclude.strip()          # Remove the leading or trailing spaces
            print(">>", includeToken, "found replacing with contents of file:", nameOfFileToInclude)

            fileTextToInclude = readFileToString(nameOfFileToInclude)
            linesOfText[index] = fileTextToInclude
    outputText = "".join(linesOfText)
    return outputText
    

def main():
    print("---------------------------")
    print("Ivaldi, The Shader Smith")
    print("---------------------------")
    
    if len(sys.argv) == 3:
        shaderName = sys.argv[1]                            # Get the shader main file name

        outputFileName = sys.argv[2]                        # Get the name for the output file
        mainFileText = readFileToString(shaderName)         # Read the shader main
        builtShaderString = executeIncludes(mainFileText)   # build the shader file, compiling down the includes/requires

        # Create the bin directory to output our file to
        try:
            os.makedirs("bin")
        except FileExistsError:
            print("Directory already exists")

        # Write the build shader string to our target file
        writeStringToFile("bin/" + outputFileName, builtShaderString)
    else:
        print(">> ERROR!")
        if len(sys.argv) == 1:
            print(">>>> Please enter source main file name and target file name")
        elif len(sys.argv) == 2:
            print(">>>> Please enter target file name")
        elif len(sys.argv) > 3:
            print(">>>> Too many parameters supplied")
        else:
            print(">>>> Unknown error - please contact developer")

if __name__ == '__main__':
    main()