# Projekt programy rozpoznającego, w jakim okresie literackim został napisany dany tekst

# Tworzenie macierzy Tf-Idf:
1. Przygotuj słownik, w którym kluczem jest nazwa klasy (gatunku literackiego) a wartością lista słów pojawiających się w tekstach danej klasy (z powtórzeniami)
2. Stwórz macierz Tf-Idf przez wołanie konstruktora z przekazanym słownikiem

# Tworzenie klasyfikatora Bayesa:
1. Wywołaj konstruktor klasyfikatora z przkazaną macierzą Tf-Idf
2. Na stworzonym obiekcie klasyfikatora należy wywołać metodę fit() aby wyszkolić klasyfikator

# Predykcja klasy tekstu:
1. Należy przygotować listę tekstów w postaci listy słów pojawiających się w danym tekście (przykład: [["Litwa", "Ojczyzna", "mój"],["sklep", "galanteria", "Wokulski"]])
2. Kolejnym krokiem jest przeprowadzenie transformacji tekstów na wektory Tf-Idf funkcją transformText()
3. Wektor Tf-Idf należy przekazać do funkcji predictClass, która zwróci nazwę najbardziej prawdodpobniej klasy dla danego wektora. 