try:
    import pyautogui
    import time
    from PIL import ImageGrab
    from functools import partial
    import ctypes, threading

    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    count = 0
    nalezeno = False
    time.sleep(5)
    print(
        """
    █     █░ ██▀███   ▄▄▄       ██▓▄▄▄█████▓ ██░ ██▓██   ██▓  ██████ 
    ▓█░ █ ░█░▓██ ▒ ██▒▒████▄    ▓██▒▓  ██▒ ▓▒▓██░ ██▒▒██  ██▒▒██    ▒ 
    ▒█░ █ ░█ ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒▒ ▓██░ ▒░▒██▀▀██░ ▒██ ██░░ ▓██▄   
    ░█░ █ ░█ ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░ ▓██▓ ░ ░▓█ ░██  ░ ▐██▓░  ▒   ██▒
    ░░██▒██▓ ░██▓ ▒██▒ ▓█   ▓██▒░██░  ▒██▒ ░ ░▓█▒░██▓ ░ ██▒▓░▒██████▒▒
    ░ ▓░▒ ▒  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓    ▒ ░░    ▒ ░░▒░▒  ██▒▒▒ ▒ ▒▓▒ ▒ ░
    ▒ ░ ░    ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░    ░     ▒ ░▒░ ░▓██ ░▒░ ░ ░▒  ░ ░
    ░   ░    ░░   ░   ░   ▒    ▒ ░  ░       ░  ░░ ░▒ ▒ ░░  ░  ░  ░  
        ░       ░           ░  ░ ░            ░  ░  ░░ ░           ░  
                                                    ░ ░              
    ▄▄▄       ███▄    █  ▄████▄   ▄▄▄▄    ▒█████  ▄▄▄█████▓          
    ▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒          
    ▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░          
    ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██░█▀  ▒██   ██░░ ▓██▓ ░           
    ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░           
    ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░             
    ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒   ▒░▒   ░   ░ ▒ ▒░     ░              
    ░   ▒      ░   ░ ░ ░         ░    ░ ░ ░ ░ ▒    ░                
        ░  ░         ░ ░ ░       ░          ░ ░                     
                        ░              ░                          
    """
    )
    while not nalezeno:
        try:
            neco = pyautogui.locateOnScreen("./anc.png", grayscale=False)
            print("nalezeno: ", count)

            if neco is not None:
                threading.Thread(
                    target=lambda: ctypes.windll.user32.MessageBoxW(
                        0, "Hej dyk pyčo ANC věc padla", "WRAITHY'S AncBot'", 0x1000
                    )
                ).start()

                while True:
                    tmpFind = pyautogui.locateOnScreen("./anc.png", grayscale=False)
                    if tmpFind is None:
                        break

                print(neco)
                count += 1

                neco = None
            time.sleep(1)
        except Exception as e:
            print(e)
            time.sleep(10)
except Exception as e:
    print(e)
    time.sleep(10000)
