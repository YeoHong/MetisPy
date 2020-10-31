import os, sys
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR) # To find local version of the library
#print(ROOT_DIR)

__appname__ = "MetisApp"


# Semantic Versioning 2.0.0 : https://semver.org/
# 1. Major Version when you make incompatible API changes;
# 2. Minor Version when you add functinality in a backwards-compatible manner
# 3. PATCH Version when you make backwards-compatible bug fixes.
__version__ = "0.0.1"