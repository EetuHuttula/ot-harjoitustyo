# Käyttöohje - ShoppingListApp

## Sovelluksen käynnistäminen

Sovelluksen käynnistäminen palautusrepositoriosta:

```bash
poetry run invoke start
```

Sovellus avautuu omassa ikkunassaan ja näyttää ensin kirjautumisnäkymän.

## Kirjautuminen ja rekisteröityminen

### Uuden käyttäjän luominen

1. Klikkaa kirjautumisnäkymässä **"Register"**-painiketta
2. Anna haluamasi käyttäjänimi (vähintään 3 merkkiä)
3. Anna haluamasi salasana (vähintään 8 merkkiä ja vähintään 1 erikoismerkki, esim. @, #, !, $)
4. Klikkaa **"Register"**-painiketta
5. Jos rekisteröinti onnistui, sinut ohjataan takaisin kirjautumisnäkymään

**Vaatimukset rekisteröinnille:**
- Käyttäjänimi: vähintään 3 merkkiä, uniikki
- Salasana: vähintään 8 merkkiä, sisältää vähintään 1 erikoismerkin

### Kirjautuminen

1. Kirjoita käyttäjänimesi kirjautumisnäkymän ensimmäiseen kenttään
2. Kirjoita salasanasi toiseen kenttään
3. Klikkaa **"Login"**-painiketta
4. Jos kirjautuminen onnistuu, sinut viedään ostoslista-näkymään

Jos kirjautumistiedot ovat väärin, näet virheilmoituksen.

## Ostoslistan hallinta

Onnistuneen kirjautumisen jälkeen näet ostoslista-näkymän.

### Tuotteen lisääminen

1. Kirjoita tuotteen nimi **"Item Name"**-kenttään (esim. "Maito")
2. Kirjoita tuotteen määrä **"Amount"**-kenttään (esim. "2")
3. Klikkaa **"Add Item"**-painiketta

Tuote lisätään ostoslistallesi. Jos sama tuote on jo listalla, määrät lasketaan yhteen automaattisesti.

**Huomio:** Sekä nimi että määrä ovat pakollisia kenttiä.

### Tuotteen poistaminen

1. Valitse tuote ostoslistasta klikkaamalla sitä
2. Klikkaa **"Remove Item"**-painiketta
3. Tuote poistetaan listasta

### Listan tyhjentäminen

Klikkaa **"Clear List"**-painiketta tyhjentääksesi koko ostoslistan kerralla.

## Vinkkejä

- **Tuotteiden määrät:** Määrää voi antaa kokonaislukuna (1, 2, 3...) tai desimaalilukuna (0.5, 1.5...)
- **Samankaltaiset tuotteet:** Jos lisäät tuotteen, jonka nimi on täsmälleen sama kuin jo olemassa oleva tuote, määrät lasketaan yhteen

