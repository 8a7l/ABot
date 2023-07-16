import keyboard
import pyautogui
import time
import threading
#=========================================================================================================================================================
pyautogui.FAILSAFE = False
#=========================================================================================================================================================

run1=True
run2=False

start_key='+'
pause_key='-'
end_key='*'


time_day_constant=60*60*24
time_attack=270
time_buffs=15
time_second_panel=0
time_third_panel=0

time_pre_cast_attack=0.2
time_pre_cast_buff=2
time_pre_cast_second_panel=2
time_pre_cast_third_panel=2


user_bottons_panel_attack='f1'
user_bottons_panel_buff='f2'
user_bottons_panel_second='f3'
user_bottons_panel_third='f4'

user_bottons_attack=4
user_bottons_buff=4
user_bottons_second=2
user_bottons_third=2


user_bottons_trigger_g=1
user_bottons_trigger_tab=1


info_start_bot='Запущено бота'
info_pause_bot='Бота зупинено'
info_start_buff='Почато баф.'
info_pause_buff='Зупинений баф'
info_start_attack='Почата атака'
info_pause_attack='Зупинена атака'

control_bottoms=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
control_bottoms_functions=['f1', 'f2', 'f3', 'f4']
control_bottoms_sp=['tab', 'g']

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


tick_run1=True
seconds2=0
def tick2():
    while tick_run1:
        start_time=time.time()
        time.sleep(1)
        pol_time=time.time()-start_time
        global seconds2
        seconds2+=pol_time
tick2= threading.Thread(name='tick2', target=tick2, daemon=True)
tick2.start()


tick_run2=True
seconds3=0
def tick3():
    while tick_run2:
        start_time=time.time()
        time.sleep(1)
        pol_time=time.time()-start_time
        global seconds3
        seconds3+=pol_time
tick3= threading.Thread(name='tick3', target=tick3, daemon=True)
tick3.start()
#=========================================================================================================================================================


def ways(string):
    global tick_run1
    global tick_run2
    if string==control_bottoms_functions[0]:
        pyautogui.press(control_bottoms_functions[0])
    
    if string==control_bottoms_functions[1]:
        pyautogui.press(control_bottoms_functions[1])
    
    if string==control_bottoms_functions[2]:
        pyautogui.press(control_bottoms_functions[2])
    
    if string==control_bottoms_functions[3]:
        pyautogui.press(control_bottoms_functions[3])
    
    if string!=control_bottoms_functions[2] or time_second_panel==0:
        global seconds2
        tick_run1=False
        seconds2=-1
    
    if string==control_bottoms_functions[3] or time_third_panel==0:
        global seconds3
        tick_run2=False
        seconds3=-1
    

def buttons(string, cont, time_pre_cast):
    ways(string)
    for k in control_bottoms:
        pyautogui.press(k)
        time.sleep(time_pre_cast)
        cont-=1
        if cont<=0:
            break
    



def on_attack_bottons():
    buttons(user_bottons_panel_attack, user_bottons_attack, time_pre_cast_attack)
    if user_bottons_trigger_tab==1:
        pyautogui.press(control_bottoms_sp[0])
    if user_bottons_trigger_g==1:
        pyautogui.press(control_bottoms_sp[1])


def on_buff_bottons():
    buttons(user_bottons_panel_buff, user_bottons_buff, time_pre_cast_buff)

def on_second_bottons():
    buttons(user_bottons_panel_second, user_bottons_second, time_pre_cast_second_panel)

def on_third_bottons():
    buttons(user_bottons_panel_third, user_bottons_third, time_pre_cast_third_panel)


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



def start():
    global seconds
    global seconds2
    global seconds3
    
    if seconds<time_buffs:
        on_buff_bottons()
    if seconds>time_buffs and seconds<(time_buffs+time_attack):
        on_attack_bottons()
    if seconds>(time_buffs+time_attack) and seconds<time_day_constant:
        seconds=0
    if seconds2>=time_second_panel:
        time_container=seconds
        seconds=time_day_constant
        on_second_bottons()
        seconds=time_container+time_buffs
        seconds2=0
    if seconds3>=time_third_panel:
        time_container=seconds
        seconds=time_day_constant
        on_third_bottons()
        seconds=time_container+time_buffs
        seconds3=0
        
keyboard.add_hotkey(start_key, on_start)
keyboard.add_hotkey(pause_key, on_pause)
keyboard.add_hotkey(end_key, on_esc)



pyautogui.PAUSE = 0.1


#=========================================================================================================================================================

while run1:
    while run2:
        start()

#=========================================================================================================================================================



    



