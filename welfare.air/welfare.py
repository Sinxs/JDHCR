# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"
from airtest.core.api import using
using("Gameplay.air")
import Gameplay
import time
# auto_setup(__file__)
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def welfare():
    Gameplay.start()
    print("----------------福利test-----------------")
    print("登录奖励test")
    time.sleep(2)
    poco = UnityPoco()
    poco("btn_welfare").click()  # 点击福利按钮
    poco(text="登录奖励").click()
    print("登录奖励test-------------------")
    for i in range(1, 9):
        img_bg = poco(text="领取成功")
        if img_bg.exists():
            poco("btn_ok").click()
            print("领取第%s天签到福利" % str(i-1))
        else:
            poco("btn_check_%d" % i).click()
            print("点击第%s天签到福利icon" % i)
    return poco("txt_title").get_text()

def selected():
    Gameplay.start()
    poco = UnityPoco()
    print("每日抽奖test")
    poco("btn_welfare").click()  # 点击福利按钮
    poco(text="每日抽奖").click()
    for i in range(1, 13):
        itme = poco("txt_item%s" % i).get_text()
        num = poco("txt_num%s" % i).get_text()
        print("第%s栏位奖励为:" % i + itme + " " + num)

    if poco("txt_lottery_free").exists():
        free = poco("txt_lottery_free").get_text()
        times = poco("txt_lottery_left_times").get_text()
        print("当前拥有" + free + "次数，剩余次数" + times)
        poco("btn_lottery").click()
        time.sleep(20)
        if poco("UIPanelLotteryDouble").child("img_bg").exists():  # 广告收益
            poco("UIPanelLotteryDouble").child("img_bg").child("btn_close").child("Image").click()  # 直接关闭

        amount = poco("txt_amount").get_text()
        print("获得奖励" + amount)
        poco(texture="btn_close").click()  # 关闭奖励弹窗
        times1 = poco("txt_lottery_left_times").get_text()

        print("点击" + free + "，剩余次数" + times1)

    else:
        print("当前没有免费抽奖次数")
    return poco("txt_title").get_text()


def cdk():
    Gameplay.start()
    poco = UnityPoco()
    print("礼包兑换test")
    poco("btn_welfare").click()  # 点击福利按钮
    poco(text="礼包兑换").click()
    poco("input_key").set_text("123456789")
    poco("btn_reward").click()
    print(poco(text="请到相应网站领取礼包兑换码（每个兑换码只能使用1次哦），兑换码不定期通过活动形式发放，请留意相关的活动公告。").get_text()
)
    return poco("txt_title").get_text()




