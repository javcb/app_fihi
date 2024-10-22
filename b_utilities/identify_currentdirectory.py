#************************************ReadMe*******************************************
# This script is used to get the parent directory of the current script
#
#**********************************End ReadMe*******************************************

import os

# Get the path of the current script
script_path = os.path.abspath(__file__)

# Get the directory one level above the current script
parent_dir = os.path.dirname(os.path.dirname(script_path))

# Print the parent directory
print("Parent directory:", parent_dir)