# Plan de mesure environnementale : KPI, collecte, fiabilité

**Principe : aucune métrique calculée ne doit prétendre provenir d'un datacenter audité si elle résulte de facteurs génériques.**

## Niveau physique / site
- Énergie site kWh, énergie IT kWh, puissance maximale et moyenne, PUE.
- Eau consommée m3, eau prélevée m3 (à distinguer), WUE, stress hydrique local ; ERF et REF avec périmètre UE [S14].
- Température, coût énergétique, pertes UPS, système de refroidissement, capacité de refroidissement.
- Sources : exploitant DCIM/BMS, compteurs, métriques publiques de fournisseur quand disponibles.

## Niveau IT
- Énergie GPU/CPU/serveur **mesurée** ; approximation kWh GPU à partir des watts échantillonnés avec intervalle et couverture.
- Réseau, stockage, CPU hôtes, RAM/HBM, allocation aux charges partagées.
- Activité : heures, usage GPU, taux d'inactivité, nombre de nœuds, data bytes transfered.
- **Éviter double comptage** : si on utilise énergie serveur complète, ne pas rajouter l'énergie GPU extraite du même serveur.

## Niveau IA / service
- Type de modèle, version, précision/quantification, contexte, nombre de tokens utiles, durée, batch.
- 1 000 réponses métier validées, taux de réussite, coût par résultat, TTFT et p95/p99.
- Entraînement : essais, checkpoints abandonnés, évaluations et hyperparamètres.
- Agent : appels outils, retries, cycles sans résultat, échec et durée du workflow.
- SCI pour IA [S12] exige une frontière et une unité fonctionnelle explicites.

## Traçabilité facteur carbone
Champ obligatoire : source, zone, horodatage, résolution, unité, convention **location-based/market-based/marginale**, émissions directes ou ACV électrique, valeur observée/estimée. **Ne jamais mélanger des méthodes pour conclure un gain comparatif**.

### Reporting minimal
| KPI | Unité | Qualité |
|---|---|---|
| Énergie totale site | kWh/période | compteur ou estimée, indiqué |
| Émissions opérationnelles | kgCO2e/période | facteur/méthode/hypothèses |
| Fabrication allouée | kgCO2e/période | source et durée de vie |
| Empreinte ACV totale | kgCO2e/période | frontières et exclusions |
| PUE | ratio | date/périmètre |
| WUE | L/kWh IT ou m3/MWh IT | période/périmètre |
| Qualité et efficacité IA | kgCO2e/1 000 résultats valides | test fixé |
| Coût / efficacité | €/1 000 résultats valides | prix et période |
| Gain net d'une optimisation | Δ kgCO2e au service constant | baseline et incertitude |

## Gouvernance de la donnée
Pour chaque série : propriétaire, origine, fréquence, unités, couverture, taux de valeurs manquantes, version et durée de rétention. Versionner la configuration et les hypothèses ; ne publier aucune donnée sensible de datacenter sans autorisation.

## Source spécifique France
RTE éCO2mix [S16] : électricité française au niveau réseau national/régional, **pas** une mesure directe de la consommation d'une IA ni la composition contractuelle du cloud. Les données live sont parfois estimées puis révisées.
