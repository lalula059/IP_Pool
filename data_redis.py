import redis

class Data_Redis:
    def __init__(self) -> None:
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    def insert_ip_host(self,value):
        value_ex = value.host+':'+value.port
        self.redis.zadd('url_rank',{value_ex:50})

    def remove(self,value):
        self.redis.zrem('url_rank',value)
    
    def get_ip(self):
        return self.redis.zscan('url_rank')[1]
    
    def max(self,value):
        self.redis.zadd('url_rank',{value:100})

    def update(self,value,score):
        self.redis.zadd('url_rank',{value:score-10})
xx = Data_Redis()
value = xx.get_ip()
print(value)