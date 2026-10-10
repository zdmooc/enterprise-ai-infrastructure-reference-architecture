# I12 — 2026–2030 : scénarios TCO, énergie et carbone, analyse de sensibilité

## Trois scénarios prospectifs — hypothèses et non prévisions garanties
| Facteur | S1 capacité contrainte | S2 croissance maîtrisée | S3 expansion accélérée |
|---|---|---|---|
| Tendance | GPU/raccordements rares | Déploiement hybrides et serving optimisé | Investissements hyperscale rapides |
| Risque dominant | Pénurie, prix, attente | Complexité multi-fournisseurs | Surcapacité locale, rebond, concentration |
| Action | Right-sizing, réservation, CPU/SLM | AI Gateway, GreenOps, FinOps/ACV | Contrôle qualité et carbone absolu |
| Souveraineté | Disponibilité offres limitée | Arbitrages région/contrat | Fournisseurs et chaînes de valeur diversifiés |
| Métrique stratégique | Utilisation GPU utile | Coût + kgCO2e par résultat valide | Demande totale énergie/eau, marge réelle |

L'[AIE](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) distingue explicitement ses propres variantes de croissance/efficacité/contraintes. S1–S3 ci-dessus sont des **scénarios de conception internes**, non des valeurs publiées par l'AIE.

## Calculateur conceptuel, pas une estimation du marché
Variables par scenario :
- N = réponses **validées**/mois ;
- H = heures de capacité GPU réservées ; r = tarif €/GPUh (date, région, contrat) ;
- C = CAPEX matériel + infrastructure, L = durée de vie économique mois ;
- EI = énergie IT affectée kWh ; p = PUE harmonisé et mesuré/estimé ;
- f = facteur électrique kgCO2e/kWh avec convention datée ;
- M = empreinte matérielle totale attribuée à la charge kgCO2e ;
- OX = stockage, réseau, licences, support, exploitation et coûts de sortie amortis.

| Résultat | Cloud/IaaS | Privé |
|---|---|---|
| CAPEX mensuel | 0 pour investissement matériel client, **pas 0 pour tous les frais** | C/L |
| Charge GPU | H×r | intégrée au TCO privé |
| Exploitation | OX, stockage, egress, support | OX, personnel, électricité, maintenance |
| Énergie totale | EI×p si périmètre connu | EI×p |
| Émissions opérationnelles | EI×p×f | EI×p×f |
| Émissions service ACV | EI×p×f + M + autres postes connus | Idem |
| €/1 000 résultats valides | coût complet / (N/1000) | Idem |
| kgCO2e/1 000 résultats valides | ACV attribuée / (N/1000) | Idem |

Si M ou EI sont indisponibles pour un fournisseur cloud, **résultat = incomplet**, non zéro et non meilleur par défaut.

## Sensibilités à produire en dossier de choix
1. Utilisation capacité GPU 20 / 50 / 80 % (**scénarios d'essai**, pas moyennes marché).
2. Croissance de N selon taux simulés, y compris effet rebond.
3. Durée de vie matériel 3 / 5 / 7 ans **hypothétique** et méthode de prorata.
4. Facteur carbone électricité : géographies / heures autorisées, et différence direct/réseau/ACV.
5. PUE/WUE variable selon densité, température, eau, modes de refroidissement.
6. Requêtes longues (KV cache), modèles petits/grands, taux d'échec et d'escalade.
7. Catastrophe région/cloud + coût de l'alternative.

## Exemple de sensibilité carbone, purement arithmétique
Pour 100 kWh **IT fictifs** à PUE fictif 1,25, le site consomme 125 kWh. À un facteur hypothétique f=0,05 le poste électrique vaut 6,25 kgCO2e ; si f=0,30 il vaut 37,5 kgCO2e ; **sans compter la fabrication**. C'est un rappel de l'influence des conventions/lieux, **pas une comparaison réelle de pays**.

## Conseil d'investissement
Ne pas acheter une capacité IA uniquement parce que son PUE est bas ni la louer uniquement parce que son GPUh est bon marché. Décision conditionnée à : risques, capacité disponible, coût total, saturation/p95, réponse correcte, data residency, réversibilité, carbone matériel/énergie et eau. Les chiffres restent paramétriques jusqu'à validation commerciale.
