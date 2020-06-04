import tkinter as tk
import time as tm

# https://www.youtube.com/watch?v=TiTkgTrHw5g
# John Philip Jones


class DigitalClock(object):
    def __init__(self, the_window, bg_colour, fg_colour):
        self.the_window = the_window
        self.the_window.title('Digital Clock')
        self.clock_label = tk.Label(
            self.the_window, font='ariel 80', bg=bg_colour, fg=fg_colour)
        self.clock_label.grid(row=0, column=0)
        self.display_time()

    def display_time(self):
        self.current_time = tm.strftime('%I:%M:%S %p')  # '%H:%M:%S'
        self.clock_label['text'] = self.current_time
        self.the_window.after(200, self.display_time)


my_window = tk.Tk()
my_other_window = tk.Tk()

my_digital_clock = DigitalClock(my_window, 'black', 'red')
my_digital_clock = DigitalClock(
    my_other_window, 'black', 'green')

my_window.mainloop()
