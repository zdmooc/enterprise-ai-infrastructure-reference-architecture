# ADR-0003 — Frontière de mesure environnementale IA

**Date :** 2026-10-10. **Statut : PROPOSED**.

## Problème
Comparer des configurations IA sans sous-estimer fabrication, réseau, refroidissement, eau, stockage, entraînement, requêtes rejetées et impacts de l'optimiseur.

## Proposition
Établir une ACV par service métier équivalent et rapporter séparément énergie, émissions opérationnelles et émissions incorporées allouées, WUE, TCO et métriques de qualité. Prendre SCI for AI (GSF), réglementation européenne datacenter et méthodologies ADEME comme références, en vérifiant périmètres.

## Alternatives
Coût/token seul (insuffisant) ; PUE seul (insuffisant) ; empreinte service incluant postes traçables (retenu comme cible).

## Invariants
Aucune valeur non sourcée ; frontières constantes ; impossibilité de déduire les scopes de l'entreprise du seul type d'équipement ; aucune économie revendiquée sans baseline, incertitudes et coût d'optimisation.

## Validation
Critères à revoir à I06–I07. Aucun bilan chiffré n'est validé par ce document.
