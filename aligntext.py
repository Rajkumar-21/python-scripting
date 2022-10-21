import os
tw = os.get_terminal_size().columns
uinput = input("Enter your input to align in the terminal window: ")
cout= print(uinput.center(tw).title())
clft= print(uinput.ljust(tw).title())
crgt= print(uinput.rjust(tw).title())