
# 🌐 HTTP vs HTTPS – Les bases

## 🧠 Objectifs pédagogiques
À la fin de cette activité, vous devez être capable de :
- Différencier HTTP et HTTPS
- Comprendre la structure d'une requête/réponse HTTP
- Connaître les méthodes et codes de statut HTTP les plus courants

---

## 🔒 HTTP vs HTTPS : les différences

| Caractéristique     | HTTP                                   | HTTPS                                        |
|---------------------|----------------------------------------|----------------------------------------------|
| Sécurité            | Aucune                                 | Chiffrement via SSL/TLS                      |
| Port par défaut     | 80                                     | 443                                          |
| Affichage URL       | http://                                | https://                                     |
| Intégrité des données | Non garantie                          | Garantie via certificats SSL/TLS             |
| Usage typique       | Sites non sensibles, anciens systèmes  | Sites sensibles (banques, messagerie, etc.)  |

🔐 **HTTPS** protège :
- Les données personnelles
- Les mots de passe
- Les paiements en ligne

---

## 🔀 Structure d’une requête et réponse HTTP

### Exemple de requête HTTP :
```
GET /users/1 HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0
Accept: application/json
```

### Exemple de réponse HTTP :
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe"
}
```

📌 **Composants importants** :
- **Ligne de requête** : méthode + chemin + version
- **En-têtes** : métadonnées (type de contenu, cookies, etc.)
- **Corps (body)** : données envoyées ou reçues (optionnel)

---

## 🔨 Méthodes HTTP les plus courantes

| Méthode | Description                          | Exemple d'utilisation                   |
|---------|--------------------------------------|------------------------------------------|
| GET     | Lire des données                     | `GET /users` → liste des utilisateurs     |
| POST    | Créer une ressource                  | `POST /users` → ajouter un utilisateur    |
| PUT     | Modifier entièrement une ressource   | `PUT /users/1` → remplacer l'utilisateur  |
| PATCH   | Modifier partiellement une ressource | `PATCH /users/1` → changer l'email        |
| DELETE  | Supprimer une ressource              | `DELETE /users/1` → supprimer un user     |

---

## ✅ Codes de statut HTTP courants

| Code | Signification        | Scénario typique                                         |
|------|----------------------|----------------------------------------------------------|
| 200  | OK                   | La requête a réussi (ex : récupération de données)       |
| 201  | Created              | Une ressource a été créée (POST réussi)                  |
| 400  | Bad Request          | La requête est mal formée                                |
| 401  | Unauthorized         | Authentification requise ou invalide                     |
| 404  | Not Found            | La ressource demandée n'existe pas                       |
| 500  | Internal Server Error| Erreur côté serveur                                      |

📌 Les codes sont regroupés :
- 1xx : Information
- 2xx : Succès
- 3xx : Redirection
- 4xx : Erreur côté client
- 5xx : Erreur côté serveur

---

## 🧪 Astuce pour apprendre

Utilise les outils développeur de ton navigateur (onglet **Réseau / Network**) :
1. Clique-droit > Inspecter
2. Recharge la page
3. Observe les requêtes envoyées (méthodes, statuts, en-têtes)

---

## 🔺 Conclusion

HTTP et HTTPS sont les fondations de la communication web :
- **HTTP** = rapide mais non sécurisé
- **HTTPS** = sécurisé, recommandé partout

Comprendre leur fonctionnement est essentiel pour développer ou consommer des **APIs REST**, créer des sites web, ou travailler en cybersécurité.