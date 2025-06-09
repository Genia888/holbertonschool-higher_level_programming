# 🌐 Qu’est-ce qu’une RESTful API ?

## 🔹 API = Application Programming Interface

Une **API** est une interface qui permet à deux applications de **communiquer entre elles**.

### 🔁 Exemples :
- Une application météo utilise une API pour obtenir les données d’un service météo.
- Une application mobile utilise une API pour envoyer un message ou afficher un profil utilisateur.

---

## 🚦 REST = Representational State Transfer

**REST** est un style d’architecture qui définit des règles simples pour faire communiquer des systèmes via le web, généralement avec le protocole **HTTP**.

---

## 🔑 Caractéristiques de REST :

| Caractéristique    | Explication courte                                                                 |
|--------------------|-------------------------------------------------------------------------------------|
| Stateless           | Chaque requête contient toutes les infos nécessaires. Pas de mémoire côté serveur. |
| Client-serveur      | Le client (navigateur, app) et le serveur sont bien séparés.                       |
| Cacheable           | Les réponses peuvent être mises en cache pour améliorer les performances.         |
| Uniform Interface   | Tout se fait avec des URL et des verbes HTTP clairs.                              |

---

## 🔀 Comment ça fonctionne concrètement ?

### 📊 Diagramme logique d’une API REST :

```
+--------+     ➡     +------------+     ➡     +-----------+     ➡     +-----------+
| Client |           | Web Server |           | API Server |           | Database  |
+--------+     ⬅     +------------+     ⬅     +-----------+     ⬅     +-----------+
   ↕              ↔            ↕               ↔           ↕              ↔
 Requête HTTP             Traitement         Logique       Données
(GET, POST...)           (routes, etc.)       métier
```

---

### 📎 Exemple de requête :

```
GET /users/1 HTTP/1.1
Host: api.exemple.com
```

➡ Le client veut consulter l’utilisateur **#1**.  
L’API :
- Cherche dans la base de données
- Formate la réponse en **JSON**
- La renvoie au client

---

## 💡 Les méthodes HTTP principales utilisées en REST :

| Méthode | Rôle                          | Exemple                   |
|---------|-------------------------------|---------------------------|
| GET     | Lire des données              | `GET /users`              |
| POST    | Créer une ressource           | `POST /users`             |
| PUT     | Modifier complètement         | `PUT /users/5`            |
| PATCH   | Modifier partiellement        | `PATCH /users/5`          |
| DELETE  | Supprimer une ressource       | `DELETE /users/5`         |

---

## 🛡️ Sécurité : Authentification

Les APIs doivent être **protégées** pour éviter les accès non autorisés.

- 🔐 Clé API
- 🔐 Token JWT
- 🔐 OAuth2 (Google, Facebook...)

✅ Ces systèmes permettent de s'assurer que seuls les utilisateurs autorisés accèdent aux bonnes routes.

---

## 🛠️ Outils de développement

- **Client CLI** : `curl`, `httpie`
- **Python** :
  - `requests` : pour consommer une API
  - `http.server` : pour créer une API simple
  - `Flask` : pour développer une vraie API REST
- **OpenAPI / Swagger** : pour documenter ton API

---

## 📘 Résumé des étapes du projet

| Étape                          | Objectif                                      |
|--------------------------------|-----------------------------------------------|
| 🔹 HTTP/HTTPS                  | Comprendre les protocoles web                 |
| 🔹 Consommer API (CLI/Python) | Lire et envoyer des données à une API        |
| 🔹 Développer API (Flask)     | Créer ta propre API REST                      |
| 🔹 Sécuriser l’API            | Ajouter authentification/token                |
| 🔹 Documenter l’API           | Générer une documentation claire (OpenAPI)   |

---

## 🎯 Pourquoi REST est si important ?

REST est **partout** aujourd’hui :
- Applications mobiles 📱
- Sites e-commerce 🛍️
- Plateformes cloud ☁️
- Intégrations logicielles 🔄

👉 **Savoir utiliser et créer une RESTful API est une compétence clé** pour tout :
- développeur **back-end**
- développeur **fullstack**
- **data engineer**
