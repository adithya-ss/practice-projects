import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="Select font color.")
    # Color is going to store a tuple. First value is the RGB combination, second if the hex code.
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), font_size_selection.get()))

def open_file():
    filename = askopenfilename(defaultextension=".txt",
                            file = [("All Files", "*.*"), 
                            ("Text Documents", "*.txt")])
    if filename is None:
        return
    else:
        try:
            window.title(os.path.basename(filename))
            text_area.delete(1.0,END)
            fopen = open(filename, "r")
            text_area.insert(1.0, fopen.read())
        except Exception:
            print("Could read the requested file. Please try again")
        finally:
            fopen.close()

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def save_file():
    save_filename = filedialog.asksaveasfilename(initialfile='New_file.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if save_filename is None:
        return
    else:
        try:
            window.title(os.path.basename(save_filename))
            sfile = open(save_filename, "w")
            sfile.write(text_area.get(1.0, END))
        except Exception:
            print("Could not save this file. Sorry! Please try again.")
        finally:
            sfile.close()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def about_app():
    showinfo("About MyEditor", "This is yet another simple text editor.")

def exit_from_app():
    window.destroy()

window = Tk()

window.title("MyEditor")
file = None

# Set deault window size.
window_height = 450
window_width = 850

# Centre the window on the screen.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Set default font and its size.
font_name = StringVar(window)
font_name.set("Consolas")
font_size = StringVar(window)
font_size.set("18")
text_area = Text(window, font=(font_name.get(), font_size.get()))

# Add scrollbar to the window
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
# Set text area = North + East + South + West
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

widget_frame = Frame(window)
widget_frame.grid()

# Button to change font color.
color_button = Button(widget_frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

# Button to change font nam.
font_selection = OptionMenu(widget_frame, font_name, *font.families(), command=change_font)
font_selection.grid(row=0, column=1)

# Option to change size of the font. Spinbox item, viz. a list selection.
font_size_selection = Spinbox(widget_frame, from_=1, to=100, textvariable=font_size, command=change_font)
font_size_selection.grid(row=0, column=2)

# Creating multiple drop down menus = MenuBar

menu_bar = Menu(window)
window.config(menu=menu_bar)

# File menu items
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File options", menu=file_menu)

file_menu.add_command(label="Create a new file", command=new_file)
file_menu.add_command(label="Open an existing file", command=open_file)
file_menu.add_command(label="Save this file", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit this application", command=exit_from_app)

# Edit menu items
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editing options", menu=edit_menu)

edit_menu.add_command(label="Copy this text", command=copy_text)
edit_menu.add_command(label="Cut this text", command=cut_text)
edit_menu.add_command(label="Paste text", command=paste_text)

# Help menu items
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Need help?", menu=help_menu)
help_menu.add_command(label="About this app", command=about_app)

window.mainloop()
