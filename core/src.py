"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: shopping_manageent
@file: src.py
@time: 2025/7/3 17:19
@desc: 用户视图层
"""
from interface import user_interface,bank_interface  # 导入用户接口层
from lib import common  # 导入公共方法库

logged_user=None # 当前登录的用户数据
logged_admin=False # 是否是管理员

# 0.退出
@common.login_auth
def sing_out():
    print("感谢使用，欢迎下次再来!")
    #exit() 用于立即终止当前程序的运行。调用它后，程序会直接退出，不再执行后续代码。常用于用户选择退出时结束整个应用
    exit(0)

# 1、注册功能
def register(is_admin=False):
  print( "注册功能!" )
  while True:
      # 这里可以添加注册逻辑，比如输入用户名、密码等
      username = input( "请输入用户名: " )
      password = input( "请输入密码: " )
      re_password = input( "请再次输入密码: " )
      # strip() 方法用于移除字符串开头和结尾的所有空白字符（如空格、换行、制表符等）。在本行代码中，strip() 可以确保用户输入时无论前后是否有多余空格，都能正确处理输入内容。
      is_register = input( "按任意键确认 /n退出 " ).strip().lower()

      # 2.机型简单的逻辑判断
      # 2.1 如果用户输入 'n'，则取消注册
      if is_register == 'n':
          print( "注册已取消!" )
          break

      # 2.2 判断密码是否一致
      if password != re_password:
          print( "两次输入的密码不一致，请重新输入!" )
          continue

      # 2.3 检验用户名是否合法
      import re
      if not re.findall( "^[a-zA-Z]\w{2,9}$", username ):
          print( "用户名不合法! 必须以字母开头，长度为3-10个字符!" )
          continue

      # 2.4 检验密码强度  使用re 断言
      # if not re.findall( "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,12}$", password ):
      #     print( "密码强度不合格! 必须包含大小写字母和数字，长度为6-12个字符!" )
      #     continue

      # 3.做密码加密
      password = common.pwd_to_sha256( password )

      #4. 调用注册接口进行注册
      from interface import user_interface  # 导入用户接口层
      flag,msg=user_interface.register_interface( username, password ,is_admin)
      if flag:
          print( msg )
      else :
          print( '\n注册失败，请稍后再试！' )

# 2.登录功能
def login():
    print("登录功能!")
    while True:
        # 1.输入用户名、密码
        username = input( "请输入用户名: " ).strip()
        password = input( "请输入密码: " ).strip()
        is_login=  input( "按任意键确认 /n退出 ").strip().lower()

        # 2.是否取消操作
        if is_login == 'n':
            print( "登录已取消!" )
            break

        # 3.做密码加密
        password=common.pwd_to_sha256(password)

        # 4.校验是否存在此用户  不能直接调用视图层的接口，因为视图层是用户交互的界面，应该调用数据库处理层来查询数据
        # from db import db_handler  # 导入数据库处理层
        # user_data = db_handler.select_data( username, data=False )
        flag, msg,is_admin = user_interface.login_interface( username, password )

        # 5.存在此用户，调用登录接口进行登录
        if flag:
            user_data = msg
            print( f"\n欢迎 {user_data.get('username')} 登录!" )

            # 登录成功后，记录登录用户日志
            global logged_user,logged_admin  #设置全局变量，后面判断用户是否是管理员
            logged_user=user_data.get('username')
            logged_admin=is_admin  # 是否是管理员
            break

        else:
            print( msg )

# 3.充值功能
@common.login_auth
def recharge(username=False):
    print( "充值功能!" )
    while True:
        # 1.这里可以添加充值逻辑，比如输入充值金额等
        amount = input("请输入充值金额: ").strip()
        is_recharge = input("按任意键确认 /n退出 ").strip().lower()

        # 2.取消充值操作
        if is_recharge == 'n':
            break
        # 3.充值校验
        if not amount:  # 如果输入为空
            print("充值金额不能为空!")
            continue
        # 检查金额是否是数字 和 大于0
        if not amount.isdigit() or int(amount) <= 0:
            print("请输入有效的充值金额!")
            continue

        # 3.1 如果没有传入用户名，则使用当前登录用户
        if not username :
            username=logged_user

        # 4.调用接口充值
        flag,msg= bank_interface.recharge_interface(username, int(amount))  # 调用充值接口
        if flag:
            print(msg)
        else:
            print("充值失败，请稍后再试!")

# 4、转账功能
@common.login_auth
def transfer():
    print("转账功能!")
    while True:
        # 这里可以添加转账逻辑，比如输入转账金额和接收人等
        amount = input( "请输入转账金额: " ).strip()
        recipient = input( "请输入接收人用户名: " ).strip()
        is_transfer = input( "按任意键确认 /n退出 " ).strip().lower()
        # 2.取消转账操作
        if is_transfer == 'n':
            break

        # 3.其他转账校验规则
        if(amount.isdigit() or int(amount) <= 0):
            print( "转账金额不能为空或小于等于0!" )
            continue

        if not recipient:
            print( "接收人用户名不能为空!" )
            continue

        if recipient == logged_user:
            print( "不能向自己转账!" )
            continue

        # 4.调用接口进行转账
        flag,msg=bank_interface.transfer_interface(logged_user, recipient, int(amount))  # 调用转账接口

        # 假设转账成功
        print(msg)

# 5、提现功能
def withdraw():
    print("提现功能!")
    # 这里可以添加提现逻辑，比如输入提现金额等

    while True:
        # 1.这里可以添加提现逻辑，比如输入提现金额等
        amount = input("请输入提现金额: ").strip()
        is_withdraw = input( "按任意键确认 /n退出 " ).strip().lower()

        # 2.取消充值操作
        if is_withdraw == 'n':
            break

        # 3.提现校验
        if not amount:  # 如果输入为空
            print( "提现金额不能为空!" )
            continue
        # 检查金额是否是数字 和 金额小于100
        if not amount.isdigit() or int( amount ) < 100:
            print( "请输入有效的提现金额!" )
            continue
        # 4.调用接口提现
        flag, msg = bank_interface.withdraw_interface( logged_user, int( amount ) )  # 调用充值接口
        if flag:
            print( msg )
        else:
            print( "充值失败，请稍后再试!" )

# 6、查看余额
@common.login_auth
def check_balance():
    print("查看余额功能!")
    # 1.调用接口查询余额
    flag,msg=bank_interface.balance_interface(logged_user)
    print(msg)

# 7、查看流水
@common.login_auth
def check_flow():
    print("查看流水功能!")
    # 1.调用接口查询流水
    flag,msg,flow_list=bank_interface.check_flow_interface(logged_user)
    if not flag:
        print(msg)
        return
    for record in flow_list:
        print( record )


# 8、购物功能
@common.login_auth
def shopping():
    print("购物功能!")
    # 这里可以添加购物逻辑，比如选择商品、添加到购物车等
    product = input("请输入要购买的商品名称: ")
    quantity = input("请输入购买数量: ")
    # 假设购物成功
    print(f"已成功购买 {quantity} 个 {product}!")

# 9、查看购物车
@common.login_auth
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
@common.login_auth
def login_out():
   global logged_user,logged_admin
   print(f"\n{logged_user} 退出登录!")
   logged_user=None
   logged_admin=False

# 11、管理员功能
@common.login_auth
def admin():

    print("管理员功能!")
    # 这里可以添加管理员逻辑，比如管理用户、查看统计等
    from core import admin
    admin.main()

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
        print("欢迎使用购物管理系统，请选择功能:")
        for num in func_dic:
            if logged_admin :
                print(f"{num}: {func_dic[num][0]}")  # 打印功能编号和名称
            else :
                if num not in ['11']:
                     print(f"{num}: {func_dic[num][0]}")
        choice = input("请输入功能编号: ").strip()

        #
        if choice not in func_dic or (not logged_admin and choice in ['11']):
            print( "无效的功能编号，请重新输入!" )
            continue

        func_dic[choice][1]()  # 调用对应的函数
