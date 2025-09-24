piket = int(input("Pikët (0–100): "))
if piket < 0 or piket > 100:
    print("Vlerë e pavlefshme")
elif piket >= 90:
    print("Shkëlqyeshëm")
elif piket >= 75:
    print("Shumë mirë")
elif piket >= 60:
    print("Mirë")
elif piket >= 40:
    print("Mjaftueshëm")
else:
    print("Dobët")
