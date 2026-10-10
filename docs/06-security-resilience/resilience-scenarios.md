# Résilience IA — scénarios et protocole d'exercice

**Statut :** plan de tests, aucune exécution affirmée. Les paramètres RTO/RPO doivent provenir d'une BIA approuvée.

## Analyse préliminaire de panne

| Défaillance | Effet probable | Stratégie candidate | Preuve |
|---|---|---|---|
| GPU indisponible | Requêtes rejetées ou retardées | Répliquer, replanifier, admission control | Injecter panne GPU/nœud |
| Serveur d'inférence saturé | p95 et files d'attente dégradés | Quotas, limites, autoscaling sous budget | Charge progressive |
| Modèle corrompu | Erreurs / sorties incohérentes | Checksum, immutable registry, rollback | Artefact falsifié refusé |
| Vector DB indisponible | RAG incomplet | Fail closed si contexte obligatoire | Arrêter index |
| Fournisseur IA externe HS | Requêtes inabouties | Circuit breaker, mode dégradé local approuvé | Injecter 5xx/timeout |
| Région cloud perdue | Rupture de service | Site alternatif autorisé par politique | Simulation région |
| Identité et secrets indisponibles | Accès bloqué | Cache prudent, rotation, break-glass audité | Défaillance IAM simulée |
| Agent interrompu après action | Risque de double traitement | Saga/checkpoint, idempotency key, statut métier | Coupure après étape |
| Fuite transversale | Exposition de données | ACL, isolation tenant, DLP, coupure d'outil | Test non autorisé |

## Principe de repli

**Jamais de fallback silencieux** depuis un modèle privé vers un service public si la classification de l'information ou le contrat ne l'autorise pas. Une panne doit conduire à un refus sûr, une dégradation explicite ou un repli validé.

## Protocole générique

1. Définir SLO, charge et jeu d'évaluation métier.
2. Capturer l'état initial : versions, topologie, coût, taux d'erreur, p95, stockage et mémoire GPU.
3. Exécuter un événement contrôlé, horodaté ; protéger les systèmes hors laboratoire.
4. Observer alertes, propagation, admissions, circuit breaker et reprise.
5. Vérifier intégrité métier, journal des agents, duplications, absence de fuite et coût.
6. Revenir à l'état stable ; consigner les écarts, le RTO constaté et preuves.

## Agence de paiement et agent IA

L'IA formule une recommandation ou une demande contrôlée ; le système de paiement applique les règles métier et ses états. En cas d'interruption, une même intention doit être reprise **sans double paiement**. Tester notamment : coupure avant/après confirmation, timeout ambigu, répétition du message, rollback interdit après effet externe.

## Critères de clôture

Rapport comprenant risques restants, versions, résultat attendu/obtenu, SLO mesurés, observation client, journal sans données sensibles, ticket de correction et décision formelle. Sans preuve : statut **NON VALIDÉ**.
