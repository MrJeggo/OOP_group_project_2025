
#main game
#imports
import sys
import time
import os

#type function, fast types stuff
def faster_type_text(text, delay=0.0000001, chunk_size=6):
    for i in range(0, len(text), chunk_size):
        sys.stdout.write(text[i:i+chunk_size])
        sys.stdout.flush()
        time.sleep(delay)

#clears console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#intro
def show_intro():
    faster_type_text(
    '''
    _________  _______   ________           ________  ________  _____ ______   _______      
    |\___   ___\\  ___ \ |\   ____\         |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
    \|___ \  \_\ \   __/|\ \  \___|_        \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
         \ \  \ \ \  \_|/_\ \_____  \        \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__  
          \ \  \ \ \  \_|\ \|____|\  \        \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \ 
           \ \__\ \ \_______\____\_\  \        \ \_______\ \__\ \__\ \__\    \ \__\ \_______
            \|__|  \|_______|\_________\        \|_______|\|__|\|__|\|__|     \|__|\|_______|
                            \|_________|                                                     

                            
                                      ( Press Spacebar to begin game )

                                        
    ("Polar Popstar" a.k.a. TES GAME THEME, by Che-kai, now playing)

    '''


    )

show_intro()
