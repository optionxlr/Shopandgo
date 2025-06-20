import os
import json

# Charger les données produit
with open('produits.json', 'r', encoding='utf-8') as f:
    produits = json.load(f)

# Générer les dossiers/pages
for produit in produits:
    dossier = f"site/produit{produit['id']}"
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
</html>"""

    with open(f"{dossier}/index.html", "w", encoding="utf-8") as f:
        f.write(contenu)

print("✅ Pages produits générées avec succès.")
