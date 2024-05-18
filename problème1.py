import re

def isValidhtml(html):
    # Modèle regex pour trouver les balises HTML
    html_tag = re.compile(r'</?([a-zA-Z]+[0-9]*)(?: [^>]*)?>')
    # balises auto-fermantes
    balise_fermante_tags = {'br', 'meta', 'link'}
    pile = []

    # trouver les tags dans html
    tags = html_tag.findall(html)
    isValid=True
    # Trouver toutes les balises dans la chaîne HTML
    for trouve in html_tag.finditer(html):
        tag = trouve.group(1)
        is_closing_tag = trouve.group(0).startswith('</')

        if not is_closing_tag:
            # C'est une balise ouvrante, on l'ajoute à la pile si elle n'est pas auto-fermante
            if tag not in balise_fermante_tags:
                pile.append(tag)
        else:
            # C'est une balise fermante, on la retire de la pile et vérifie si elle correspond
            if not pile or pile.pop() != tags:
                return isValid

    # Si lapile est vide tous les tags sont fermés
    return len(pile) == 0

# Example
html_vrai = "<p></p>"
html_faux = "<p><span>"
print(isValidhtml(html_vrai))
print(isValidhtml(html_faux))
