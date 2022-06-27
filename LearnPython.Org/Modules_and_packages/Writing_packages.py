# Packages are namespaces containing multiple packages and modules. 
# They're just directories, but with certain requirements. Like the following : 

# Modules_and_packages/ 
#                    NineLife/ <- a package
#                            __init__.py <- this indicates the directory it's in is a Python package
#                            NineHealth.py <- a module inside package
#                    Writing_packages.py <- from here, we import modules from packages

from NineLife import NineHealth

myHealth = NineHealth.NineHealth()
print(myHealth)

