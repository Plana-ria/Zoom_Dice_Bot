import re
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as pg
import time
from time import sleep
from playsound import playsound
import pyperclip as pc

def main():
    #開始処理
    ans = input('Change settings? (y or skip:enter)\n')
    if ans =='y' or ans == 'Y':
        f = open('log.txt', 'r', encoding='UTF-8')
        log = f.readlines()
        f.close()
        if not log:
            log = ['0\n', '0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n']
        f = open('log.txt', 'w', encoding='UTF-8')
        ans = input('Reset the count? (y or skip:enter)\n')
        if ans =='y' or ans == 'Y':
            log[0] = '0\n'
        ans = input('Setting chat file directory? (full file path or skip:enter)\n')
        if ans != '':
            log[1] = ans + '\n'
        ans = input('Change the click position? :y or n (enter)\n')
        if ans =='y' or ans == 'Y':
            input('Enter on […] (details) botton.\n')
            x, y = pg.position()
            log[2] = str(x) + '\n'
            log[3] = str(y) + '\n'
            input('Enter on save chat botton.\n')
            x, y = pg.position()
            log[4] = str(x) + '\n'
            log[5] = str(y) + '\n'
            input('Enter on chat box.\n')
            x, y = pg.position()
            log[6] = str(x) + '\n'
            log[7] = str(y) + '\n'
            input('Enter on left top of chat.\n')
            x, y = pg.position()
            log[8] = str(x) + '\n'
            log[9] = str(y) + '\n'
            w = int(x)
            h = int(y)
            input('Enter on right bottom of chat.\n')
            x, y = pg.position()
            w = int(x) - w
            h = int(y) - h
            log[10] = str(w) + '\n'
            log[11] = str(h) + '\n'


        f.writelines(log)
        f.close()
        print ('All setting compleated.\n')
    print ('Start Zoom Dice Bot.\n')
    
        #ボット監視開始
    try:
        while True:
            #設定ファイル読み込み
            f = open('log.txt', 'r', encoding='UTF-8')
            log = f.readlines()
            f.close()
            
            #チャット保存
            pg.click(int(log[2]), int(log[3])) #x=1335 y=628
            sleep(0.5)
            pg.click(int(log[4]), int(log[5])) #x=1335 y=572
            t = time.time() + 8
            #新規入力チャット読み込み
            k = 0
            f = open(log[1].replace('\n',''), 'r', encoding='UTF-8') #絶対パスでファイル指定

            while True:
                data = f.readline()
                if int(log[0]) <= k:
                    parenthesis = re.search(r'\(', data)
                    endcom = re.search(r'Botout', data)
                    if endcom != None and parenthesis == None:
                        f.close()
                        pg.click(int(log[6]), int(log[7])) #x=1100 y=668
                        sleep(0.5)
                        pg.write('END')
                        pg.press('enter')
                        f = open('log.txt', 'w', encoding='UTF-8')
                        k += 2
                        log[0] = str(k) + '\n'
                        f.writelines(log)
                        f.close()
                        print('Exit.') 
                        return 0;
                    command = re.search(r'(\d{1,3})([d|D|ｄ|D|Ｄ]{1})(\d{1,3})([+|-|*|/|＋|ー|－|-|-|−|＊|×|✖|⋇|/|／]{0,1})(\d{0,3})([d|D|ｄ|D|Ｄ]{0,1})(\d{0,3})', data)
                    user_name = re.search(r'開始 (.*?) に', data)

                    if command != None and parenthesis == None:
                        #コマンド判定/コマンド処理
                        if command.group(6) != '':
                            item = sum(np.random.randint(1, int(command.group(7)) + 1, int(command.group(5))))
                            com = command.group(1) + command.group(2) + command.group(3) + command.group(4) + command.group(5) + command.group(6) + command.group(7)
                        else:
                            if command.group(5) != '':
                                item = int(command.group(5))
                                com = command.group(1) + command.group(2) + command.group(3) + command.group(4) + command.group(5)
                        if '+' in str(command) or '＋' in str(command):
                            res = sum(np.random.randint(1, int(command.group(3)) + 1, int(command.group(1)))) + item
                        elif '-' in str(command) or 'ー' in str(command) or '－' in str(command) or '-' in str(command) or '-' in str(command) or '−' in str(command):

                            res = sum(np.random.randint(1, int(command.group(3)) + 1, int(command.group(1)))) - item
                        elif '*' in str(command) or '＊' in str(command) or '×' in str(command) or '✖' in str(command) or '⋇' in str(command):
                            res = sum(np.random.randint(1, int(command.group(3)) + 1, int(command.group(1)))) * item
                        elif '/' in str(command) or '/' in str(command) or '／' in str(command):
                            res = sum(np.random.randint(1, int(command.group(3)) + 1, int(command.group(1)))) / item
                        else:
                            res = sum(np.random.randint(1, int(command.group(3)) + 1, int(command.group(1))))
                            com = command.group(1) + command.group(2) + command.group(3)

                        #チャットボックス入力
                        #print('> {0}'.format(res))
                        pg.click(int(log[6]), int(log[7])) #x=1100 y=668
                        sleep(0.5)
                        pc.copy(user_name.group(1))
                        pg.hotkey('ctrl', 'v')
                        pg.write('(')
                        pg.write(com)
                        pg.write(')> ')
                        pg.write(str(res))
                        playsound("sound.wav")
                        pg.press('enter')

                if data == '':
                    break
                k += 1
            f.close()
            f = open('log.txt', 'w', encoding='UTF-8')
            log[0] = str(k) + '\n'
            f.writelines(log)
            f.close()
            #チャット変化監視       #x=1048, y=74, w=105, h=462
            sc1 = pg.screenshot(region=(int(log[8]), int(log[9]), int(log[10]), int(log[11])))
            while time.time() < t:
                sc2 = pg.screenshot(region=(int(log[8]), int(log[9]), int(log[10]), int(log[11])))
                if sc1 != sc2:
                    break
                sc1 = sc2
            sleep(3)
            sc1 = pg.screenshot(region=(int(log[8]), int(log[9]), int(log[10]), int(log[11])))
            while True:
                sc2 = pg.screenshot(region=(int(log[8]), int(log[9]), int(log[10]), int(log[11])))
                if sc1 != sc2:
                    break
                sc1 = sc2

    except KeyboardInterrupt: #例外処理: ^ + c
        f = open('log.txt', 'w', encoding='UTF-8')
        log[0] = str(k) + '\n'
        f.writelines(log)
        f.close()
        print('Exit.') 
        return 0;   

if __name__ == '__main__':
    main()