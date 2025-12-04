# ShoppingList - Ostoslista-sovellus
Yksinkertainen ja käyttäjäystävällinen ostoslista-sovellus, jolla voit hallita omaa ostoslistaasi ja jakaa sen helposti muille.

## Ominaisuudet

-  **Käyttäjätilit** - Luo oma käyttäjätili ja hallinnoi omaa ostoslistaasi
-  **Ostoslistan hallinta** - Lisää ja poista tuotteita listaltasi
-  **Jakaminen** - Kopioi ostolista leikepöydälle ja jaa se esimerkiksi WhatsAppissa

## Asennus

### Vaatimukset
- Python 3.14+
- Poetry

### Asennusvaiheet

1. Kloonaa repositorio
```bash
git clone https://github.com/EetuHuttula/ot-harjoitustyo.git
cd ot-harjoitustyo/shoppingList
```

2. Asenna riippuvuudet
```bash
poetry install
```

3. Käynnistä sovellus
```bash
poetry run invoke start
```

## Käyttö

### Käynnistäminen

```bash
poetry run invoke start
```

### Testien suorittaminen

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage
```

### Testikattavuusraportti

```bash
poetry run invoke coverage-report
```
### Pylint

```bash
poetry run invoke lint
```


Komento kerää testikattavuustiedot ja avaa HTML-raportin selaimessa.

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimuusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Release](https://github.com/EetuHuttula/ot-harjoitustyo/releases/tag/Viikko5)
## Tekijä

Eetu Huttula
