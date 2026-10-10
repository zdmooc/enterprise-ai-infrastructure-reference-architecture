# Feuille de route des laboratoires IA Infrastructure

**Statut initial : 0/6 labs exécutés.** Les critères ci-dessous ne valent pas certification de sécurité ou de conformité.

## Protocole partagé

Pour chaque expérience : dépôt et commit, date, plateforme, versions, commandes, ressource GPU/CPU, configuration anonymisée, sorties horodatées, mesures brutes, comparaison avant/après, difficultés, retour arrière, verdict.

| ID | Objectif | Pré-requis | Validation attendue |
|---|---|---|---|
| L1 | Gateway, routage, politiques sans GPU | Docker/Kind ou OpenShift CPU | Deux backends simulés ; routage correct, refus d'une région interdite |
| L2 | Model serving GPU sur OCP / KServe / vLLM | Accès GPU, matrice versions | Modèle chargé, métriques TTFT/p95, rollback |
| L3 | Multi-tenancy et isolation données | Deux namespaces/tenants et datasets factices | Tests d'accès croisés négatifs, logs expurgés |
| L4 | Agent outillé et actions sensibles | API métier simulée, idempotence | Refus action interdite, ré-exécution sans doublon, approbation |
| L5 | Chaîne LLMOps GitOps | Registry, CI, GitOps | Signature/contrôle hash, scan, drift et rollback reproductibles |
| L6 | Chaos + FinOps + Green IT | Métrologie et injection de pannes | Mesures avant/après, saturation, coût/token, bilan électrique |

## L1 — Design détaillé

Interface commune REST ; backend A/B = mocks déterministes ; policy par classification PUBLIC / INTERNE / RESTREINT ; quotas par tenant ; timeouts ; circuit breaker ; IDs de corrélation et logs sans prompt.

**Cas de tests :** public accepté sur A/B ; restreint refusé sur backend cloud non autorisé ; quota dépassé -> 429 ; backend indisponible -> statut explicite ; aucun repli non autorisé ; aucune opération d'état métier sans approbation.

## L2 — Matrice matérielle

Documenter modèle GPU, quantité VRAM, driver, CUDA/ROCm, opérateur, OpenShift version, version KServe/vLLM, mémoire par requête. Une démo CPU ou mock **ne prouve pas** une capacité GPU.

## L4 — Précautions financières

Utiliser une API bancaire simulée uniquement ; aucun compte bancaire ou système réel. Tester transaction avec idempotency-key stable, validation du statut métier, reprise après timeout et audit de l'agent.

## Livrables par lab

README du lab, diagramme, prérequis, scripts, tests, sortie brutes **sans données sensibles**, preuves horodatées, tableau attendus/observés, décision et liens ADR.

## Gouvernance

Le lab passe « VALIDÉ » seulement si les assertions critiques sont appuyées par des sorties reproductibles ; à défaut, « PLANIFIÉ », « BLOQUÉ » ou « ÉCHEC ».
