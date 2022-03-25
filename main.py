# import language as language
import pyttsx3
import wikipedia
import smtplib
import speedtest
import datetime as dt
import webbrowser as wb
import speech_recognition as sr
import time
import os
import pyautogui
import psutil
import pyjokes

from selenium import webdriver

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def iime():
    Time = dt.datetime.now().strftime("%I:%M:%S")
    speak("Sir The current time is ")
    speak(Time)


def date():
    Year = int(dt.datetime.now().year)
    Month = int(dt.datetime.now().month)
    Date = int(dt.datetime.now().day)
    speak("current date is ")
    speak(Date)
    speak(Month)
    speak(Year)

def jokes():
    speak(pyjokes.get_jokes())
def start_wish():
    speak("Welcome Sir,I am Curo ")
    hour = dt.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("I am Here to help you, Tell me how may i help you?")
def Speed_internet():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    print(res["download"], res["upload"], res["ping"])
    # st = Speedtest()
    # print("Your connection's Download speed is:", st.download())
    # print("Your Connection's Upload speed is:", st.upload())

def search_in_Browser():
    speak("What Should I Search For you")
    chromepath = 'C:\chromedriver\chromedriver.exe'
    search = takecommand().lower()
    webdriver.get(chromepath).open_new_tab(search+'.com')

def cpu_info():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
def about():
    speak("hello! I am curo. A voice assistant designed to make your life simple.")
    speak("This assistant is designed by two computer science students ")
    speak(
        "this assistant can perform several tasks by using voice command like - telling date and time ,searching smoething on web , emailing ,messaging , uploading files , and turn on/off your computer and lot more")
    speak("in future it will be modified and will also able to control some other appliences")
    speak("thank You sir for reviewing us")

class InstaBot():
    def __init__(self):
        self.url = "https://instagram.com"
        self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    def credentials(self):
        # self.userName = input("Enter your username \n")
        # self.passWord = input("Enter your password \n")
        self.userName = "kpkbon89"
        self.passWord = "pareekkus"
        self.search = "ratijindall"

    def login(self):
        self.driver.get(self.url)
        time.sleep(2)
        u_name = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        u_name.send_keys(self.userName)
        u_pass = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        u_pass.send_keys(self.passWord)
        submit = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        submit.click()
        time.sleep(3)

        try:
            login_pop = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div/div/div/button")
            login_pop.click()
        except:
            pass
        try:
            notif = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            notif.click()
        except:
            pass
class Facebook():
    def __init__(self):
        self.url = "https://facebook.com"
        self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
    def credintials(self):
        self.Username = "9829593419"
        self.Password = "hackerboy404@"
    def login(self):
        self.driver.get(self.url)
        user = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
        user.send_keys(self.Username)
        Pass = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
        Pass.send_keys(self.Password)
        Login_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
        Login_button.click()


def email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kushpareekpareek@gmail.com', 'hackerboy404@')
    server.sendmail('psycotechkp@gmail.com', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\Projects\\curo\\ss.png")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizning..")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry,i didn't get that please repeat")
        query = input("Enter What you want me to do")
        return "Noun"
    return query


if __name__ == '__main__':
    start_wish()
    while True:
        query = takecommand().lower()
        if 'time' in query:
            iime()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        # elif 'search' in query:



        elif 'about' in query:
            about()
        elif 'internet speed' in query:
            Speed_internet()
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                speak("Sir please Enter email address to whom you want to send email")
                to = input("Enter the email address")
                email(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play song' in query:
            songs_dir = ''
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'remember that' in query:
            speak("what should i remember ?")
            data = takecommand()
            speak("You said me to remember that" +data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
            speak("everything is noted sir")
        elif 'what i said to remember' in query:
            remember= open('data.txt','r')
            speak("You said me to remember that" +remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done Sir!")
        elif 'cpu' in query:
            cpu_info()
        elif 'joke' in query:
            jokes()
            time.sleep(3)
            exit()
        elif 'instagram' in query:
            if __name__ == "__main__":
                InstaBot = InstaBot()
                InstaBot.credentials()
                InstaBot.login()
        elif 'facebook' in query:
            speak("opening facebook sir")
            if __name__ == '__main__':
                        Facebook = Facebook()
                        Facebook.credintials()
                        Facebook.login()
        elif 'whatsapp' in query:
            os.startfile("C:\\Users\\CODXKP\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        elif 'unread mails' in query:
            os.startfile("C:\\Users\\CODXKP\\Desktop\\mail")

        elif 'offline' in query:
            quit()

