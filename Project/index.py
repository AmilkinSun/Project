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
        for friend in user['friends']:
            try:
                job = friend['job']
                if best < job['salary']:
                    best = job['salary']
                    best_occupation = {'occupation':job['occupation'], 'salary':job['salary']} 
                    vip_user = friend['name']
            except:
                pass
print('\nЛучшая зарплата:',best_occupation)
#Point 4
print('\nVIP:', vip_user)
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
                    cars = friend['flights']
                    flightn+=1
                except:
                    pass
avg_flights = round(flightn/carsowners,5)
print ('\nСреднее количество перелетов на владельцев машин', avg_flights)

#Point 6
list_fl = []
print(len(users))
for user in users:
    friends = user.get('friends')
    found_fr = True
    i=0
    try:
        while i<len(friends) and found_fr:
            found = True
            flights = friends[i].get('flights')
            j=0
            i+=1
            while found and j<len(flights):
                fl = flights[j]
                for cntry in countries:
                    if fl.get('country')==cntry:
                        found = False
                        found_fr = False
                        users.remove(user)
                        break
                j+=1
    except:
        pass

print(len(users))

