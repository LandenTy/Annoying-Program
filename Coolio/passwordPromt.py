# LIBRARIES
import tkinter, sys
from controller import Phase1

# VARIABLES
password = "a super secret password"
isPasswordCorrect = False

# WINDOW
root = tkinter.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.configure(bg="#EE82EE") 

entry = tkinter.Entry(root, bd=15, fg="#C0FF00", width=290, font=('Times', 24))
entry.pack()
print(entry.get())

def on_button():
    
    if entry.get() == "a super secret password":
        
        sys.exit()
    
    else:
        
        tlabel = tkinter.Label(root, text="INCORRECT PASSWORD!", fg="#800000")
        tlabel.pack()
        Phase1()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()