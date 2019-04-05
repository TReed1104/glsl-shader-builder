import sys

def main():
    print("---------------------------")
    print("Ivaldi, The Shader Smith")
    print("---------------------------")
    
    # Get the shader main file name
    shaderName = sys.argv[1]
    print("Shader Name:", shaderName)
    shaderFile = open(shaderName, "r+")    # Open the file
    for x in shaderFile:
        print(x)
    shaderFile.close()  # close the file
    print()

if __name__ == '__main__':
    main()