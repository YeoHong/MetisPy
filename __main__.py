import sys, os
sys.path.append(os.path.abspath('..')) # To find local version of the library

from MetisPy import ROOT_DIR
from MetisPy import __appname__

def main():
    print(__appname__)
    print(ROOT_DIR)




if __name__ == "__main__":
    main()