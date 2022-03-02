from tkinter.filedialog import askopenfile
import tkinter.ttk as ttk
import tkinter as tk
from json import loads
from tkinter import messagebox as msgdlg

def OpenFile():
    try:
        f = askopenfile()
    except FileNotFoundError:
        msgdlg.showerror("File Not Found", "Error 404. The named File does not exist.")


def main():
    root = tk.Tk()
    

    root.mainloop()

if __name__ == '__main__':
  main()
