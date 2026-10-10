# I03 — Europe et France : fiches infrastructures, souveraineté et statut

**Date** : 2026-10-10. Projets **annoncés** ≠ **contractualisés** ≠ **livrés** ≠ **disponibles commercialement**.

## Cadre européen confirmé
Commission européenne [F] : **19 AI Factories et 13 antennes en cours de création**, dont **AI2F (France)** ; elles mettent en relation calcul EuroHPC, recherche, PME, compétences et industrie. [Liste officielle](https://digital-strategy.ec.europa.eu/en/policies/ai-factories). Une AI Factory n'est ni une région GPU publique disponible à tous prix, ni une qualification SecNumCloud.

Les **AI Gigafactories** se situent à un autre ordre de grandeur : initiative européenne visant des installations comportant **plus de 100 000 processeurs IA avancés** par installation selon la présentation de la Commission ; **cible de politique publique**, pas constat d'infrastructures installées. [Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-factories).

## Exemples EuroHPC (liste de programmes, non inventaire de capacité)
| Pays | Initiative publiée | Statut que l'on peut soutenir |
|---|---|---|
| France | AI2F | Sélectionnée / programme en création |
| Allemagne | JAIF et HammerHAI | Programmes AI Factory listés |
| Finlande | LUMI AIF | Programme listé |
| Italie | IT4LIA | Programme listé |
| Espagne | BSC AIF et 1HealthAI | Programmes listés |
| Suède | MIMER | Programme listé |
| Pays-Bas | NLAIF | Programme listé |

La carte institutionnelle et les noms évoluent ; ne pas en déduire des GPU libres ni le prix d'accès. [Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-factories).

## France : quatre typologies de fournisseurs
1. **Infrastructure publique EuroHPC** : accès sous règles/programmes ; mission recherche/startups/innovation, non substitut automatique à une plate-forme DORA.
2. **Datacenters commerciaux et colocation** : salle/puissance/rack, responsabilité matériel et logiciel à la charge contractuelle des parties.
3. **GPU cloud français/européens** : matériel géré, Kubernetes, modèle ou inférence à la demande ; souveraineté à démontrer offre par offre.
4. **Hyperscalers opérant des régions françaises** : région hébergée localement ≠ garantie de contrôle juridique et opérationnel dans tous les cas.

## Souveraineté multidimensionnelle : grille de preuve
| Question | Document probant requis |
|---|---|
| Données prompt, embeddings, journaux et backups situés où ? | DPA + flux détaillés, logs |
| Administrateurs privilégiés sous quelle juridiction ? | Contrats, accès, journal PAM |
| Service SecNumCloud réellement qualifié ? | **Nom précis** dans liste ANSSI, périmètre, date |
| Support / sous-traitants / sauvegardes / clé KMS ? | Matrice contractuelle et de responsabilités |
| Sortie d'offre, récupération des modèles et datasets ? | Test export + coût/temps |
| Electricité/CO₂/eau du traitement ? | Source métrique fournisseur, zone, date, incertitudes |

[ANSSI — prestataires qualifiés et en cours](https://cyber.gouv.fr/offre-de-service/solutions-certifiees-et-qualifiees/services-de-securite-evalue/solutions-en-cours-de-qualification/prestataires-secnumcloud/) : les deux catégories sont différentes.

## Green IT France
Pour l'électricité française, **RTE éCO2mix** calcule un indicateur d'émissions directes **par kWh produit**, qui **ne couvre pas les échanges aux interconnexions**. Ce n'est ni une ACV de l'électricité ni le facteur contractuel d'un datacenter cloud donné. [RTE](https://www.rte-france.com/donnees-publications/eco2mix-donnees-temps-reel/emissions-co2-par-kwh-produit-france).

## Approche banque/assurance
Demander les preuves de localisation, l'adéquation aux politiques métier, l'homologation d'un service précis et les droits d'audit. La sécurité, la continuité et la classification précèdent tout arbitrage climatique de placement.

### Points restant non accessibles publiquement
Nombre réel de GPU installés par banque, PUE/WUE par site bancaire, consommation énergie des modèles propriétaires, RTO/RPO contractuels non divulgués. **Non estimés** en l'absence de sources publiques fiables.