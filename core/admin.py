"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: admin.py
@time: 2025/7/8 10:25
@desc: 管理员视图层
"""
from core import src
from interface import admin_interface

# 添加账户功能
def add_user():
    is_admin=input("是否为管理员账户？(y/n): ").strip().lower()
    #通过管理员注册的用户是管理员
    if is_admin=='y':
        src.register(True)
    else :
        src.register(False)

# 冻结账户功能
def lock_user():
    while True:
        # 1.获取要冻结的账户名
        lock_username = input("请输入要冻结/解冻的账户名: ").strip()
        is_lock = input("是否确认冻结该账户？(y/n): ").strip().lower()

        # 2.判断用户是否想要退出
        if is_lock=='y':
            break

        # 3.调用冻结接口层冻结账户
        flag, msg=admin_interface.lock_user_interface(lock_username)
        print(msg)
        if flag:
            break

# 给用户充值
def recharge_to_user():
  pass

func_dic = {
    '0': ('退出管理员',),  # 退出管理员功能
    '1': ('添加账户功能', add_user),
    '2': ('冻结/解冻账户功能', lock_user),
    '3': ('给用户充值', recharge_to_user),
}

# 管理员视图层主程序
def main():
    while True:
        print("\n欢迎使用管理员功能，请选择操作：")
        for key in func_dic:
            print(f"{key}. {func_dic.get(key)[0]}".center(20, "="))

        choice = input("请输入选项编号: ").strip()

        if choice not in func_dic:
            print("此功能不存在，请重新输入！")
            continue

        if choice == '0':
            break

        # 执行对应的功能
        func_dic.get(choice)[1]()  # 调用对应的函数
