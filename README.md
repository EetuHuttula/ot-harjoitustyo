# ShoppingList

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa ostoslistoistaan. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen ostoslistansa.

## Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.8 tai uudempi. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Dokumentaatio

- [Käyttöohje](./shoppingList/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./shoppingList/dokumentaatio/vaatimuusmaarittely.md)
- [Arkkitehtuurikuvaus](./shoppingList/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./shoppingList/dokumentaatio/testaus.md)
- [Työaikakirjanpito](./shoppingList/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./shoppingList/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston _.pylintrc_ määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimuusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Release](https://github.com/EetuHuttula/ot-harjoitustyo/releases/tag/Viikko5)