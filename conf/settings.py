"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: settings.py
@time: 2025/7/4 10:28
@desc: 配置信息
"""

#获取项目根目录
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONFIG_PATH = os.path.join(BASE_DIR, 'settings.cfg')

# 获取USER_DAT路径 检查配置文件是否存在
import configparser  #导入 Python 标准库中的 configparser 模块，用于读取和解析配置文件（如 .ini 或 .cfg 文件）。
config=configparser.ConfigParser()  #创建一个 ConfigParser 对象，用于操作配置文件的数据。
config.read(CONFIG_PATH,encoding='utf-8')  #读取指定路径（CONFIG_PATH）下的配置文件内容，加载到 config 对象中，便于后续通过 config.get() 等方法获取配置信息。

# 获取配置文件中的数据库路径
USER_DATA_DIR=config.get('path', 'USER_DATA_DIR')

# 检查user_data目录是否存在，如果不存在则创建
if not os.path.isdir(USER_DATA_DIR):
    # 获取user_data文件路径
    USER_DATA_DIR = os.path.join( BASE_DIR, 'db', 'user_data' )

print('USER_DATA_DIR',USER_DATA_DIR)