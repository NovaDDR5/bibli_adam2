# <Bibliotheque d'encodage 64bit / HTML>

## Description

J'ai essayé de créer une bibliotheque utilisable avec pip. Chaque module a quatre fonctions chacune avec documentation.

## Installation

Telecharge le fichier "bibli_adam_64bit_html-0.0.1.tar.gz" dans le dossier "dist" et extrait le avec winrar (https://www.win-rar.com/) ou 7-zip (https://7-zip.org/). Les modules d'encodage 64bit et HTML sont à l'interieur du dossier "my_package" dans deux fichiers differents avec une documentation chacun dans leurs dossier respectifs (module1 --> 64bit / module2 --> HTML).

## Usage

Dans le terminal lance la ligne :  
pip install -i https://test.pypi.org/simple/ bibli-adam-64bit-html==0.0.4  

Ensuite rajoute en début de fichier :  
import my_package  
from my_package.module1 import encodage_64  
from my_package.module2 import encodage_html  

Et voilà tu peux utiliser les fonctions avec :  
encodage_64.<nomdelafonction>(<parametre>)
---
