
__author__ = "v-wutaotao"

from airtest.core.api import *
auto_setup(__file__)
import time
import random

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()

def start():
    stop_app('com.example.gcloudu3ddemo')
    time.sleep(2)
    start_app('com.example.gcloudu3ddemo')
    time.sleep(10)
    
    poco = UnityPoco()
    if poco("Scroll View").exists():
        poco("btn_go").click()
        if poco(text="是否进入新手引导？").exists():
            poco("btn_close").click()
            
            print("启动成功")
        else:
            
            print("启动成功")
    else:
        print("启动失败")


def head():
    start()
    poco = UnityPoco()
    poco("btn_setting").click()
    print("点击设置")
    if poco("btn_head").exists():
        poco("btn_head").click()
        print("头像")
    else:
        print("没有头像")
    for i in range(35, 37):
        print(i)
        if i >= 21:
            print("up")
            x, y = poco(texture="team_20").get_position()
            dir = [0, -0.5]
            poco.swipe([x, y], direction=dir)
            poco("Batch_bg").child("img_head_bg")[i].click()
            if i < 36:
                poco("btn_head").click()
                print("切换%s号头像test成功" % i)
        else:
            print(i)
            poco("Batch_bg").child("img_head_bg")[i].click()
            poco("btn_head").click()
            print("切换%s号头像test成功" % i)     
    print("测试完成")
    return poco("img_icon")

def name(): 
    start()
    poco = UnityPoco()
    poco("btn_gm").click()
    poco("btn_reg").click()
    time.sleep(3)
    start()
    poco = UnityPoco()
    
        

    poco("btn_setting").click()

    print("--------------------头像tets-----------------")
    name=random.randint(100, 999)
    name1 = str(name)
    if poco("panel_name").child("txt_name").exists():
        print("呼出设置界面")
        poco("panel_name").child("txt_name").click()
        print("点击用户名")
    else:
        print("没有呼出用户名"+"\n")
    poco("input").set_text("123456123")
    time.sleep(1)
    txt_tips = poco("txt_tips_3")
    if txt_tips.exists():
        print("输入不符合规范的用户名，正确提示用户名格式test错误：重新输入正确格式的用户名")
    else:
        print("EROOR:用户名格式test错误")

    def panel_name():
        poco("input").set_text("ttw" + name1)
        poco("btn_name").click()
        if poco(text="用户名已存在").exists():
            print("用户名已存在，重新输入用户名")
            poco("panel_name").child("img").click()
            panel_name()
    panel_name()
    print("设置用户名ttw"+name1)
    poco("btn_modify_password").click()
    poco("input_0").set_text("")
    poco("input_0").set_text(name1 + name1)
    time.sleep(1)
    poco("btn_create").click()
    if poco(text="密码长度仅支持8-14位").exists():
        print("密码验证成功" )
    else:
        print("EROOR:passwordtestpass")
    poco("input_0").set_text("tt" + name1+name1)
    print("tt"+name1+name1)
    time.sleep(1)
    poco("txt_page_0_confirm").click()
    
    poco("txt_age").click()
    poco("input").set_text(name1)
    time.sleep(2)
    poco("btn_ok").click()
#     if poco(text="修改年龄成功").exists():
#         print(poco(text="修改年龄成功").get_text())
#     else:
#         print("EROOR:设置年龄失败")
    
        #  选择性别
    A = "female"
    B = "male"
    C = [A,B]
    D = random.choice(C)
    if poco(D).child("Image").exists():
        poco(D).child("Image").click()
        print("点击选择性别：%s" % D)
    if poco(texture="btn_check").exists():
        print("已经选择过性别")    
        print(poco("txt_account").get_text())
    return poco("txt_title").get_text()
    

        
