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
