import sys

def main():
    print("---------------------------")
    print("Ivaldi, The Shader Smith")
    print("---------------------------")
    
    # Get the shader main file name
    shaderName = sys.argv[1]
    print("Shader Name:", shaderName)

    try:
        shaderFile = open(shaderName, "r+")    # Open the file
        for x in shaderFile:
            print(x)
        shaderFile.close()  # close the file
        print()
    except (OSError, IOError) as e:
        print("An error occured: ", e)

if __name__ == '__main__':
    main()