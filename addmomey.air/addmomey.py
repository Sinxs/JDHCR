# -*- encoding=utf8 -*-
__author__ = "v-wutaotao"

from airtest.core.api import using
using("Gameplay.air")
import Gameplay

auto_setup(__file__)

import time
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
def addmoney():
    poco("btn_gm").click()
    for momey in range(2):
        poco(text="增加1000砖石").click()
        poco(text="增加1000金币").click()
    Gameplay.start()
         
addmoney()
