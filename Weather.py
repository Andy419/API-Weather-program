# tkinter is like a base GUI used for python, there are others
# but this is the simplest
import tkinter as tk
from PIL import ImageTk, Image
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key = "e69eef4bc29f5d28c7285f810bd32fb9"

Height = 500
Width = 600

def test_function(entry):
    weather = get_weather(entry)
    if weather:
        print(weather)
        path = "C:\\Users\\A3\\Documents\\GUI\\GUI-Webscraper\\weather_icons\\{}.png".format(weather[4])
        img = ImageTk.PhotoImage(Image.open(path))
        w_image.configure(image=img)
        w_image.image = img  # image reference, will not work without !
        temp_lbl.configure(text=str(weather[2]) + "°C")
        actual_place.configure(text = weather[0])
        w_conditions.configure(text=weather[5])
        country.configure(text = weather[1])
    # else:
    #     messagebox.showerror('Error', 'City not Found'.format(entry))

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        Json = result.json()
        # (City, Country, temp_celsius, icon)
        city = Json['name']   
        country = Json['sys']['country']
        temp_kelvin = Json['main']['temp']
        temp_celsius = int(temp_kelvin - 273.15)
        temp_faherheit = int((temp_kelvin - 273.15) * 9/5 + 32) 
        icons = Json['weather'][0]['icon']
        weather = Json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_faherheit, icons, weather)
        return final
    else:
        return None

# Initialize window
root = tk.Tk()

# Title for window
root.title("Weather?")


# add widgets (the meat of program) to do something inside the window

# Dimension of display box
canvas = tk.Canvas(root, height = Height, width = Width)
canvas.pack()

# background Image
background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\A3\\Documents\\GUI\\GUI-Webscraper\\landscape.png"))
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
button = tk.Button(frame, text="Search Weather", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')


# like a title with text (once again, bg is colour)
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

# For the Name to reappear
actual_place = tk.Label(root, text = "", font = ("Courier",35))
actual_place.place(relx = 0.5, rely = 0.3, relwidth = 0.5, relheight = 0.15, anchor = 'n')

# Place for the Country
country = tk.Label(root, text="", font = ("Courier", 30))
country.place(relx = 0.5, rely = 0.4, relwidth = 0.2, relheight = 0.15, anchor = 'n')

# For Image of weather (cloud or rain ect.)
w_image = tk.Label(root, image="")
w_image.place(relx = 0.3, rely = 0.4, relwidth = 0.25, relheight = 0.25, anchor = 'n')

# For the Actual temperature
temp_lbl = tk.Label(root, text='', font= ("Courier", 40))
temp_lbl.place(relx = 0.65, rely = 0.5, relwidth = 0.25, relheight = 0.15, anchor = 'n')

# For Conditions
w_conditions = tk.Label(root, text="", font = ("Courier",30) )
w_conditions.place(relx = 0.3, rely = 0.6, relwidth = 0.25, relheight = 0.15, anchor = 'n')

# To run application
root.mainloop()
