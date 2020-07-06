# Display Weather

# Import tkinter and tkinter.font
from tkinter import *
import tkinter.font as tkFont
from PIL import Image
from PIL import ImageTk
import requests

url = "https://us-weather-by-city.p.rapidapi.com/getweather"
headers = {
    'x-rapidapi-host': "us-weather-by-city.p.rapidapi.com",
    'x-rapidapi-key': "2b7c311c98mshd1f9398161f2ab7p1ebdd8jsn29e872848476"
    }





# Create window
window = Tk()

# Set icon
window.iconbitmap(r'weather.ico')

# Set window title, size and background color
window.geometry("500x400")
window.configure(bg = '#6DD3CE')
window.title("Weather App")

# window.resizable(0,0)

#Variable for default font
fontStyle = tkFont.Font(family = "Lato", size = 16)

bgcol = '#C8E9A0'

# Create a Frame and place it relative to window
start = Frame(window, bg = bgcol, relief='flat', borderwidth = 10)
start.place(relx = 0.025, rely = 0.025, relwidth = 0.95, relheight = 0.15)
Label(start, text = 'US Weather App', font = ("Verdana", 24), bg = bgcol).place(relwidth = 1, relheight = 1)

frame = Frame(window, bg = bgcol, relief='flat', borderwidth=10)
frame.place(relx = 0.025, rely = 0.25, relwidth = 0.95, relheight = 0.70)

prompttext = Label(frame, text = 'Enter a US city for weather: \n("City, State Code")', bg = bgcol, font=fontStyle)
prompttext.pack()

# Create Entry and add to Frame grid
e1 = Entry(frame, font=fontStyle, width = 18)
e1.focus()
e1.pack()



# Define button function
def get_weather():
    output.delete(0.0, END)
    output2.delete(0.0, END)
    output_data = ''
    output2_data = ''

    input_data= str(e1.get())
    city, state = input_data.split(',')
    querystring = {"city":city,"state":state}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    output_data = response.json()['TempF']
    forecast = response.json()['Weather']
    print(output_data)
    output.insert(END, str(output_data + " F"))
    output2.insert(END, str(forecast))
    

btn = Button(frame, text = "Get weather",  font=fontStyle, command = get_weather, bg = bgcol)
btn.pack(pady=20)

# Create Text box output and place in frame
output = Text(frame, font = fontStyle, height = 1, width = 18)
output.pack()
output2 = Text(frame, font = fontStyle, height = 1, width = 18)
output2.pack()

# Run application
window.mainloop()

