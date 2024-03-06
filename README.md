# Aandrijftechniek
Casus uitwerking aandrijftechniek in latex

## vraagstelling
### Hoofdvraag
voldoet de gekozen motor aan de gestelde eisen?
### Deelvragen
- Hoeveel kracht moet de motor kunnen leveren?
    - Welke krachten spelen er op de motor
    - Hoeveel rolweerstand is er
    - Hoeveel kracht is er nodig om met 0.7m/s/s de traagheid te overwinnen
- Kan de motor de berekende vereiste kracht leveren, en met hoeveel marge?
- Hoe efficient is de motor in verschillende situaties?

## Feiten:
### Rover
- 40 x 25 [cm]
- 6 [kg]
- 15 [cm] Wiel diameter
- 2.1 X 10 -3 [kgm^2] Massa traagheid wiel
- 0.9 wrijvings coëfficiënt
- 0.1 rolweerstandcoëfficiënt

### Eisen
- 0.7 [m/s^2] versnellen
- 0.5 [m/s^2] remmen
- 2.1 [m/s] top snelheid
- 30  [graden] helling (op en af)
- 

### Terrein

## Berekeningen
- Fz = 6[kg] X 1.62[m/s^2] = 9.72 [N]
- Fn = Fz / 4 = 2.43[N]  
- Fr = 0.1 X Fn = 0.243[N]
- 

#### Versnelling
De kracht die nodig is om de massa van de buggy te versnellen wordt beschreven met de onderstaande formule.
$$
    F_a = ma
$$

#### Kracht de heuvel af
De kracht die de rover de helling afduwt wordt gegeven in $F_{zh}$ en wordt beschreven met de onderstaande formule.  
$$
    F_{zh} = mg\sin(\theta)  
$$
Hier is $m$ de massa van de rover, $g$ de valversnelling en $\theta$ de hoek van het oppervlak.

#### Rolweerstand 
De kracht die het rollen van de rover tegenwerkt $F_{rw}$ wordt beschreven met de volgende formule. 
$$
    F_{rw} = \mu_r F_N 
$$
De formule voor de normaalkracht $F_N$ is
$$
    F_N = mg\cos(\theta)
$$
Dus:
$$
    F_{rw} = \mu_r m g \cos(\theta) 
$$   
Hier is $\mu_r$ de rolweerstandscoëfficiënt, $m$ de massa van de rover, $g$ de valversnelling en $\theta$ de hoek van het oppervlak.

#### Wieltraagheid
De versnelling van een wiel als gevolg van een toegepast koppel wordt beschreven in de onderstaande formule.
$$
    T = J \alpha 
$$
Hier is $J$ de massatraagheid van het wiel en $\alpha$ de hoekversnelling. Door de hoek te schrijven als functie van de verplaatsing van de buggy krijgen we deze formule:
$$
    x =  \theta r 
$$
dus de versnelling is
$$
    a = \alpha r
$$
En het koppel is
$$
    T_{J} =  \frac{aJ}{r}
$$

#### Samenvoeging

In de bovenstaande kopjes zijn $F_a,F_{zh},F_{rw}$ beshreven. Door ze allemaal als koppel te beschrijven kunnen ze samengevoegd worden met de formule voor de wieltraagheid.
$$
    T_{a,zh,rw} = (F_a + F_{zh} +  F_{rw})r
$$
want:
$$
    T = F r
$$
Nu kan de koppel voor de wieltraagheid hierbij worden opgeteld. Hierbij is het belangrijk te onthouden dat alle krachtbeschrijvingen de buggy als geheel beschrijven, en $T_J$ die van een enkel wiel beschrijft. 
$$
    T_{tot} = \frac{(F_a + F_{zh} +  F_{rw})r}{N}+T_J
$$
Waar $N$ het aantal wielen is.

Het uitschrijven van alle componenten resulteerd in de onderstaande formule.
$$
    T_{tot} = \frac{(ma + mg \sin(\theta)  +  \mu_r m g \cos(\theta) )r}{N} + \frac{aJ}{r}
$$
Dat versimpelt kan worden naar 
$$
    T_{tot} = \frac{(a + g \sin(\theta)  +  \mu_r g \cos(\theta) )r m }{N} + \frac{aJ}{r}
$$



