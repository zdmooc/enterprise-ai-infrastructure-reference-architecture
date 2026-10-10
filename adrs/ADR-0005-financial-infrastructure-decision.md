# ADR-0005 — Choix de placement Enterprise AI banque/assurance

**Date :** 2026-10-10. **Statut : PROPOSED (pas de comité décideur réel)**.

## Décision proposée
Placer les charges IA selon politique combinant classification/contrats, BIA/résilience, adéquation du modèle et coût/empreinte ACV. Étudier les options sans LLM, privé, cloud européen, hyperscaler et hybride plutôt que sélectionner un fournisseur à l'avance.

## Critères
1. Sécurité et exigences légales/contractuelles, non négociables.
2. Qualité métier et supervision humaine appropriée.
3. Latence, disponibilité, PRA/exit plan.
4. Coût sur durée de vie et données fournisseurs datées.
5. Carbon intensity par résultat **valide**, empreinte incorporée et eau.

## Scénarios
A assistant banque sensible ; B assurance documentaire ; C fraude temps réel sans LLM critique. Voir [I13](../studies/I13-architecture-decision-banking-insurance.md).

## Statut de preuve
**Proposition documentaire** uniquement. Aucune donnée client, mesure réelle, homologation, prix, test de cluster ou conformité certifiée.

## Clôture de décision
Exige BIA, contrats et SLA, workloads représentatifs, évaluation de qualité, TCO et ACV validés, sign-off.