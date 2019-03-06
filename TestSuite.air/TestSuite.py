# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"

from airtest.core.api import *
import os
from HTMLTestRunner import HTMLTestRunner
import unittest
from airtest.core.api import using
using("test_mathfunc.air")
from test_mathfunc import TestMathFunc
using("emalitest.air")
import emalitest
auto_setup(__file__)

# if __name__ == "__main__":
wake()
shell("input swipe 525 1723 525 1087 300")
home()
"""唤醒MI6设备并进入主界面"""
test_suite = unittest.TestSuite()
tests =   [TestMathFunc("test_add"),TestMathFunc("test_minus"),TestMathFunc("test_multi"),TestMathFunc("test_divide"),TestMathFunc("test_name"),TestMathFunc("test_game"),TestMathFunc("test_btnopt"),TestMathFunc("test_facial"),TestMathFunc("test_head"),TestMathFunc("test_welfare"),TestMathFunc("test_selected"),TestMathFunc("test_cdk"),TestMathFunc("test_jianjinbi")] # 添加测试套件
# tests = [TestMathFunc("test_name")] # 测试单独模块
test_suite.addTests(tests)

with open('D:\\乱斗火柴人测试结果.html', 'wb') as f:  # 形成html报告结果
    runner = HTMLTestRunner(stream=f,
                             title='自动化测试报告.',
                             description='乱斗火柴人测试结果.'
                                )
    runner.run(test_suite)   
emalitest.emalitest()  # 把结果邮件发送给目标
home() # 回到主界面
