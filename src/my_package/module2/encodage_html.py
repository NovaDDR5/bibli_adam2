
# Module d'encodage HTML
'''
Ce module fournit des fonctionnalités pour encoder et décoder des entités HTML,
permettant ainsi de manipuler du texte HTML en toute sécurité et de le rendre 
compatible avec différents navigateurs web.

Fonctions disponibles :
- encode_html_entities(text) : Encode le texte en remplaçant les caractères spéciaux 
  par leurs entités HTML équivalentes.
- decode_html_entities(text) : Décode le texte en remplaçant les entités HTML par 
  leurs caractères spéciaux correspondants.
- strip_html_tags(text) : Supprime toutes les balises HTML du texte, ne laissant 
  que le texte brut.
- extract_html_text(text) : Extrait le texte visible d'une chaîne HTML, en excluant 
  les balises HTML.

Ce module est utile pour sécuriser le contenu HTML en échappant les caractères spéciaux, 
ainsi que pour extraire et manipuler le texte brut d'une page HTML.
'''


def encode_html_entities(text):
    '''
    Cette fonction prend du texte en entrée et remplace les caractères spéciaux 
    par leurs équivalents en entités HTML. Par exemple, elle remplacerait "<" par "&lt;", 
    ">" par "&gt;", etc.

    Arguments :
    - text : str, le texte à encoder en entités HTML.

    Returns :
    - str, le texte avec les caractères spéciaux remplacés par leurs entités HTML.

    Principe :
    L'encodage en entités HTML consiste à remplacer certains caractères spéciaux, tels que 
    les chevrons (< et >), les guillemets ("), et les ampersands (&), par leurs équivalents 
    en entités HTML. Cela permet d'éviter les problèmes d'interprétation incorrecte du texte 
    par les navigateurs web.

    Usage typique :
    Cette fonction est utilisée pour échapper les caractères spéciaux dans le texte afin de 
    l'afficher correctement dans une page HTML, évitant ainsi les problèmes de sécurité et d'affichage.

    Exemple :
    >>> encode_html_entities('<p>Hello, World!</p>')
    '&lt;p&gt;Hello, World!&lt;/p&gt;'
    '''

    encoded_text = ""
    # Remplacement des caractères spéciaux par leurs entités HTML
    for char in text:
        if char == '<':
            encoded_text += '&lt;'
        elif char == '>':
            encoded_text += '&gt;'
        elif char == '&':
            encoded_text += '&amp;'
        elif char == '"':
            encoded_text += '&quot;'
        elif char == "'":
            encoded_text += '&#39;'
        else:
            encoded_text += char
    return encoded_text


def decode_html_entities(text):
    '''
    Cette fonction prend du texte en entrée et remplace les entités HTML par les 
    caractères spéciaux correspondants. Par exemple, elle remplacerait "&lt;" par "<", 
    "&gt;" par ">", etc.

    Arguments :
    - text : str, le texte à décoder à partir d'entités HTML.

    Returns :
    - str, le texte avec les entités HTML remplacées par les caractères spéciaux.

    Principe :
    Le décodage des entités HTML consiste à remplacer les entités HTML, telles que "&lt;", 
    "&gt;", "&quot;", etc., par les caractères spéciaux correspondants. Cela permet de 
    récupérer le texte original à partir d'une chaîne HTML.

    Usage typique :
    Cette fonction est utilisée pour décoder les entités HTML dans le texte, permettant de 
    récupérer le texte original à partir d'une chaîne HTML.

    Exemple :
    >>> decode_html_entities('&lt;p&gt;Hello, World!&lt;/p&gt;')
    '<p>Hello, World!</p>'
    '''

    # Remplacement des entités HTML par leurs caractères spéciaux
    decoded_text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
    return decoded_text


def strip_html_tags(text):
    '''
    Cette fonction prend du texte en entrée et supprime toutes les balises HTML, 
    ne laissant que le texte brut.

    Arguments :
    - text : str, le texte avec des balises HTML à supprimer.

    Returns :
    - str, le texte sans les balises HTML.

    Principe :
    La suppression des balises HTML consiste à supprimer toutes les balises ainsi que leur 
    contenu du texte, ne laissant que le texte brut.

    Usage typique :
    Cette fonction est utilisée pour extraire le contenu textuel d'une page HTML, par exemple 
    pour analyser le texte brut sans les balises HTML.

    Exemple :
    >>> strip_html_tags('<p>Hello, <b>World</b>!</p>')
    'Hello, World!'
    '''

    in_tag = False
    result = ""
    # Parcours du texte et suppression des balises HTML
    for char in text:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result += char
    return result


def extract_html_text(text):
    '''
    Cette fonction prend du texte en entrée et extrait le texte contenu entre les 
    balises HTML, en excluant les balises elles-mêmes.

    Arguments :
    - text : str, le texte contenant du contenu entre des balises HTML.

    Returns :
    - str, le texte visible extrait des balises HTML.

    Principe :
    L'extraction du texte HTML consiste à supprimer toutes les balises HTML du texte, ne 
    laissant que le texte visible entre les balises.

    Usage typique :
    Cette fonction est utilisée pour extraire uniquement le texte visible d'une page HTML, en 
    excluant les balises et autres éléments de formatage.

    Exemple :
    >>> extract_html_text('<p>Hello, <b>World</b>!</p>')
    'Hello, World!'
    '''

    in_tag = False
    result = ""
    # Parcours du texte et extraction du texte entre les balises HTML
    for char in text:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result += char
    return result