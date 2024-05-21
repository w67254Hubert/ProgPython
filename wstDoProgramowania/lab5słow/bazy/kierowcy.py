import random

idprac=list(range(1, 61))
stanID=2
data=['2024-05-11', '2025-12-11', '2026-09-23', '2027-03-03', '2028-07-07']

i=59
while i>=0:
    losowa_data = random.choice(data)

    print("(",idprac[i],",",stanID,",'",losowa_data,"'),")
    i=i-1