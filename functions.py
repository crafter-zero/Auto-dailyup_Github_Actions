import requests
import os
import platform

os_name = platform.system()

def replace_char(s, len_pwd):
    """
    强行对密码所在内存地址进行编辑。用于增强对密码的隐私保护功能。
    输入值： 字符串、修改的位置
    返回值： 0
    """
    import ctypes
    OFFSET = ctypes.sizeof(ctypes.c_size_t) * 6
    a = ctypes.c_char.from_address(id(s) + OFFSET)
    pi = ctypes.pointer(a)
    for idx in range(len_pwd):
        pi[idx] = ord('*')
    return 0

def checkInternetConnection():
    try:
        requests.get("https://xxcapp.xidian.edu.cn/site/ncov/xisudailyup", timeout=5)
    except:
        return False
    return True

def getInfo():
    # 初始化配置信息
    env_dist = os.environ # 获取环境变量
    config = dict()
    for idx_key in ("stuNum", "passWord", "Location", "ServerToken"):
        if not (idx_key in config):
            config[idx_key] = 0
    # 读取学号
    config["stuNum"] = env_dist.get('USERNAME')
     # 确认学号是合法的非0数字
    assert int(config["stuNum"], base=10)
    # 读取密码
    config["passWord"] = env_dist.get('PASSWORD')
    #强制使用广研院地址(1：南校区，2：北校区，3：广研院)
    config["Location"] = "1" 
    return config
