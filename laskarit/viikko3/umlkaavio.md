---
config:
  layout: elk
---
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Vankila
    Monopolipeli "1" -- "1" Aloitusruutu
    Vankila "1" -- "1" Ruutu
    Aloitusruutu "1" -- "1"  Ruutu
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "1" Toiminto
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1"  -- "0..*" Katu : Omistaa 
    Pelaaja -- Raha
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- SattumaJaYhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu
    SattumaJaYhteismaa "1" -- "0..*" Kortti
    Kortti "1" -- "1" Toiminto
    Katu -- Nimi
    Katu "1" -- "0..4" Talo
    Katu "1" -- "0..1" Hotelli
