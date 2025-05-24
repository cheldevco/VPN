import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


    
def server():
    print("Server: connecting to vpn server")
    time.sleep(1)
    print("conected")
    showinfo(title="vpn", message="Connected!")
    

def conect():
    window = Tk()
    window.title("Connecting to VPN")
    btn1 = Button(window, text="Connect to VPN", command=server)
    btn1.pack()
    
    window.mainloop()

root = Tk()
root.title("VPN")
lbl = Label(text="VPN")
lbl.pack()
btn = Button(text="Connect", command=conect)
btn.pack()

root.mainloop()
