"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: admin_interface.py
@time: 2025/7/4 13:50
@desc: 文件功能描述
"""
from db import db_handler

def lock_user_interface(username):
    """
    冻结用户账户接口
    :param username: 用户名
    :return: (bool, str) 返回冻结结果和提示信息
    """
    # 1.调用用户接口层，查询用户名是否存在
    from interface import user_interface
    user_data = user_interface.db_handler.select_data(username)

    if not user_data:
        return False, '\n用户名不存在，请重新输入用户名！'

    # 2.冻结账户
    if user_data['locked']:
        # 如果账户已经被冻结，则解冻
        user_data['locked'] = False
        return True, f'\n用户: {username} 已解冻'



    # 3.保存冻结状态到数据库
    user_data['locked'] = True
    flag= db_handler.save(user_data)

    if flag:
        return True, f'\n用户: {username} 已被冻结'
