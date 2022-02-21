listgood = []
listmid = []
listbad = []
N = int(input("Cik ir skolenu: "))
for x in range(N):
 x = int(input("Īevadi visu prieksmetu videjo atzimi: "))
 if x > 8:
   listgood.append(x)
 if 3 < x < 9:
   listmid.append(x)
 if x < 4:
   listbad.append(x)
print("Teicamnieks ir: ")
print(len(listgood))
print("Viduveji macas: ")
print(len(listmid))
print("Neseksmigais skolens ir: ")
print(len(listbad))