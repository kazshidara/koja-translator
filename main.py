import os
import requests
import json
import emoji






def translate():
    print("Welcome to KoJa Translation!")
    text = input("Please enter a word or phrase in English:")
    api_url_ko = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190925T232709Z.d6fbd196e24efe3d.962ac209c4d4300fb4cd4b889b5c171d537aef0a&text={text}&lang=en-ko'
    api_url_jpn = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20190925T232709Z.d6fbd196e24efe3d.962ac209c4d4300fb4cd4b889b5c171d537aef0a&text={text}&lang=en-ja'

    response1 = requests.get(api_url_jpn)
    response2 = requests.get(api_url_ko)
    data1 = response1.json()
    data2 = response2.json()
    jpn_text = data1['text']
    ko_text = data2['text']
    print(u"\U0001F1FA\U0001F1F8",[f"{text}"])
    print(u'\U0001F1EF\U0001F1F5',f"{jpn_text}")
    print(u"\U0001F1F0\U0001F1F7",f"{ko_text}")
    text2 = input("Did you want to translate again (y/n):")
    if text2 == 'y':
        translate()
    elif text2 == 'n':
        print("Hope to see you soon! Matane! Anyyeong!")
        return 
    else:
        print("Sorry, we don't understand. Would you like to continue translating? (y/n):")
        text2 = input("Did you want to translate again (y/n):")
        if text2 == 'y':
            translate()
        elif text2 == 'n':
            print("Hope to see you soon! Matane! Anyyeong!")
            return 
        else:
            print("See you again soon!")
            return
    






translate()

# unicodes:

# american flag: U0001F1FA U0001F1F8
# japan flag:U0001F1EF U0001F1F5  
# korean flag: U0001F1F0 U0001F1F7



# https://www.geeksforgeeks.org/python-program-to-print-emojis/