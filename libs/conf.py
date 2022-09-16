# -*- coding: UTF-8 -*-
# @Time     : 2022/08/27 18:26
# @Author   : Ranshi
# @File     : conf.py
# @Doc      : 读取toml设置文件

import toml

conf = toml.load(f="setting.toml")
