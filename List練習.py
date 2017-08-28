number_list = [3,1,4,1,5,9,26,83,49,100,25]
over30 = sorted(i for i in number_list if i > 30)
print over30
under40 = sorted((i for i in number_list if i < 40), reverse=True)
print under40