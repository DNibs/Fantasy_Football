import random

# Reigning Champ Nick Nahrwold, initials NN = 1414
""" Use current year and the numerical initials of last season’s winner – 
in this case, Nick Narwhold: NN -> 1414 – as the seed, making the seed 20181414"""

SEED = 20191319

teams = ['David', 'Daniel', 'Mitch', 'Zech', 'Mike M', 'Mike A', 'Mark', 'Chris', 'Alex', 'Nick', 'Matt', 'Ryan']

random.seed(SEED)
random.shuffle(teams)
print(teams)
