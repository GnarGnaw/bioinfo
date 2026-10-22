#FIND THE FREQUENCY FOR ALL THE COMBINATIONS OF 2 AND 3 NUCLEOTIDES (LETTERS)
# AND PLOT THOSE FREQUENCIES ON A CHART

S = "ATCCCTTTTTTTTTTCGGAGGTCCGG"
freq= {}
freq3={}

for i in range(len(S)-1):
    if (S[i] + S[i+1]) in freq:
        freq[S[i] + S[i+1]] += 1
    else:
        freq[S[i] + S[i+1]] = 1
print(freq)

for i in range(len(S)-2):
    if (S[i] + S[i+1] + S[i+2]) in freq3:
        freq3[S[i] + S[i+1] + S[i+2]] += 1
    else:
        freq3[S[i] + S[i+1] + S[i+2]] = 1
print(freq3)


import matplotlib.pyplot as plt

plt.bar(*zip(*freq.items()))
plt.show()

plt.bar(*zip(*freq3.items()))
plt.show()
