# I13 — Dossier d'aide au choix : Plateforme IA hybride, banque et assurance

**Usage** : support direction d'architecture. **Toutes les architectures sont proposées, non des installations existantes.** Aucun tarif ni carbone constructeur non vérifié.

## Décision demandée à un comité
Choisir **quels types de charges IA** peuvent aller sur des environnements privés, clouds européens, hyperscalers, HPC ou CPU — et quelles preuves exigées avant mise en production.

## Hypothèses de travail à confirmer
Cas A : Assistant documentaire bancaire et de conformité, données classifiées, nombreux utilisateurs, p95 défini par métier.  
Cas B : Traitement documentaire assurance et pré-tri sinistres, décision finale humaine, données sensibles.  
Cas C : Détection de fraude paiements — moteur déterministe/ML sous p99 strict ; IA générative éventuellement **hors chaîne transactionnelle**.

## Options à comparer
| Option | Atout | Risque/limite | Décision possible |
|---|---|---|---|
| S0 — sans LLM/GPU | Simplicité, efficience, auditabilité | Couverture fonctionnelle limitée | Base incontournable sur fraude/règles |
| S1 — privé GPU/CPU | Contrôle et capacité réservée | CAPEX, renouvellement, underutilization | Candidate aux données sensibles et charge stable |
| S2 — cloud européen admissible | Elasticité/contrat local selon service | Conformité à documenter, variations offre | Candidate si contrat + contrôles validés |
| S3 — hyperscaler GPU/managé | Catalogue et capacité, expertise | Concentration, coûts, dépendances et données | Candidate pour traitements autorisés |
| S4 — hybride routeur | Placement workload par risque, modèle et qualité | Complexité et gouvernance élevée | **Orientation proposée à approfondir**, pas choix automatique |
| S5 — HPC/AI Factory | Accès calcul avancé selon programme | Pas une plateforme d'inférence financière standard | Recherche/expérimentation autorisées |

## Analyse multicritère sans « chiffres fabriqués »
| Critère / preuve | S0 | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|
| Confidentialité et résidence | à valider données locales | dépend lieu/ops | contrat précis | contrat précis | politique routage |
| DORA tiers/concentration | peu de tiers IA | fournisseur HW/support | fournisseur service | fournisseur service | pluralité + dépendances |
| AI Act / RGPD | selon traitement | selon cas d'usage | selon cas + contrat | selon cas + contrat | audit par route |
| RTO/RPO | BIA | test privé | test fournisseur | test fournisseur | exercice de bout en bout |
| Coût TCO | CPU/ops | CAPEX + OPEX | GPUh + frais | GPUh + frais | cumuls + gateway |
| Fabrication/ACV | HW CPU local | HW dédié amorti | ACV fournisseur à requérir | ACV fournisseur à requérir | mesurer composants répartis |
| Eau/PUE | datacenter sous-jacent | mesurés site si accès | réclamer données | réclamer données | métriques par route |
| Qualité métier | vérifier adéquation | modèle validé | modèle validé | modèle validé | validation tout routage |

## Préconisations conditionnelles
**Pour A** : explorer S4 avec règle *sensible → S1/S2 admissible*, et S0/SLM pour simples requêtes. Si preuve cloud absente, limiter au privé autorisé.  
**Pour B** : comparer OCR/ML spécialisé + RAG/SLM à un grand LLM ; gating qualité/validation humaine et données santé le cas échéant.  
**Pour C** : démarrer S0/ML spécifique hors LLM ; réserver la génération aux explications ou analyses différées, jamais comme unique transaction processor.

## Décision Green IT
Choix validé seulement si carbone opérationnel + fabrication allouée, eau quand disponible, qualité, coût et SLO sont présentés conjointement. Relever données absentes : ne pas transformer « non publié » en « zéro ». Ne pas appliquer carbon-aware scheduling à une obligation critique.

## Actions nécessaires pour un arbitrage réel
1. BIA et classification des trois cas par métier/RSSI/risques.
2. Fournisseur/contrat/région/qualifications et capacité réellement disponible.
3. Jeu d'évaluation de qualité et workloads volumétriques **anonymisés**.
4. Trois chiffrages fournisseurs et une baseline CPU/SLM, méthode commune.
5. Inventaire émissions incorporées/E IT/PUE/WUE/facteur daté avec bornes.
6. Exercice panne et test repli sans fuite ni double opération.
7. Comité décideur : arbitrage signé, risques résiduels et réexamen.

## Conclusion direction
**Décision proposée : autoriser une étude comparative S0/S1/S2/S3/S4 plutôt qu'acheter des GPU ou choisir un cloud aujourd'hui.** Chaque charge recevra sa cible après preuve de conformité, performance, coût, réversibilité et bilan environnemental.  
Aucun scénario ne garantit à lui seul conformité, économie ou souveraineté.
