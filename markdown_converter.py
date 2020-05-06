import markdown
import os
# import re (au cas où il faut utiliser la regex)

# On définint le dossier avec tous les fichiers importés
input_folder = './input'

# Pour chaque fichier dans ce dossier
for file in os.scandir(input_folder):
  # On ouvre le fichier
  with open(file, 'r') as myfile:
      contents = myfile.read() # On récupère le contenu
      filename = os.path.basename(myfile.name) # On récupère le nom du fichier (sans le chemin d'accès)

  print(filename)
  # formatted_filename = re.sub(r'\.\w+$', '', filename)
  formatted_filename = os.path.splitext(filename)[0] # On retire l'extension (.txt) du nom du fichier
  print(formatted_filename)

  output_file = open(f'./output/{formatted_filename}.html', 'a') # On crée le fichier avec le même nom dans le dossier ./output

  # On ajoute les balises header pour link le CSS
  header = f"<head>\n<meta charset='UTF-8'>\n<title>{formatted_filename}</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
  output_file.write(header)

  # On convertit le markdown en HTML
  html = markdown.markdown(contents)

  # On insère le HTML converti entre deux balises body
  output_file.write("<body>\n")
  output_file.write(html)
  output_file.write("\n</body>")
