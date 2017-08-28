# encoding=utf-8
sales = {'iphone6':500, 'iphone6+': 400, 'iphone6s':300, 'iphone6s+':200}
print sales['iphone6'], sales['iphone6+']
# print sales['Sony'] 不行喔
# 但是用get取用沒有的資料會直接告訴你None
print sales.get('iphone6s'), sales.get('iphone7s')

print [key + '/' + str(sales[key]) for key in sales.keys()]
print [value for value in sales.values()]
print [item for item in sales.items()]
# key + value 用 item來表示。item其實是一組一組key+ value
print [item[0] + '/' + str(item[1]) for item in sales.items()]

sales['iPad'] = 50
print [key + '/' + str(value) for key, value in sales.items()]
sales.update({'iphone6':150, 'iphone6s':150})
print [item for item in sales.items()]
print sales