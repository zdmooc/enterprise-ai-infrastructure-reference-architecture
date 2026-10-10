# ADR-0002 — Placement IA guidé par la classification et le risque

**Date :** 2026-10-10
**Statut :** PROPOSED (non validé par un client ou comité)

## Question
Exécuter les modèles en cluster privé, cloud européen, cloud hyperscaler ou edge ?

## Proposition
Adopter un portefeuille hybride et décider par workload. **La politique de données prime sur l'optimisation coût/latence.**

## Critères dans l'ordre
1. Autorisation légale, confidentialité, politique de donnée et résidence.
2. Criticité, dépendances, SLO issu de la BIA.
3. Disponibilité technique du modèle et de l'accélérateur.
4. Audit, sécurité, qualité et contrôle fournisseur.
5. TCO, coût/token utile, énergie/carbone et délais.
6. Réversibilité, portabilité et capacité de reprise.

## Options
- **Privé** : contrôle direct ; coût fixe et ressources finies.
- **Cloud européen** : capacité externe, contrôles contractuels à valider pour l'offre précise.
- **Cloud hyperscaler** : catalogue et élasticité, risques de sortie et juridiques à examiner.
- **Edge/CPU** : confidentialité/latence sous conditions, calcul limité.
- **Sans LLM** : règles ou modèle de ML classique, souvent adapté aux chaînes transactionnelles.

## Invariant
Un routeur ne peut **jamais** relâcher la politique de placement lors d'une panne. Fail-closed ou fallback uniquement vers une cible pré-approuvée.

## Preuve avant ACCEPTED
Matrice de classification, BIA, évaluation des offres, test de routage négatif, coûts comparables, protocole PRA et décision risques/conformité.
