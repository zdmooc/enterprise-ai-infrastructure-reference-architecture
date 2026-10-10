# I05 — Comparatif Cloud GPU / HPC / privé / GPU-as-a-Service

## Offres techniques vérifiées dans la documentation de fournisseurs (pas disponibilité garantie à Paris)
| Famille | Configuration documentée | Enjeu architectural et preuve |
|---|---|---|
| AWS EC2 P6-B200 | Instance 8 × NVIDIA B200, **1 440 GB mémoire GPU** annoncée par AWS | Réseau EFA, réservation/capacité selon zone, [AWS](https://aws.amazon.com/ec2/instance-types/p6/) |
| Microsoft Azure ND GB200 v6 | VM 4 × GPU Blackwell + 2 Grace | Fabric NVLink, compatibilité OS et région à vérifier, [Azure](https://learn.microsoft.com/fr-fr/azure/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series) |
| Google Cloud A4 | VM 8 × B200, **1 440 GB mémoire GPU** | Quotas/réservation/spot selon produit et région, [GCP](https://docs.cloud.google.com/compute/docs/gpus) |
| Google Cloud TPU7x | TPU Ironwood 192 GiB HBM par puce | JAX/PyTorch supportés, **TensorFlow non supporté sur TPU7x** selon GCP, [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x) |
| Datacenter privé | Serveur GPU choisi et réseau propriétaire | Contrôle direct mais investissements, maintenance, spare, HW refresh |
| EuroHPC AI Factory | Accès à supercalcul sous politique programme | Peut privilégier R&D/PME ; ne remplace pas une offre bancaire DORA standard |
| Cloud GPU spécialisé | VM GPU ou capacité réservée selon fournisseur | Sous-traitance, egress, coûts, région et sécurité à évaluer fournisseur par fournisseur |
| CPU / logiciel traditionnel | CPU x86/ARM, ML ciblé | Souvent un vrai candidat pour fraude/attribution/règles, réduire la VRAM |

Aucune grille régionale ni prix de cloud n'est inventé : prix et disponibilités changent rapidement et varient par contrat.

## Dossier de placement : 7 gates séquentiels
**G1. Métier** : type de calcul (training / interactive / batch / RAG / ML traditionnel), criticité, qualification de qualité.
**G2. Réglementaire** : données et finalité, AI Act, DORA, RGPD, politique et contrat.
**G3. Technique** : VRAM, réseau, stockage, latence, disponibilité, changement de version, dépendances.
**G4. Résilience** : perte de zone, panne GPU, boucle agentique, failover autorisé, audit, réversibilité.
**G5. Économique** : CAPEX/OPEX, coût / réponse utile, egress, support, capacité idle, coûts de sortie.
**G6. Environnemental** : kWh, fabrication, PUE, WUE, kgCO2e/résultat utile, frontière/certitude.
**G7. Choix** : risques résiduels, décision justifiée et propriétaire, revalidation périodique.

## Différences de responsabilité
| Mode | Qui exploite l'alimentation/physique ? | Qui pilote modèle et données ? | Point à vérifier |
|---|---|---|---|
| On-prem | Entreprise/infogérant | Entreprise | Lifecycle GPU et maintenance |
| Colocation bare-metal | Colocation/DC + locataire/infogérant | Contrat à décrire | Refroidissement, énergie et comptage |
| GPU IaaS | Fournisseur infrastructure | Souvent client | GPU quota, responsabilité patch/driver |
| Inférence managée | Fournisseur sur une plus grande partie | Partagée contractuellement | Logs, entraînement sur prompts, exports |
| HPC/AI Factory | Exploitant EuroHPC selon programme | Selon politique d'accès | Données autorisées et capacité réservable |

## Modèle de décision initial
- **Données sensibles, charge stable** : examiner en premier instance privée ou cloud de confiance admissible.
- **Charge variable, traitement autorisé et contrôlé** : GPU cloud à la demande ou réservé à comparer économiquement.
- **Grande campagne d'entraînement exploratoire** : HPC / capacité spécialisée à examiner selon conditions d'accès.
- **Traitement tabulaire faible latence** : prototype CPU/ML non génératif pour constituer la baseline.
- **Hybride** : API/model router vers régions et fournisseurs **explicitement permis** ; pas de fallback sauvage.

## Contrôles Green IT non négociables
Comparer énergie IT **et installation** sans double compter, heures GPU inactives, émissions incorporées réparties et qualité métier. Une région « propre » ne signifie pas nécessairement que toute l'ACV du service est basse ; prendre en compte données réseau, egress, effet rebond et prolongation de vie des matériels.

## Conclusion
Aucune plateforme universellement « meilleure » ; la solution dépend du service, des données, de l'accès réel à la capacité et de la preuve TCO/ACV. La [méthode documentaire](../docs/00-governance/methodology.md) exclut les comparaisons prix absolues non datées.