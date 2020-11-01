import argparse
import logging

import sys, os
sys.path.append(os.path.abspath('..')) # To find local version of the library

from PySide2 import QtCore, QtWidgets

from MetisPy import ROOT_DIR
from MetisPy import __appname__, __version__

from MetisPy.canvas.app import MainWindow
from MetisPy.utils.logger import logger 



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", "-V", action="store_true", help="show version")
    parser.add_argument("--logger-level",
                        default="info",
                        choices=["debug", "info", "warning", "fatal", "error"],
                        help="logger level",
                        )
    
    args = parser.parse_args()

    if args.version:
        print("{0} {1}".format(__appname__, __version__))
        sys.exit(0)
    
    logger.setLevel(getattr(logging, args.logger_level.upper()))

    logger.info("{0} {1}".format(__appname__, __version__))    

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)

    win = MainWindow()
    
    win.show()
    win.raise_()

    sys.exit(app.exec_())

    

if __name__ == "__main__":
    main()