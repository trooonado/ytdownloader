import os
import time
from pytubefix import YouTube
from pytubefix.cli import on_progress
from colorama import Fore

def banner():
   os.system("clear")
   print(f"{Fore.GREEN}""""""""""
       _         _                     _                 _
 _   _| |_    __| | _____      ___ __ | | ___   __ _  __| |
| | | | __|  / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
| |_| | |_  | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |
 \__, |\__|  \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|
 |___/

 created by Satyabrata Mitra
 version - 0.1
""""""""""")

try:
            banner()
            print(f"{Fore.GREEN} starting ..........")
            time.sleep(2)
            link = input("enter the vedio link :")
            youtube = YouTube(link , on_progress_callback = on_progress)
            print("getting vedio info !!")
            time.sleep(1)
            print(f"video title : {youtube.title}")
            time.sleep(1)
            print(f"vedio views : {youtube.views}")
            time.sleep(1)
            print(f"vedio id : {youtube.video_id}")
            time.sleep(1)
            print(f"vedio tumnail download :{youtube.thumbnail_url}")
            time.sleep(1)
            try:
               choise  =str(input(f"do you want only audio (y/n):"))

            except Exception as e:
               os.system("clear")
               print(f"Error:{Fore.RED}{e}")
               exit(0)
            try:
              location =str(input(f"where you want to download the vedio/audio : "))

            except Exception as e:
               os.system('clear')
               print(f"Error:{Fore.RED} {e}")
               exit(0)

            if choise =="y" or choise=="yes" or choise=="YES":
                 try:
                  only_audio = youtube.streams.filter(only_audio=True).first()
                  only_audio.download(location,filename=f"{youtube.title}.mp3")
                  print(f"your audio has sussesfully downloaded on {location} and file name is {youtube.title}.mp3")
                  time.sleep(2)
                 except Exception as e:
                      exit(0)
                      os.system("clear")
                      print(f"Error:{Fore.RED}{e}")

            elif choise =="n" or choise=="no" or choise=="NO":
             try:
                        both_vedio_audio = youtube.streams.get_highest_resolution()
                        both_vedio_audio.download(location)
                        time.sleep(2)
                        print(f"your vedio has succesfully downloaded on {location} and file name is {youtube.title}.mp4")
             except Exception as e:
                     os.system("clear")
                     print(f"Error:{Fore.RED} , {e}")
            else:
                   os.system("clear")
                   print(f"Error:{Fore.RED} an error occurese")
except Exception as e:
              os.system("clear")
              print(f"Error:{Fore.RED}{e}")
