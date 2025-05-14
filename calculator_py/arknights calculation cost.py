'''
10 OP = 1800 Orundum (600 orundum per pull)
1 OP = 180 Orundum
€ 5 voor 6 OP

OP per pull = 3.3333333333333335

max pity voor limited : 120 pulls
'''
# print(10/3)

one_pull_kost  = 3.3333333333333335
# OVERSCHRIJF DEZE WAARDE OM TE BEREKENEN WAT DE KOST IS VOOR X- aantal pulls
# amount_of_pulls = 120 # spent 400 OP for 120 pulls -> gegarandeerd limited operator from banner
# (600 Originite = 1 pull, 6000 originite = 10 pulls)
AMOUNT_OF_PULLS = 10
# 
print("*"*20)
print("")
print(f"For {AMOUNT_OF_PULLS} pulls:")

spent_op_for_pulls = AMOUNT_OF_PULLS * one_pull_kost
print("Total Originite Prime spent for pulls = ",spent_op_for_pulls)

# hoeveel pakkenten van 6 op zijn gekocht moeten wezen?

aantal_gekochte_pakketen = round(spent_op_for_pulls/6)
print("Aantal originite prime(6stuks) packetten(van 5€) gekocht: ",round(spent_op_for_pulls / 6)) # aantal OP pakketen van 6 gekocht

prijs_per_pakket = 5 # in euro(€)

totale_kostprijs = prijs_per_pakket * aantal_gekochte_pakketen
print("Totale kostprijs: €", totale_kostprijs)

print(f"Totale Orundum(rode steentjes kost): {spent_op_for_pulls * 180}")
print("")
print("*"*20)