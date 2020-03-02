"""
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
@modifier: Won Seok Park
@date: March 1st, 2020
@instructor: Prof. VanderLinden (cs344)
""" 


from aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
P[T, T] = 0.25
P[F, T] = 0.25
P[T, F] = 0.25
P[F, F] = 0.25

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Coin1', {'Coin2': T}, P)
print(PC.show_approx())

"""
Exercise 4.1

b.
    i.
        P(Cavity | Catch) = P(Cavity ^ Catch) / P(Catch)
        P(Cavity | Catch) = (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144) = 0.529
    ii. 
        enumerate_joint_ask('Cavity', {'Catch': T}, P)
        False: 0.471, True: 0.529
"""