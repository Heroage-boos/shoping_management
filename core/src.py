"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: shopping_manageent
@file: src.py
@time: 2025/7/3 17:19
@desc: 用户视图层
"""


# 0.退出
def sing_out():
    print("退出功能!")
    exit(0)

# 1、注册功能
def register():
    print("注册功能!")
    # 这里可以添加注册逻辑，比如输入用户名、密码等
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    # 假设注册成功
    print("用户 {username} 注册成功!")

# 2.登录功能
def login():
    print("登录功能!")
    # 这里可以添加登录逻辑，比如输入用户名、密码等
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    # 假设登录成功
    print(f"用户 {username} 登录成功!")

# 3.充值功能
def recharge():
    print("充值功能!")
    # 这里可以添加充值逻辑，比如输入充值金额等
    amount = input("请输入充值金额: ")
    # 假设充值成功
    print(f"已成功充值 {amount} 元!")

# 4、转账功能
def transfer():
    print("转账功能!")
    # 这里可以添加转账逻辑，比如输入转账金额和接收人等
    amount = input("请输入转账金额: ")
    recipient = input("请输入接收人用户名: ")
    # 假设转账成功
    print(f"已成功向 {recipient} 转账 {amount} 元!")

# 5、提现功能
def withdraw():
    print("提现功能!")
    # 这里可以添加提现逻辑，比如输入提现金额等
    amount = input("请输入提现金额: ")
    # 假设提现成功
    print(f"已成功提现 {amount} 元!")

# 6、查看余额
def check_balance():
    print("查看余额功能!")
    # 这里可以添加查看余额逻辑
    # 假设余额为1000元
    balance = 1000
    print(f"您的当前余额为 {balance} 元!")

# 7、查看流水
def check_flow():
    print("查看流水功能!")
    # 这里可以添加查看流水逻辑
    # 假设有一些流水记录
    flow_records = [
        "2025-07-01 充值 1000元",
        "2025-07-02 转账 200元 到 用户A",
        "2025-07-03 提现 300元"
    ]
    print("您的流水记录如下:")
    for record in flow_records:
        print(record)

# 8、购物功能
def shopping():
    print("购物功能!")
    # 这里可以添加购物逻辑，比如选择商品、添加到购物车等
    product = input("请输入要购买的商品名称: ")
    quantity = input("请输入购买数量: ")
    # 假设购物成功
    print(f"已成功购买 {quantity} 个 {product}!")

# 9、查看购物车
def check_shop():
    print("查看购物车功能!")
    # 这里可以添加查看购物车逻辑
    # 假设购物车中有一些商品
    cart_items = [
        "商品A x 2",
        "商品B x 1",
        "商品C x 3"
    ]
    print("您的购物车中有以下商品:")
    for item in cart_items:
        print(item)

# 10、退出账号
def login_out():
    print("退出账号功能!")
    # 这里可以添加退出账号逻辑
    # 假设退出成功
    print("已成功退出账号!")

# 11、管理员功能
def admin():
    print("管理员功能!")
    # 这里可以添加管理员逻辑，比如管理用户、查看统计等
    action = input("请输入管理员操作 (1: 查看用户, 2: 查看统计): ")
    if action == "1":
        print("查看用户功能!")
        # 假设有一些用户记录
        users = ["用户A", "用户B", "用户C"]
        print("当前用户列表:")
        for user in users:
            print(user)
    elif action == "2":
        print("查看统计功能!")
        # 假设有一些统计数据
        stats = {"总用户数": 100, "总交易额": 50000}
        print("系统统计数据:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    else:
        print("无效的管理员操作!")


# 函数字典
func_dic={
        '0':('退出功能', sing_out),
        '1':('注册功能', register),
        '2':('登录功能', login),
        '3':('充值功能', recharge),
        '4':('转账功能', transfer),
        '5':('提现功能', withdraw),
        '6':('查看余额', check_balance),
        '7':('查看流水', check_flow),
        '8':('购物功能', shopping),
        '9':('查看购物车', check_shop),
        '10':('退出账号', login_out),
        '11':('管理员功能', admin),
    }

# 主程序
def main():
    while True:
        print("欢迎使用银行系统，请选择功能:")
        for key, (desc, _) in func_dic.items():
            print(f"{key}: {desc}")
        choice = input("请输入功能编号: ").strip()
        if choice in func_dic:
            func_dic[choice][1]()  # 调用对应的函数
        else:
            print("无效的功能编号，请重新输入!")