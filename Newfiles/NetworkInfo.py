import requests
from datetime import date

class GetAPIInfo():

    def __init__(self,app):
        #Gets Data from NASA
        self.date="2020-11-20"
        dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + date).json()
    
        #fix this
        self.imgpath = r"C:\Users\filph\Repos\NASA-Daily-Wallpaper\Newfiles\Resources\sample.jpg"
        self.backuppath = r"C:\Users\filph\Repos\NASA-Daily-Wallpaper\Newfiles\Resources\space.jpg"
        self.path = ""
        self.dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + self.date).json()
        #Gets HD image URL
        self.imgurl = requests.get(self.dailyapi["hdurl"])
        #Saves image in directory and Sets as background
        

    def getApi(self):
        self.dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + self.date).json()
        self.imgurl = requests.get(self.dailyapi["hdurl"])



    def saveImg(self):
        File = open("Resources\sample.jpg","wb")
        File.write(self.imgurl.content)
        File.close()

