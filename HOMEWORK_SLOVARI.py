#1
 
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict.keys()) + max(my_dict.keys()))

#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

#заканчивается на 8
result = [user['name'] for user in users if user['phone'].endswith('8')]


print(*sorted(result))

#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]


result = [user['name'] for user in users if not user.get('email')]


print(*sorted(result))


#4
digits = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

num = input()

result = [digits[d] for d in num]

print(*result)

#5
course = input()

data = {
    'CS101': {'room': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
    'CS102': {'room': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
    'CS103': {'room': '6755', 'teacher': 'Рич', 'time': '10:00'},
    'NT110': {'room': '1244', 'teacher': 'Берк', 'time': '11:00'},
    'CM241': {'room': '1411', 'teacher': 'Ли', 'time': '13:00'}
}

info = data[course]

print(f"{course}: {info['room']}, {info['teacher']}, {info['time']}")


#6
keypad_map = {
    ',': '11', '.': '1', '?': '111', ':': '1111', '!': '11111', 
    'A': '2', 'B': '22', 'C': '222', 'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444', 'J': '5', 'K': '55', 'L': '555', 
    'M': '6', 'N': '66', 'O': '666', 'P': '7', 'Q': '77', 'R': '777', 
    'S': '7777', 'T': '8', 'U': '88', 'V': '888', 'W': '9', 'X': '99', 
    'Y': '999', 'Z': '9999', ' ': '0',
    'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 
    'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 
    's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 
    'y': '999', 'z': '9999'
}

message = input()


result = ""

for char in message:
    if char in keypad_map:
        result += keypad_map[char]

print(result)

#7
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
    ' ': ' ' }

message = input().upper()

encoded_message = []

for char in message:
    if char in MORSE_CODE:
        encoded_message.append(MORSE_CODE[char])

print(' '.join(encoded_message))

#8
result = {i: i*i for i in range(11, 16)}


#9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

all_keys = set(dict1.keys()) | set(dict2.keys())

for key in all_keys:
    value1 = dict1.get(key, 0)
    value2 = dict2.get(key, 0)
    
    result[key] = value1 + value2


#10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

result = {char: text.count(char) for char in text}

#11
#12
#13
#14 не смог найти решение 😭


