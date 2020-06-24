'''
@Description: 用于 redis 操作
@Author: 妄想
@Date: 2020-06-24 19:03:28
@LastEditTime: 2020-06-24 20:28:23
@LastEditors: 妄想
'''
import redis

class RedisUtil:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.r = redis.Redis(host=ip, port=port, db=0, password='123456')
    
    def insert(self, str, type):
        if type == 1:
            self.r.lpush('start_urls', str)
        elif type == 2:
            self.r.lpush('requests', str)