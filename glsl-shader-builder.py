import sys

def readFile(shaderName):
    fileContent = ""
    try:
        shaderFile = open(shaderName, "r+")    # Open the file
        for x in shaderFile:
            fileContent += x
        shaderFile.close()  # close the file
        print(">> The file ", shaderName, " was read successfully!")
        return fileContent
    except (OSError, IOError) as e:
        print(">> ERROR! - An error occured: ", e)
        return fileContent

def main():
    print("---------------------------")
    print("Ivaldi, The Shader Smith")
    print("---------------------------")
    
    shaderName = sys.argv[1]                    # Get the shader main file name
    mainFileText = readFile(shaderName)          # Read the file
    print("\n", mainFileText)

if __name__ == '__main__':
    main()