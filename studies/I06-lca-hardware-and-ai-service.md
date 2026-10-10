# I06 — ACV complète des infrastructures IA (GPU, HBM, réseau, énergie, fin de vie)

**Nature** : méthode applicable aux infrastructures mondiales et aux banques/assurances, sans équipement détenu. **Sources primaires** : [Green Software Foundation SCI for AI](https://github.com/Green-Software-Foundation/sci-ai/blob/main/SPEC.md), [ADEME, avis 22/07/2026](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/), [Boavizta](https://doc.api.boavizta.org/Explanations/embedded_methodology/).

## Périmètre physique et software

```text
Extraction matières → GPU / HBM / CPU / carte / PSU / réseau / stockage
                    → fabrication serveur / racks / bâtiment
                    → transport et installation
                    → usage : entraînement / fine-tuning / inférence / agents
                         GPU + CPU + mémoire + stockage + réseau
                         refroidissement + UPS (site, selon périmètre)
                    → maintenance, changement de composants, reconditionnement
                    → fin de vie et traitement des déchets
```

Séparer « fabrication incorporée » des « émissions opérationnelles » et distinguer **fabrication du datacenter entier** des seules machines. Spécifier si on inclut équipements utilisateur, réseau externe, préparation données, RAG, training, cache, évaluation, service d'agent, supervision et renouvellements. Le réemploi exige une méthode d'allocation cohérente, pas un crédit carbone automatique.

## Unité fonctionnelle

**SCI for AI** distingue plusieurs acteurs/périmètres du cycle de vie (provider/consumer). Pour une application bancaire, retenir à la fois *kgCO2e / 1 000 résultats métier validés* et, pour diagnostic, kgCO2e / 1 M tokens ; un workflow multi-appels inclut outils, recherche et retries. Pour le training : kgCO2e par entraînement convergé **à qualité comparable**. [SCI for AI](https://github.com/Green-Software-Foundation/sci-ai/blob/main/SPEC.md).

SCI=(O+M)/R, O=E×I (unités cohérentes), M=émissions incorporées attribuées, R=unité fonctionnelle. L'allocation M doit traiter temps de réservation, part des ressources, capacité partagée, durée de vie et sous-utilisation, sans additionner deux fois serveur+GPU.

## Matrice disponibilité des données

| Poste | Données idéales | Cas sans accès au site |
|---|---|---|
| GPU/HBM/serveur fabrication | ACV équipement fabricant / BOM | Modèle estimatif à bornes, donnée « non publique » |
| Énergie IT | Compteur PDU ou télémétrie serveur étalonnée | Watt nominal impossible comme mesure ; scénario illustratif |
| Énergie site | Compteur site, PUE période | Hypothèse PUE explicite **non mesurée** |
| Réseau et stockage | Compteurs affectés aux workloads | Hypothèses séparées et incertitudes |
| Eau | Compteur, WUE site/période | Non disponible : ne pas mettre zéro |
| Intensité électrique | Facteur de réseau pour lieu/temps et méthode | Proxys seulement en fourchette déclarée |
| Cloud partagé | Disclosure fournisseur et convention allocation | Empreinte matérielle **incertaine**, ne pas déclarer zéro |
| Fin de vie | Traitement réel et rapport ACV | Écart méthodologique à signaler |

## Exemple STRICTEMENT fictif pour vérifier les formules
**Unité de service : 10 000 réponses métier valides sur une période** ; toutes les valeurs choisies arbitrairement pour illustrer les calculs, **aucune ne représente une banque ni un fournisseur**.

| Hypothèse | Scénario privé fictif | Scénario cloud fictif |
|---|---:|---:|
| E_IT | 100 kWh | 70 kWh |
| PUE **hypothétique** | 1,25 | 1,18 |
| Facteur électrique **hypothétique** | 0,05 kgCO2e/kWh | 0,30 kgCO2e/kWh |
| M attribué **hypothétique** | 8 kgCO2e | 3 kgCO2e |
| E_site = E_IT × PUE | 125 kWh | 82,6 kWh |
| O = E_site × I | 6,25 kgCO2e | 24,78 kgCO2e |
| O+M | **14,25 kgCO2e** | **27,78 kgCO2e** |
| Intensité pour 1 000 réponses valides | 1,425 kgCO2e | 2,778 kgCO2e |

Même si le cloud fictif consomme moins de kWh, son intensité électrique **choisie arbitrairement** le défavorise ici. Si le facteur d'intensité change, le résultat peut s'inverser : **ce n'est pas un classement environnemental des clouds**.

## Erreurs critiques
- Attribuer l'ensemble des 945 TWh 2030 [AIE](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) à l'IA.
- Estimer charge GPU nominale × heures et présenter comme mesurée.
- Déduire l'empreinte par prompt sans taille/qualité/contexte.
- Additionner consommation GPU à celle du serveur total.
- Poser M=0 parce que cloud fournisseur non transparent.
- Confondre compensation/carbone « évité » avec inventaire d'émissions.
- Employer un facteur RTE de **production directe** comme facteur ACV du réseau consommé.
- Affirmer réduction absolue en présence d'un rebond d'usage.

## Recommandation de dossier d'architecture
Comparer au minimum privé, cloud et solution CPU/SLM pour le même service, avec fourchettes d'incertitude sur M et I, non seulement des valeurs centrales. Compléter carbone par eau, ressources, qualité, résilience, conformité et coûts.
