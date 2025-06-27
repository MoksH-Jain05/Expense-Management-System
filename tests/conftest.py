import os
import sys

project_root = os.path.join(os.path.dirname(__file__),"..")
sys.path.insert(0,project_root)
print(project_root)

# here dirname defines the path of current directory
# .. defines the parent i.e is root
# join is used to join dir with root

# after that it is inserted at path 