def game():  # 游戏设置
    start()
    poco = UnityPoco()
    time.sleep(2)
    poco("btn_setting").click()
    poco("btn_game").click()
    txt_title = poco("txt_title").get_text()
    if txt_title == "游戏设置":
        Slider_Music = poco("slider_music").child("Handle Slide Area").child("Handle").child("img_")  # 背景音乐滚动条
        poco("btn_music_close").child("Text").click()
        poco("btn_music_open").child("Text").long_click()
        print("背景音乐开关pass")
        Slider_Music.swipe([-0.2, 0])
        Slider_Music.swipe([0.2, 0])
        print("背景音乐滚动条pass")
        Slider_Music_Effect = poco("slider_music_effect").child("Handle Slide Area").child("Handle").child("img_")  # 音效滚动条
        poco("btn_effect_close").click()
        poco("btn_effect_open").long_click()
        print("音效开关pass")
        Slider_Music_Effect.swipe("left")
        Slider_Music_Effect.swipe("right")
        print("音效滚动条pass")
        Slider_Voice = poco("slider_voice").child("Handle Slide Area").child("Handle").child("img_")  # 语音滚动条
        poco("btn_chat_close").click()
        poco("btn_chat_open").long_click()
        print("语音开关pass")
        Slider_Voice.swipe("left")
        Slider_Voice.swipe("right")
        print("语音滚动条pass")
        img_quality=["低", "中", "高"]
        for img_quality1 in img_quality:
            poco(text = img_quality1).click()
        print("画质开关pass")
        poco("btn_facial_open").click()
        poco("btn_facial_close").click()  # 局内聊天
        poco("btn_team_invite_open").click()
        poco("btn_team_invite_close").click()  # 组队邀请
        poco("btn_room_invite_open").click()
        poco("btn_room_invite_close").click()  # 房间邀请
        poco("btn_room_invite_open").swipe("up")
        poco("btn_follow_open").click()
        poco("btn_follow_close").click()  # 关注提示
    else:
        print("eroor:没有进入游戏设置")        
    return poco("txt_title").get_text()
   

def btnopt():  # 操作设置。
    start()
    poco = UnityPoco()
    time.sleep(2)
    poco("btn_setting").click()
    poco("btn_opt").click()
    txt_title = poco("txt_title").get_text()
    if txt_title == "操作设置":
        poco("btn_btn").click()
        poco("btn_joystick").click()
        print("遥感模式pass")
        poco("btn_cancel_fire2").click()
        poco("btn_cancel_fire1").click()
        print("滑至取消按钮pass")
        poco(text="键位自定义").click()

        def SliderSize():
            poco = UnityPoco()
            SliderSize = poco("SliderSize").child("Handle Slide Area").child("Handle")
            SliderSize.swipe([-0.2, 0])
            SliderSize.swipe([0.4, 0])
            SliderAlpha = poco("SliderAlpha").child("Handle Slide Area").child("Handle")
            SliderAlpha.swipe([-0.2, 0])
            SliderAlpha.swipe([0.4, 0])

        poco("Joystick").click()
        SliderSize()
        poco(texture="btn_zd_gongji").click()
        SliderSize()
        poco(texture="btn_zd_fangyu").click()
        SliderSize()
        poco(texture="btn_zd_tiaoyue").click()
        SliderSize()
        poco(texture="btn_zd_quxiao").click()
        SliderSize()
        print("自定义操作按钮设置大小、透明度pass")
        poco(text="确定").click()
        poco(text="键位自定义").click()
        poco(text="重置").click()
        poco(text="确定").click()
        poco(text="键位自定义").click()
        poco(text="退出").click()
        print("自定义操作按钮设置pass")
    else:
        print("error:没有进入操作设置")        
    return poco("txt_title").get_text()

def facial(): # 表情设置
    start()
    poco = UnityPoco()
    time.sleep(2)
    poco("btn_setting").click()
    poco("txt_facial").click()
    poco("btn_bg").click()
    if poco(text="白蛋蛋").exists():
        poco(texture="btn_close").click()
    else:
        print("没有找到白蛋蛋表情")
    return poco("txt_title").get_text()




    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def add(a, b):
    
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b


