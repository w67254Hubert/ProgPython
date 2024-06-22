# import random
# opis=[[5,"'prawojazdy kat D'",24],[4,"'prawojazdy kat D1'",21],[2,"'prawojazdy kat D1+E'",21],[1,"'prawojazdy kat D+E'",24]]

# i=60
# while i>=0:
#     losopis = random.choice(opis)
#     print("(",losopis,"),")  
#     i=i-1


# uprawnienia kierowców
uprawid= list(range(1, 61))
idprac=list(range(1, 61))
doiedy=['2028-01-11', '2030-12-11', '2030-09-23', '2032-03-03', '2033-07-07', '2028-08-24', '2028-09-28', '2032-12-24', '2023-07-29', '2024-01-07']
import random
i=0
while i<=59:
    losowa_data = random.choice(doiedy)
    print("(",uprawid[i],",",idprac[i],",'",losowa_data,"'),")
    i=i+1