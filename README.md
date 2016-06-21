## Fetch Formula1 data using Ergast Developer API.

**This Python script provides data for the Formula One series, from the beginning of the world championships in 1950.**

**Usage:**
```
$ get_F1_data.py [-h] [-race] [-q] [-d] [-c] [-y YEAR] [-r ROUND] [-v]

Python script to fetch Formula 1 data.

optional arguments:
  -h, --help            show this help message and exit
  -race, --race         Race Results
  -q, --qualifying      Qualifying Results
  -d, --driver_standings
                        Driver Standings
  -c, --constructor_standings
                        Constructor Standings
  -y YEAR, --year YEAR  Year
  -r ROUND, --round ROUND
                        Round
  -v, --version         show program's version number and exit

Examples:

$ get_F1_data.py -d

1  Nico      Rosberg    141
2  Lewis     Hamilton   117
3  Sebastian Vettel     96
4  Kimi      Räikkönen  81
5  Daniel    Ricciardo  78
6  Max       Verstappen 54
7  Valtteri  Bottas     52
8  Sergio    Pérez      39
9  Felipe    Massa      38
10 Daniil    Kvyat      22
11 Romain    Grosjean   22
12 Nico      Hülkenberg 20
13 Fernando  Alonso     18
14 Carlos    Sainz      18
15 Kevin     Magnussen  6
16 Jenson    Button     5
17 Stoffel   Vandoorne  1
18 Esteban   Gutiérrez  0
19 Jolyon    Palmer     0
20 Marcus    Ericsson   0
21 Felipe    Nasr       0
22 Pascal    Wehrlein   0
23 Rio       Haryanto   0

$ get_F1_data.py -c

1  Mercedes       258
2  Ferrari        177
3  Red Bull       140
4  Williams       90
5  Force India    59
6  Toro Rosso     32
7  McLaren        24
8  Haas F1 Team   22
9  Renault        6
10 Sauber         0
11 Manor Marussia 0

$ get_F1_data.py -y 2016 -r 8 -q

European Grand Prix - 2016-06-19
---------------------------------
1  Nico      Rosberg       1:43.685  1:42.520  1:42.758
2  Sergio    Pérez         1:44.462  1:43.939  1:43.515
3  Daniel    Ricciardo     1:44.570  1:44.141  1:43.966
4  Sebastian Vettel        1:45.062  1:44.461  1:43.966
5  Kimi      Räikkönen     1:44.936  1:44.533  1:44.269
6  Felipe    Massa         1:45.494  1:44.696  1:44.483
7  Daniil    Kvyat         1:44.694  1:44.687  1:44.717
8  Valtteri  Bottas        1:44.706  1:44.477  1:45.246
9  Max       Verstappen    1:44.939  1:44.387  1:45.570
10 Lewis     Hamilton      1:44.259  1:43.526  2:01.954
11 Romain    Grosjean      1:45.507  1:44.755
12 Nico      Hülkenberg    1:44.860  1:44.824
13 Carlos    Sainz         1:44.827  1:45.000
14 Fernando  Alonso        1:45.525  1:45.270
15 Esteban   Gutiérrez     1:45.300  1:45.349
16 Felipe    Nasr          1:45.549  1:46.048
17 Rio       Haryanto      1:45.665
18 Pascal    Wehrlein      1:45.750
19 Jenson    Button        1:45.804
20 Marcus    Ericsson      1:46.231
21 Kevin     Magnussen     1:46.348
22 Jolyon    Palmer        1:46.394

$ get_F1_data.py -y 1993 -r 5 -race

Spanish Grand Prix - 1993-05-09
---------------------------------
1  Alain     Prost         10
2  Ayrton    Senna         6
3  Michael   Schumacher    4
4  Riccardo  Patrese       3
5  Michael   Andretti      2
6  Gerhard   Berger        1
7  Mark      Blundell      0
8  Christian Fittipaldi    0
9  Érik      Comas         0
10 Aguri     Suzuki        0
11 Thierry   Boutsen       0
12 Rubens    Barrichello   0
13 Derek     Warwick       0
14 AlessandroZanardi       0
15 Jyrki     Järvilehto    0
16 Luca      Badoer        0
17 Karl      Wendlinger    0
18 Andrea    de Cesaris    0
19 Damon     Hill          0
20 Jean      Alesi         0
21 Fabrizio  Barbazza      0
22 Philippe  Alliot        0
23 Martin    Brundle       0
24 Ukyo      Katayama      0
25 Johnny    Herbert       0
26 Michele   Alboreto      0
```
