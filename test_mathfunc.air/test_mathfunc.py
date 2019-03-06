# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"

from airtest.core.api import *
from airtest.core.api import using
using("Gameplay.air")
import Gameplay
using("welfare.air")
import welfare
using("activity.air")
import activity
from HTMLTestRunner import HTMLTestRunner
auto_setup(__file__)
import unittest

class TestMathFunc(unittest.TestCase):

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作")

   # @unittest.skip("我想临时跳过这个测试用例.")
    def test_add(self):

        #self.assertEqual(7,add(7))
        self.assertEqual(3, Gameplay.add(1, 2))
        #self.assertNotEqual(3, test_单元测试.add(2, 2))  # 测试业务方法add

    def test_minus(self):
        #self.skipTest('跳过这个测试用例')
        self.assertEqual(1, Gameplay.minus(3, 2))  # 测试业务方法minus
        print("测试业务方法")
    def test_multi(self):
        self.assertEqual(6, Gameplay.multi(2, 3))  # 测试业务方法multi

    def test_divide(self):
        self.assertEqual(2, Gameplay.divide(6, 3))  # 测试业务方法divide
        self.assertEqual(2.5, Gameplay.divide(5, 2))
    
    def test_name(self):
        self.assertEqual("账号设置",Gameplay.name())
    def test_game(self):
        self.assertEqual("游戏设置",Gameplay.game())
    def test_btnopt(self):
        self.assertEqual("操作设置",Gameplay.btnopt())  
    def test_facial(self):
        self.assertEqual("表情设置",Gameplay.facial()) 
    def test_head(self):
        self.assertTrue(Gameplay.head())
        
        
        
    def test_welfare(self):
        self.assertEqual("登录奖励",welfare.welfare()) 
    def test_selected(self):
        self.assertEqual("每日抽奖",welfare.selected()) 
    def test_cdk(self):
        self.assertEqual("礼包兑换",welfare.cdk()) 
        
    
    
    
    def test_ceyice(self):
        self.assertEqual("测一测",activity.ceyice()) 
    def test_jianjinbi(self):
        self.assertEqual("捡金币",activity.jianjinbi()) 
        
# if __name__ == "__main__":
#     runner.run(test_suite)


