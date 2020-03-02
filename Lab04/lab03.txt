@author: Won Seok Park
@date: March 1st, 2020
@instructor: Prof VanderLinden (cs344)

Exercise 4.3
a.
NO TEST         D User      ND User
american        0.089       0.911

TEST        drug    n-drug
positive    0.99    0.02
negative    0.01    0.98

'-' represents 'not'
I am assuming 
  1. user is a drug user and -user is non drug user since there is no such thing as non-user
  2. american is -test and positive & negative as test 

    i.      P*(User) = 0.089 + 0.911 = 1.000
    ii.     P(test | user) = P(test ^ user) / P(user) = 0.99 / 1.000 = 0.99
    iii.    P(-test | user) = P(-test ^ user) / P(user) = 0.089 / 1.000 = 0.089
    iv.     P(test | -user) = P(test ^ -user) / P(user) = 0.98 / 1.000 = 0.98
    v.      P*(User | test) = P(User ^ test) / P(test) = ?

b.
    P(positive | cancer) = P(cancer | positive)*P(cancer) / P(positive) = 0.8 * 0.01 / (0.8 + 0.096) = 0.089 or 8.9%