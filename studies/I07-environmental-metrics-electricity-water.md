# I07 — KPI datacenter, intensités électriques, eau et règles de mesure

## Cadre européen spécifique
Le [règlement délégué (UE) 2024/1364](https://eur-lex.europa.eu/eli/reg_del/2024/1364/oj?locale=eng) établit un mécanisme de déclaration pour les exploitants de datacenters concernés **dont la puissance IT installée atteint 500 kW ou plus**. Il définit en particulier :

- **PUE = E_DC / E_IT**, énergie datacenter / énergie IT (même période et périmètre).
- **WUE = W_IN / E_IT** : W_IN selon définition du règlement ; si W_IN en m³ et E_IT en MWh, le résultat m³/MWh est numériquement identique à L/kWh.
- **ERF = E_REUSE / E_DC** : énergie réutilisée / énergie datacenter.
- **REF = E_RES-TOT / E_DC** : énergie renouvelable / énergie datacenter.

Le reporting public est notamment agrégé par États membres et UE, pas nécessairement publié par site ni par client cloud.

## Les facteurs « carbone de l'électricité » ne sont pas interchangeables

| Méthode | Ce qu'elle mesure | Limites |
|---|---|---|
| RTE éCO2mix production | Émissions directes par kWh **produit en France** | Hors import/export, hors ACV des filières |
| Facteur *location-based* réseau consommé | Intensité moyenne réseau d'une zone et période | Dépend géographie, mix et inclusion imports |
| Facteur *market-based* | Instruments contractuels et méthode comptable organisationnelle | Ne prouve pas forcément effet physique local |
| Intensité marginale prévue | Changement estimé d'émissions si consommation déplacée | Estimation causale, modèle, incertitude |
| ACV électricité | Fabrication infra, combustibles, transport et exploitation | Frontière et mise à jour distinctes |

Source RTE : [explication précise des émissions par kWh produit](https://www.rte-france.com/donnees-publications/eco2mix-donnees-temps-reel/emissions-co2-par-kwh-produit-france).

## Mesure couche par couche
1. **Bâtiment** : E_DC, E_IT, W_IN, heures, puissance et disponibilité, région du réseau.
2. **Serveur** : watt mesuré x temps, energy domain GPU/CPU, mémoire, stockage, réseau, tuilage CPU / GPU.
3. **Service** : requêtes, tokens, taux validation, retries, batch, quotas, p95/p99 et interruptions.
4. **Cycle de vie** : E + émissions fabrication allouées par ressource/temps + renouvellement + traitement connu.
5. **Contrôle** : version métrique, horodatage, source, instrument, données manquantes et méthodes.

## Comparabilité Green IT
Pour comparer deux offres, conserver exactement les mêmes frontières : même qualité/latence cible, mêmes données, taille/contexte des requêtes et charge. Une amélioration de PUE avec consommation d'eau supplémentaire ne suffit pas à conclure à un meilleur bilan global ; WUE, stress hydrique et carbone sont arbitrés conjointement.

## Grille de confiance de chaque chiffre
- **A** : mesure compteur/instrument calibré et complet, donnée primaire, période précise.
- **B** : mesure observée partielle, extrapolation documentée.
- **C** : paramètre fournisseur et estimation modélisée avec hypothèses.
- **D** : ordre de grandeur/illustration, hors toute conclusion chiffrée.

Chaque résultat de référence conserve **qualité donnée et bornes**, l'absence de donnée est explicitement « NA » et jamais « 0 ».

## Source ADEME
L'[ADEME, juillet 2026](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/) attire l'attention sur les effets environnementaux **directs et indirects** des IA génératives et agentiques : consommation d'infrastructure, production matérielle et possible effet rebond. Une économie technique d'énergie par service n'implique pas nécessairement une baisse absolue annuelle.
