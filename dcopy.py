import os
import subprocess
import sys
import shutil

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
    search(departure, destination, departure, extensions)
    

def move(fromdir, todir):
    shutil.move(fromdir, todir)

def mkdir(dir):
    os.mkdir(dir)

def search(dep, des, cd, ext):
    os.chdir(cd)
    dirnames = os.listdir()
    for node in dirnames:
        if os.path.isdir(node):
            print("searching " + cd + '...')
            mkdir(cd.replace(dep,des,1) + '/' + node)
            search(dep, des, cd + '/' + node, ext)
            os.chdir("..")
        if os.path.isfile(node):
            extension = node.split('.')[-1]
            if extension in ext or len(ext) == 0:
                print('copying' + cd + '/' + node)
                newname = node[:100] + '.' + extension
                move(cd + '/' + node, cd.replace(dep,des,1) + '/' + newname)
        

##########################
if __name__ == "__main__":
    main(sys.argv)
##########################