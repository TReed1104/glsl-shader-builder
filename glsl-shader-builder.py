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
        print(">> The file ", shaderName, " was read successfully!")
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
            print(">> #include found", nameOfFileToInclude)

            fileTextToInclude = readFileToString(nameOfFileToInclude)
            linesOfText[index] = fileTextToInclude
    outputText = "".join(linesOfText)
    return outputText
    

def main():
    print("---------------------------")
    print("Ivaldi, The Shader Smith")
    print("---------------------------")
    
    #shaderName = sys.argv[1]                    # Get the shader main file name
    shaderName = "src/fragment_main.glsl"
    outputFileName = "fragment_test.frag"
    mainFileText = readFileToString(shaderName)         # Read the file
    builtShaderString = executeIncludes(mainFileText)
    print(builtShaderString)
    
if __name__ == '__main__':
    main()