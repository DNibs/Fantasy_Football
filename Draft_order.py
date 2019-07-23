import random

# Reigning Champ Nick Nahrwold, initials NN = 1414
"""Follow the input prompts. Note - this does not test for bad inputs!"""

year = input('What year is the coming season? (Four Digit Year) ')
if int(year) < 1920 or int(year) > 3000:
    print('Bad year input - run app again.')
    exit()

first_initial = input('What is first initial of recent champ? (Upper Case!) ')
first_initial = ord(first_initial)
if first_initial < 65 or first_initial > 90:
    print('Bad first initial input - run app again.')
    exit()

second_initial = input('What is second initial of recent champ? (Again... Upper Case!) ')
second_initial = ord(second_initial)
if second_initial < 65 or second_initial > 90:
    print('Bad second initial input - run app again.')
    exit()

first_initial = chr(first_initial)
second_initial = chr(second_initial)
SEED = year + first_initial + second_initial
x = ''.join(str(ord(c)) for c in SEED)
print('The Draft Order for the {} season is...'.format(year))

teams = ['David', 'Daniel', 'Mitch', 'Zech', 'Mike M', 'Mike A', 'Mark', 'Chris', 'Alex', 'Nick', 'Matt', 'Ryan']

random.seed(x)
random.shuffle(teams)
for i in range(len(teams)):
    print('{}. {}'.format(i+1, teams[i]))

input('Press enter')
