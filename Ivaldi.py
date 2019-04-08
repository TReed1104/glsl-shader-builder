import sys
import re
import os

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
    # Create the output directory to output our file to
    try:
        os.makedirs("output")
    except FileExistsError:
        pass
    numberOfParamtersSupplied = len(sys.argv)
    if numberOfParamtersSupplied > 1 and numberOfParamtersSupplied <= 3:
        print(">> Building shader:", sys.argv[1])
        mainShaderSource = readFileToString(sys.argv[1])  # Read the shader main
        if mainShaderSource != "":
            builtShaderSource = executeIncludes(mainShaderSource)  # Compile the shader file, compiling down the includes/requires
            if (numberOfParamtersSupplied == 3):
                writeStringToFile("output/" + sys.argv[2], builtShaderSource)  # Write the compiled shader string to our target file
                print(">> Shader source saved to:", "output/" + sys.argv[2])
            else:
                fileName = sys.argv[1].split("\\")[-1]                      # trims the second parameter down to its last sub-string, which SHOULD be the file name
                writeStringToFile("output/" + fileName, builtShaderSource)  # Write the compiled shader string to our target file
                print(">> Shader source saved to:", "output/" + fileName)
        else:
            print(">>>> ERROR! - unable to open main source file, please check the entered name")
    else:
        if numberOfParamtersSupplied > 3:
            print(">> ERROR! - Too many command line parameters supplied")
        else:
            print(">> ERROR! - Please check your supplied parameters")

if __name__ == '__main__':
    main()