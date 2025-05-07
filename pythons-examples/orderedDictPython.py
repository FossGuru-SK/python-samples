from collections import OrderedDict

user = OrderedDict(name='sujit', id='100', email='sujit@gmail.com')

for key in user:
    print(key + ":" + user[key])

for key, value in user.items():
    print(key + ':' + value)

keys = ['demo1', 'demo2', 'demo3']
demo = OrderedDict.fromkeys(keys, 0)
print(demo)

import json
user = OrderedDict(name='sujit', id='100', email='sujit@gmail.com')
print(json.dumps(user))
