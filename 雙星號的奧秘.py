# encoding=utf-8
# 一個星號傳位置
# 兩個星號傳key, value

def sample_variable_argument(fix1, fix2, **kargs):
    print 'fix part: ', fix1, fix2
    print [key + '/' +str(kargs[key]) for key in kargs]

if __name__ == '__main__':
    sample_variable_argument('Hello World', True, name='Mark', age=42, weight=72.5)
    dict1 = {'name': 'Mark', 'age': 42, 'weight': 72.5}
    sample_variable_argument('Hello World', True, **dict1)