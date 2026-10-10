# Empreinte environnementale des infrastructures IA — ACV 2026–2030

**Statut : cadre d'étude documentaire, aucune empreinte d'infrastructure réelle auditée.** **Date : 2026-10-10.**

## Objectif

Comparer, à service **équivalent**, l'empreinte de stations IA, serveurs GPU, clusters privés, offres GPU-as-a-Service, AI Factories et centres hyperscale, monde / Europe / France et banque / assurance. Traiter le Green IT **comme critère de décision d'architecture**.

## Frontières ACV

1. **Amont / scope 3 généralement :** extraction des matières, semi-conducteurs (GPU, CPU, HBM), serveurs, cartes, stockage, réseau, batteries, bâtiment, construction, fabrication/transport, allocation aux années ou unités fonctionnelles.
2. **Utilisation :** CPU/GPU/HBM, équipement réseau/stockage, veille/idle, refroidissement, alimentation/UPS, pertes électriques, eau, énergie des traitements et des expérimentations.
3. **Exploitation :** maintenance, remplacement, pièces et allongement de durée de vie, réemploi.
4. **Aval :** transport, reconditionnement, recyclage et fin de vie — quantifier seulement avec données disponibles, sans prétendre que tous les outils les intègrent.
5. **Effets indirects :** augmentation de l'usage (rebond), substitution effective à un service antérieur, émissions évitées *séparées* des émissions comptables.

### Classification importante

Scopes 1/2/3 du GHG Protocol dépendent de **l'entité déclarante et de la structure contractuelle**. L'électricité d'un datacenter acheté comme service n'est pas automatiquement le scope 2 du client. Une empreinte produit ACV et un inventaire d'entreprise ne sont **pas** interchangeables.

## Calculs

Pour un site dont l'électricité de l'IT et l'installation sont mesurées :

- PUE = énergie totale datacenter (kWh) / énergie IT (kWh).
- E_site = E_IT × PUE, **seulement si** E_IT et PUE se rapportent à une même frontière et période et que l'énergie du refroidissement n'est pas comptée deux fois.
- Émissions opérationnelles localisées ≈ E_site (kWh) × intensité électrique (kgCO2e/kWh), lorsque la convention retenue le permet ; déclarer mix, zone et période.
- Empreinte totale = émissions opérationnelles + empreinte incorporée allouée + autres postes inclus, **sans doublons**.
- SCI = (O + M) / R ; O émissions opérationnelles, M émissions matérielles allouées, R unité fonctionnelle, selon SCI for AI [S12].
- WUE = volume d'eau utilisé / énergie IT (sur la période et avec unités cohérentes) ; ERF = énergie réutilisée / énergie datacenter, suivant l'acte UE [S14].
- Une valeur « gCO2e par prompt » **sans taille des requêtes, qualité de réponse, région, backend et frontière** n'est pas comparable.

### Équivalences de service à retenir

| Charge | Unité de comparaison recommandée |
|---|---|
| Inférence LLM texte | 1 000 réponses **validées**, p95/qualité/seuil de précision égaux ; tokens publiés en parallèle |
| RAG | 1 000 questions résolues correctement selon un test fixé |
| Agent | 1 000 workflows métier **terminés sans erreur**, outils inclus |
| Entraînement | Objectif de score de benchmark atteint, incluant essais échoués |
| Datacenter | 1 kWh IT et volume de calcul effectivement livré, avec frontières documentées |
| Banque / fraude | 1 000 transactions évaluées avec taux de faux positifs comparable |

## Inconnues et limitations

La fabrication des accélérateurs, en particulier les GPU/HBM, n'est pas entièrement transparente. BoaviztAPI [S15] fournit une méthode d'estimation de l'empreinte incorporée de certains composants/équipements, **mais tous les postes et la fin de vie ne sont pas toujours inclus**. Pour toute estimation incertaine, afficher un intervalle, des hypothèses, l'origine du facteur et le statut *estimé / mesuré / fabricant*.

Les données de RTE éCO2mix [S16] décrivent le réseau français et non la consommation d'un datacenter donné. Leur intensité ne doit pas être injectée arbitrairement dans un service cloud dont la localisation réelle est inconnue. Différencier énergie produite vs consommée, moyenne vs marginale, location-based vs market-based, émissions directes vs cycle de vie de l'électricité.

## Water & resource awareness

Inclure WUE, stress hydrique régional, prélèvement vs consommation, éventuel refroidissement adiabatique, chaleur réutilisée, disponibilité en eau, terres et métaux critiques. **Une baisse de PUE peut accroître la demande en eau** : ne pas optimiser un indicateur isolé.

## Méthodologie d'étude de cas

1. Définir les options (station/serveur/cluster/privé/cloud/CPU) et la même qualité de service.
2. Documenter l'inventaire matériel, durée de vie, taux de partage et allocation du hardware.
3. Mesurer ou estimer l'énergie complète et le traitement, en déclarant l'incertitude.
4. Appliquer des facteurs électriques datés, sources et conventions distinctes.
5. Ajouter eau, ressources, coût, performance et contraintes de souveraineté.
6. Analyser sensibilités : taux d'utilisation, durée de vie, région, qualité, prompt, pression de charge.
7. Publier **émissions absolues et intensité fonctionnelle**, en plus du TCO.
8. Recommander un choix seulement après comparaison multi-critères ; résultat non prouvé sinon.

## Sources

[S01] AIE ; [S12] Green Software Foundation SCI for AI ; [S13] ADEME (22/07/2026) ; [S14] Règlement UE 2024/1364 ; [S15] Boavizta ; [S16] RTE. Voir [registre](../09-strategy/sources-register.md).
