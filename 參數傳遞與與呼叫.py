# encoding=utf-8
# 一個星號傳位置
# 兩個星號傳key, value
def myEmployee(username, id):
    print 'username = ' + username
    print 'id = ' + id

dict1 = {'username': 'Mark', 'id': '02270001234'}
myEmployee(**dict1)