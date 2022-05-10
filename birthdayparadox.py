import random


def main():
    print(''' The Birthday Paradox,
          How many birthday should I generate ? ''')
    num = input('>>')
    birthdays = generateBirthday(num)
    print('Here are {} birthdays' .format(num))
    print(birthdays)


def getMatch()


def generateBirthday(num):
    list_birthdays = []
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
#     days = [i for i in range(0, 32)]

    for i in range(int(num)):
        rand_month = random.randint(0, 11)
        rand_month = months[rand_month]
        if rand_month == 'feb':
            rand_day = random.randint(1, 29)
        elif rand_month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
            rand_day = random.randint(1, 31)
        else:
            rand_day = random.randint(1, 30)
        rand_birth = f"{rand_day} {rand_month}"
        list_birthdays.append(rand_birth)
    return list_birthdays


main()
