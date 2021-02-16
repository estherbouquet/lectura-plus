class Builder:
  def __init__(self, formatted_filename):
    self.weather_article = formatted_filename.startswith("METEO")
    self.formatted_filename = formatted_filename
    self.output_file = self.open_file()
    self.converted_html = self.build_html()
    self.write_html()

  def build_html(self):
    html = markdown.markdown(contents)
    return adding_graphic_lines.add(html)

  def write_html(self):
    self.insert_head()
    self.insert_html_body()
    self.insert_image()
    self.insert_lines()
    self.insert_presentation_text()
    self.insert_lines()
    self.insert_logo()
    self.insert_lines()
    self.insert_legal_mentions()
    self.insert_lines()
    self.insert_logo_block()
    self.insert_lines()
    self.insert_qr_code()
    self.close_file()

  def open_file(self):
    open(r'./output/'+ self.formatted_filename +'.html', 'w')

  def insert_head(self):
    if self.weather_article:
      header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet_meteo.css' rel='stylesheet'>\n</head>\n"
    else:
      header = r"<head><meta charset='UTF-8'><title>"+formatted_filename+"</title><link href='../stylesheet.css' rel='stylesheet'>\n</head>\n"
    self.output_file.write(header)  # et on l'écrit dans le fichier

  def insert_html_body(self):
    # E- On écrit l'ouverture de la balise body
    self.output_file.write("<body>\n")
    self.output_file.write(self.converted_html) # on insère le HTML converti

  def insert_image(self):
    output_file.write(img_detection.corresponding_image_for_filename(formatted_filename, input_folder, subdir)) # on insère ce que retourne la fonction returnIfCorrespondingImgFor

  def insert_lines(self):
    if self.weather_article:
      self.output_file.write('<div class="blocplus">\n<img src="../assets/element-barre-nb.png"></img>\n</div>')
    else:
      self.output_file.write('<div class="blocplus">\n<img src="../assets/element-barre.png"></img>\n</div>')

  def insert_presentation_text(self):
    self.output_file.write('<div class="ticket">\n<p>Un ticket de presse ancienne proposé par Lectura Plus, le site du patrimoine écrit et graphique en Auvergne-Rhône-Alpes.<br>À lire dans la minute ! Pour plus de découvertes, rendez-vous sur <u>www.lectura.plus</u></p>\n</div>')
    self.output_file.write('<div class="italic">\n<p>Ticket lecteur à conserver - ne pas jeter sur la voie publique</p>\n</div>')

  def insert_logo(self):
    self.output_file.write('<div class="logoL">\n<img src=../assets/LogoL.png></img>\n</div>')

  def insert_legal_mentions(self):
    self.output_file.write('<div class="mentions">\n<p>Lectura Plus est un projet coopératif des Villes et Agglomérations d\'Annecy, Bourg-en-Bresse, Chambéry, Clermont-Ferrand, Grenoble, Lyon, Roanne, Saint-Étienne et Valence, réalisé avec le soutien de la DRAC Auvergne-Rhône-Alpes et coordonné par Auvergne-Rhône-Alpes Livre et Lecture.</p>\n</div>')
    self.output_file.write('<div class="mentions">\n<p>Un projet imaginé et coordonné par Alizé Buisse et Priscille Legros, Auvergne-Rhône-Alpes Livre et Lecture. Dispositif numérique conçu par Léa Belzunces et Esther Bouquet. Conception graphique menée par Déborah-Loïs Séry. Fabrication artisanale par Guillaume Buisson, Atelier Regards.</p>\n</div>')

  def insert_logo_block(self):
    if self.weather_article:
      self.output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet-nb.jpg"></img>\n</div>')
    else:
      self.output_file.write('<div class="bloclogo">\n<img src="../assets/blog-logo-complet.jpg"></img>\n</div>')

  def insert_qr_code(self):
    qrcode = f"../input/{self.formatted_filename}.png"
    self.output_file.write('<div class="qrcode">\n<img src="' + qrcode + '"></img>\n</div>')

  def close_file(self):
    self.output_file.write("\n</body>")
    self.output_file.close()
