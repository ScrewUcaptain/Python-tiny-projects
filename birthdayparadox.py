import random

# boucle principale


def main():
    print("The Birthday Paradox...")
    while True:
        print('''
          How many birthday should I generate ? ('quit' for exit) ''')
        num = input('>>')
        if num == 'quit':
            print("Goodbye")
            break
        elif not num.isdecimal():
            continue

        birthdays = generateBirthday(num)
        print('Here are {} birthdays' .format(num))  # remplace fstring
        print(birthdays)

        match = getMatch(birthdays)
        if match != None:
            print(match, " est une date d'anniversaire présente plusieurs fois")
        else:
            print("Tous les anniversaires sont uniques !")


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for i, date in enumerate(birthdays):
        for j, date2 in enumerate(birthdays[i+1:]):
            if date == date2:
                return date


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
