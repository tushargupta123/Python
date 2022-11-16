# __init__.py helps the Python interpreter to recognise the folder as package. It also specifies the resources to be imported from the modules. If the __init__.py is empty this means that all the functions of the modules will be imported. We can also specify the functions from each module to be made available.

from .mod1 import gfg
from .mod2 import sum