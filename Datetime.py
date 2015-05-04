import datetime
import time

data = datetime.date(2015,4,27)
print(data,end='\n\n')
print(data.day)
print(data.month)
print(data.year,end='\n\n')

data += datetime.timedelta(days=2)
print(data,end='\n\n')

data2 = datetime.datetime(2015,5,10,4,25,14)
data3 = datetime.datetime(2015,5,11,5,12,29)
print(data2,end='\n\n')
print(data3,end='\n\n')

delta = data3 - data2
print('As datas estão',delta,'distantes',end='\n\n')


tempo1 = datetime.time(0,0,30)
print(tempo1)
tempo1 = tempo1.replace(0,0,29)
print(tempo1)





tempo = datetime.time.(0,1,30)
for i in range(91):
    if tempo.seconds == 0:
        tempo
    elif i >= 60:
        tempo = tempo - datetime.time(0,0,i-60)
    else:
        tempo = tempo - datetime.time(0,0,i)
    print(tempo)
    time.sleep(1)
