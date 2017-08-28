# encoding=utf-8
from datetime import datetime

now = datetime.now()

print 'repr = ' + repr(now)
print 'str = ' + str(now)
print now

# 放在container中就會變成repr
print [now]
print (now)
print {now}
print {'key': now}