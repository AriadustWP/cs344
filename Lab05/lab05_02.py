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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# Exercise 5.2
# P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1 = T, Test2 = T), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1 = T, Test2 = T), cancer).show_approx())
print(gibbs_ask('Cancer', dict(Test1 = T, Test2 = T), cancer).show_approx())

# P(Cancer | a positive result on test 1, but negative result on test2)
print(enumeration_ask('Cancer', dict(Test1 = T, Test2 = F), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1 = T, Test2 = F), cancer).show_approx())
print(gibbs_ask('Cancer', dict(Test1 = T, Test2 = F), cancer).show_approx())