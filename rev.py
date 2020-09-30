import pyautogui
from PIL import Image
import pytesseract
import time
from googletrans import Translator
import fonts
import re
import sys
import pyautogui
import requests


trans = Translator()

while True:
     
     a = pyautogui.screenshot(region=(356,640,819,46))
     text = pytesseract.image_to_string(a)
     text = re.sub(r"\d.*","",text)
 
     if re.search(r"Youtube (.*)",text):
        parsed = re.search(r"Youtube (.*)",text).group(1)
        query = 'https://www.youtube.com/results?search_query={}'.format(parsed)
        req = requests.get(query).text
 
        try:
            link=re.findall(r'yt-lockup-content"><h3 class="[^\"]+\"><a href=\"([^\"]+)\"',req)
            link_="https://www.youtube.com"+str(link[0])
            print(link_)
            pyautogui.moveTo(484, 730)
            pyautogui.click()
            printed = '{}'.format(link_)
            pyautogui.typewrite("tunggu sebentar...")
            pyautogui.hotkey("enter")
            pyautogui.moveTo(484, 730)
            pyautogui.click()
            pyautogui.typewrite(printed)
            time.sleep(5)
            pyautogui.hotkey("enter")
        except Exception as e:
            print(e)
        
     elif re.search(r"Translate (\w+) (\w+) (.+)",text):
        parsed = re.search(r"Translate (\w+) (\w+) (.+)",text)
        src = parsed.group(1)
        dest = parsed.group(2)
        tl = parsed.group(3)
        if re.search(r"ja", dest):
            try:
                payload = trans.translate(tl, dest=dest).extra_data['translation'][1][2].encode('utf-8')
                pyautogui.moveTo(484, 730)
                pyautogui.click()
                printed = 'Hasil terjemahan kamu adalah : {}'.format(payload)
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
                
            except Exception as e:
                print(e)
                pyautogui.moveTo(484, 730)
                pyautogui.click()
                printed = "Terjadi kesalahan, hubungi pembuat bot"
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
        else:
            try:
                payload = trans.translate(tl, dest=dest).text
                pyautogui.moveTo(484, 730)
                pyautogui.click()
                printed = 'Hasil terjemahan kamu adalah : {}'.format(payload)
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
            except Exception as e:
                pyautogui.moveTo(484, 730)
                pyautogui.click()
                printed = "Terjadi kesalahan, hubungi pembuat bot"
                pyautogui.typewrite(printed)
                pyautogui.hotkey("enter")
     time.sleep(0.5)