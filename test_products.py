import unittest
from products import adauga_produs, produse


class TestProduse(unittest.TestCase):

    def setUp(self):
        produse.clear()

    def test_adaugare_produs(self):
        produs = adauga_produs("Ruj", "Machiaj", 45)

        self.assertEqual(produs["nume"], "Ruj")
        self.assertEqual(produs["categorie"], "Machiaj")
        self.assertEqual(produs["pret"], 45)
        self.assertEqual(len(produse), 1)

    def test_nume_gol(self):
        with self.assertRaises(ValueError):
            adauga_produs("", "Machiaj", 45)

    def test_pret_negativ(self):
        with self.assertRaises(ValueError):
            adauga_produs("Ruj", "Machiaj", -10)


if __name__ == "__main__":
    unittest.main()
