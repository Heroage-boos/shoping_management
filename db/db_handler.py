"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: db_handler.py
@time: 2025/7/4 10:27
@desc: 数据处理层
"""

import json
import os
from conf import settings


#查询数据
def select_data(username,data=True):
    """
    查询数据
    :param username: 用户名
    :param data: data为false时，表示只查询文件是否存在，不返回数据
    :return: 数据
    """
    #1. 接收逻辑接口层传过来的username，并拼接处用户名.json文件的路径
    user_path = os.path.join(settings.USER_DATA_DIR, f'{username}.json')  # 使用用户名作为文件名保存用户数据

    #2.判断用户名.json文件是否存在
    if not os.path.exists( user_path ):
        return

    #3.判断接口层是否存在数据，不需要则返回True
    if not data:
        return True
    #4，如果存在，则打开文件，读取数据
    with open(user_path, 'rt', encoding='utf-8') as f:
        user_data = json.load(f)
        return user_data
