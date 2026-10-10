# Enterprise AI Infrastructure — Reference Architecture

> Référentiel public d'architecture technique, études de marché, scénarios 2026–2030 et laboratoires pour les infrastructures IA d'entreprise — focus Europe, France, banque et assurance.

**Version :** 1.0.0-documentaire · **Date de référence :** 2026-10-10 · **Statut :** 14/14 études documentaires publiées ; évaluations physiques et prix contractuels non validés

## Mission

Documenter et évaluer les infrastructures IA, des serveurs GPU aux plateformes d'inférence d'entreprise : accélérateurs, datacenters, énergie, réseaux, stockage, cloud et souveraineté, Kubernetes/OpenShift AI, MLOps/LLMOps, sécurité, résilience, FinOps et Green IT.

L'objectif n'est **pas** de reproduire une architecture interne d'établissement financier, ni de présenter des preuves de déploiement inexistantes. Les exemples de banques/assurances reposent uniquement sur des annonces publiques ; la cible proposée est une **architecture de référence indépendante**.

## Principes du périmètre

**Ce dépôt est une étude mondiale d'architectures d'infrastructures IA que nous ne possédons pas.** Aucun OpenShift CRC, serveur privé ou GPU personnel n'est nécessaire à la V1.0 documentaire. Les laboratoires demeurent des annexes facultatives, sans condition de clôture. Le Green IT et l'empreinte carbone sur le cycle de vie sont **un fil conducteur de toutes les comparaisons**, non un sujet périphérique.

## Démarrage rapide — V1.0 documentaire

- [Synthèse exécutive banque, assurance, Europe et Green IT](reports/V1.0-EXECUTIVE-SUMMARY.md)
- [Audit V1.0 : couverture, preuves, limites](studies/I14-final-audit.md)
- [Les 14 itérations livrées](studies/README.md)
- [Dossier décisionnel banque/assurance](studies/I13-architecture-decision-banking-insurance.md)
- [Calculateur carbone transparent et exemple *entièrement fictif*](tools/estimate_lca.py) — utilisable sans cloud, GPU ou CRC.
- [Versionnement et historique](CHANGELOG.md)

La version **1.0 documentaire** signifie : étude et architecture de référence rédigées et sourcées. Elle ne signifie **pas** benchmark réel, mesure carbone mesurée, SLA, capacité cloud réservée ou conformité certifiée.

## Lire le référentiel

| Domaine | Document |
| --- | --- |
| Doctrine & qualité des sources | [Méthode](docs/00-governance/methodology.md) |
| Monde 2026–2030 | [Panorama global](docs/01-global/global-landscape.md) |
| Europe & France | [Capacités et souveraineté](docs/02-europe-france/europe-france.md) |
| GPU & datacenters | [Infrastructure physique](docs/03-hardware/gpu-datacenter.md) |
| Architecture de référence | [Enterprise AI Platform](docs/04-platform/reference-architecture.md) |
| Banque & assurance | [Besoins sectoriels](docs/05-finance/banking-insurance.md) |
| Sécurité & réglementation | [Contrôles](docs/06-security-resilience/regulatory-controls.md) |
| PRA & continuité | [Scénarios de résilience](docs/06-security-resilience/resilience-scenarios.md) |
| TCO, coût d'inférence, énergie | [FinOps](docs/07-finops-green-it/economics.md) |
| Green IT / ACV des infrastructures IA | [Empreinte environnementale](docs/07-finops-green-it/lifecycle-environmental-footprint.md) |
| IA pour diminuer l'empreinte | [AI for Sustainable Datacenters](docs/07-finops-green-it/ai-for-sustainable-datacenters.md) |
| Énergie, carbone, eau, données | [Plan de mesure](docs/07-finops-green-it/measurement-and-kpis.md) |
| Green AI banque / assurance | [Dossiers de choix](docs/07-finops-green-it/banking-insurance-green-ai.md) |
| POC démontrables | [Parcours de laboratoires](docs/08-labs/lab-roadmap.md) |
| Scénarios & jalons | [Feuille de route](docs/09-strategy/roadmap-2026-2030.md) |
| Sources datées | [Registre des sources](docs/09-strategy/sources-register.md) |
| Décisions | [ADR-0001](adrs/ADR-0001-scope.md) · [ADR-0002](adrs/ADR-0002-hybrid-placement.md) · [ADR-0003](adrs/ADR-0003-carbon-boundary.md) · [ADR-0004](adrs/ADR-0004-green-ai-safety.md) · [ADR-0005](adrs/ADR-0005-financial-infrastructure-decision.md) |

