# I02 — Géographie mondiale des infrastructures IA, 2026–2030

**Objet** : comparer les modèles industriels et les contraintes. **Méthode** : séparer équipement, modèles, opérateurs, infrastructures énergétiques et barrières d'accès.

## Monde : scénario chiffré comparable
L'AIE [P, source 2025] projette une consommation **mondiale des datacenters tous usages** d'environ **945 TWh en 2030** dans son scénario central, contre environ 415 TWh consommés en 2024. Les serveurs accélérés contribuent fortement à la hausse, mais ce chiffre n'est **pas** « l'électricité de l'IA ». L'étude distingue scénarios Lift-Off, High Efficiency et Headwinds : impossible d'en tirer une valeur par requête sans mesures spécifiques. [AIE](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)

### Perspectives régionales AIE (scénario central ; ne pas confondre avec des capacités installées)
| Région | Augmentation 2024–2030 selon AIE | Interprétation |
|---|---:|---|
| États-Unis | environ +240 TWh | Datacenters hyperscale, dépendance raccordement/réseau |
| Chine | environ +175 TWh | Forte demande de calcul, contraintes composant/énergie |
| Europe | plus de +45 TWh | Décarbonation, capacité HPC, coût et localisation |
| Japon | environ +15 TWh | Croissance infra dense, contraintes foncières/énergie |

Source : [AIE, Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai). Ces valeurs sont des **projections**, non les consommations courantes et non l'IA seule.

## Comparatif structurel
| Zone | Construction des capacités | Software/hardware dominants à surveiller | Risque spécifique | Opportunité |
|---|---|---|---|---|
| États-Unis | Hyperscalers, GPU clouds, collocations | GPU NVIDIA/AMD, ASIC Trainium/TPU, clouds intégrés | Électricité, files de raccordement, concentration | Catalogue très étendu |
| Chine | Fournisseurs cloud et fabricants nationaux | Accélérateurs domestiques, frameworks et modèles locaux | Accès aux semi-conducteurs, compatibilité | Innovation hors CUDA |
| UE | EuroHPC, AI Factories, clouds européens, hyperscalers | HPC + cloud-native + modèles ouverts | Fragmentation, délai d'industrialisation | Diversification et souveraineté |
| Inde | Extension datacenters et services IT/IA | Hyperscalers, intégrateurs régionaux | Réseau et disponibilité énergie/eau | Demande et compétences IT |
| Golfe | Grands projets d'infrastructures et partenariats | GPUs, clusters hyperscale | Refroidissement, eau, contractualisation | Financement et nouvelles capacités |
| Asie du Sud-Est | Hubs datacenter et interconnexion | GPU cloud, colocation | Foncier, énergie et politiques locales | Accès régional à la demande |

**Statut** : les cinq dernières lignes sont des descriptions qualitatives et **non des classements**, aucune puissance nationale ou budget n'est inventé.

## Taxonomie des chaînes de valeur
- Puces : conception accélérateur/ASIC, fabrication, packaging, HBM, firmware.
- Serveurs/racks : CPU, GPU, fabrics scale-up NVLink/Infinity, mémoire.
- Sites : transformateurs, alimentation, UPS, refroidissement liquide/air, sécurisation, eau.
- Opérations : orchestrateur, control plane, observabilité, maintenance, sécurité.
- Services : entraînement, fine-tuning, inférence, RAG, plateforme agents.
- Externalités : électricité, carbone, eau, émissions incorporées, fin de vie.

## Trajectoires prospectives et risques
**2026–2027** : contraintes de construction et coexistence GPU/ASIC; priorité à l'allocation du matériel existant. **2028–2030** : scénario plausible de serving multi-modèle/SLM, infrastructures intégrées et arbitrage énergie/qualité ; trajectoire dépendante du raccordement électrique et des usages réels.

## Ce qu'un architecte doit demander
État réel des installations, spécification d'accélérateur, délai d'accès, data plane, région, egress, offre opérée vs bare metal, chaîne d'approvisionnement, SLA/SLO, origine et facteur carbone daté, WUE, durée d'allocation des matériels, garantie réversibilité.

**Garde-fou** : l'AIE avertit qu'environ 20 % des projets datacenters planifiés pourraient subir des retards si les contraintes de réseau ne sont pas traitées ; ce n'est pas une prévision individualisée pour un site. [AIE synthèse](https://www.iea.org/reports/energy-and-ai/executive-summary).