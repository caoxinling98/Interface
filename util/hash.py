from hashlib import sha1
from hashlib import md5
from Crypto.Cipher import AES,DES
from Crypto.Hash import SHA256
import binascii
def my_md5(msg):
    """
    md5算法加密
    :param msg:待加密的 字符串
    :return: 加密后的字符串
    """
    md = md5()
    md.update(msg.encode('utf-8'))
    return md.hexdigest()

def my_sha1(msg):
    """
    sha1加密算法
    :param msg:
    :return:
    """
    sh1 = sha1()
    sh1.update(msg.encode('utf-8'))
    return sh1.hexdigest()

def my_sha256(msg):
    """
    sha256算法
    :param msg:
    :return:
    """
    sh256 = SHA256.new()
    sh256.update(msg.encode('utf-8'))
    return sh256.hexdigest()

def my_des(msg,key):
    """
    DES加密算法
    :param msg: 待加密的字符串，长度必须为8的倍数，不足添加“=”
    :param key: 8个字符
    :return:
    """
    des = DES.new(key,DES.MODE_ECB)
    msg1 = msg + (8 - (len(msg) % 8)) * '='
    text = des.encrypt(msg1.encode())
    return binascii.b2a_hex(text).decode()

def my_aes(msg,key,vi):
    """
    AES加密算法
    :param msg:待加密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return:
    """
    obj = AES.new(key,AES.MODE_CBC,vi)
    text = obj.encrypt(msg.encode())
    return binascii.b2a_hex(text).decode()

def my_aes_decrypt(msg,key,vi):
    """
    AES 解密算法
    :param msg:待解密的字符串
    :param key: 必须为16，24，32位
    :param vi: 必须为16位
    :return:
    """
    msg = binascii.b2a_hex(msg)
    obj = AES.new(key,AES.MODE_CBC,vi)
    return obj.decrypt(msg).decode()