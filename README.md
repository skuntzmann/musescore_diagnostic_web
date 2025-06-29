# MuseScore Diagnostic Web

Cette application Flutter Web est une version simple de l'app de diagnostic MuseScore.

## Installation

1. Installe Flutter (https://flutter.dev/docs/get-started/install)
2. Active Flutter Web :
   ```
   flutter config --enable-web
   ```
3. Pour lancer l'app localement :
   ```
   flutter run -d chrome
   ```

## Déploiement GitHub Pages

1. Crée un dépôt GitHub vide nommé `musescore_diagnostic_web`
2. Clone ce dépôt ou décompresse ce projet dans un dossier
3. Compile le projet web :
   ```
   flutter build web --release
   ```
4. Installe `gh-pages` (si pas déjà) :
   ```
   npm install -g gh-pages
   ```
5. Déploie le site sur la branche `gh-pages` :
   ```
   gh-pages -d build/web
   ```
6. Dans GitHub, va dans **Settings > Pages**, choisis la branche `gh-pages` comme source
7. Ton site sera accessible à :
   ```
   https://<ton-utilisateur>.github.io/musescore_diagnostic_web/
   ```

## Note

- Cette version Web est une démo simple, la version mobile Flutter supporte caméra et OCR.