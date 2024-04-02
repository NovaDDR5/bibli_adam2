
# Module d'encodage 64 bit
'''
Ce module fournit des fonctions pour encoder et décoder differents types de données 
en base64. Le codage en base64 est utilisé pour représenter des données binaires sous 
forme de texte ASCII, ce qui le rend utile pour la transmission sûre de données sur 
des canaux qui peuvent ne pas prendre en charge correctement les données binaires.

Fonctions disponibles :
- encode_base64(data) : Encode les données binaires en base64.
- decode_base64(encoded_data) : Décode les données base64 en données binaires.
- url_safe_encode_base64(data) : Encode les données en base64 en utilisant un 
  alphabet modifié pour les rendre compatibles avec les URLs.
- url_safe_decode_base64(encoded_data) : Décode les données base64 encodées en 
  utilisant un alphabet modifié pour les URLs.

Ce module est utile pour plusieurs cas d'utilisation, notamment l'envoi sécurisé de 
données via des protocoles de communication, le stockage de données binaires dans 
des formats de texte, etc.
'''

# Définition de l'alphabet base64
base64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode_base64(data):
    '''
    Cette fonction prend des données binaires en entrée et les encode en base64.

    Arguments :
    - data : bytes, les données binaires à encoder en base64.

    Returns :
    - str, la chaîne encodée en base64.

    Principe :
    L'encodage en base64 consiste à représenter des données binaires sous forme 
    de texte ASCII. Pour cela, les données binaires sont divisées en groupes de 
    3 bytes. Ensuite, chaque groupe est converti en 4 caractères base64, qui sont 
    des caractères spéciaux utilisés pour représenter les données binaires. Si la 
    taille des données en entrée n'est pas un multiple de 3, cela signifie qu'il 
    reste des bytes non utilisés pour former un groupe complet. Dans ce cas, un ou 
    deux caractères de remplissage sont ajoutés à la fin de la chaîne base64 pour 
    indiquer quels bytes sont manquants.

    Usage typique :
    Cette fonction est utilisée pour convertir des données binaires en une chaîne 
    base64. Par exemple, elle peut être utilisée pour l'envoi sécurisé de données 
    via des protocoles de communication.

    Exemple :
    >>> encode_base64(b"Hello, World!")
    'SGVsbG8sIFdvcmxkIQ=='
    '''

    encoded = ""
    padding = ""
    # Conversion de chaque groupe de 3 bytes en base64
    for i in range(0, len(data), 3):
        group = data[i:i+3]
        # Ajout de remplissage si le groupe n'a pas une taille de 3 bytes
        if len(group) < 3:
            padding = "=" * (3 - len(group)) # Remplissage avec autant de caractères '=' que nécessaire pour compléter le dernier groupe de 4 caractères base64
            group += b'\x00' * (3 - len(group)) # Complétion du dernier groupe de bytes avec des zéros pour obtenir un groupe de 3 bytes
        # Conversion du groupe en nombre entier
        num = 0
        for byte in group:
            num = (num << 8) + byte
        # Conversion du nombre en base64
        for j in range(4):
            index = (num >> (6 * (3 - j))) & 63
            encoded += base64_charset[index]
    # Retour de la chaîne encodée avec le remplissage
    return encoded[:-len(padding)] + padding



def decode_base64(encoded_data):
    '''
    Cette fonction prend une chaîne base64 en entrée et la décode en données binaires.

    Arguments :
    - encoded_data : str, la chaîne encodée en base64.

    Returns :
    - bytes, les données binaires décodées.

    Principe :
    Le décodage en base64 consiste à récupérer les données binaires à partir d'une 
    chaîne base64. Pour cela, chaque groupe de 4 caractères base64 est converti en 
    un groupe de 3 bytes correspondants. Les caractères de remplissage, s'il y en a, 
    sont ignorés lors du décodage.

    Usage typique :
    Cette fonction est utilisée pour décoder une chaîne base64 en données binaires, 
    par exemple pour récupérer des données envoyées via des protocoles de communication.

    Exemple :
    >>> decode_base64('SGVsbG8sIFdvcmxkIQ==')
    b'Hello, World!'
    '''

    decoded = bytearray()
    padding = encoded_data.count('=')
    # Conversion de chaque groupe de 4 caractères base64 en bytes
    for i in range(0, len(encoded_data), 4):
        group = encoded_data[i:i+4]
        num = 0
        # Conversion des caractères base64 en nombre entier
        for char in group:
            num = (num << 6) + base64_charset.index(char)
        # Conversion du nombre en bytes et suppression du padding
        for j in range(3):
            decoded.append((num >> (8 * (2 - j))) & 255)
    # Retour des données décodées
    return bytes(decoded[:-padding])


