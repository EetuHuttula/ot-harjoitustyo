```mermaid
---
config:
  look: neo
---
sequenceDiagram
    participant main
    participant laitehallinto as HKLLaitehallinto
    participant rautatietori as Lataajalaite
    participant ratikka6 as Lukijalaite
    participant bussi244 as Lukijalaite
    participant lippu_luukku as Kioski
    participant kallen_kortti as Matkakortti
    main->>laitehallinto: create()
    main->>rautatietori: create()
    main->>ratikka6: create()
    main->>bussi244: create()
    main->>laitehallinto: lisaa_lataaja(rautatietori)
    main->>laitehallinto: lisaa_lukija(ratikka6)
    main->>laitehallinto: lisaa_lukija(bussi244)
    main->>lippu_luukku: create()
    main->>lippu_luukku: osta_matkakortti("Kalle")
    lippu_luukku->>kallen_kortti: create("Kalle")
    lippu_luukku-->>main: kallen_kortti
    main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
    rautatietori->>kallen_kortti: kasvata_arvoa(3)
    main->>ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka6->>kallen_kortti: vahenna_arvoa(1.5)
    ratikka6-->>main: True
    main->>bussi244: osta_lippu(kallen_kortti, 2)
    bussi244->>kallen_kortti: vahenna_arvoa(3.5)
    bussi244-->>main: False
```