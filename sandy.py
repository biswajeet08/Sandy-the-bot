import os
import sys
import psutil
from selenium import webdriver
import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


app_dict = {
    'chrome': "chrome.exe", 'browser': "chrome.exe", 'notepad++': "notepad++.exe",
    'notepad': "notepad.exe", 'sticky': "StikyNot.exe", 'plus': "notepad++.exe",
    'pycharm': "pycharm64.exe", 'manager': "Taskmgr.exe", 'explorer': "explorer.exe",
    'file': "explorer.exe", 'snipping': "SnippingTool.exe", 'tool': "SnippingTool.exe", 'command': "cmd.exe",
    'prompt': "cmd.exe", 'torrent': "uToreent.exe", 'paint': "mspaint.exe"
}

app_list = ['chrome', 'browser', 'notepad++', 'plus', 'notepad', 'sticky', 'pycharm', 'manager', 'explorer', 'file',
            'word', 'excel', 'powerpoint', 'snipping', 'tool', 'command', 'prompt', 'all', 'wait', 'quit',
            'restart', 'torrent', 'paint']


def flipkart(search):
    product = search
    browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
    browser.get("https://www.flipkart.com/")
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(
        product)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
    time.sleep(5)
    do_Sandy()
    while (True):
        pass


def amazon(search):
    product = search
    browser = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
    browser.get("https://www.amazon.in/")
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys(product)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id='nav-search-submit-text']/input").click()
    time.sleep(5)
    do_Sandy()
    while (True):
        pass


def sorry():
    talk("sorry Vicky, didn't get you. Can you come again?")
    ok = listen()
    return ok


def check(check_list, check_sent):
    check_list = check_list
    check_sent = check_sent
    for ele in check_list:
        for word in check_sent:
            if ele == word:
                return ele
                break


def check2(check_list, check_sent):
    return_list = []
    check_list = check_list
    check_sent = check_sent
    for ele in check_list:
        for word in check_sent:
            if ele == word:
                return_list.append(word)
    return return_list


def search():
    search_dict = {
        'flipkart': flipkart, 'amazon': amazon, 'youtube': pywhatkit.playonyt,
        'google': pywhatkit.search,
        'wikipedia': pywhatkit.info
    }
    platform_list = ['flipkart', 'amazon', 'youtube', 'google', 'wikipedia', 'quit', 'shutdown', 'restart']
    search_for = None
    while search_for == None:
        talk('ok Vicky, what do you want me to search for?')
        search_for = listen()

    talk('and where do you want me to look for it?')
    platform = listen()
    platform = platform.split()
    var = check(platform_list, platform)
    while var not in platform_list:
        var1 = sorry()
        if var1:
            var1 = var1.split()
        var = check(platform_list, var1)
    if var in ['flipkart', 'amazon', 'youtube', 'google', 'wikipedia']:
        talk('ok Vicky, let me search for you in {0}'.format(var))
        search_dict[var](search_for)
    elif 'restart' == var:
        do_Sandy()
    elif 'quit' == var or 'shutdown' == var:
        talk('ok Vicky, I am shutting down now. bye')
        quit()
    time.sleep(5)
    do_Sandy()


def open_app():
    pass


def open_app():
    app = None
    while app == None:
        talk('ok Vicky, which application you want to open?')
        app = listen()
    app = app.split()
    app = check2(app_list, app)
    # if app not in app_list:
    while app == []:
        app2 = sorry()
        if app2:
            app2 = app2.split()
        app = check2(app_list, app2)
    for item in app:
        if item == 'wait':
            talk('ok vicky, i will wait for 5 seconds')
            time.sleep(5)
            close_app()
        elif item == 'quit':
            talk('ok Vicky, I am shutting down now. bye')
            quit()
        elif 'restart' in app:
            do_Sandy()
        else:
            os.startfile("{0}".format(app_dict[item]))

    talk('i have opened the asked applications, Vicky. do you want to open any other application?')
    answer = listen()
    while answer == None:
        talk('do you want to open any other application?')
        answer = listen()
    answer = answer.split()
    answer = check(['yes', 'no'], answer)
    while answer not in ['yes', 'no']:
        answer2 = sorry()
        if answer2:
            answer2 = answer2.split()
        answer = check(['yes', 'no'], answer2)
    if answer == 'yes':
        open_app()


