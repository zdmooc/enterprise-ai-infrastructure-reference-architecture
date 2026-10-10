# L'IA au service des infrastructures IA durables : technologies et cas d'usage

**Question de recherche :** quels systèmes d'IA et de décision peuvent optimiser énergie, carbone, ressources, coût et qualité de service des infrastructures IA ?

**Ce document est un catalogue d'options et de méthodes d'évaluation**, pas la preuve de gains sur nos propres infrastructures.

## Types d'IA

| Approche | Exemple technique | Décision possible | Risque à traiter |
|---|---|---|---|
| Prévision séries temporelles | XGBoost/LightGBM, modèles statistiques, réseaux selon valeur démontrée | Anticiper charge, GPU demandés, énergie | Prévisions fausses en pic |
| Détection d'anomalies | Isolation Forest, détection statistique | Identifier GPU inactif, cooling inefficace, dérive électrique | Alertes intempestives |
| Optimisation sous contraintes | MILP, heuristiques, solveur multiobjectif | Consolidation placement, allocation GPU, capacité | Pas d'action sans SLO/contraintes |
| Apprentissage par renforcement | Contrôle RL uniquement en simulation puis validations sûres | Ajuster refroidissement et régulation | Dérive, surchauffe, risques physiques |
| Prédiction carbone | Modèle de prévision intensité + données réseau | Décaler batch/training dans le temps autorisé | Intensité prévue ≠ intensité observée |
| Routage intelligent de modèles | Classificateur léger/règles + évaluations | Orienter requête vers SLM/LLM/CPU selon difficulté | Baisse de qualité, biais, confidentialité |
| Autoscaling prédictif | Modèle de demande + politiques et quotas | Pré-dimensionner serving GPU | Scale-in trop agressif, load time |
| Optimisation paramétrique | Bayesian optimization, recherche hyperparamètres | Ajuster batch/quantification/cache/precision | Changement silencieux de qualité |
| Agent IA assisté | LLM + tools en lecture seule, RAG documentaire | Expliquer anomalies, conseiller opérateur | Hallucination et exécution non autorisée |

**L'IA n'est pas systématiquement nécessaire** : une règle de scheduler, le power-capping, le right-sizing ou une meilleure instrumentation peuvent avoir un meilleur ratio bénéfice/coût/carbone qu'un agent LLM.

## Six cas d'usage à analyser dans l'étude

### G1 — Optimisation du refroidissement
Données : températures entrée/sortie, débit et température eau, météo, puissance IT, consignes et alertes. Comparatif : contrôle existant vs optimiseur ML/RL. Garde-fous : limites physiques, override manuel, simulation, vérification indépendante. **FAIT PUBLIC [S17] :** DeepMind a annoncé jusqu'à 40 % d'économie **sur l'énergie de refroidissement**, dans une étude de ses datacenters, en 2016. **Ne pas généraliser ce taux ni le convertir en économie totale site.**

### G2 — Prévision de charge et right-sizing GPU
Données : profils horaires de requêtes, tokens entrants/sortants, durée, KV cache, consommation GPU/CPU, taux de rejet. Mesures : taux d'utilisation, énergie site, p95, erreurs, coût, charge non servie. Comparer modèle de prévision vs règles simples.

### G3 — Ordonnancement carbon-aware
Données : intensité carbone localisée *observée / prévue*, contraintes calendrier, souveraineté, réseau, deadlines. Activer uniquement sur tâches différables (préprocessing, entraînement, indexation, batch inference). Exclure paiement temps réel et toute tâche à contrainte de disponibilité stricte. Carbon Aware SDK [S18] documente un mécanisme temporel/géographique ; la validité du fournisseur de signal et les émissions réellement évitées restent à démontrer.

### G4 — Routeur intelligent vers les modèles sobres
Données : difficulté des requêtes, taux de réussite, confidentialité, coût, Wh/1 000 réponses valides, p95. Routes : règles/no-LLM → modèle ML spécialisé → petit modèle → grand modèle. Un grand modèle peut rester requis pour sécurité/qualité ; **ne pas optimiser la consommation au prix d'une mauvaise décision métier**.

### G5 — Maintenance prédictive
Données : erreurs GPU/ECC, thermiques, ventilation, pannes et consommation. ML de détection ou séries temporelles. Vérifier détection précoce vs faux positifs et coûts induits. Remplacement inutile prématuré = impact matériel supplémentaire.

### G6 — Assistant GreenOps
Un LLM/RAG peut expliquer des factures, rapprocher mesures et méthodes, suggérer des ADR. **Pas d'écriture autonome** dans BMS/DCIM, alimentation, ordonnanceur critique ou contrôle des transactions sans approbation explicite et contrôles déterministes. Mesurer l'empreinte de l'assistant.

## Architecture de contrôle proposée

[Diagramme Mermaid](../../diagrams/green-ai-control-plane.mmd) : télémétrie énergie + matériel + IT + météo + réseau → consolidation et qualité des données → prévisions / optimisation / règles → politique DORA/sécurité/SLO → simulation et validation humaine → actions approuvées → mesures avant-après et audit.

## Protocole d'évaluation rigoureux

1. Décrire une situation de référence **sans IA** (même service, même charge, même région/météo ou correction).
2. Choisir une unité de performance utile et les contraintes (p95, disponibilité, qualité, température).
3. Évaluer l'optimiseur sur données tenues à l'écart et cas extrêmes ; comparer avec une heuristique/règle.
4. Quantifier le coût énergétique et matériel de l'optimiseur lui-même.
5. Recalculer énergie, émissions et eau **nettes** sur frontières équivalentes.
6. Séparer résultat *modélisé*, *expérimental*, *déployé et mesuré* et *source tierce*.
7. Détecter rebond : augmentation de demandes ou puissance liée à l'amélioration d'efficacité.
8. Refuser toute conclusion de réduction carbone lorsque les données de référence manquent.

## Secteurs critiques

**Banque :** ne jamais reporter ou dégrader une opération de paiement critique pour réduire l'empreinte. Évaluer plutôt batch, indexation, environnement d'expérimentation ou serving non critique, sous classification/contrats.

**Assurance :** privilégier traitements documentaires batch, scoring hors chaîne urgente et RAG interne en horaires flexibles, sous contrôle des SLA et confidentialité. Les flux sinistres urgents ont leur propre BIA.

## Sources de travail
[S12] SCI for AI, [S13] ADEME, [S17] DeepMind, [S18] Carbon Aware SDK, [S19] Hugging Face AI Energy Score ; [registre](../09-strategy/sources-register.md).
