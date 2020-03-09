'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
@editor: Won Seok Park
@date: March 08 2020
'''

from aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling, likelihood_weighting

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Exercise 5.1 a.i
'''
Exercise 5.1 a.i

P(Alarm | burglary ^ ¬earthquate) = <0.94, 1-0.94> 
                                  = <0.94, 0.6>

It is one of the given value ('Alarm', 'Burglary Earthquake', {(T, F): 0.94})
'''
print(enumeration_ask('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx())      # False: 0.06, True: 0.94
print(elimination_ask('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx())      # False: 0.06, True: 0.94
print(gibbs_ask('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx())            # False: 0.049, True: 0.951
print(rejection_sampling('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx())   # False: 0.0769, True: 0.923
print(likelihood_weighting('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx()) # False: 0.063, True: 0.937


# Exercise 5.1 a.ii
'''
P(JohnCalls | burglary ^ ¬earthquake) = alarm.sum( P(John | alarm) * P(alarm | burg ^ ¬earth) * P(burg) * P(¬earth) )
                                      = P(burg) * P(¬earth) * alarm.sum( P(John | alarm) * P(alarm | burg ^ ¬earth) )
                                      = 0.001 * 0.998 [ P(John | alarm) * P(alarm | burg ^ ¬earth) + P(John | ¬alarm) * P(¬alarm | burg ^ ¬earth),
                                                        P(¬John | alarm) * P(alarm | burg ^ ¬earth) + P(¬John | ¬alarm) * P(¬alarm | burg ^ ¬earth) ]
                                      = 0.001 * 0.998 [ (0.90 * 0.94) + (0.05 * 0.06), (0.1 * 0.94) + (0.95 * 0.06) ]
                                      = [ 0.0008473, 0.0001507 ]
                                      = <0.849, 0.151>
'''
print(enumeration_ask('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx())      # False: 0.151, True: 0.849
print(elimination_ask('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx())      # False: 0.151, True: 0.849
print(gibbs_ask('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx())            # False: 0.127, True: 0.873
print(rejection_sampling('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx())   # False: 0.25, True: 0.75
print(likelihood_weighting('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx()) # False: 0.15, True: 0.85


# Exercise 5.1 a.iii
'''
** I will put handwork in separate file from here on as working on vscode seems too messy to read + takes longer to write
P(Burglary | alarm)
'''
print(enumeration_ask('Burglary', dict(Alarm = T), burglary).show_approx())      # False: 0.626, True: 0.374 
print(elimination_ask('Burglary', dict(Alarm = T), burglary).show_approx())      # False: 0.634, True: 0.366
print(gibbs_ask('Burglary', dict(Alarm = T), burglary).show_approx())            # False: 0.65, True: 0.35
print(rejection_sampling('Burglary', dict(Alarm = T), burglary).show_approx())   # False: 0.626, True: 0.374
print(likelihood_weighting('Burglary', dict(Alarm = T), burglary).show_approx()) # False: 0.613, True: 0.387



# Exercise 5.1 a.iv
'''
P(Alarm | JohnCalls ^ ¬MaryCalls)
'''
print(enumeration_ask('Alarm', dict(JohnCalls = T, MaryCalls = F), burglary).show_approx())      # False: 0.986, True: 0.0136
print(elimination_ask('Alarm', dict(JohnCalls = T, MaryCalls = F), burglary).show_approx())      # False: 0.986, True: 0.0136
print(gibbs_ask('Alarm', dict(JohnCalls = T, MaryCalls = F), burglary).show_approx())            # False: 0.992, True: 0.008
print(rejection_sampling('Alarm', dict(JohnCalls = T, MaryCalls = F), burglary).show_approx())   # False: 0.994, True: 0.00616
print(likelihood_weighting('Alarm', dict(JohnCalls = T, MaryCalls = F), burglary).show_approx()) # False: 0.989, True: 0.0108

# Exercise 5.4
'''
Gibbs sampling, rejection sampling, and likelihood weighting are all algorithms based on stochastic simulation. They often require less computational time, but less accurate compared to exact inference algorithms (including a hand calculation), hence they show different results.
'''





















