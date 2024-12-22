nombre_coca  = 150
prix_unité_coca = 1.50
nombre_pepsi = 130
prix_unité_pepsi = 1.50
depansse_total = 2.500
vente_total_coca =  nombre_coca * prix_unité_coca
vente_total_pepsi = nombre_pepsi * prix_unité_pepsi
vente_total = vente_total_coca + vente_total_pepsi
bénéfice = vente_total
marge = bénéfice / depansse_total



print("Valeurs de l'année dernières")
print("\n")
print(' Quels ont été les revenus  du Pepsi du magasin ? ')
print(f"le revenu du papsi est : {vente_total_pepsi} $")
print("\n")
print(' Quels ont été les revenus du magasin en  matière de Coca-Cola ? ')
print(f"le revenu du magasin en matière de coca-cola est : {vente_total_coca} $ ")
print("\n")
print(' Quel a été le bénéfice du magasin ? ')
print(f"le bénéfice est : {bénéfice} $")
print("\n")
print(' Quelle était la marge du magasin ? (Rapoelez-vous, marge =Bénéfice / Depansse). Pas besoun de formater en pourcentage ')
print(f"le marge du magasin est: {marge} $")



