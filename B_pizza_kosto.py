diametri = int(input("Diametri (cm): "))
cmimi_baze = int(input("Çmimi bazë (Lek): "))
if diametri >= 30:
    cmimi_baze += cmimi_baze * 10 // 100
print("Çmimi final:", cmimi_baze, "Lek")
