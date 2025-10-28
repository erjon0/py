# word=('nig','ddd','rrr')
#
# print(word[2])
#
# person=('daris',13,'non')
#
# name,age,profession=person
#
# print(name,"'s",profession,"profession","his age",age)
from operator import concat

#dictionaries

coctackt_info={
    'alice':'088345635',
    'bob': '0878337'
}

alice_phone=contact_info["alice"]
print(alice_phone)

contact_info['daris']='09088784734'

print(contact_info)


keys=contact_info.keys()
print(keys)

values=contact_info.values()
print(values)

items=contact_info.items()
print(items)


contact_info={
    'alice':{
        'phone':'67838120',
        'email':'alice@gmail.com'
    }
}

alice_info=contact_info['alice']
print(alice_info)

contact_info={
    "alice":('67838120','alice@gmail.com')
}

alice_info=contact_info['alice']
phone=alice_info[0]
print(phone)