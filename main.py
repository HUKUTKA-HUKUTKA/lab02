print("AJIrOPUTM EPATOCFEHA\n")
MACCUB_4UCEJI = []
KOJIU4ECTBO_4UCEJI = int(input("BBEgUTE HATyPAJIbHOE 4UCJIO: "))
MACCUB_nPOCTbIX = []
for i in range(KOJIU4ECTBO_4UCEJI): MACCUB_4UCEJI.append(i + 2)
for i in range(KOJIU4ECTBO_4UCEJI - 2):
    nPOCTOE = True
    for j in range(i):
        if (MACCUB_4UCEJI[i] % MACCUB_4UCEJI[j] == 0): nPOCTOE = False
    if (nPOCTOE): MACCUB_nPOCTbIX.append(MACCUB_4UCEJI[i])
print(MACCUB_nPOCTbIX)
