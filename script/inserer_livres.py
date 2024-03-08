import csv
import hashlib

input_csv_file = './data/biblio.csv'

output_sql_file = './data/livres_insertion.sql'

editeurs_inseres = {}

categories_inseres = {}

def escape_string(s):
    return s.replace("'", "''")

def generate_category_code(category_name):
    hashed = hashlib.sha256(category_name.encode()).hexdigest()
    return hashed[:8]

with open(input_csv_file, newline='', encoding='utf-8') as csvfile:
    with open(output_sql_file, 'w', encoding='utf-8') as sqlfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            titre = escape_string(row['titre'])
            description = escape_string(row['description'])
            isbn = escape_string(row['isbn'])
            annee_apparition = row['annee_apparition']
            image = escape_string(row['image'])
            editeur = escape_string(row['editeur'])
            auteurs = escape_string(row['auteurs'])
            categories = escape_string(row['categories'])

            if editeur not in editeurs_inseres:
                sqlfile.write(f"INSERT IGNORE INTO editeur (nom) VALUES ('{editeur}');\n")
                editeurs_inseres[editeur] = True

            sqlfile.write(f"INSERT IGNORE INTO livre (titre, description, isbn, annee_apparition, image, editeur_id) "
                          f"SELECT '{titre}', '{description}', '{isbn}', {annee_apparition}, '{image}', e.id "
                          f"FROM editeur e WHERE e.nom = '{editeur}';\n")

            for auteur in auteurs.split(','):
                sqlfile.write(f"INSERT IGNORE INTO auteur (nom) VALUES ('{auteur.strip()}');\n")
                sqlfile.write(f"INSERT IGNORE INTO livre_auteur (livre_id, auteur_id) "
                              f"SELECT lv.id, a.id FROM livre lv JOIN auteur a ON lv.titre = '{titre}' "
                              f"WHERE a.nom = '{auteur.strip()}' AND lv.editeur_id = (SELECT id FROM editeur WHERE nom = '{editeur}');\n")

            for categorie in categories.split(','):
                if categorie not in categories_inseres:
                    category_code = generate_category_code(categorie.strip())
                    sqlfile.write(f"INSERT IGNORE INTO categorie (nom, code) VALUES ('{categorie.strip()}', '{category_code}');\n")
                    categories_inseres[categorie] = category_code

                sqlfile.write(f"INSERT IGNORE INTO livre_categorie (livre_id, categorie_id) "
                              f"SELECT lv.id, c.id FROM livre lv JOIN categorie c ON lv.titre = '{titre}' "
                              f"WHERE c.nom = '{categorie.strip()}' AND lv.editeur_id = (SELECT id FROM editeur WHERE nom = '{editeur}');\n")

print("Script SQL généré avec succès !")
