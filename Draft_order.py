import random

# Reigning Champ Nick Nahrwold, initials NN = 1414
SEED = 20181414

teams = ['David', 'Daniel', 'Mitch', 'Zech', 'Mike M', 'Mike A', 'Mark', 'Chris', 'Alex', 'Nick', 'Matt', 'Ryan']

random.seed(SEED)
random.shuffle(teams)
print(teams)
