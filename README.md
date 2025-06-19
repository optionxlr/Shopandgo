# Shopandgo
/* Projet ElectroniShop Full Stack: Frontend (Next.js + Tailwind) + Backend (Python + Brevo API) */

// === frontend/src/pages/index.js === import { fetchProduits } from '../lib/ali' import CardProduit from '../components/CardProduit' import FormulaireNewsletter from '../components/FormulaireNewsletter'

export async function getStaticProps() { const produits = await fetchProduits() return { props: { produits }, revalidate: 3600 } }

export default function Home({ produits }) { return ( <div className="container mx-auto px-4 py-8"> <h1 className="text-3xl font-extrabold mb-6">Nos gadgets électroniques</h1>

<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    {produits.map(p => (
      <CardProduit key={p.productId} produit={p} />
    ))}
  </div>

  <section className="mt-12 bg-gray-100 p-6 rounded-lg text-center">
    <h2 className="text-2xl font-semibold mb-4">Restez informé</h2>
    <p className="mb-4">Inscrivez-vous à notre newsletter pour recevoir les nouveautés directement dans votre boîte mail.</p>
    <FormulaireNewsletter />
  </section>
</div>

) }

// === frontend/src/components/CardProduit.js === export default function CardProduit({ produit }) { return ( <div className="bg-white border border-gray-200 rounded-2xl shadow-lg hover:shadow-neon transition p-4"> <img src={produit.imageUrl} alt={produit.title} className="w-full h-48 object-cover rounded-xl mb-4" /> <h3 className="text-xl font-semibold mb-2">{produit.title}</h3> <p className="text-gray-600 mb-4">{produit.description}</p> <a href={produit.url} className="text-blue-500 underline hover:text-blue-700">Voir produit</a> </div> ) }

// === frontend/src/components/FormulaireNewsletter.js === import { useState } from 'react'

export default function FormulaireNewsletter() { const [email, setEmail] = useState('') const handleSubmit = async (e) => { e.preventDefault() const res = await fetch('/api/subscribe', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ email }) }) setEmail('') }

return ( <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-2 justify-center"> <input type="email" value={email} onChange={e => setEmail(e.target.value)} required className="px-4 py-2 rounded-lg border w-full sm:w-auto" placeholder="Votre adresse email" /> <button type="submit" className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"> S'inscrire </button> </form> ) }

// === backend/envoyer_emails.py === #!/usr/bin/env python3

-- coding: utf-8 --

import os import json import logging from pathlib import Path from typing import List from sib_api_v3_sdk import ApiClient, TransactionalEmailsApi from sib_api_v3_sdk.models import SendSmtpEmail

logging.basicConfig( level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S" ) logger = logging.getLogger(name)

BREVO_API_KEY = os.getenv("BREVO_API_KEY") if not BREVO_API_KEY: raise RuntimeError("Variable BREVO_API_KEY manquante")

BASE_DIR = Path(file).parent SUBSCRIBERS_FILE = BASE_DIR / "subscribers.json"

def load_subscribers(filepath: Path) -> List[str]: if not filepath.exists(): return [] data = json.loads(filepath.read_text(encoding="utf-8")) return [e.strip() for e in data if isinstance(e, str) and e.strip()]

def send_email(api_instance: TransactionalEmailsApi, recipient: str): html = """ <html><body><h1>Salut 👋</h1><p>Découvre nos gadgets innovants sur <a href='https://electronishop.com'>ElectroniShop</a>.</p></body></html> """ email = SendSmtpEmail( sender={"name": "ElectroniShop", "email": "noreply@electronishop.com"}, to=[{"email": recipient}], subject="🆕 Nouveaux gadgets disponibles !", html_content=html ) api_instance.send_transac_email(email)

def send_bulk_emails(subscribers: List[str]): config = ApiClient.Configuration() config.api_key["api-key"] = BREVO_API_KEY with ApiClient(config) as api_client: api = TransactionalEmailsApi(api_client) for email in subscribers: send_email(api, email)

def main(): logger.info("Démarrage envoi d'e-mails") subs = load_subscribers(SUBSCRIBERS_FILE) if not subs: logger.warning("Aucun destinataire trouvé") return send_bulk_emails(subs)

if name == "main": main()

// === backend/subscribers.json === [ "client1@email.com", "client2@email.com" ]

// === frontend/src/lib/ali.js === export async function fetchProduits() { return [ { productId: "1", title: "Station de recharge sans fil", description: "Rechargez vos appareils rapidement sans câble.", imageUrl: "https://via.placeholder.com/300", url: "https://aliexpress.com/item1" }, { productId: "2", title: "Mini ventilateur USB", description: "Compact, puissant, idéal pour l'été.", imageUrl: "https://via.placeholder.com/300", url: "https://aliexpress.com/item2" } ] }

// === frontend/tailwind.config.js === module.exports = { content: ['./src/**/*.{js,ts,jsx,tsx}'], theme: { extend: { boxShadow: { neon: '0 0 15px rgba(0, 153, 255, 0.7)' } } }, plugins: [] }

// === .env.local === BREVO_API_KEY=ta_clé_secrète_brevo
