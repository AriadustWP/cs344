'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
emotion = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1}),
    ])

# Exercise 5.3 a. in respective order
print(enumeration_ask('Raise', dict(Sunny = T), emotion).show_approx()) # False: 0.99, True: 0.01
print(elimination_ask('Raise', dict(Sunny = T), emotion).show_approx()) # False: 0.99, True: 0.01
print(gibbs_ask('Raise', dict(Sunny = T), emotion).show_approx())       # False: 0.996, True: 0.004

print(enumeration_ask('Raise', dict(Happy = T, Sunny = T), emotion).show_approx()) # False: 0.986, True: 0.0142
print(elimination_ask('Raise', dict(Happy = T, Sunny = T), emotion).show_approx()) # False: 0.986, True: 0.0142
print(gibbs_ask('Raise', dict(Happy = T, Sunny = T), emotion).show_approx())       # False: 0.988, True: 0.012

print(enumeration_ask('Raise', dict(Happy = T), emotion).show_approx()) # False: 0.982, True: 0.0185
print(elimination_ask('Raise', dict(Happy = T), emotion).show_approx()) # False: 0.982, True: 0.0185
print(gibbs_ask('Raise', dict(Happy = T), emotion).show_approx())       # False: 0.977, True: 0.023

print(enumeration_ask('Raise', dict(Happy = T, Sunny = F), emotion).show_approx()) # False: 0.917, True: 0.0833
print(elimination_ask('Raise', dict(Happy = T, Sunny = F), emotion).show_approx()) # False: 0.917, True: 0.0833
print(gibbs_ask('Raise', dict(Happy = T, Sunny = F), emotion).show_approx())       # False: 0.9, True: 0.1

'''
**hand-written work will be on separate file
Being sunny has no influence on the "raise" as they are not causally linked. 
However, being happy can increase the chance of "raise" as those two are causally linked (if someone is happy, than one of the cause of the happiness could be the raise).

One is more likely to have received raise if it he/she is happy but don't know the weather as one of the factors that can increase the chance of happiness is unknown and probability of "Raise" needs to go up to compensate
One is even more likely to have received raise if it isn't sunny outside but he/she is happy because one of the factors that can increase the chance of happiness is gone and probability of "Raise" needs to go up further to compensate
'''









