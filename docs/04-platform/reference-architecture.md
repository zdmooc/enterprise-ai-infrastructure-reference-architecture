# Enterprise AI Platform — architecture de référence

**Statut : PROPOSITION.** Aucun schéma ne représente le SI d'une entreprise existante.

## Composants

| Plan | Composants | Invariant |
|---|---|---|
| Métier | Applications paiement, crédit, sinistre, IT | Systèmes transactionnels font autorité |
| Contrôle | API Gateway, AI Gateway, IAM, WAF, quotas | Vérification de tenant, données et finalité |
| Orchestration | Workflows, agents, outils approuvés, humain | Autorisations sur chaque action |
| Données | Catalog, RAG, ACL, vector store, S3 | Retrieval filtré au droit de l'utilisateur |
| Routage | Catalogue de modèles, policy engine, routeur | Jamais de fallback vers une région non approuvée |
| Exécution | Kubernetes/OpenShift, KServe/vLLM ou service externe | Observabilité, isolation, quotas GPU |
| Cycle de vie | Registry, MLOps/LLMOps, GitOps, tests | Versions, lineage, rollback |
| Contrôle transverse | Audit, FinOps, sécurité, évaluation | Évidences et traçabilité |

Voir [diagramme source](../../diagrams/enterprise-ai-platform.mmd).

## Flux autorisé d'inférence

1. Identifier application, utilisateur, tenant et finalité du traitement.
2. Classifier données/prompt et évaluer la politique de traitement.
3. Choisir la liste **autorisée** de modèles/régions.
4. Appeler le modèle avec quotas et timeout ; enregistrer version et identifiants de corrélation.
5. Vérifier sortie selon risque ; exiger validation humaine pour actions critiques.
6. Produire journaux minimisés, métriques et facturation interne.

**Invariants de sécurité :** aucun secret dans les prompts ; pas de données personnelles dans les traces par défaut ; jetons de service éphémères ; RBAC/ABAC contrôlé côté outil ; protection des entrées et des sorties ; approbation humaine des mutations critiques.

## Chaîne de livraison

Source/artefact → scanning/supply chain → registry attesté → policy admission → GitOps → déploiement → tests → canary → observabilité → rollback. Les images, modèles et prompts sont versionnés indépendamment.

## SLO à établir par la BIA

TTFT, latence totale p95/p99, débit, refus, disponibilité, mémoire GPU saturée, délai de chargement du modèle, temps de reprise, exactitude mesurée sur évaluations métiers, incidents de sécurité, coût par million de tokens utiles.

Aucun objectif chiffré n'est imposé sans étude de charge.

## Typologie de services

- **Tier A — assistance :** réponse consultative, dégradation possible.
- **Tier B — supervision de décision :** exigence de journalisation, reprise et validation humaine.
- **Tier C — action sensible :** tool gateway, approbation conditionnelle, journal opposable si applicable, idempotence et protections contre double exécution.

Un LLM ne doit jamais être le seul garant d'une opération financière irréversible.

## Technologies possibles

Kubernetes/OpenShift, KServe, vLLM, MLflow, stockage objet, Postgres/pgvector, OpenTelemetry, Prometheus, Vault, OPA/Kyverno. **Liste d'options**, pas une prescription de produits. Les choix doivent être validés en ADR, par matrice de compatibilité et laboratoire. Red Hat documente KServe et vLLM sur OpenShift AI [S10].

## Green IT by Design (transverse)

La plateforme proposée doit intégrer la gouvernance carbone comme critère de placement **après** confidentialité, conformité et SLO. Mesurer énergie GPU/CPU, refroidissement/périmètre site, empreinte matérielle allouée et efficacité par résultat métier utile. Inclure alternatives sans LLM, petits modèles, quantification et cache lorsque la qualité ne se dégrade pas. Pour un job différable : scheduling carbon-aware seulement entre régions/horaires déjà autorisés, avec vérification des émissions nettes. Un modèle d'optimisation AI GreenOps conseille par défaut et n'écrit pas sur le BMS/DCIM/ordonnanceur critique sans contrôle humain. Voir [ACV](../07-finops-green-it/lifecycle-environmental-footprint.md), [Green AI](../07-finops-green-it/ai-for-sustainable-datacenters.md) et [ADR-0004](../../adrs/ADR-0004-green-ai-safety.md).

## Risques à traiter

Prompt injection (notamment via documents RAG), fuite multi-tenant, exfiltration par outils, compromission du registre de modèles, exhaustion GPU, dépendance fournisseur, non-déterminisme d'actions agentiques, coûts non plafonnés, dérive de modèle.

Se référer aux [contrôles réglementaires](../06-security-resilience/regulatory-controls.md), [scénarios résilience](../06-security-resilience/resilience-scenarios.md) et à [ADR-0002](../../adrs/ADR-0002-hybrid-placement.md).
