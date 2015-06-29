#! /usr/bin/python
# A Python script that simulates rolling two dice a few times.
#Now add your own code.

# Module for dealing with random numbers.
import random


# How many times to roll the dice.
NUM_DICE_ROLLS = 5


print 'Rolling the dice ' + str(NUM_DICE_ROLLS) + ' times'
for dice_rolls in range(NUM_DICE_ROLLS):
  roll1 = random.randint(1, 6)
  roll2 = random.randint(1, 6)
  print 'Rolled', roll1, roll2
