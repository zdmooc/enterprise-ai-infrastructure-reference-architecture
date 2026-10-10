# Europe et France — capacités, acteurs, souveraineté

**Date :** 2026-10-10. **Attention :** annoncés, contractualisés, en chantier et opérationnels sont quatre statuts différents.

## Europe : écosystème

**FAIT PUBLIC [S02] :** la Commission européenne indique que **19 AI Factories et 13 antennes** sont en cours de création. Ces initiatives articulent supercalcul, données, compétences et écosystème industriel.

Une AI Factory ne doit pas être assimilée à une GPU farm bancaire : l'accès, le financement, les contrôles et les workloads diffèrent. Le projet AI Gigafactories vise des installations d'un tout autre ordre de grandeur ; les projets doivent être suivis selon leurs étapes d'attribution, construction, interconnexion et mise en service.

## France : éléments à cartographier

- Filière HPC et EuroHPC, centres de calcul et recherche.
- Fournisseurs d'infrastructures cloud européens et offres de confiance.
- Développeurs de modèles et intégrateurs.
- Sites et projets de datacenters ; distinguer puissance électrique réservée, raccordée, IT installée et usage actif.
- Contraintes territoriales : énergie, eau, foncier, réseaux, acceptabilité, délais de livraison.

**À documenter lors d'une itération future :** tableau fournisseur/service/région/GPU disponibles/contrat/DPA/réversibilité/date de vérification. Aucune capacité fournisseur n'est affirmée sans source récente.

## Matrice de souveraineté

| Dimension | Question | Preuve attendue |
|---|---|---|
| Résidence | Où vont prompt, contexte, journaux, embedding, sauvegardes ? | DPA, architecture des flux |
| Juridique | Qui est soumis à quelle loi et à quels accès ? | Contrat, analyse juridique |
| Opérationnelle | Qui peut administrer, suspendre ou accéder au service ? | IAM, contrôle des accès, audits |
| Technique | Où résident composants, modèles, firmware, dépendances ? | SBOM, architecture, chaîne de support |
| Réversibilité | Peut-on exporter données, embeddings, modèles, évaluations ? | Test d'export, délais, coûts |
| Continuité | Existe-t-il un repli approuvé ? | RTO/RPO issu BIA, exercice |

**FAIT PUBLIC [S07] :** SecNumCloud qualifie des offres/services sur un périmètre précis, non une entreprise dans tous ses services. Une offre « en cours de qualification » n'est pas qualifiée. La qualification de l'hébergeur ne garantit pas la sécurité de l'application hébergée.

## Décision d'architecture

Le lieu d'exécution ne doit pas être uniquement fondé sur la localisation du datacenter. Le [modèle de placement hybride](../../adrs/ADR-0002-hybrid-placement.md) exige classification des données, criticité, capacité de contrôle, latence, coût et réversibilité.

## Sources

[S02] Commission AI Factories ; [S07] ANSSI SecNumCloud, voir [registre](../09-strategy/sources-register.md).
