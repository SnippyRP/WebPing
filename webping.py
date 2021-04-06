import socket
import time
import ctypes
import webbrowser

import requests
from colorama import init

init()
from colorama import Fore, Style

ctypes.windll.kernel32.SetConsoleTitleW("WebPing!")
print("WebPing! use 'commands' for help")
while True:
    maincmd = input("> ")
    if maincmd == "massping":
        with open('URL.txt') as f:
            mainurl = f.readlines()
        with open('DATA.txt') as d:
            dat = d.readlines()
            print("Would you like to send data to", mainurl, "with data", dat)
            confirm = input("(Y)/(N)")
            if confirm == "Y":
                print(Fore.YELLOW + "Sending data packets.." + Style.RESET_ALL)
                time.sleep(2)
                def do_request():
                    while True:
                        response = response.post(mainurl, data=dat).text
                        print(response)

                        threads = []

                        for i in range(50):
                            t = threading.Thread(target=do_request)
                            t.daemon = True
                            threads.append(t)

                        for i in range(50):
                            threads[i].start()

                        for i in range(50):
                            threads[i].join()
    if maincmd == "showip":
        print("Are you sure you want your IP address? Anyone watching can find your location!")
        confirm2 = input("(Y)/(N)")
        if confirm2 == "Y":
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(Fore.GREEN + "Local IP is "+local_ip + Style.RESET_ALL)
        else:
            print(Fore.RED + "Request declined." + Style.RESET_ALL)
    if maincmd == "discord":
        inp = input("Discord Webhook: ")
        print("message / exit")
        state = input("discord > ")
        if state == "message":
            msg = input("message > ")
            usernamed = input("username for webhook > ")
            print(Fore.YELLOW + "Sending.." + Style.RESET_ALL)
            time.sleep(0.5)
            r = requests.post(inp, data={"content":msg, "username":usernamed})
            print(Fore.GREEN + "Successfully sent message" + Style.RESET_ALL)
        if state == "exit":
            print(Fore.RED + "Request declined." + Style.RESET_ALL)
    if maincmd == "commands":
        print("________________________________")
        print("massping // If your tech savvy enough, use URL.txt and DATA.txt to send data packets to a website")
        print("showip // Shows the local IP for your internet. This does have a confirmation")
        print("discord // Sends messages through discord webhooks")
        print("commands // Shows a list of commands")
        print("title // Sets the window title")
        print("credits // Shows the credits")
        print("web // Redirects to a website")
        print("vouch // Sends an anonymous comment to the #vouches channel in our server")
        print("invite // Joins our discord server. Come join and chat!")
        print("________________________________")
    if maincmd == "title":
        titleset = input("Title here > ")
        ctypes.windll.kernel32.SetConsoleTitleW(titleset)
    if maincmd == "credits":
        print("Scripted by SnippyRO/Snippy#1118")
    if maincmd == "web":
        url = input("URL to redirect to > ")
        try:
            webbrowser.open(url)
            print(Fore.GREEN + "Successfully redirected" + Style.RESET_ALL)
        except:
            print(Fore.RED + "An unknown error occurred" + Style.RESET_ALL)
    if maincmd == "vouch":
        msg2 = input("Vouch comment > ")
        print(Fore.YELLOW + "Sending.." + Style.RESET_ALL)
        time.sleep(0.5)
        r = requests.post("https://discord.com/api/webhooks/828783248129654796/gYQC-T7RAdaMnLQ6unORUA1cLf9071Gma-w1cUq8cWqoTMVOUD2CU4DTWko2jvbegzXt", data={"content": msg2}) #please no
        print(Fore.GREEN + "Successfully sent message" + Style.RESET_ALL)
    if maincmd == "invite":
        webbrowser.open("https://discord.gg/UtyPpNq82P")
        print(Fore.GREEN + "Successfully invited. Come join us!" + Style.RESET_ALL)