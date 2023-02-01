from threading import Thread
from time import sleep
from PIL import ImageFilter,ImageOps,ImageGrab
import pytesseract
import win32gui as w
import telegram_send as ts
from random import random,randint,choice
from pynput.keyboard import Controller,Listener,Key
from json import load 
pytesseract.pytesseract.tesseract_cmd = '' # path to ocr exe


kb = Controller()
active = True
killprog = False

def focusonpokemon(): ## check we are in the pokemon screen
    return w.GetWindowText(w.GetForegroundWindow()) == 'PROClient'


def variance_sleep(sleep_time,var=0.1):
    a = var*2
    sleep(random()*a + sleep_time - var)



pokesets = {
    1: ['pidgey','rattata','zigzagoon','zubat','golbat','crobat','spearow','fearow'], # speed
    2: ['plusle','minun','sandile','machamp','mareep','shinx','heracross','pineco','stantler','staryu','misdreavus'], # rare 
    3: ['spinarak','sentret','weedle','snubbull','machamp','bellsprout','weepinbell'], # attack
    4: ['kakuna','metapod','golem','sandshrew','sandslash','geodude'], # defense
    5: ['gastly','haunter','gengar','spinda'],# sp attack
    20 :['no pp left','trying to learn'],
    21: ['misdreavus'] # specific pokemon
    
}

def move():
    global inbattle , killprog, active
    while not killprog :
        if active and not inbattle and focusonpokemon(): #not in battle
            kb.press('a')
            variance_sleep(0.5)
            kb.release('a')
            # variance_sleep(0.01,var=0.005)
            kb.press('d')
            variance_sleep(0.5)
            kb.release('d')
        else:
            sleep(0.5)
def fight():
    global inbattle , killprog, moverange, noppleft, lastmove, wanttofight,active,wanttocatch
    wanttofight = False
    noppleft = False
    while not killprog:
        sleep(1)
        if active and inbattle and focusonpokemon(): #not in battle
            if wanttocatch:
                sleep(10)# spore
                kb.press('1')
                kb.release('1')
                sleep(0.5)
                kb.press('1')
                kb.release('1')
                # sleep(20)# false swipe
                # kb.press('1')
                # kb.release('1')
                # sleep(0.5)
                # kb.press('4')
                # kb.release('4')
                sleep(20)# catch 
                kb.press('3')
                kb.release('3')
                sleep(0.5)
                kb.press('1')
                kb.release('1')
            elif wanttofight:
                sleep(4)
                kb.press('1')
                kb.release('1')
                sleep(1)
                lastmove = choice(moverange)
                p = str(lastmove)
                kb.press(p)
                kb.release(p)
                sleep(1)
            if noppleft:
                if len(moverange) <= 1:
                    ts.send(messages=["out of pp"])
                    sleep(30)
                else:
                    if lastmove in moverange:
                        moverange.remove(lastmove)

def relode():
    global pokelist,moverange,pokesets,inbattle
    inbattle = False
    with open('poke-data.json','r') as f:
        data = load(f)
    if data:
        pokesets = data
        pokelist = [ ]
        for i in data["current"]:
            pokelist.extend(data[i])
        pokelist = list(set(pokelist))
        pokelist.sort()
        print("changed",pokelist)
        moverange = data["range"]
        moverange = list(range(moverange[0],moverange[1]+1))

def status():
    global inbattle, moverange, noppleft, wanttofight,active
    while True:
        try:
            values = [inbattle, moverange, noppleft, wanttofight,active,wanttocatch]
            names = ["inbattle", "moverange", "noppleft", "wanttofight","active","wanttocatch"]
            for i in range(len(names)):
                print(names[i],values[i])
            print("#########################")
        except Exception as e:
            pass
        finally:
            sleep(4)
            
def main():
    global inbattle, noppleft, wanttofight,active,wanttocatch
    active = True
    inbattle = False
    wanttocatch = False
    def onp(key):
        global active , killprog
        try:
            if key.char == 'e':
                active = not active
            elif key.char == 'q':
                killprog = True
            elif key.char == 'r':
                relode()
        except:
            pass
        
    status_printer = Thread(target=status)
    status_printer.setDaemon(True)
    status_printer.start()
    fighter = Thread(target=fight)
    fighter.setDaemon(True)
    fighter.start()
    mover = Thread(target=move)
    mover.setDaemon(True)
    mover.start()
    l = Listener(on_press=onp)
    l.setDaemon(True)
    l.setName('program-status-manager')
    l.start()
    relode()
    
    while not killprog:
        if focusonpokemon() and active:
            image = ImageGrab.grab()
            image = ImageOps.grayscale(image).filter(ImageFilter.EDGE_ENHANCE)
            text = pytesseract.image_to_string(image).lower()
            if 'awild' in text:
                inbattle = True
                if any(['awild '+i in text for i in pokelist]): 
                    if any('awild '+i in text for i in pokesets["rare"]+pokesets["specific"]):
                        ts.send(messages=['Found '+str([i for i in pokesets["rare"]+pokesets["specific"] if i in text])])
                        wanttocatch = True
                        sleep(30)
                    else: #want to fight 
                        wanttofight = True
                    if "no pp left" in text:
                        noppleft = True
                else: # run away 
                    wanttofight = False
                    wanttocatch = False
                    kb.press('4')
                    kb.release('4')            
            else:
                wanttocatch=False
                wanttofight = False
                inbattle = False
if __name__ == "__main__":
    main()


