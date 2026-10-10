# I04 — Matrice accélérateurs IA 2026 : caractéristiques **fournisseurs**

**Attention** : ces données sont tirées de fiches constructeur ou clouds, **pas des benchmarks indépendants**. Mémoire HBM `GB` / `GiB` et TB/s sont conservés selon source et **ne doivent pas être fusionnés sans normalisation**.

| Équipement ou offre | Architecture / unité | Mémoire accélérateur | Bande passante HBM | Puissance | Statut et source |
|---|---|---|---|---|---|
| NVIDIA H100 (cloud GCP A3) | Hopper, 1 GPU | 80 GB HBM3 | 3,35 TB/s | à qualifier SKU | [Google Cloud](https://docs.cloud.google.com/docs/compute-area/gpus) |
| NVIDIA H200 (cloud GCP A3 Ultra) | Hopper, 1 GPU | 141 GB HBM3e | 4,8 TB/s | à qualifier SKU | [Google Cloud](https://docs.cloud.google.com/docs/compute-area/gpus) |
| NVIDIA B200 (cloud GCP A4) | Blackwell, 1 GPU | 180 GB HBM3e | 8 TB/s, fournisseur | à qualifier SKU | [Google Cloud](https://docs.cloud.google.com/docs/compute-area/gpus) |
| NVIDIA GB300 NVL72 | 72 GPU + 36 Grace, **rack**, liquide | GPU aggregate jusqu'à 21 TB | jusqu'à 576 TB/s **aggregate**, constructeur | puissance système non déduite ici | [NVIDIA](https://www.nvidia.com/fr-fr/data-center/gb300-nvl72/) |
| AMD Instinct MI355X | CDNA4, 1 module OAM | 288 GB HBM3e | jusqu'à 8 TB/s | **TBP 1 400 W** | [AMD fiche MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html) |
| Google TPU7x Ironwood | TPU, 1 puce | **192 GiB HBM** | 7 380 GB/s constructeur | puissance à obtenir | [GCP TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x) |
| Google TPU7x Pod | 9 216 puces au maximum | distribution 9 216 × 192 GiB (non mémoire unique) | fabric ICI | non publiée ici | [GCP TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x) |

**Limitation majeure** : les FLOPS annoncés mélangent précision FP4/FP8/BF16, sparsité, modèles et interfaces ; pas de classement direct NVIDIA vs AMD vs Google sur ces chiffres.

## Profils de charges et axes décisifs
| Workload | Ressource déterminante | Métrique à demander |
|---|---|---|
| Pretraining / distributed | GPU et réseau scale-up/scale-out, checkpoints | Time-to-train à qualité fixe, échecs/restarts |
| Fine-tuning LoRA | VRAM et mémoire activations | Modèle/dataset, coût training convergé |
| Batch inference | Mémoire et débit token, batching | kWh/1 000 résultats valides |
| Interactive RAG | TTFT, retrieval, p95 | Réponses valides, SLO, coût complet |
| Agent tools | Durée workflow, appels outils et retries | kWh et réussite/workflow |
| Fraude / scoring tabulaire | Souvent CPU suffisant | Fraude évitée / performance / p95, pas tokens |

## Dimensionnement (pas de règle universelle)
Poids du modèle + KV cache + activations + overhead framework + marge = enveloppe mémoire requise ; la quantification varie selon précision et fidélité. Une mémoire distribuée sur plusieurs GPU exige communications et *parallelism* ; l'addition de VRAM n'est pas « une carte virtuelle unique ».

**Décision critique :** benchmarker *le même modèle, quantification, prompts, contexte, batch, p95 et taux de réponses correctes* sur chacun des environnements. Inclure consommation site et empreinte matérielle allouée ; sinon pas de meilleur choix démontré.

## Matériel, souveraineté et empreinte
- GPU HBM = consommation élevée possible et fabrication multi-composants ; **ne pas extrapoler** TBP à une consommation réelle continue.
- Évaluer réseau, racks, mémoire, stockage, eau, refroidissement, chaîne de fabrication et période d'amortissement.
- Pour le Green IT, mesurer équipement **inactif** autant que charge active et capacité surprovisionnée.
- Les factures d'électricité et les émissions de fabrication des GPU ne sont généralement pas publiées au niveau d'un workload bancaire.

## Critères d'audit fournisseur (fiche standard)
GPU/SKU | VRAM et unité | bande passante | précision | puissance **mesurée** (idle/médiane/p95) | coût | driver/runtime | version | disponibilité région | matrice compliance | ACV constructeur ou hypothèse | preuve lien+date.

**Conclusion de conception** : privilégier l'architecture capable de servir le besoin à coût, empreinte et risque mesurés. Un CPU ou petit modèle peut être préférable à un accélérateur haute densité pour des traitements spécialisés.