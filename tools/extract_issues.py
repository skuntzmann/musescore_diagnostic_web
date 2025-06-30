import os
import requests
import json
import time

# Configuration de l'accès à l'API GitHub
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"}
OWNER = "musescore"
REPO = "MuseScore"
PER_PAGE = 100
MAX_PAGES = 100  # limite de sécurité (100 x 100 = 10 000 max)

# Mots-clés typiques d'erreur à détecter
KEYWORDS = [
    "crash", "error", "exception", "denied", "permission", "freeze",
    "failed", "cannot", "undefined", "null", "not working", "hang", "segfault",
    "fatal", "abort", "timeout", "blocked", "corrupted", "conflict", "bug"
]

# Liste finale des erreurs
errors = []

def fetch_issues():
    all_issues = []
    print("📡 Téléchargement des issues de GitHub...")
    for page in range(1, MAX_PAGES + 1):
        print(f"  → Page {page}")
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
        params = {
            "state": "all",
            "per_page": PER_PAGE,
            "page": page
        }
        r = requests.get(url, headers=HEADERS, params=params)
        if r.status_code != 200:
            print("Erreur lors de la requête :", r.status_code, r.text)
            break
        data = r.json()
        if not data:
            break
        all_issues.extend(data)
        time.sleep(0.5)
    print(f"✅ {len(all_issues)} issues récupérées.")
    return all_issues

def issue_matches(issue):
    title = (issue.get("title") or "").lower()
    body = (issue.get("body") or "").lower()
    text = title + " " + body
    labels = [lbl["name"].lower() for lbl in issue.get("labels", [])]
    matches = [k for k in KEYWORDS if k in text]
    return {
        "matches": matches,
        "is_error": matches or any(lab in labels for lab in ["bug", "crash", "regression"])
    }

def extract_issues():
    issues = fetch_issues()
    for issue in issues:
        match_info = issue_matches(issue)
        if not match_info["is_error"]:
            continue
        errors.append({
            "issue_id": issue["number"],
            "title": issue.get("title"),
            "labels": [lbl["name"] for lbl in issue.get("labels", [])],
            "match_keywords": match_info["matches"],
            "solution": "",  # à remplir manuellement ou ultérieurement
            "url": issue.get("html_url")
        })

    print(f"🧠 {len(errors)} erreurs identifiées avec mots-clés ou labels.")
    with open("errors.json", "w", encoding="utf-8") as f:
        json.dump(errors, f, indent=2, ensure_ascii=False)
    print("📁 Fichier 'errors.json' généré avec succès.")

if __name__ == "__main__":
    extract_issues()
