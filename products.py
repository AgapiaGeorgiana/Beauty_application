produse = []


def adauga_produs(nume, categorie, pret):

    if not nume.strip():
        raise ValueError("Numele produsului nu poate fi gol")

    if not categorie.strip():
        raise ValueError("Categoria nu poate fi goala")

    if pret <= 0:
        raise ValueError("Pretul trebuie sa fie pozitiv")

    produs = {
        "nume": nume,
        "categorie": categorie,
        "pret": pret
    }

    produse.append(produs)
    return produs
