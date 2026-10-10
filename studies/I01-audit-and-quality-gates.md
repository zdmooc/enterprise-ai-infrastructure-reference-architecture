# I01 — Audit initial du référentiel et gates de qualité

**Date** : 2026-10-10 · **Statut** : analyse documentaire, aucune infrastructure testée.

## Revue de l'existant au lancement
28 fichiers sur main, dont panorama, Europe/France, hardware, architecture, finance, DORA, Green IT/Green AI, roadmap, sources, ADR et modèles CSV. Points positifs : distinction source / hypothèse / POC, gestion des alternatives « sans LLM », ACV amorcée, prudence sur les gains revendiqués.

## Lacunes concrètes relevées
1. Panorama mondial encore qualitatif : absence de comparaison structurée par région et d'un indicateur de couverture des sources.
2. Fiches matériel sans tableau homogène mémoire/bande passante/TBP/interconnexions et sans ligne explicite « performances non comparables sans benchmark identique ».
3. Différence entre simple résidence UE et souveraineté contractuelle/administrative à prouver pour chaque offre.
4. Modèles TCO/ACV trop libres : risque de double comptage et de mélange g/kg, heures, kW et unités fonctionnelles.
5. Cas banque-assurance à décliner en 3 scénarios décisionnels avec sécurité + Green IT sur la même grille.
6. Dossier final exécutif et plan de veille 2027–2030 à publier.

## Gates V1.0 documentaire
| Gate | Exigence vérifiable |
|---|---|
| G1 | Chiffre clé sourcé, daté, unité et statut mesuré/annoncé/projeté |
| G2 | Ne jamais attribuer à l'IA seule l'énergie de tous les datacenters |
| G3 | Distinguer matériel disponible, offre commerciale et projet de construction |
| G4 | Au moins 3 scénarios d'infrastructure et une option sans GPU/LLM |
| G5 | ACV scope documenté : fabrication, énergie site, eau, maintenance, fin de vie |
| G6 | Aucun gain carbone affirmé sans baseline, périmètre et qualité métier constante |
| G7 | DORA / AI Act / RGPD / ANSSI analysés **selon cas d'usage et service** |
| G8 | Résilience + souveraineté priment sur carbon-aware scheduling du critique |
| G9 | Comparateur TCO/CO2e explicite et hypothèses tracées |
| G10 | Aucun CRC ou GPU personnel requis ; POC hors gate V1.0 |

## Registre de risque documentaire
| ID | Risque | Prévention |
|---|---|---|
| R-01 | Spec fournisseur prise pour capacité effective en région France | Vérifier disponibilité région/zone et quota à date |
| R-02 | Sous-estimer émissions incorporées HBM, GPU, réseau | Bornes, déclaration « données non disponibles » |
| R-03 | Comparer modèles à qualité différente | Unité « résultat utile et valide » commune |
| R-04 | Greenwashing d'émissions évitées | Inventaire séparé des impacts évités/induits |
| R-05 | Hypothèse SLO traitée comme SLA contractuel | BIA, preuves, statut explicitement proposé |
| R-06 | Non-conformité provoquée par optimisation multi-région | Politique de placement *fail closed* |
| R-07 | Étude figée face aux nouvelles générations GPU | Registre daté + revue trimestrielle |

## Convention source
[F] fait public daté ; [C] communication du constructeur (spécifications annoncées) ; [P] projection ; [H] hypothèse illustrée ; [D] décision proposée. Chaque tableau conserve le lien primaire de l'affirmation. Une performance publiée par un vendeur n'est pas un benchmark indépendant.

**Verdict I01** : socle cohérent, mais V1.0 non fermable avant couverture I02–I14 et revue croisée des chiffres.