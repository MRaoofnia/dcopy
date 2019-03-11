import os
import subprocess
import sys

def main(args):
    departure = ""
    destination  = ""
    extensions = []
    limit = 255
    if len(args) < 3:
        departure = input("Enter the path to copy .xlsx files, please: ")
        destination = input("Enter the destination path, please: ")
    else:
        departure = args[1]
        destination = args[2]
    
    #error detection part
    if not os.path.isdir(departure):
        print("Error! '%s' is not directory." %(departure), file = sys.stderr)
        exit(1)
    if not os.path.isdir(destination):
        print("Error! '%s' is not directory." %(destination), file = sys.stderr)
        exit(2)
    if (args[3] == "-l" and len(args) < 5) or (args[4] == "-l" and len(args) < 6):
        print("Error! please enter a number for limitation after -l", file = sys.stderr)
        exit(3)
    
    if args[3] == "-l":
        limit = int(args[4])
    else:
        limit = int(args[5])
        extensions = args[3].split(',')

    


    os.chdir(departure)
    


##########################
if __name__ == "__main__":
    main(sys.argv)
##########################