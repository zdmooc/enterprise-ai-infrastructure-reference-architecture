# Green AI dans la banque et l'assurance — dossiers de choix

**Statut : PROPOSITION de référentiel d'architecture.** La consommation/empreinte exacte des banques et assureurs cités n'est pas connue publiquement.

## Questions d'architecture
1. Le service exige-t-il un LLM, un petit modèle, du ML classique, un jeu de règles ou une recherche documentaire ?
2. Quelle décision métier reste autoritaire ? Quels effets en cas de panne ou d'erreur du modèle ?
3. Où sont données, modèle, outils agentiques, métadonnées et logs ?
4. Quel coût, carbone, eau et matériel par **résultat métier validé** et non par simple prompt ?
5. Quelle part du calcul est déplaçable dans le temps ou entre régions **autorisées** ?
6. Quels arbitrages énergie/qualité/latence/résilience/souveraineté et combien d'émissions incorporées ?

## Cas comparables
| Secteur | Exemple de workload | Opportunité Green IT | Limite métier |
|---|---|---|---|
| Banque | Détection fraude paiement | Modèle ML efficace sur CPU/GPU adapté plutôt que grand LLM | Latence et prévention de fraude d'abord |
| Banque | RAG conformité documentaire | Quantification, cache et SLM pour recherche simple | Accès documentaire par droits |
| Banque | Batch scoring portefeuille | Scheduling carbon-aware dans plages permises | Fenêtre opérationnelle, données et audit |
| Assurance | Pré-tri de dossiers sinistres | Vision spécialisée, batch, modèle compact | Cas critiques sous supervision |
| Assurance | Classification contrats | SLM ou modèle discriminatif | Qualité juridique, traçabilité |
| Assurance | Aide à la gestion commerciale | Routage sur modèle dimensionné au besoin | Protection clients et confidentialité |

## Dossier décisionnel « 3 scénarios »
- A — Service privé : infrastructure et émissions incorporées allouées visibles si données disponibles, charge stable.
- B — Service cloud : facture et métriques service, empreinte fournisseur, incertitude sur hardware/allocation.
- C — Hybride : classification + routage + empreinte des deux environnements et effets réseau.

Tableaux obligatoires : TCO 3/5 ans, kgCO2e ACV avec intervalle de confiance/qualité, kWh, WUE quand disponible, délai de réponse p95, qualité sur dataset métier, garanties DORA/AI Act/RGPD, réversibilité, capacité de continuité.

## Garde-fous
Pas d'« émissions évitées » prétendues sans contrefactuel auditable ; pas de dégradation des SLO pour économiser l'énergie ; IA autonome jamais autorisée à déclencher un paiement ni à couper un dispositif critique ; pilotage humain des changements de puissance/placement en banque et assurance.

## Critères de clôture documentaire
Trois cas d'usage banque/assurance comparés, hypothèses et sources, architecture HLD, risques et contrôles, cadre ACV et recommandations conditionnelles. **Aucun CRC ou GPU n'est requis pour produire cette étude**.
