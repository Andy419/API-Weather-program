# tkinter is like a base GUI used for python, there are others
# but this is the simplest
import tkinter as tk

Height = 500
Width = 600

def test_function(entry):
    print("This is the entry:", entry)

# Initialize window
root = tk.Tk()

# add widgets (the meat of program) to do something inside the window

# Dimension of display box
canvas = tk.Canvas(root, height = Height, width = Width)
canvas.pack()

# background Image
background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# bg = colour (currently in hexadecimal)
# frame is the colour/image inside the canvas
frame = tk.Frame(root, bg='#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor='n')


# a box where you can type text into
entry = tk.Entry(frame, font=40)
entry.place(relwidth = 0.65, relheight = 1)


# add a button to press
button = tk.Button(frame, text="Get Weather", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')


# like a title with text (once again, bg is colour)
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

# To run application
root.mainloop()
