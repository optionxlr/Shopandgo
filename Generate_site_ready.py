import os
import json
import shutil

# Dossier de sortie = la racine du projet
output_folder = "."

# Charger les produits
with open('produit.json', 'r', encoding='utf-8') as f:
    produits = json.load(f)

# Vider les anciens dossiers produits si existants
for produit in produits:
    produit_folder = f"{output_folder}/produit{produit['id']}"
    if os.path.exists(produit_folder):
        shutil.rmtree(produit_folder)

# Générer chaque page produit
liens_html = ""

for produit in produits:
    dossier = f"{output_folder}/produit{produit['id']}"
    os.makedirs(dossier, exist_ok=True)

    contenu = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{produit['titre']}</title>
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      background-color: #4B0000;
      color: white;
      padding: 40px;
      text-align: center;
    }}
    img {{
      width: 300px;
      border-radius: 10px;
    }}
    .box {{
      background: #5e0000;
      padding: 20px;
      border-radius: 20px;
      box-shadow: 0 0 12px #00000088;
      display: inline-block;
    }}
  </style>
</head>
<body>
  <div class="box">
    <h1>{produit['titre']}</h1>
    <img src="{produit['image']}" alt="{produit['titre']}">
    <p>{produit['description']}</p>
    <h3>Prix : {produit['prix']}</h3>
  </div>
</body>
</html>
"""

    with open(f"{dossier}/index.html", "w", encoding="utf-8") as f:
        f.write(contenu)

    liens_html += f"""
    <div class="product">
      <a href="produit{produit['id']}/">
        <div class="description">{produit['titre']}</div>
        <img src="{produit['image']}" alt="{produit['titre']}">
        <div class="neon-bar"></div>
      </a>
    </div>
    """

# Page d'accueil
accueil = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Shopandgo</title>
  <style>
    body {{
      background-color: #4B0000;
      color: white;
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
    }}
    h1 {{
      text-align: center;
      padding: 40px 0;
    }}
    .container {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 30px;
      padding: 20px;
      max-width: 1200px;
      margin: auto;
    }}
    .product {{
      background-color: #5e0000;
      padding: 10px;
      border-radius: 12px;
      box-shadow: 0 0 15px #00000088;
      transition: transform 0.3s ease;
    }}
    .product:hover {{
      transform: scale(1.03);
    }}
    .product img {{
      width: 100%;
      border-radius: 10px;
    }}
    .description {{
      margin-top: 10px;
      font-size: 14px;
      text-align: center;
    }}
    .neon-bar {{
      height: 5px;
      background: #00faff;
      box-shadow: 0 0 12px #00faff, 0 0 24px #00faff;
      margin-top: 8px;
      border-radius: 3px;
    }}
  </style>
</head>
<body>
  <h1>Bienvenue sur Shopandgo</h1>
  <div class="container">
    {liens_html}
  </div>
</body>
</html>"""

# Sauvegarder la page d'accueil
with open(f"{output_folder}/index.html", "w", encoding="utf-8") as f:
    f.write(accueil)

print("✅ Site généré à la racine, prêt pour GitHub Pages.")
