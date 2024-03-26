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

## Berekening vereiste kracht 
- Fz = 6[kg] X 1.62[m/s^2] = 9.72 [N]
- Fn = Fz / 4 = 2.43[N]  
- Fr = 0.1 X Fn = 0.243[N]
- 

### Versnelling
De kracht die nodig is om de massa van de buggy te versnellen wordt beschreven met de onderstaande formule.
$$
    F_a = ma
$$

### Kracht de heuvel af
De kracht die de rover de helling afduwt wordt gegeven in $F_{zh}$ en wordt beschreven met de onderstaande formule.  
$$
    F_{zh} = mg\sin(\theta)  
$$
Hier is $m$ de massa van de rover, $g$ de valversnelling en $\theta$ de hoek van het oppervlak.

### Rolweerstand 
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

### Wieltraagheid
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

### Samenvoeging

In de bovenstaande kopjes zijn $F_a,F_{zh},F_{rw}$ beshreven. Door ze allemaal als koppel te beschrijven kunnen ze samengevoegd worden met de formule voor de wieltraagheid.
$$
    T_{a,zh,rw} = (F_a + F_{zh} +  F_{rw})r
$$
want de formule voor koppel is:
$$
    T = F r
$$
Nu kan de koppel voor de wieltraagheid hierbij worden opgeteld. Hierbij is het belangrijk te onthouden dat alle krachtbeschrijvingen de buggy als geheel beschrijven, en $T_J$ die van een enkel wiel beschrijft. 
$$
    T_{tot} = \frac{(F_a + F_{zh} +  F_{rw})r}{N}+T_J
$$
Waar $N$ het aantal wielen is.

### Invulling
Nu zullen de componenten van de fomule worden ingevuld en berekend.
We weten de waarde van de volgende elementen:
$$
\begin{split}   
    m &= 6 \space kg\\
    a &= 0.7 \space ms^{-2}\\
    J &= 2.1 \cdot 10^{-3} \space  kg \cdot m^2\\
    \mu_r &= 0.1\\
    r &= 0.075 \space m\\
    N &= 4\\
    v_{max} &= 2.1 ms^{-1}\\
    g_{maan} &= 1.62 \space ms^{-2}
\end{split}
$$
Voor de hoek van het oppervlak moeten verschillende waarden worden ingevuld voor drie situaties: vlak, berg op, berg af.
$$
    \begin{split}
        \theta_{vlak} &= 0\degree\\
        \theta_{op} &= 20\degree\\
        \theta_{af} &= -20\degree
    \end{split}
$$
Hieruit kunnen we per situatie de krachten berekenen

#### Berekening vlak
De krachten voor de situatie $\theta_{vlak} = 0\degree$ komen uit op de volgende waarden:
$$
    \begin{split}
        F_a = ma &= 6 \cdot 0.7 = 4.2  \space N\\
        F_{zh} = mg\sin(\theta) &= 6 \cdot 1.62 \cdot \sin(0) = 0 \space N\\
        F_{rw} = \mu_r m g \cos(\theta) &= 0.1 \cdot 6 \cdot 1.62 \cdot \cos(0) = 0.972 \space N
    \end{split}
$$

Hiermee kan vervolgens het totale koppel berekend worden.
$$
\begin{split}
    T_{a,zh,rw} = (F_a + F_{zh} +  F_{rw})r &= (4.2 + 0+0.972)\cdot 0.075 = 388  \space mNm\\
    T_{J} =  \frac{aJ}{r} &= \frac{0.7 \cdot 2.1 \cdot 10^{-3}}{0.075} = 19.6 \space mNm\\
    T_{tot} =  \frac{T_{a,zh,rw}}{4} + T_{J} &= \frac{388}{4} + 19.6 = 117 \space mNm
\end{split}
$$
Ter conclusie: op een vlak oppervlak wordt er maximaal  $117 \space mNm$ vereist van elke motor, ongeacht van het toerental.

#### Berekening berg op
De krachten voor de situatie $\theta_{op} = 20\degree$ komen uit op de volgende waarden:
$$
    \begin{split}
        F_a = ma &= 6 \cdot 0.7 = 4.2  \space N\\
        F_{zh} = mg\sin(\theta) &= 6 \cdot 1.62 \cdot \sin(20) = 3.33 \space N\\
        F_{rw} = \mu_r m g \cos(\theta) &= 0.1 \cdot 6 \cdot 1.62 \cdot \cos(20) = 0.913 \space N
    \end{split}
$$

Hiermee kan vervolgens het totale koppel berekend worden.
$$
\begin{split}
    T_{a,zh,rw} = (F_a + F_{zh} +  F_{rw})r &= (4.2 + 3.33 + 0.913)\cdot 0.075 = 633\space mNm\\
    T_{J} =  \frac{aJ}{r} &= \frac{0.7 \cdot 2.1 \cdot 10^{-3}}{0.075} = 19.6 \space mNm\\
    T_{tot} =  \frac{T_{a,zh,rw}}{4} + T_{J} &= \frac{633}{4} + 19.6 = 178 \space mNm
\end{split}
$$
Ter conclusie: op een steigende helling van $20 \degree$ wordt er maximaal  $178 \space mNm$ vereist van elke motor, ongeacht het toerental.

#### Berekening berg af
De krachten voor de situatie $\theta_{af} = -20\degree$ komen uit op de volgende waarden:
$$
    \begin{split}
        F_a = ma &= 6 \cdot 0.7 = 4.2  \space N\\
        F_{zh} = mg\sin(\theta) &= 6 \cdot 1.62 \cdot \sin(-20) = -3.33 \space N\\
        F_{rw} = \mu_r m g \cos(\theta) &= 0.1 \cdot 6 \cdot 1.62 \cdot \cos(-20) = 0.913 \space N
    \end{split}
$$

Hiermee kan vervolgens het totale koppel berekend worden.
$$
\begin{split}
    T_{a,zh,rw} = (F_a + F_{zh} +  F_{rw})r &= (4.2 - 3.33 + 0.913)\cdot 0.075 = 134\space mNm\\
    T_{J} =  \frac{aJ}{r} &= \frac{0.7 \cdot 2.1 \cdot 10^{-3}}{0.075} = 19.6 \space mNm\\
    T_{tot} =  \frac{T_{a,zh,rw}}{4} + T_{J} &= \frac{134}{4} + 19.6 = 53 \space mNm
\end{split}
$$
Ter conclusie: op een dalende helling van $-20 \degree$ wordt er maximaal  $53 \space mNm$ vereist van elke motor, ongeacht het toerental.