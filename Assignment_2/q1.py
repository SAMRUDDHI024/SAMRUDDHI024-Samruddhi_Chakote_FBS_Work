#1. Convert the time entered in hh,min and sec into seconds

# take input
hh = int(input('enter the time in hours : '))
min = int(input('enter the time in min : '))
sec = int(input('enter the time in sec : '))

# preform opration
time =  hh * 60 *60
time = time + (min * 60)
time = time + sec

# display the result
print(f'with hour :{hh}, min:{min} and sec:{sec} the total time in second is : {time} .')