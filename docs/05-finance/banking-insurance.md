# Banque et assurance — cas d'usage et contraintes

**État des observations : 2026-10-10.** Les exemples ci-dessous sont issus de communications publiques et **ne dévoilent aucune architecture interne non publiée**.

## Preuves sectorielles publiques

| Établissement | Déclaration publique | Ce que cela permet d'inférer, et ce que cela ne prouve pas |
|---|---|---|
| BNP Paribas | LLM-as-a-Service mutualisé sur GPU dans les datacenters du Groupe [S08] | Existence déclarée d'une offre GPU interne ; pas de nombre de GPU, RTO, ni TCO public |
| Groupe BPCE | MAiA : assistants métier et plus de deux millions de prompts/mois annoncés [S11] | Adoption et besoin d'accès aux modèles ; topologie GPU et routage non publics |
| AXA | Global AI Hub annoncé pour agents multi-entités, contrôle et FinOps [S09] | Plateforme agentique mutualisée ; stack matériel, coût et SLA non détaillés |
| EIOPA | Enquête 2026 : 347 assureurs, 25 pays, adoption GenAI largement encore en POC [S04] | Signal sectoriel, pas équivalent à généralisation en production |

## Domaines métier

| Domaine | Approche à évaluer | Point d'architecture |
|---|---|---|
| Fraude paiement | Modèles ML classiques + explication assistée | La décision temps réel ne doit pas dépendre d'un LLM génératif |
| LCB-FT | Graph analytics, NLP, ML, RAG | Justification et chaîne de preuve |
| Crédit | Modèles spécialisés et contrôles humains | Risques et règles AI Act selon l'usage |
| Service client banque | RAG et assistants | Limitation des données et contrôles d'accès |
| Sinistres assurance | Vision/documents/agents | Contrôle des règlements et validation |
| Souscription | Modèles de risque et génération | Encadrement des biais et explication |
| IT Operations | Agents de diagnostic | Accès lecture seule par défaut |

## Découplage vital : IA et transaction

Pour paiements, ordres et indemnisation, une réponse LLM n'est **pas** l'état transactionnel. Les ordres restent validés par le système métier et ses règles. Pour l'agent :
- allowlist d'outils, permissions minimales, identité technique unique et traçable ;
- séparation « conseil » / « demande » / « exécution » ;
- idempotence, anti-rejeu et contrôle anti-double opération ;
- approbation humaine en fonction du niveau de risque ;
- arrêt sûr si le modèle, le retrieval ou la gateway sont indisponibles.

## Due diligence fournisseur

Évaluer contrat, concentration, sous-traitants, localisation, logs, droits d'audit, fin du service, migration des embeddings, export du catalogue de modèles, gestion d'incident et supervision. DORA [S05] doit être examiné au regard du périmètre effectif des entités et de leurs prestataires.

## Livrables pour un dossier de choix

Contexte et BIA, cartographie de flux, classification des données, architecture logique/physique, scénarios hybride/privé/managé, matrice de contrôles, chiffrage TCO avec fourchettes, exercice de continuité, risques résiduels, décision formelle.

**Sources :** [registre](../09-strategy/sources-register.md) [S04], [S05], [S08], [S09], [S11].
