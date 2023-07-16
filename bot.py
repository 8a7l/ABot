import keyboard
import pyautogui
import time
import threading
#=========================================================================================================================================================

#=========================================================================================================================================================

run1=True
run2=False

start_key='+'
pause_key='-'
end_key='*'


time_attack=270
time_attacked=0.2
time_buffs=15
time_buffed=2



info_start_bot='Старт бот'
info_pause_bot='Стоп бот'
info_start_buff=''
info_pause_buff=''
info_start_attack=''
info_pause_attack=''

control_bottoms=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#=========================================================================================================================================================


#=========================================================================================================================================================
seconds=0
def tick():
    while run1:
        start_time=time.time()
        time.sleep(1)
        pol_time=time.time()-start_time
        global seconds
        seconds+=pol_time
tick= threading.Thread(name='tick', target=tick, daemon=True)
tick.start()


seconds2=0
def tick2():
    while run1:
        start_time=time.time()
        time.sleep(1)
        pol_time=time.time()-start_time
        global seconds2
        seconds2+=pol_time
tick2= threading.Thread(name='tick2', target=tick2, daemon=True)
tick2.start()


seconds3=0
def tick3():
    while run1:
        start_time=time.time()
        time.sleep(1)
        pol_time=time.time()-start_time
        global seconds3
        seconds3+=pol_time
tick3= threading.Thread(name='tick3', target=tick3, daemon=True)
tick3.start()
#=========================================================================================================================================================


def on_pause():
    print('['+time.asctime()+']'+' '+info_pause_bot)
    global run2
    if run2==True:
        run2=False


def on_start():
    print('['+time.asctime()+']'+' '+info_start_bot)
    global run2
    global seconds
    global seconds2
    global seconds3
    if run2==False:
        run2=True
        seconds=0
        seconds2=0
        seconds3=0


def on_esc():
    global run1
    run1=False

def on_buttons1():
    pyautogui.press('f2')
    pyautogui.press('1')
    time.sleep(time_buffed)
    pyautogui.press('2')
    time.sleep(time_buffed)
    pyautogui.press('3')
    time.sleep(time_buffed)
    pyautogui.press('4')
    time.sleep(time_buffed)
    pyautogui.press('5')
    time.sleep(time_buffed)
    pyautogui.press('6')
    time.sleep(time_buffed)

def on_buttons2():
    pyautogui.press('f1')
    pyautogui.press('1')
    time.sleep(time_attacked)
    pyautogui.press('2')
    time.sleep(time_attacked)
    pyautogui.press('3')
    time.sleep(time_attacked)
    pyautogui.press('4')
    time.sleep(time_attacked)
    pyautogui.press('5')
    time.sleep(time_attacked)
    pyautogui.press('6')
    time.sleep(time_attacked)
#    pyautogui.press('tab')
#    pyautogui.press('g')

def start():
    global seconds
    if seconds<time_buffs:
        on_buttons1()
    if seconds>time_buffs and seconds<(time_buffs+time_attack):
        on_buttons2()
    if seconds>(time_attack-time_buffs):
        seconds=0

        
keyboard.add_hotkey(start_key, on_start)
keyboard.add_hotkey(pause_key, on_pause)
keyboard.add_hotkey(end_key, on_esc)



pyautogui.PAUSE = 0.1


#=========================================================================================================================================================

while run1:
    while run2:
        start()

#=========================================================================================================================================================



    



