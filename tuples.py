# tuples :sequenses of element of any tYpe ,that are mmutable
fullname = ('grace','m','hopper')
#using tuples of the elements inside the tuple have meaning 
#when a function returning more than one value it is ectually returning a tuple

def convert_seconds(seconds):
    hours = seconds//3600
    minute=(seconds-hours *3600)//60
    remaining_seconds = seconds - 3600*hours - 60*minute
    return hours,minute,remaining_seconds

result = convert_seconds(1500)
print(type(result))
print(result)
hours , minutes , seconds= result
print(hours , minutes , seconds)