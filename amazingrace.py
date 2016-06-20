import sys
import numpy as np

python3 = sys.version_info.major == 3 # set a boolean indicating if we are in python 2 or 3

dir = [-1,1]

l = 1 # enter some number

def get_keypress(ver3):
  '''
  Utility function so that getting a keypress
  will work in either Python 2 or 3. 
  '''
  if not ver3:
    return raw_input('Press [R] to Roll or [Q] to Quit [Default R]: ')
  else:
    return input('Press [R] to Roll or [Q] to Quit [Default R]: ')

roll = True
rolls = []
while roll:
  rolls.append(l * np.random.choice(dir))
  print(rolls[-1])
  key = get_keypress(python3)
  roll = not (key.lower() == 'q') # if user enters Q, exit. Otherwise new roll
  
print('\n ===== Statistics ======')
print('Rolls: %i'%len(rolls))
print('Sum: %i'%np.sum(rolls))
print('\nHow much wood would a woodchuck chuck ...')


