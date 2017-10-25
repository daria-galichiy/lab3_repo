from get_id_from_username import GetIDFromUsername
from get_list_of_friends import GetFriends
import matplotlib.pyplot as plt

username = input('Username: ')
user = GetIDFromUsername(username)
uid = user.execute()

user_friends = GetFriends(uid)
statistics, undef_age = user_friends.execute()

X = []
Y = []
for k in sorted(statistics.keys()):
    print(k,statistics[k])
    X.append(k)
    Y.append(len(statistics[k]))
print ('- ', end='')
for el in undef_age:
    print(el, end='')

fig, ax = plt.subplots()
plt.bar(X, Y, align='center')
ax.set_xlabel('Age')
ax.set_ylabel('Amount of friends')
ax.set_title(r'Histogram of a spreading of ages')
plt.show()
