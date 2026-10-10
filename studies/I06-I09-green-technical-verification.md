# Contrôles de cohérence des itérations I06–I09

**Statut** : calculs d'illustration contrôlés arithmétiquement ; AUCUNE mesure terrain.

## Vérification unités fictives I06
- Privé : E_site=100 × 1,25 = 125 kWh. O=125 × 0,05 = 6,25 kgCO2e. O+M=6,25+8=14,25 ; /10=1,425 kgCO2e par 1 000 résultats valides.
- Cloud : E_site=70 × 1,18 = 82,6 kWh. O=82,6 × 0,30 = 24,78 kgCO2e. O+M=24,78+3=27,78 ; /10=2,778 kgCO2e par 1 000 résultats valides.
- Ces calculs n'incluent ni eau ni éléments de fabrication non chiffrés, et les paramètres sont **fictifs**.

## Green claims interdits sans preuve
- « La France = 0 carbone » : faux.
- « PUE plus faible = impact global plus faible » : incomplet, dépend IT, énergie, eau, matériel.
- « Tous les datacenters 945 TWh en 2030 = IA seule » : mauvaise attribution AIE.
- « GPU cloud sans données d'ACV = empreinte nulle » : faux.
- « 40 % cooling Google = 40 % total datacenter » : faux.
- « Appeler un LLM pour optimiser garantit un gain net » : non démontré.
- « Le modèle IA minimise le carbone même s'il change la qualité du service » : comparaison invalide.

## Validation documentaire
- Formules SCI cohérentes sous unités homogènes.
- PUE, WUE, ERF, REF alignés règlement UE 2024/1364.
- Chiffres ADEME et DeepMind correctement attribués et datés.
- Séparation prédiction / estimation / mesure et classement de confiance A–D.

## Travaux ultérieurs si données accessibles
Mesures réelles : choisir deux environnements, même workload, extraire compteurs IT/site/eau et ACV fournisseur puis calculer impact net (intervalle). Ce n'est pas un gate de la V1.0.