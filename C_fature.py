cmimi = float(input("Cmimi (Lek): "))
sasia = int(input("Sasia (copë): "))

if sasia < 0:
    print("Sasia e pavlefshme")
else:
    karta = input("Ke kartë studenti? (po/jo): ").lower().strip()
    nentotal = cmimi * sasia
    zbritje = 0
    if karta in ["po", "yes", "y"]:
        zbritje = nentotal * 0.10
    tvsh = (nentotal - zbritje) * 0.15
    total = round(nentotal - zbritje + tvsh, 2)

    print("------------------------------")
    print("Nën-total:", round(nentotal, 2), "Lek")
    print("Zbritja: 10% (Vlera:", round(zbritje, 2), "Lek)")
    print("TVSH (15%):", round(tvsh, 2), "Lek")
    print("Totali për pagesë:", format(total, '.2f'), "Lek")
    if total >= 1000:
        print("Kupon fiskal: PO")
    else:
        print("Kupon fiskal: JO")
