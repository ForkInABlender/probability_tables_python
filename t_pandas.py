# Dylan Kenneth Eliot


"""
In order to carve down the risk of what problem leads to brown-versus-blue eye color tests being played with, this now exists here for.

Analyze given a set of 135 actors total and remove the common actors amongst both subgroups ( p-2 versus p-3 ). Instead of looping forward,
 loop backwards to see at each decrement where the problem space could/likely be given a max of 135 potential actors at play given 
 any chaotic system.

"""


import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

data = []
for p in range(135, 3, -1):
    kp2 = p - 2
    kp3 = p - 3
    try:
        N = 135 - (kp2 / kp3)
        data.append((p, kp2, kp3, N))
    except:
        pass

df = pd.DataFrame(data, columns=["p      ", "K_p-2        ", "K_p-3      ", "N     "])

print(df)
