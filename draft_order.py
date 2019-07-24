import random

# Reigning Champ Nick Nahrwold, initials NN = 1414
"""Follow the input prompts.
    Note: to build a new executable, install Pyinstaller
    Then in the console, type Pyinstaller --onefile draft_order.py"""

year = input('What year is the coming season? (Four Digit Year) ')
if int(year) < 1920 or int(year) > 3000:
    print('YOU HAVE BEEN HAXXED! WE ARE ANONYMOUS!')
    print('')
    print('jk you just really suck at simple instructions. run it again but this time dont suck at at.')
    input('Press enter to close and try again!')
    exit()

first_initial = input('What is first initial of recent champ? (Upper Case!) ')
if len(first_initial) != 1:
    print("Whelp. You're really, really dumb. I literally needed one capital letter. "
          "Run it again... but this time just give me a single capital letter.")
    input('Press enter to close and try again!')
    exit()
first_initial = ord(first_initial)
if first_initial < 65 or first_initial > 90:
    print("Whelp. You're really, really dumb. I literally needed one capital letter. "
          "Run it again... but this time just give me a single capital letter.")
    input('Press enter to close and try again!')
    exit()

second_initial = input('What is second initial of recent champ? (Again... Upper Case!) ')
if len(second_initial) != 1:
    print("Ok... somehow you are able to give me a single capital letter the first time, but then the second time "
          "you have no fucking clue what you're doing. Expended all that mental energy on the first one I guess. "
          "Run the app again. I believe in you.")
    input('Press enter to close and try again!')
    exit()
second_initial = ord(second_initial)
if second_initial < 65 or second_initial > 90:
    print("Ok... somehow you are able to give me a single capital letter the first time, but then the second time "
          "you have no fucking clue what you're doing. Expended all that mental energy on the first one I guess. "
          "Run the app again. I believe in you.")
    input('Press enter to close and try again!')
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

input('Please rate us on the Google Play Store!\nFeel free to write any comments or suggestions below.\n')
