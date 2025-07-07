"""
@author: yaojy  # 使用yaojy自动填充当前系统用户名
@contact: yjy18593128603@163.com
@project: shopping_manageent
@file: bank_interface.py
@time: 2025/7/3 17:15
@desc: 银行相关接口
"""
import db.db_handler
from db import db_handler

# 充值接口
def recharge_interface(username, amount):
    """
    充值接口
    :param user_data: 用户数据
    :param amount: 充值金额
    :return: (bool, str) 返回充值结果和提示信息
    """
    user_data=db.db_handler.select_data(username)  # 确保用户数据存在

    # 更新用户余额
    user_data['balance'] += amount

    # 调用数据处理层，保存修改后的用户数据
    db.db_handler.save(user_data)

    return True, f"充值成功，当前余额为: {user_data['balance']}"

