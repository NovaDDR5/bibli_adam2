
# Encodage HTML
'''
HTML Entity Encoder/Decoder

Ce module fournit des fonctionnalités pour encoder et décoder des entités HTML, permettant ainsi de manipuler du texte HTML en toute sécurité et de le rendre compatible avec différents navigateurs web.

Fonctions disponibles :
- encode_html_entities(text) : Encode le texte en remplaçant les caractères spéciaux par leurs entités HTML équivalentes.
- decode_html_entities(text) : Décode le texte en remplaçant les entités HTML par leurs caractères spéciaux correspondants.
- strip_html_tags(text) : Supprime toutes les balises HTML du texte, ne laissant que le texte brut.
- extract_html_text(text) : Extrait le texte visible d'une chaîne HTML, en excluant les balises HTML.

Ce module est utile pour sécuriser le contenu HTML en échappant les caractères spéciaux, ainsi que pour extraire et manipuler le texte brut d'une page HTML.

Auteur : [Votre nom]
Date de création : [Date de création]
'''

def encode_html_entities(text) :
    '''
    Principe : Cette fonction prend du texte en entrée et remplace les caractères spéciaux par leurs équivalents en entités HTML. Par exemple, elle remplacerait "<" par "<", ">" par ">", etc.
    Usage typique : Utilisé pour échapper les caractères spéciaux dans le texte afin de l'afficher correctement dans une page HTML, évitant ainsi les problèmes de sécurité et d'affichage.
    '''



def decode_html_entities(text) :
    '''
    Principe : Cette fonction prend du texte en entrée et remplace les entités HTML par les caractères spéciaux correspondants. Par exemple, elle remplacerait "<" par "<", ">" par ">", etc.
    Usage typique : Utilisé pour décoder les entités HTML dans le texte, permettant de récupérer le texte original à partir d'une chaîne HTML.
    '''



def strip_html_tags(text) :
    '''
    Principe : Cette fonction prend du texte en entrée et supprime toutes les balises HTML, ne laissant que le texte brut.
    Usage typique : Pour extraire le contenu textuel d'une page HTML, par exemple pour analyser le texte brut sans les balises HTML.
    '''



def extract_html_text(text) :
    '''
    Principe : Cette fonction prend du texte en entrée et extrait le texte contenu entre les balises HTML, en excluant les balises elles-mêmes.
    Usage typique : Pour extraire uniquement le texte visible d'une page HTML, en excluant les balises et autres éléments de formatage.
    '''