def close_app():
    app = None
    while app == None:
        talk('ok Vicky, which application you want to close?')
        app = listen()
    app = app.split()
    app = check2(app_list, app)
    # if app not in app_list:
    while app == []:
        app2 = sorry()
        if app2:
            app2 = app2.split()
        app = check2(app_list, app2)
    for item in app:
        if item == 'wait':
            talk('ok vicky, i will wait for 5 seconds')
            time.sleep(5)
            close_app()
        elif item == 'quit':
            talk('ok Vicky, I am shutting down now. bye')
            quit()
        elif 'restart' in app:
            do_Sandy()
        else:
            try:
                for process in (process for process in psutil.process_iter() if
                                process.name() == "{0}".format(app_dict[item])):
                    process.kill()
            except:
                pass
    talk('i have closed the asked applications, Vicky. do you want to close any other application?')
    answer = listen()
    while answer == None:
        talk('do you want to close any other application?')
        answer = listen()
    answer = answer.split()
    answer = check(['yes', 'no'], answer)
    while answer not in ['yes', 'no']:
        answer2 = sorry()
        if answer2:
            answer2 = answer2.split()
        answer = check(['yes', 'no'], answer2)
    if answer == 'yes':
        close_app()


def weather():
    api_key = '9b0d29adbb76c46b7a476c0ff8a9d6a4'
    talk('ok vicky, which city\'s weather you want to know?')
    city = listen()
    while city == None:
        talk('ok Vicky, which city\'s weather you want to know?')
        city = listen()
    while len(city.split()) > 2:
        talk('please give me city name, not a long sentence')
        city = listen()
        if city == None:
            weather()
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}".format(city=city, key=api_key))
    report = response.json()
    if 'message' in list(report.keys()):
        talk(report['message'])
        talk('lets try again')
        weather()
    else:
        talk(
            'the temperature of {city} is {temp} degree celcius with {hum} percent of humidity and {wind} meter per '
            'second.'.format(city=city,
                             temp=round(report['main']['temp'] - 273.15, 2),
                             hum=report['main']['humidity'],
                             wind=report['wind']['speed']))
    time.sleep(4)
    do_Sandy()


def do_Sandy():
    to_do_list = ['search', 'time', 'message', 'shutdown', 'options', 'date', 'open application', 'close application',
                  'weather report']
    matching_words = ['search', 'date', 'time', 'message', 'shutdown', 'options', 'option', 'quit', 'logoff', 'sleep',
                      'wake',
                      'restart', 'wait', 'open', 'close', 'weather']
    var1 = None
    while var1 == None:
        talk('what do you want me to do?')
        var1 = listen()
    var1 = var1.split()
    var = check(matching_words, var1)
    while var not in matching_words:
        var2 = sorry()
        if var2:
            var2 = var2.split()
        var = check(matching_words, var2)
    if 'options' == var or 'option' == var:
        talk('ok Vicky, the options are ' + ','.join(to_do_list))
        do_Sandy()
    elif 'search' == var:
        search()
    elif 'restart' == var:
        do_Sandy()
    elif 'date' == var:
        mydate = datetime.datetime.now()
        month = mydate.strftime("%B")
        day = mydate.strftime("%A")
        date = mydate.strftime("%d")
        year = mydate.strftime("%Y")
        talk('today\'s date is:{day}-{date}-{month}-{year}'.format(day=day, date=date, month=month, year=year))
    elif 'time' == var:
        mydate = datetime.datetime.now()
        hour = mydate.strftime("%I")
        minute = mydate.strftime("%M")
        meridian = mydate.strftime("%p")
        talk('current time is {hour}-{minute}-{meridian}'.format(hour=hour, minute=minute, meridian=meridian))
    elif 'open' == var:
        open_app()
    elif 'close' == var:
        close_app()
    elif 'wait' == var:
        talk('ok vicky, i will wait for 5 seconds')
        time.sleep(5)
        do_Sandy()
    elif 'quit' == var or 'shutdown' == var:
        talk('ok Vicky, I am shutting down now. bye')
        sys.exit(0)
    elif 'weather' == var:
        weather()
    elif 'sleep' == var:
        talk('ok vicky, am going to sleep mode. wake me up when you want me back')
        while True:
            command = listen()
            try:
                if 'wake up' in command:
                    do_Sandy()
            except:
                pass
    time.sleep(4)
    do_Sandy()


def hi_Sandy():
    talk('hi Vicky')
    var = listen()
    if not var:
        hi_Sandy()
    else:
        do_Sandy()


hi_Sandy()
