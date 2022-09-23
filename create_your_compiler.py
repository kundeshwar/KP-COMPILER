
from distutils.log import error
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from winreg import SaveKey
import subprocess
compile = Tk()
compile.title("HARE KRISHANA COMPILER(IDE)")
file_path = ""

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[("Python files", "*.py")])
    with open(path, 'r') as file:
        code= file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path== "":
        path = asksaveasfilename(filetypes=[("Python files", "*.py")])
    else:
        path = file_path
    with open(path, 'w') as file:
        code= editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    Command = f'python {file_path}'
    process = subprocess.Popen(Command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0',output)

menu_bar = Menu(compile)

file_menu= Menu(menu_bar, tearoff=0)
file_menu.add_command(label='open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save as', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar= Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compile.config(menu=menu_bar)
editor = Text()
editor.pack()

code_output= Text()
code_output.pack()#it is creat output region

compile.mainloop()
