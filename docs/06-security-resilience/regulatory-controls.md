# IA, sécurité, réglementation et gouvernance

**Statut :** grille d'ingénierie à adapter ; n'est ni un avis juridique ni une attestation de conformité.

## Textes applicables / référentiels

- **DORA [S05] :** applicable depuis le 17 janvier 2025 aux entités financières de son champ ; implique gestion des risques TIC, incidents, résilience et prestataires.
- **AI Act [S06] :** application progressive ; selon l'article 113 consolidé, les obligations des catégories de systèmes à haut risque de l'annexe III doivent s'appliquer à partir du 2 décembre 2027. Les obligations et exceptions doivent être évaluées **par système**.
- **RGPD :** base légale, minimisation, finalité, sécurité, durées de conservation, transferts et droits.
- **ANSSI SecNumCloud [S07] :** qualification de **services** dans un périmètre précis, pas certification générale de toute application hébergée.

## Matrice de contrôle de référence

| Risque | Contrôle technique | Preuve attendue |
|---|---|---|
| Prompt/response divulgués | Classement, DLP, chiffrement, politique de journalisation | Test d'exfiltration, trace expurgée |
| Accès multi-tenant | IAM, namespace, network policy, autorisation côté retrieval | Test négatif inter-tenant |
| RAG contaminé | Provenance documentaire, ACL au retrieval, filtre de sources | Tests adversariaux |
| Agent trop privilégié | Outils approuvés, scopes, validation humaine, limites budget | Essais de refus et journal action |
| Modèle compromis | Signature/hash, provenance, scan images, contrôle registre | Attestations d'artefacts |
| Indisponibilité GPU | Répliques, capacité, mode dégradé autorisé | Rapport d'exercice |
| Dépendance fournisseur | Exit plan, inventaire de sous-traitants, transfert données | Test d'export de données et modèles |
| Risque AI Act | Inventaire des systèmes, classification, documentation, supervision | Fiche d'évaluation et registre |
| Dérapage financier | Plafonds tokens, quotas, budget, anomalies | Dashboard et preuve de blocage |

## Tests de sécurité minimum

Jeux de tests d'injection directe/indirecte ; demande d'accès interdit ; tentative de sortie vers un outil non approuvé ; demande de secrets ; changement de tenant ; modèle/région non autorisé ; surcharge/DoS logique ; rejeu d'action sensible.

## Séparation des responsabilités

Le fournisseur du modèle, l'exploitant de la plateforme, le propriétaire des données, l'application métier et le responsable de conformité n'ont pas nécessairement les mêmes rôles et obligations. Documenter la matrice RACI et le partage contractuel.

## Gate « prêt pour la production »

Inventaire modèle/données validé ; BIA et SLO approuvés ; droits et secrets vérifiés ; logs et rétention conformes ; évaluation fonctionnelle et sécurité ; test de reprise ; plan de repli ; réversibilité ; approbation métiers, RSSI, risques et conformité selon organisation.

**Sources :** [S05], [S06], [S07] du [registre](../09-strategy/sources-register.md).
