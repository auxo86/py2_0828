# encoding=utf-8
# 一個星號傳位置
# 兩個星號傳key, value

def sample_variable_argument(fix1, fix2, *args):
    print 'fix1 = ', fix1
    print 'fix2 = ', fix2
    print ['var: ' + str(arg) for arg in args]

if __name__ == '__main__':
    sample_variable_argument('Hello', 567, True, 123.4, 'Hi~Welcome', 'XXXXXXXXXYZ')
    sample_variable_argument('Hello', 567, ['a','b','c'])
    sample_variable_argument('Hello', 567, ('a', 'b', 'c'))
    # 星號可以做拆開包裝的用途
    sample_variable_argument('Hello', 567, *['a', 'b', 'c'])
    sample_variable_argument('Hello', 567, *('a', 'b', 'c'))

    # set沒有順序
    sample_variable_argument('Hello', 567, {'a', 'b', 'c'})
    sample_variable_argument('Hello', 567, *{'a', 'b', 'c'})

    sample_variable_argument('Hello', 567, {'k1':'a', 'k2':'b', 'k3':'c'})
    sample_variable_argument('Hello', 567, *{'k1': 'a', 'k2': 'b', 'k3': 'c'})