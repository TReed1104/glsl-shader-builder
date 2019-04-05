import sys

def main():
    print("-----------------------")
    print("Starting: ", sys.argv[0])
    print("-----------------------")
    for args in sys.argv:
        print(args)

    print("")

if __name__ == '__main__':
    main()