def url_safe_encode_base64(data):
    '''
    Similaire à encode_base64(data), mais utilise un alphabet base64 modifié pour 
    produire une chaîne base64 sécurisée pour les URL.

    Arguments :
    - data : bytes, les données binaires à encoder en base64.

    Returns :
    - str, la chaîne encodée en base64 sécurisée pour les URL.

    Principe :
    Cette fonction encode les données binaires en utilisant un alphabet base64 
    modifié pour être compatible avec les URLs. Cet alphabet modifié remplace les 
    caractères '+' et '/' par '-' et '_', respectivement. Le principe de l'encodage 
    reste le même que pour la fonction encode_base64.

    Usage typique :
    Cette fonction est utilisée pour encoder des données à utiliser dans une URL sans 
    avoir à encoder les caractères spéciaux comme '/' ou '+'.

    Exemple :
    >>> url_safe_encode_base64(b"Hello, World!")
    'SGVsbG8sIFdvcmxkIQ=='
    '''

    encoded = ""
    padding = ""
    # Conversion de chaque groupe de 3 bytes en base64
    for i in range(0, len(data), 3):
        group = data[i:i+3]
        # Ajout de remplissage si le groupe n'a pas une taille de 3 bytes
        if len(group) < 3:
            padding = "=" * (3 - len(group)) # Remplissage avec autant de caractères '=' que nécessaire pour compléter le dernier groupe de 4 caractères base64
            group += b'\x00' * (3 - len(group)) # Complétion du dernier groupe de bytes avec des zéros pour obtenir un groupe de 3 bytes
        # Conversion du groupe en nombre entier
        num = 0
        for byte in group:
            num = (num << 8) + byte
        # Conversion du nombre en base64
        for j in range(4):
            index = (num >> (6 * (3 - j))) & 63
            encoded += base64_charset[index]
    # Retour de la chaîne encodée avec le remplissage
    return encoded[:-len(padding)] + padding


def url_safe_decode_base64(encoded_data):
    '''
    Similaire à decode_base64(encoded_data), mais pour décoder des chaînes base64 
    sécurisées pour les URL.

    Arguments :
    - encoded_data : str, la chaîne encodée en base64 sécurisée pour les URL.

    Returns :
    - bytes, les données binaires décodées.

    Principe :
    Cette fonction décode une chaîne base64 qui a été encodée pour être utilisée dans 
    une URL. Elle utilise un alphabet base64 modifié, dans lequel les caractères '+' et 
    '/' ont été remplacés par '-' et '_', respectivement. Le principe de décodage reste 
    le même que pour la fonction decode_base64.

    Usage typique :
    Cette fonction est utilisée pour décoder une chaîne base64 sécurisée qui a été encodée 
    pour être utilisée dans une URL.

    Exemple :
    >>> url_safe_decode_base64('SGVsbG8sIFdvcmxkIQ==')
    b'Hello, World!'
    '''

    decoded = bytearray()
    padding = encoded_data.count('=')
    # Conversion de chaque groupe de 4 caractères base64 en bytes
    for i in range(0, len(encoded_data), 4):
        group = encoded_data[i:i+4]
        num = 0
        # Conversion des caractères base64 en nombre entier
        for char in group:
            num = (num << 6) + base64_charset.index(char)
        # Conversion du nombre en bytes et suppression du padding
        for j in range(3):
            decoded.append((num >> (8 * (2 - j))) & 255)
    # Retour des données décodées
    return bytes(decoded[:-padding])