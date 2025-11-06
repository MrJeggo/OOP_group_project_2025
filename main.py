
#main game
#imports
import sys
import time
import os

#ignore
try:
    import msvcrt
    WINDOWS = True
except ImportError:
    WINDOWS = False


#type function, fast types stuff
def faster_type_text(text, delay=0.0000001, chunk_size=6):
    for i in range(0, len(text), chunk_size):
        sys.stdout.write(text[i:i+chunk_size])
        sys.stdout.flush()
        time.sleep(delay)

#clears console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#waits for space input
def wait_for_space():
    print("\n[ Press Spacebar to continue... ]")
    if WINDOWS:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ':
                    break
    else:
        # mac/linux fallback (still requires Enter unfortunately)
        while True:
            key = input().strip().lower()
            if key == "":
                break

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


def cinematic_intro():
    clear()
    faster_type_text("You wake up in the Phase 1 cafeteria.\n")
    faster_type_text("Cold air hums through the vents. The lights flicker.\n")
    wait_for_space()
    
    faster_type_text("\nA sound. Footsteps.\n")
    faster_type_text("A student — Mati — stumbles toward you, clutching his chest.\n")
    faster_type_text("His uniform is torn, his eyes wide with fear.\n")
    wait_for_space()
    
    faster_type_text('\n"Don’t—tru—" he gasps, trying to speak.\n')
    faster_type_text("He collapses before he can finish.\n")
    wait_for_space()
    
    faster_type_text("\nThe lights go out.\n")
    time.sleep(1)
    faster_type_text("A calm voice cuts through the dark.\n")
    faster_type_text('"Ah, you’re awake," a man says softly.\n')
    faster_type_text('"I’m Mr. Jeggo."\n')
    wait_for_space()
    
    name = input("\n'What’s your name, student?' > ")
    faster_type_text(f"\nMr. Jeggo adjusts his glasses. 'Alright, {name}... you’re safe now.'\n")
    faster_type_text("‘The teachers have been infected by a virus. They attack on sight. We need to stop them before it’s too late.’\n")
    wait_for_space()
    
    faster_type_text("\nHe steps over Mati’s body without a glance.\n")
    faster_type_text("‘Come with me. There’s much to do.’\n")



# Run sequence
show_intro()
wait_for_space()
cinematic_intro()
