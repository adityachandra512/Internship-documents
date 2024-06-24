from tkinter import *
from PIL import ImageTk,Image
import requests
import json
root=Tk()
root.title('weateher app')
root.iconbitmap('notepad.ico')
root.geometry("400x40")
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=0548D6AB-0241-4619-B95D-C20BEE388C69


try:
    api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=0548D6AB-0241-4619-B95D-C20BEE388C69")
    api=json.loads(api_request.content)
    city=api[0]['ReportingArea']
    quality=api[0]['AQI']
    category=api[0]['Category']['Name']
except Exception as e:
    api="error..."

myLable=Label(root,text=city+"Air quality" + str(quality)+" "+category,font=("Helvetica",20),background="green")
myLable.pack()
root.mainloop()