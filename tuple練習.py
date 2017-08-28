day_of_week = ('Saturday', 'Monday', 'Tuesday')
print type(day_of_week)
day_of_week += 'Wednesday',
print day_of_week
print day_of_week[0], day_of_week[1], day_of_week[2]
print [day for day in day_of_week]
def split_head(seq):
    return seq[0], seq[1:]
countries = ['Taiwan', 'Japan', 'Korea', 'Singapore', 'India']
first, second = split_head(countries)
print first
print second