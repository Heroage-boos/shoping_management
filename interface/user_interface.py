"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: user_interface.py
@time: 2025/7/7 14:12
@desc: 用户相关接口
"""

from db import db_handler

# 注册接口
def register_interface(username,password,is_admin=False,balance=0):
    '''
    用户注册接口
    :param username:用户名称
    :param password: 密码
    :param is_admin: 是否是管理员
    :param balance: 余额
    :return： (bool, str) 返回注册结果和提示信息
    '''
    #1.调用用户接口层，查询用户名是否存在
    if db_handler.select_data(username,False):
        return False,'\n用户名已存在，请重新输入用户名！'

    #2.组织用户数据
    user_data = {
        'username': username,
        'password': password,
        "balance": balance,  # 初始余额为0
        "shopping_card": [],  # 初始购物车为空
        'flow': [],  # 初始流水记录为空
        'is_admin': is_admin,  # 初始不是管理员
        'locked': False,  # 初始不锁定账号
    }

    #。3.调用核心层的用户服务进行注册
    flag=db_handler.save(user_data)
    if flag:
        return True, f'\n用户: {username} 注册成功'

# 登录接口
def login_interface(username,password):
    # 1.调用用户接口层，查询用户名是否存在
    user_data = db_handler.select_data(username)
    if not user_data:
        return False, '\n用户名不存在，请重新输入用户名！',False
    # 2.判断密码是否正确
    if not password == user_data.get('password'):
        return False, '\n密码错误，请重新输入密码！',False
    # 3.判断账号是否被锁定
    if user_data.get('locked'):
        return False, '\n账号已被锁定，请联系管理员解锁！'
    # 4.登录成功，返回用户数据
    return True, user_data,user_data.get('is_admin')