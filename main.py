import pyautogui
import pydirectinput
import time
import threading
import datetime
def total_cout(system_const,zero_count,one_count,two_count,three_count,four_count):
    if system_const == 0:
        system_const = 1
    print(time.ctime() + "：刷第" + str(system_const) + "次首抽\n" +
          time.ctime() + "：一張指定要的都沒有 >> " + str(zero_count) + "次" + " 目前機率：" + str(round(zero_count/system_const,5)*100) + "% \n" +
          time.ctime() + "：抽到0突的次數 >> " + str(one_count) + "次" + " 目前機率：" + str(round(one_count/system_const,5)*100) + "% \n" +
          time.ctime() + "：抽到可以1突的次數 >> " + str(two_count) + "次" + " 目前機率：" + str(round(two_count/system_const,5)*100) + "% \n" +
          time.ctime() + "：抽到可以2突的次數 >> " + str(three_count) + "次" + " 目前機率：" + str(round(three_count/system_const,5)*100) + "% \n" +
          time.ctime() + "：抽到可以3突以上的次數 >> " + str(four_count) + "次" + " 目前機率：" + str(round(four_count/system_const,5)*100) + "% \n" +
          "↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓目前動作↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")

#pyautogui.moveTo(1100, 485)  # 中心座標
# nox=pyautogui.locateOnScreen('NOX.jpg' , confidence=0.8)
# x, y = pyautogui.center(nox)
# pyautogui.click(x,y)
#pyautogui.click(1100, 1426) #夜神XY座標
house=0
add =0
temp=0
home=0
flag=0
zero=0
ssr=0
counst = 98
getgogo_counst = 0
GG=0 #
system_const = 0
zero_count = 0 #紀錄一張都沒有的計數器
one_count = 0 #紀錄抽到0突的計數器
two_count = 0 #紀錄抽到1突的計數器
three_count = 0 #紀錄抽到2突以上的計數器
four_count = 0 #紀錄抽到3突以上的計數器
while 1:
    print("初始化")
    #  pyautogui.click(1100, 485)  # 中心座標
    CYGAMES=pyautogui.locateOnScreen('CYGAMES.jpg' , confidence=0.8)
    if CYGAMES and counst ==98:
        print("跳過CYGAMES動畫")
        x, y = pyautogui.center(CYGAMES)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        pyautogui.click(clicks=2, interval=0.25)
        time.sleep(2)
    START = pyautogui.locateOnScreen('START.jpg', confidence=0.7)
    if START and counst ==98:
        total_cout(system_const,zero_count,one_count,two_count,three_count,four_count)
        system_const += 1
        ssr = 0
        zero = 0
        add = 0
        counst =1
        print(time.ctime() + "： TAP TO START")
        x, y = pyautogui.center(START)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(5.5)
        while pyautogui.locateOnScreen('jumpstart.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        jumpstart = pyautogui.locateOnScreen('jumpstart.jpg', confidence=0.8)
        total_cout(system_const,zero_count,one_count,two_count,three_count,four_count)
        print(time.ctime() + "： 確定要跳過教學內容嗎？跳過")
        # print(jump_start)
        x, y = pyautogui.center(jumpstart)
        pydirectinput.moveTo(x, y)
        pyautogui.click(x, y)
        time.sleep(1)
        edit = pyautogui.locateOnScreen('edit.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 寫入名字")
        x, y = pyautogui.center(edit)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        pyautogui.typewrite('Dot')
        login = pyautogui.locateOnScreen('login.jpg', confidence=0.5)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 點選灰字登入")
        x, y = pyautogui.center(login)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        login_1 = pyautogui.locateOnScreen('login_1.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 綠色登入")
        x, y = pyautogui.center(login_1)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(0.8)
        ok = pyautogui.locateOnScreen('ok.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 訓練員登入")
        x, y = pyautogui.center(ok)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(4)
        while pyautogui.locateOnScreen('jump.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        jump = pyautogui.locateOnScreen('jump.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 跳過開場介紹")
        time.sleep(0.4)
        x, y = pyautogui.center(jump)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        while pyautogui.locateOnScreen('closure.jpg', confidence=0.8) is None:
            pydirectinput.moveTo(x, y)
            pydirectinput.click(x, y)
            time.sleep(0.5)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        x, y = pyautogui.center(closure)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 第1次關閉")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(0.5)
        while pyautogui.locateOnScreen('closure.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        x, y = pyautogui.center(closure)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 第2次關閉")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(0.5)
        while pyautogui.locateOnScreen('closure.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        x, y = pyautogui.center(closure)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 最後一次關閉")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        while pyautogui.locateOnScreen('5.jpg', confidence=0.8) is None: #等待辨識主要任務的圖片
            time.sleep(0.1)
        first5 = pyautogui.locateOnScreen('5.jpg', confidence=0.8)
        x, y = pyautogui.center(first5)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 點選主要任務")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(2)
        while pyautogui.locateOnScreen('jump.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        jump = pyautogui.locateOnScreen('jump.jpg', confidence=0.8)
        x, y = pyautogui.center(jump)
        pydirectinput.moveTo(x, y)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print (time.ctime() + "： 跳過理事長的廢話")
        pydirectinput.click(x, y)
        time.sleep(1.5)
        tap5 = pyautogui.locateOnScreen('first5.jpg', confidence=0.8)
        x, y = pyautogui.center(tap5)
        pydirectinput.moveTo(x, y)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 領取主要任務送的獎勵")
        pydirectinput.click(x, y)
        time.sleep(1)
        getall = pyautogui.locateOnScreen('getall.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 領取全部獎勵")
        x, y = pyautogui.center(getall)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 領取完畢後案的關閉")
        x, y = pyautogui.center(closure)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1.3)
        while pyautogui.locateOnScreen('gohome.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        gohome = pyautogui.locateOnScreen('gohome.jpg', confidence=0.8)
        x, y = pyautogui.center(gohome)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 領取主要任務獎勵結束，點選主畫面")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1.5)
        tap23 = pyautogui.locateOnScreen('23.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 點擊禮物盒")
        x, y = pyautogui.center(tap23)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1.5)
        getall = pyautogui.locateOnScreen('getall.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 領取禮物盒裡的所有獎勵")
        x, y = pyautogui.center(getall)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 禮物盒領取完畢，案關閉")
        x, y = pyautogui.center(closure)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 再點一次關閉")
        x, y = pyautogui.center(closure)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        smoke = pyautogui.locateOnScreen('house.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 點選轉蛋")
        x, y = pyautogui.center(smoke)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(1)
        while pyautogui.locateOnScreen('rightsmoke.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        rightsmoke = pyautogui.locateOnScreen('rightsmoke.jpg', confidence=0.68)
        x, y = pyautogui.center(rightsmoke)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 選擇轉蛋類別")
        time.sleep(1.5)
        gethouse = pyautogui.locateOnScreen('gethouse.jpg', confidence=0.8)
        x, y = pyautogui.center(gethouse)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 抽10次")
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(0.5)
        gethouse_2 = pyautogui.locateOnScreen('89GOGO.jpg', confidence=0.8)
        total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
        print(time.ctime() + "： 抽第一次轉蛋")
        x, y = pyautogui.center(gethouse_2)
        pydirectinput.moveTo(x, y)
        pydirectinput.click(x, y)
        time.sleep(0.5)
        while pyautogui.locateOnScreen('jump.jpg', confidence=0.8) is None:
            time.sleep(0.1)
        jump = pyautogui.locateOnScreen('jump.jpg', confidence=0.8)
        while add<6:
            if jump :
                while pyautogui.locateOnScreen('jump.jpg', confidence=0.8) is None:
                    time.sleep(0.1)
                jump = pyautogui.locateOnScreen('jump.jpg', confidence=0.8)
                x, y = pyautogui.center(jump)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "： 跳過抽獎")
                time.sleep(1)
                while pyautogui.locateOnScreen('oneget.jpg', confidence=0.8) is None:
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    print(time.ctime() + "： 再次跳過抽獎")
                    time.sleep(2)
                # time.sleep(3.5)
                # print("...辨識中...")
                # ssr_counst = ['ssr_1.jpg','ssr_2.jpg','ssr_3.jpg', 'ssr_4.jpg']
                temp_count = 0
                # for i in ssr_counst :
                #     ssrcounst = pyautogui.locateOnScreen(i, confidence=0.7)
                #     if ssrcounst:
                #        print ("抽到小北")
                #        ssr +=1
                #        break
                #     else:
                #         temp_count += 1
                # if temp_count % 4 == 0 and temp_count != 0:
                #     zero+=1
                add+=1
                # time.sleep(2)
                # print("目前小北卡持有：" + str(ssr) + "張")
                # print("共估" + str(zero) + "次")
                # print("總共抽了" + str(add) + "次")
                GG=1
            if add == 6 :
                if pyautogui.locateOnScreen('cancel.jpg', confidence=0.8) :
                    cancel = pyautogui.locateOnScreen('cancel.jpg', confidence=0.8) #辨識取消圖片
                    x, y = pyautogui.center(cancel)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點擊取消")
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    time.sleep(0.5)
                else:
                    while pyautogui.locateOnScreen('back.jpg', confidence=0.77) is None: #等待返回圖片
                        time.sleep(0.1)
                back = pyautogui.locateOnScreen('back.jpg', confidence=0.8) #辨識返回圖片
                x, y = pyautogui.center(back)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(4.7)
                while pyautogui.locateOnScreen('good.jpg', confidence=0.77) is None: #等待編組強化的圖片
                    time.sleep(0.1)
                good = pyautogui.locateOnScreen('good.jpg', confidence=0.8) #辨識編組強化的圖片
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "： 點擊編組強化")
                x, y = pyautogui.center(good)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(0.3)
                while pyautogui.locateOnScreen('check.jpg', confidence=0.8) is None: #等待支援卡片的圖片
                    print (time.ctime() + "： 搜尋點擊支援卡片")
                    time.sleep(0.1)
                check = pyautogui.locateOnScreen('check.jpg', confidence=0.8) #辨識支援卡片的圖片
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "： 點擊支援卡片")
                x, y = pyautogui.center(check)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(1)
                checkgood = pyautogui.locateOnScreen('checkgood.jpg', confidence=0.8) #辨識開放上限圖片
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "： 點擊開放上限")
                x, y = pyautogui.center(checkgood)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(1)
                while pyautogui.locateOnScreen('closure.jpg', confidence=0.8) is None: #等待關閉圖片
                    print (time.ctime() + "： 正在辨識關閉圖片")
                    time.sleep(0.1)
                closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8) #辨識關閉圖片
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "： 關閉")
                x, y = pyautogui.center(closure)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(1)
                if pyautogui.locateOnScreen('smallN.jpg', confidence=0.8) is None: #如果沒有辨識到小北的圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 沒...沒有小北...準備砍帳號.....")
                    zero_count +=1
                    time.sleep(0.5)
                    pydirectinput.moveTo(1631, 103)
                    pydirectinput.click(1631, 103)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選單")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('menu2.jpg', confidence=0.8) is None:
                        time.sleep(0.2)
                        pydirectinput.click(1631, 103)
                    menu2 = pyautogui.locateOnScreen('menu2.jpg', confidence=0.8)
                    x, y = pyautogui.center(menu2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選項")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('one.jpg', confidence=0.8) is None: #辨識下拉滑桿
                        time.sleep(0.1)
                    one = pyautogui.locateOnScreen('one.jpg', confidence=0.8)
                    x, y = pyautogui.center(one)
                    pyautogui.mouseDown(x,y)
                    pyautogui.dragTo(1618, 1250,0.6, button='left')
                    while pyautogui.locateOnScreen('delete.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete = pyautogui.locateOnScreen('delete.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 刪除使用者資料")
                    time.sleep(0.2)
                    while pyautogui.locateOnScreen('delete2.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete2 = pyautogui.locateOnScreen('delete2.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 確認刪除使用者資料")
                    time.sleep(0.6)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 最後確認刪除使用者資料")
                    time.sleep(0.5)
                    closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
                    x, y = pyautogui.center(closure)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 關閉")
                    time.sleep(1.5)
                    counst = 98
                    add = 6
                    GG = 0

                elif pyautogui.locateOnScreen('smallN.jpg', confidence=0.8): #等待小北圖片
                    print (time.ctime() + "： 正在辨識小北圖片")
                    time.sleep(0.1)
                    smallN = pyautogui.locateOnScreen('smallN.jpg', confidence=0.8) #辨識小北圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點擊小北")
                    x, y = pyautogui.center(smallN)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    time.sleep(1)
                    choose = pyautogui.locateOnScreen('choose.jpg', confidence=0.8) #辨識選擇圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 選擇")
                    x, y = pyautogui.center(choose)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    time.sleep(1)
                if pyautogui.locateOnScreen('noup.jpg', confidence=0.8) : #如果有"張數不足"的圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print (time.ctime() + "： 靠北 只有一張 連1突都不行= = 重新刷一次")
            # if (add ==6 and ssr >=2) or zero==5:
                # while pyautogui.locateOnScreen('back.jpg', confidence=0.77) is None:
                #     print ("正在辨識返回圖片")
                #     time.sleep(0.1)
                # back = pyautogui.locateOnScreen('back.jpg', confidence=0.8)
                # print ("可憐 啥都沒有：( 重新再刷一次嚕")
                # x, y = pyautogui.center(back)
                # pydirectinput.moveTo(x, y)
                # pydirectinput.click(x, y)
                # time.sleep(1)
                # while pyautogui.locateOnScreen('backhome.jpg', confidence=0.8) is None:
                #     time.sleep(0.2)
                # backhome = pyautogui.locateOnScreen('backhome.jpg', confidence=0.8)
                # print("可憐 啥都沒有：( 重新再刷一次嚕")
                # print("點選主畫面")
                # x, y = pyautogui.center(gohome)
                # pydirectinput.moveTo(x, y)
                # pydirectinput.click(x, y)
                # pyautogui.click(clicks=2, interval=0.25)
                    one_count += 1
                    time.sleep(1)
                    pydirectinput.moveTo(1631, 103)
                    pydirectinput.click(1631, 103)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選單")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('menu2.jpg', confidence=0.8) is None:
                        time.sleep(0.2)
                        pydirectinput.click(1631, 103)
                    menu2 = pyautogui.locateOnScreen('menu2.jpg', confidence=0.8)
                    x, y = pyautogui.center(menu2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選項")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('one.jpg', confidence=0.8) is None:  # 辨識下拉滑桿
                        time.sleep(0.1)
                    one = pyautogui.locateOnScreen('one.jpg', confidence=0.8)
                    x, y = pyautogui.center(one)
                    pyautogui.mouseDown(x, y)
                    pyautogui.dragTo(1618, 1250, 0.6, button='left')
                    while pyautogui.locateOnScreen('delete.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete = pyautogui.locateOnScreen('delete.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 刪除使用者資料")
                    time.sleep(0.2)
                    while pyautogui.locateOnScreen('delete2.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete2 = pyautogui.locateOnScreen('delete2.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 確認刪除使用者資料")
                    time.sleep(0.6)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 最後確認刪除使用者資料")
                    time.sleep(0.5)
                    closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
                    x, y = pyautogui.center(closure)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 關閉")
                    time.sleep(1.5)
                    counst = 98
                    add = 6
                    GG = 0
                if pyautogui.locateOnScreen('11.jpg', confidence=0.8) : #如果有"張數不足"的圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print ("靠北 只有2張 只能1突= = 重新刷一次")
                    two_count += 1
                    time.sleep(1)
                    pydirectinput.moveTo(1631, 103)
                    pydirectinput.click(1631, 103)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選單")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('menu2.jpg', confidence=0.8) is None:
                        time.sleep(0.2)
                        pydirectinput.click(1631, 103)
                    menu2 = pyautogui.locateOnScreen('menu2.jpg', confidence=0.8)
                    x, y = pyautogui.center(menu2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選項")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('one.jpg', confidence=0.8) is None:  # 辨識下拉滑桿
                        time.sleep(0.1)
                    one = pyautogui.locateOnScreen('one.jpg', confidence=0.8)
                    x, y = pyautogui.center(one)
                    pyautogui.mouseDown(x, y)
                    pyautogui.dragTo(1618, 1250, 0.6, button='left')
                    while pyautogui.locateOnScreen('delete.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete = pyautogui.locateOnScreen('delete.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 刪除使用者資料")
                    time.sleep(0.2)
                    while pyautogui.locateOnScreen('delete2.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete2 = pyautogui.locateOnScreen('delete2.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 確認刪除使用者資料")
                    time.sleep(0.6)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 最後確認刪除使用者資料")
                    time.sleep(0.5)
                    closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
                    x, y = pyautogui.center(closure)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 關閉")
                    time.sleep(1.5)
                    counst = 98
                    add = 6
                    GG = 0
                if pyautogui.locateOnScreen('21.jpg', confidence=0.6) : #如果有"張數不足"的圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print (time.ctime() + "： 靠北 只有3張 只能2突= = 重新刷一次")
                    three_count +=1
                    time.sleep(1)
                    pydirectinput.moveTo(1631, 103)
                    pydirectinput.click(1631, 103)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選單")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('menu2.jpg', confidence=0.8) is None:
                        time.sleep(0.2)
                        pydirectinput.click(1631, 103)
                    menu2 = pyautogui.locateOnScreen('menu2.jpg', confidence=0.8)
                    x, y = pyautogui.center(menu2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 點選選項")
                    time.sleep(1)
                    while pyautogui.locateOnScreen('one.jpg', confidence=0.8) is None:  # 辨識下拉滑桿
                        time.sleep(0.1)
                    one = pyautogui.locateOnScreen('one.jpg', confidence=0.8)
                    x, y = pyautogui.center(one)
                    pyautogui.mouseDown(x, y)
                    pyautogui.dragTo(1618, 1250, 0.6, button='left')
                    while pyautogui.locateOnScreen('delete.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete = pyautogui.locateOnScreen('delete.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 刪除使用者資料")
                    time.sleep(0.2)
                    while pyautogui.locateOnScreen('delete2.jpg', confidence=0.8) is None:
                        time.sleep(0.1)
                    delete2 = pyautogui.locateOnScreen('delete2.jpg', confidence=0.8)
                    x, y = pyautogui.center(delete2)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 確認刪除使用者資料")
                    time.sleep(0.6)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 最後確認刪除使用者資料")
                    time.sleep(0.5)
                    closure = pyautogui.locateOnScreen('closure.jpg', confidence=0.8)
                    x, y = pyautogui.center(closure)
                    pydirectinput.moveTo(x, y)
                    pydirectinput.click(x, y)
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print(time.ctime() + "： 關閉")
                    time.sleep(1.5)
                    counst = 98
                    add = 6
                    GG = 0
                if pyautogui.locateOnScreen('41.jpg', confidence=0.6) : #如果有"張數不足"的圖片
                    total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                    print (time.ctime() + "： 靠北 中了 停止")
                    four_count += 1
                    time.sleep(54000)
                    time.sleep(54000)
                    break
            if (add==6 or ssr >=3)and counst ==1:
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print ("抽到三張以上的小北 查看一下")
                break
            while (pyautogui.locateOnScreen('oneget.jpg', confidence=0.8) is None )and counst ==1:
                time.sleep(0.1)
            if counst ==1 and GG==1:
                while pyautogui.locateOnScreen('oneget.jpg', confidence=0.8) is None:
                    time.sleep(0.1)
                oneget = pyautogui.locateOnScreen('oneget.jpg', confidence=0.8)
                x, y = pyautogui.center(oneget)
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "：再抽一次")
                pydirectinput.moveTo(x, y)
                time.sleep(1)
                pydirectinput.click(x, y)
                time.sleep(0.5)
                while pyautogui.locateOnScreen('getgogo.jpg', confidence=0.8) is None:
                    time.sleep(0.1)
                    getgogo_counst +=5
                    if getgogo_counst >= 40 :
                        pydirectinput.click(x, y)
                        time.sleep(0.5)
                        getgogo_counst = 0
                getgogo = pyautogui.locateOnScreen('getgogo.jpg', confidence=0.8)
                total_cout(system_const, zero_count, one_count, two_count, three_count, four_count)
                print(time.ctime() + "：抽轉蛋")
                x, y = pyautogui.center(getgogo)
                pydirectinput.moveTo(x, y)
                pydirectinput.click(x, y)
                time.sleep(0.3)
#
#         # print ("點空白處")
#         # pyautogui.click(1100, 485)  # 中心座標

# while 1:
#     a = pyautogui.position()
#     print(a)
#     time.sleep(1)


'''
pydirectinput.click(997, 1426)
count = 240
temp_F9 = 1
temp_GG = 1
while 1:
    now = datetime.datetime.now()
    a = now.strftime("%Y-%m-%d %H:%M:%S")
    print(count)
    if count >= 240:
        pydirectinput.press('F9')
        print (a+'施放了'+str(temp_F9)+'次輪迴')
        count = 0
        temp_F9 +=1
    time.sleep(5)
    temp = pyautogui.locateOnScreen('GGGGGG.jpg', confidence=0.8)
    if temp:
        print(a+"死了第"+str(temp_GG)+"次")
        #pydirectinput.click(1474, 764)
        x,y = pyautogui.center(temp)
        pydirectinput.click(x, y)
        time.sleep(3)
        temp_GG +=1
        count =240
    count += 5
'''