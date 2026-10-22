#design a software application that is able to analyze a DNA sequence S = "invent a sequence of about 2 letters"
#ATCG
#S = "ATCCCTTTTTTTTTTCGGAGGTCCGG"
#the output of the application must show the frequency for each letter in the alphabet of the sequence

S = "ATCCCTTTTTTTTTTCGGAGGTCCGG"

A=0
T=0
C=0
G=0

for i in S:
    if i == "A": A+=1
    elif i == "T": T+=1
    elif i == "C": C+=1
    elif i == "G": G+=1

print(f"A= {A}, T={T}, C={C}, G={G}")

