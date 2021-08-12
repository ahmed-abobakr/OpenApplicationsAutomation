import os
import webbrowser
import datetime


class OpenApplicationAutomation:
    
    
    
    def __init__(self):
        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        week_num= datetime.datetime.now().weekday()
        if(week_days[week_num] == "Friday" or week_days[week_num] == "Saturday"):
            os.startfile('"C:\\Users\\ahmed.abubakr\\Documents\\Android Studio1\\bin\\studio64.exe"')
            self.openURLInFirefox("http://jsonviewer.stack.hu/")
            self.openURLInFirefox("https://www.google.com")
        else :
            os.startfile("outlook")
            os.system('"C:\\Users\\ahmed.abubakr\\AppData\\Local\\slack\\slack.exe"')
            os.startfile('"C:\\Users\\ahmed.abubakr\\Documents\\Android Studio1\\bin\\studio64.exe"')
            self.openURLInFirefox("https://mail.google.com/mail/u/0/#inbox")
            self.openURLInFirefox("https://app.zeplin.io/")
            self.openURLInFirefox("http://jsonviewer.stack.hu/")
            self.openURLInFirefox("https://www.google.com")
                
            
    def openURLInFirefox(self, url):
        webbrowser.register('firefox',
                    None,
        webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)
    
    


automation = OpenApplicationAutomation()    



