# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

```mermaid
graph TD
    UI[ui]
    Services[services]
    Repository[repository]
    Entities[entities]
    
    UI -.-> Services
    Services -.-> Repository
    Services -.-> Entities
    Repository -.-> Entities
```

Pakkaus _ui_ sisältää käyttöliittymästä, _services_ sovelluslogiikasta ja _repository_ tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus _entities_ sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Kirjautuminen
- Uuden käyttäjän luominen
- Ostoslista

Jokainen näistä on toteutettu omana luokkanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään sovelluslogiikasta.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat [User](../src/entities/user.py) ja ShoppingList, jotka kuvaavat käyttäjiä ja ostoslistoja:

```mermaid
  classDiagram
    User "*" --> "1" ShoppingList
    class User{
        username
        password
    }
    class ShoppingList{
        id
        items
        username(User)
    }

```

Toiminnallisista kokonaisuuksista vastaa luokka [ShoppingListService](../src/services/shopping_list_service.py). Luokka tarjoaa käyttöliittymän toiminnoille metodit ostoslistan hallintaan.

Sovelluslogiikka pääsee käsiksi käyttäjiin tietojen tallennuksesta vastaavan luokan [UserRepository](../src/repository/user_repository.py) kautta.


## Tietojen pysyväistallennus

Pakkauksen _repository_ luokka `UserRepository` huolehtii käyttäjätietojen tallettamisesta.

### Tiedostot

Sovellus tallettaa käyttäjien tiedot JSON-tiedostoon.

Käyttäjät tallennetaan JSON-taulukkoon seuraavassa formaatissa:

```json
[
    {
        "username": "matti",
        "password": "salasana123"
    }
]
```




## Päätoiminnallisuudet 
 

    ämä sekvenssikaavio kuvaa prosessia, kun käyttäjä lisää tuotteen ostoslistaan. Sovellus aggregoi määrät automaattisesti, jos tuote on jo listalla.

```mermaid
sequenceDiagram
    actor User as Käyttäjä
    participant UI as ShoppingView
    participant Service as ShoppingListService
    participant Repo as shopping_repository
    participant Storage as shopping.json

    User->>UI: Syötä tuotteen nimi ja määrä,<br/>klikkaa "Add Item"
    
    UI->>UI: Validoi: nimi ei tyhjä
    UI->>Service: add_item(username, nimi, määrä)
    
    Service->>Repo: add_item(nimi, määrä, owner)
    
    Repo->>Storage: Lue kaikki tuotteet
    Storage-->>Repo: JSON-lista
    
    alt Tuote on jo omistajalla
        Repo->>Repo: Jäsennä määrät numeroiksi
        Repo->>Repo: Laske yhteen:<br/>uusi_määrä = vanha + uusi
        Repo->>Storage: Tallenna päivitetty määrä
    else Uusi tuote
        Repo->>Repo: Luo uusi tuote ID:llä
        Repo->>Storage: Tallenna uusi tuote
    end
    
    Storage-->>Repo: OK
    Repo-->>Service: Shopping-objekti
    Service-->>UI: Tuote lisätty
    
    UI->>Service: get_shopping_list(username)
    Service->>Repo: list_items_by_owner(username)
    Repo->>Storage: Lue tuotteet
    Storage-->>Repo: Käyttäjän tuotteet
    Repo-->>Service: Lista
    Service-->>UI: Päivitetty lista
    
    UI->>UI: Tyhjennä input-kentät
    UI->>UI: Päivitä Treeview näyttö
    UI-->>User: Näytä päivitetty ostolista
```