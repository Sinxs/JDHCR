# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"

from airtest.core.api import *
from airtest.core.api import using
using("Gameplay.air")
import Gameplay
import time
import random
auto_setup(__file__)
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def ceyice():
    Gameplay.start()
    print("----------------活动test-----------------")
    print("测一测活动test")
    time.sleep(2)
    poco = UnityPoco()
    poco("btn_activity").click() #点击活动按钮
    poco("Canvas")[0].offspring("Content").offspring("txt").click() # 点击测一测
    poco("btn_start_test").click()
    for i in range(3):
        A = random.randint(1,3)
        poco("T%d" % A).click()
        if poco(text="下一题").exists():
            poco(text="下一题").click()
        else:
            poco("btn_question_result").click()        
    poco(text="保存图片").click()
    time.sleep(1)
    poco(texture="img_btn_close").click()
    return poco("txt_title").get_text()

def jianjinbi():
    Gameplay.start()
    print("----------------活动test-----------------")
    print("捡金币活动test")
    time.sleep(2)
    poco = UnityPoco()
    poco("btn_activity").click() #点击活动按钮
    poco(text="捡金币").click()  # 点击捡金币
    txt_count_down = poco("txt_count_down").get_text()
    print(txt_count_down)

    for A in range(30):
        img_reward = "img_reward" + str(A)
        if poco(img_reward).exists():
            pass
            if (A == 2 or A == 4 or A == 6 or A == 9 or A == 11 or A == 14 or A == 16 or
                    A == 19 or A == 21 or A == 24 or A == 26 or A == 29):
                img_effect = poco(img_reward).child("PickRewardItem").child("img_reward_base").child("img_effect")
                if img_effect.exists():
                    poco(img_reward).child("PickRewardItem").child("img_reward_base").child("img_effect").click()
                    if poco("img_light").exists():
                        print("第" + str(A) + "步奖励已验证")
                    else:
                        print("第"+str(A)+"步奖励出错")
                else:
                    print("第" + str(A) + "步奖励异常，没有奖励显示，可能是已经被领取了，需要验证")
            else:
                print("第" + str(A) + "步没有奖励")
        else:
            print("error：UI出错，界面没有控件")
    if poco("txt_free").exists():
        poco("txt_free").click()
        if poco(text="获得奖励").exists():
            poco(text="获得奖励").click()
            poco("btn_ok").click()
            
        else:
            print("没有奖励")
    else:
        print("当前不能免费前进")
        
    return poco("txt_title").get_text()

 
    



