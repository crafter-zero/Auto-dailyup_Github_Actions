from random import randint, random
from utils import UPLOAD
from utils import LOGIN
import time
import random
from functions import getInfo, replace_char

if __name__ == '__main__':
    # 随机等待1-60秒
    time.sleep(random.randint(1.60))
    # 获取 学号/位置/密码等信息
    config = getInfo()
    # 登录获得 cookie
    cookie = LOGIN.login(config)
    # 如果是第一次登录，则会有密码，需要在内存空间中擦除密码
    if config["passWord"]:
        # 采用逐字节擦写，更大限度的隐私保护
        if replace_char(config["passWord"], len(config["passWord"])):
            raise RuntimeError("内存地址访问失败。")

    #上报开始
    if UPLOAD.upload_ncov_message(cookie, config) :
        print("上报失败")
    else :
        print("上报成功")
