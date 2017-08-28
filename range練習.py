import numpy as np

startRange = range(0, 20)
print [i for i in startRange]

startRangeBy2 = range(0, 20, 2)
print [i for i in startRangeBy2]

startRangeBy3 = range(0, 20, 3)
print [i * 0.8 for i in startRangeBy3]

# 裝了numpy後才可以有累加0.5的index
startRange4 = np.arange(0, 10, 0.5)
print [i for i in startRange4]