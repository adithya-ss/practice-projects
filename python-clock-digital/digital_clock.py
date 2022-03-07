from tkinter import *
from time import *

# Update time every second, which should be displayed on the clock.
def update_time():
    time_str = strftime("%I:%M:%S %p")
    time_label.config(text=time_str)

    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    window.after(1000,update_time)

# Create a window to display the clock
window = Tk()
window.title("Clock")
window.configure(bg="black")

time_label = Label(window, font=("Consolas",28), fg="yellow", bg="black")
time_label.pack()

date_label = Label(window, font=("Consolas",16), fg="white", bg="black")
date_label.pack()

day_label = Label(window, font=("Consolas",16), fg="white", bg="black")
day_label.pack()

# The time, date and day are in the same function, as it has to be updated regularly.
# Post midnight, the day and date should change after the 1 second recursive call.
# If day and date are kept seperately, they need to have their own recursive calls, if not they wont get updated.
update_time()

window.mainloop()