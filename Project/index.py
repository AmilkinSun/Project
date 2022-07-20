from ast import Pass
from dataset import users, countries
import pprint
#Point 1
users_wrong_password = []
#pprint.pprint(users)
for user in users:
    try:
        if user['password'].isdigit():
            try:
                item = {'name': user['name'], 'mail': user['mail'] }
                users_wrong_password.append(item)
            except: 
                pass
    except:
        pass
#print('Пользователи с плохими паролями:\n', users_wrong_password)

#Point 2
girls_drivers = []
for user in users:
    try:
        user['friends']
    except:
        pass
    else:
        for friend in user['friends']:
            if friend['sex']=='F' and friend.get('cars')!=None:
                try:
                    x = friend['cars'][0]
                except:
                    pass
                else:
                    girls_drivers.append(friend['name'])
#print('\nЖенщины-водители:\n', girls_drivers)

#point 3
best_occupation = {}
best = 0
for user in users:
    try:
        user['friends']
    except:
        pass
    else:
        all_friends = {}
        for friend in user['friends']:
            try:
                job = friend['job']
                if best < job['salary']:
                    best = job['salary']
                    best_occupation = {'occupation':job['occupation'], 'salary':job['salary']} 
                    
            except:
                pass

print('\nЛучшая зарплата:',best_occupation)
#Point 4
max = 0
vip_user = ''
for user in users:
    try:
        sum = 0
        for fr in user['friends']:
            j = fr.get('job')
            sum += j.get('salary')
        if max < sum:
            max = sum
            vip_user = user['name']
    except:
        pass

print ('VIP', vip_user)
#Point 5
carsowners = 0
flightn = 0
for user in users:
    try:
        user['friends']
    except:
        pass
    else:
        for friend in user['friends']:
            try:
                cars = friend['cars']
                carsowners+=1
            except:
                pass
            else:
                try:
                    flightsn = friend['flights']
                    for f in flightsn:
                        flightn+=1
                except:
                    pass
avg_flights = round(flightn/carsowners,5)
print ('\nСреднее количество перелетов на владельцев машин', avg_flights)

#Point 6
users_copy = users.copy()
#print(len(users))
#for user in users:
#    friends = user.get('friends')
#    found = True
#    i=0
#    while friends!= None and i<len(friends) and found:
#        flights = friends[i].get('flights')
#        j=0
#        i+=1
#        while flights!=None and found and j<len(flights):
#            fl = flights[j]
#            if fl.get('country') in countries:
#                found = False
#                j+=1
#    if found == False:
#        users.remove(user)

#print(len(users))

i = 0
while i < len(users):
    need_remove = False
    friends = users[i].get('friends', [])
    j=0
    while need_remove == False and j<len(friends):
        friend = friends[j]
        j+=1
        flights = friend.get('flights', [])
        k=0
        while need_remove == False and k<len(flights):
            flight = flights[k]
            k+=1
            if flight['country'] in countries:
                need_remove = True
    if need_remove:
        del users[i]
    else:
        i += 1

