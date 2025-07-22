from core.src import shopping
from db import db_handler
from interface import bank_interface


# 查询商品的接口
def check_goods_interface(goods_name=None):
    """
    查询商品接口
    :param goods_name: 商品名称，默认为None，查询所有商品
    :return: (bool, list) 返回查询结果和商品列表
    """
    # 1.调用商品接口层，查询商品数据
    goods_data = db_handler.select_data(goods_name, is_user=True)

    if not goods_data:
        return False, '没有找到相关商品'

    return True, goods_data

#添加商品
def add_shopping_cart_interface(username,shopping_card):
    """
    添加商品到购物车接口
    :param username: 用户名
    :param shopping_card: 商品信息
    :return: (bool, str) 返回添加结果和提示信息
    """
    # 1.获取用户数据
    user_data = db_handler.select_data(username)
    shopping_card_file=user_data['shopping_cart']

    if not user_data:
        return False, '用户不存在'

    # 2.添加商品到购物车
    for name in shopping_card.keys():
        if name in shopping_card_file:
            shopping_card_file[name]['数量']+=shopping_card.get(name).get('数量')
        else:
            shopping_card_file[name] = shopping_card.get(name)

    # 3.保存修改后的用户数据
    db_handler.save(user_data)

    return True, f"商品 {shopping_card} 已添加到购物车')"


#结算商品
def close_account_interface(username, shopping_card):
   # 1、计算结算的总金额
   total=0
   for good_info in shopping_card.values():
       price=good_info.get('price')
       num=good_info.get('数量')
       total+= (price * num)

   flag, msg = bank_interface.pay_interface( username, total )  # 调用支付接口
   return flag, msg

