import win32gui as w
from time import sleep
from pynput.keyboard import Controller,Key
from random import randint
import tensorflow as tf 
from PIL import ImageGrab
import numpy as np

# The global keyaborad 
keyboard = Controller()
left = 'a'
right = 'd'


def goleft(t):
    print("go left")
    keyboard.press(left)
    sleep(t)
    keyboard.release(left)
    
def goright(t):
    print("go right")
    keyboard.press(right)
    sleep(t)
    keyboard.release(right)

def pressfight():
    keyboard.press('1')
    keyboard.release('1')

def pressmove(index):
    keyboard.press(str(index))
    keyboard.release(str(index))



def focusonpokemon(): ## check we are in the pokemon screen
    return w.GetWindowText(w.GetForegroundWindow()) == 'PROClient'



def main():
    ## The most basic ass code
    # load model 
    # model = tf.keras.models.load_model('./battle-recognition')
    # def infight():
    #     screenshot = ImageGrab.grab().convert("RGBA").resize((800,800))
    #     screenshot = np.array(screenshot).reshape(1,800,800,4)
    #     ans = model(screenshot)
    #     # print(ans[0][0])
    #     return ans[0][0]
            
    
    ##
    
    while True:
        if focusonpokemon():
            # ans = 0
            # for i in range(4):
            #     ans += infight()
            #     sleep(0.5)
            # ans /= 4
            # print(ans)
            # if ans>= 5:
            #     if ans >= 1.6:
            #         print("fight moder fucker")
            #         sleep(7)
            #         pressfight()
            #         sleep(1)
            #         # if infight():
            #         pressmove(randint(1,4))
            #     else:
            #         print("run")
            #         sleep(4)
            #         pressmove(4)
            # else:
            goleft(1)
            sleep(0.1)
            goright(1)
        # sleep(1)


if __name__ == "__main__":
    main()