## Architecture logique

[Diagramme Mermaid source](diagrams/enterprise-ai-platform.mmd) : applications métier → AI Gateway → contrôle d'accès → orchestration d'agents / RAG → routeur de modèles → inférence privée ou cloud autorisé, avec observabilité, gouvernance et FinOps transverses.

Le GPU n'est qu'une composante. Le périmètre inclut également **les alternatives CPU/ASIC** et le *droit de ne pas utiliser de LLM* quand un modèle classique répond mieux au besoin métier.

## Questions d'architecture centrales

1. Quelles charges doivent être exécutées en datacenter privé, cloud européen, cloud hyperscaler ou en périphérie ?
2. Comment dimensionner la mémoire, les accélérateurs, les réseaux, le stockage et l'énergie ?
3. Comment isoler équipes, données, modèles et agents dans une plateforme partagée ?
4. Comment prouver disponibilité, traçabilité, sécurité et réversibilité dans une institution financière ?
5. Quels arbitrages coût / tokens utiles / latence p95 / qualité / carbone ?
6. Quel niveau de souveraineté **juridique, opérationnelle, technique et contractuelle** est réellement obtenu ?

## Principes de preuve

Les assertions utilisent les marqueurs suivants :
- **FAIT PUBLIC** : source publique primaire datée, vérifiable ;
- **PROJECTION SOURCE** : scénario d'un organisme cité, pas un fait établi ;
- **HYPOTHÈSE / PROPOSITION** : conception interne à valider ;
- **LAB VALIDÉ** : reproductible avec commande, environnement, résultats et preuve archivée ; aucun lab n'a encore ce statut.

Les estimations 2030 ne sont pas des certitudes, et les coûts ne doivent jamais être présentés hors date, région, unité, taxes et hypothèses de consommation. Voir [méthodologie](docs/00-governance/methodology.md).

## Green IT et Green AI dans chaque comparaison

- **Empreinte complète :** extraction / fabrication GPU et serveurs, fonctionnement IT et refroidissement, eau, réseau, datacenter, allongement de vie, fin de vie et incertitudes.
- **Méthodes :** ACV, SCI for AI, PUE, WUE, ERF, émissions scopes 1/2/3 selon entité, indicateurs par **résultat utile** et non par prompt brut.
- **Optimisation par IA :** prévisions énergie/charge, anomaly detection, cooling ML/RL avec garde-fous, placement carbon-aware, routage de petits/grands modèles, agents GreenOps conseillers.
- **Exigence anti-greenwashing :** gains nets après énergie dépensée par l'optimiseur ; jamais de pourcentages extrapolés sans mesure, pas d'émissions évitées compensant artificiellement l'inventaire.

[Diagramme Green AI](diagrams/green-ai-control-plane.mmd) · [14 itérations documentaires V1.0 achevées](docs/09-strategy/roadmap-2026-2030.md)

## Laboratoires (annexes facultatives pour une V2 expérimentale, non bloquantes)

- L1 : gateway et routage de deux modèles factices **sans GPU** ;
- L2 : inférence réelle OpenShift AI / KServe / vLLM **si GPU disponible** ;
- L3 : confidentialité, RBAC, quotas et séparation des tenants ;
- L4 : défaillance d'inférence, circuit breaker, audit agentique ;
- L5 : mesures p95, débit, coût / 1 M tokens et consommation.

**Les expériences ne font pas partie du critère de clôture V1.0 documentaire. Aucun cluster, GPU, coût ni scénario de résilience n'est déclaré testé sur infrastructure réelle.**

## Sources de départ

- [AIE — Energy and AI (2025)](https://www.iea.org/reports/energy-and-ai)
- [Commission européenne — AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories)
- [EIOPA — Scaling AI in finance (2026)](https://www.eiopa.europa.eu/publications/scaling-ai-finance-systemic-risks-resilience-and-european-sovereignty_en)
- [ESMA — DORA](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora)
- [Commission européenne — AI Act, article 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)
- [ANSSI — SecNumCloud](https://cyber.gouv.fr/enjeux-technologiques/cloud/)

## Relation avec d'autres travaux

Ce dépôt conserve la doctrine transverse. Les implémentations multicloud, projets métier, travaux agentiques et déploiements OpenShift de l'écosystème restent dans leurs dépôts respectifs ; ici figurent seulement les références d'architecture et les interfaces contractuelles, sans dupliquer leur code.

**Langue de référence :** français, avec les termes techniques anglais usuels. **Licence :** non spécifiée à ce stade.
