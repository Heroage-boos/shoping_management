"""
@author: yaojy  # 使用yaojy自动填充当前系统用户名
@contact: yjy18593128603@163.com
@project: shopping_manageent
@file: bank_interface.py
@time: 2025/7/3 17:15
@desc: 银行相关接口
"""
import db.db_handler
from datetime import datetime # 用于获取当前时间
from db import db_handler
from conf import settings


# 充值接口
def recharge_interface(username, amount):
    """
    充值接口
    :param user_data: 用户数据
    :param amount: 充值金额
    :return: (bool, str) 返回充值结果和提示信息
    """
    user_data=db.db_handler.select_data(username)  # 确保用户数据存在

    #  如果是登录用户充值user_data一定是有的，但管理员充值可以自定义充值人的名称，则可能不存在此用户，所以返回True
    if not user_data:
        return True

    # 1.更新用户余额
    user_data['balance'] += amount

    # 2.记录流水
    msg= f"\n {datetime.now()} 用户:{username} 充值 {amount} 元,成功，当前余额为: {user_data['balance']}元"
    user_data['flow'].append(msg)

    # 3.调用数据处理层，保存修改后的用户数据
    db.db_handler.save(user_data)

    return True, f"充值成功，当前余额为: {user_data['balance']}"

# 提现接口
def withdraw_interface(username, amount):
    """
    提现接口
    :param username: 用户名
    :param amount: 提现金额
    :return: (bool, str) 返回提现结果和提示信息
    """
    # 1. 获取用户数据
    user_data = db_handler.select_data(username)  # 确保用户数据存在
    balance = user_data.get('balance')

    # 2.计算手续费，并判断用余额是否充足
    service_fee=amount * settings.RATE
    if (service_fee + amount) > balance:
        return False, "\n余额不足，无法提现"

    # 3.更新用户余额
    user_data['balance'] -= amount

    # 4.记录流水
    msg = f"\n {datetime.now()} 用户:{username} 提现 {amount} 元,成功，手续费为 {service_fee} ，当前余额为: {user_data['balance']}元"
    user_data['flow'].append( msg )

    # 调用数据处理层，保存修改后的用户数据
    db_handler.save(user_data)

    return True, f"提现成功，当前余额为: {user_data['balance']}"

#余额查新
def balance_interface(username):
    """
    余额查询接口
    :param username: 用户名
    :return: (bool, str) 返回查询结果和提示信息
    """
    # 1. 获取用户数据
    user_data = db_handler.select_data(username)  # 确保用户数据存在

    # 2.返回余额信息
    return True, f"当前余额为: {user_data['balance']}"

# 转账
def transfer_interface(sender, recipient, amount):
    """
    转账接口
    :param sender: 发送者用户名
    :param recipient: 接收者用户名
    :param amount: 转账金额
    :return: (bool, str) 返回转账结果和提示信息
    """
    # 1. 获取发送者数据
    sender_data = db_handler.select_data(sender)
    if not sender_data:
        return False, "发送者不存在"

    # 2. 获取接收者数据
    recipient_data = db_handler.select_data(recipient)
    if not recipient_data:
        return False, "接收者不存在"

    # 3. 检查余额是否充足
    if amount > sender_data['balance']:
        return False, "余额不足，无法转账"

    # 4. 扣除发送者余额并增加接收者余额
    sender_data['balance'] -= amount
    recipient_data['balance'] += amount

    # 5.记录流水
    #5.1 发送者流水记录
    send_msg = f"\n {datetime.now()} 用户:{sender_data.get('username')} 转账 {amount} 元,成功，，当前余额为: {sender_data['balance']}元"
    sender_data.flow.append( send_msg )
    # 5.2 接收者流水记录
    receive_msg = f"\n {datetime.now()} 用户:{recipient_data.get('username')} 收到{sender_data['balance']} 转账 {amount} 元,成功，当前余额为: {recipient_data['balance']}元"
    recipient_data.flow.append( receive_msg )

    # 6. 保存修改后的用户数据
    db_handler.save(sender_data)
    db_handler.save(recipient_data)

    return True, f"转账成功，{sender} 当前余额为: {sender_data['balance']}, {recipient} 当前余额为: {recipient_data['balance']}"

# 查看流水接口
def check_flow_interface(username):
    """
    查看流水接口
    :param username: 用户名
    :return: (bool, list) 返回流水记录和提示信息
    """
    # 1. 获取用户数据
    user_data = db_handler.select_data(username)  # 确保用户数据存在

    # 2.返回流水记录
    if not user_data.get('flow'):
        return False, "没有流水记录",[]

    return True,"", user_data['flow']  # 返回流水记录列表