# Matériel et datacenter IA — modèle d'analyse

## Profils de charge à distinguer

1. **Training distribué :** synchronisation GPU/GPU, bande passante réseau, checkpoints, stockage haute performance.
2. **Fine-tuning :** mémoire pour paramètres, gradients, états optimiseur ; LoRA/QLoRA modifient les besoins.
3. **Inférence online :** qualité de service, débit tokens, TTFT, ITL, p95/p99, capacité KV cache.
4. **Inférence batch :** débit total, énergie et coût, plus flexible en temps.
5. **RAG/embedding :** souvent mémoire, CPU et I/O autant que GPU.
6. **IA traditionnelle :** modèles CPU ou accélérateurs légers pouvant supprimer le besoin de LLM.

## Fiche de dimensionnement d'un accélérateur

Pour chaque modèle matériel, recueillir : génération, précision supportée, VRAM/HBM, bande passante mémoire, interconnect GPU, compatibilité framework, consommation électrique, refroidissement, drivers, disponibilité, coût total et fiabilité.

Les tailles d'un modèle en mémoire dépendent des poids, quantification, KV cache, batch, fenêtre de contexte et runtime ; **ne pas utiliser le seul nombre de paramètres** pour dimensionner un serveur.

## Réseau

- **North-south :** applications vers gateway/serveur d'inférence.
- **East-west :** communication entre services et GPU/nœuds ; train distribué plus sensible à la fabric.
- Mesurer RTT, débit soutenu, congestion, retransmissions, perte et comportement sous panne.
- RDMA, InfiniBand ou Ethernet rapide uniquement quand les charges le justifient.
- Segmenter réseau de management, dataplane, stockage, sauvegarde et télémétrie.

## Stockage et modèle

- Référentiel immuable et vérifiable de poids de modèle ; hash et provenance.
- Cache local rapide pour chargement et rechargement.
- S3/objet pour artefacts, logs et jeux d'évaluation lorsque adapté.
- Réplication distincte des artefacts, metadata, index RAG et données sources.
- Garantir le droit de suppression et l'effacement des données sensibles.

## Énergie et datacenter

Bilan à établir sur puissance **IT** (kW), puissance **installation** (kW), PUE mesuré et profil de charge. Refroidissement air ou liquide selon densité, garanties fournisseur et installation. Distinguer puissance électrique contractualisée d'une capacité effectivement disponible.

## Décision : make / rent / burst

Comparer au moins : achat serveurs GPU, GPU cloud à la demande, capacité réservée, inférence managée et CPU. Inclure sous-utilisation, maintenance, EOL, ingénierie, sécurité et coûts de sortie.

Voir [modèle de coûts](../07-finops-green-it/economics.md) et [protocole de laboratoire](../08-labs/lab-roadmap.md).
