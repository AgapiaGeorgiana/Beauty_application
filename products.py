# Lista in care stocam produsele cosmetice
produse = []


def adauga_produs(nume, categorie, pret):
    produs = {
        "nume": nume,
        "categorie": categorie,
        "pret": pret
    }

    produse.append(produs)
    return produs
