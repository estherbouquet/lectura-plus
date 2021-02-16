import os
import markdown # à installer à la main via `sudo apt-get install python3-markdown`
import img_detection
import update_markdown
import adding_graphic_lines
import html_builder

# Fonction qui convertit notre fichier .txt courant dans ./input/ avec du texte en markdown à l'intérieur,
# en fichier .html balisé dans ./output/
def layout(fullpath, input_folder, subdir):
  update_markdown.rearrangeMardownOrder(fullpath) # on reformate le markdown utilisé pour un autre plus lisible
  with open(fullpath, 'r') as myfile:
    contents = myfile.read() # on récupère le contenu dans la variable contents
    filename = os.path.basename(myfile.name) # on récupère le chemin d'accès au fichier
  formatted_filename = os.path.splitext(filename)[0] # on retire l'extension (.txt) du nom+chemin d'accès du fichier
  return HTMLBuilder(formatted_filename)
