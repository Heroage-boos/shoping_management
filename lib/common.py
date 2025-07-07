"""
@author: yaojy  
@contact: yjy18593128603@163.com 
@project: PythonProject1
@file: common.py
@time: 2025/7/7 15:47
@desc: 公共方法
"""

# 密码加密
def pwd_to_sha256(pwd: str) -> str:
    """
    将密码转换为SHA-256哈希值
    :param pwd: 明文密码
    :return: SHA-256哈希值
    """
    import hashlib
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode('utf-8'))
    sha256.update('接着奏乐接着舞'.encode('gbk'))  # 添加盐值，增强安全性
    return sha256.hexdigest()  # 返回十六进制字符串表示的哈希值

# 登录认证装饰器
def login_auth(func):
    """
    登录认证装饰器
    :param func: 被装饰的函数
    :return: 包装后的函数
    """
    def wrapper(*args, **kwargs):
        from core import src
        if src.logged_user:
            res=func(*args, **kwargs)
            return res
        else :
            print('\n请先登录！')
            return False
    return wrapper
