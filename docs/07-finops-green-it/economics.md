# FinOps, Green IT et analyse TCO des infrastructures IA

**Statut :** modèle méthodologique ; aucun tarif commercial n'est figé dans ce dépôt.

## Variables

- C = coût d'acquisition (€) ; L = durée d'amortissement (mois).
- H = heures GPU/mois ; R = tarif GPU (€ / heure) ; U = taux d'utilisation effectif.
- P = puissance IT moyenne (kW) ; PUE = énergie site / énergie IT.
- E = prix de l'électricité (€ / kWh) ; I = intensité carbone (kgCO2e / kWh).
- N = millions de tokens **utiles** servis ; O = coûts mensuels autres (stockage, réseau, licences, supervision, support, personnel).

## Modèles de coûts

**Cloud à la demande (mensuel)**
Coût = H × R + stockage + transferts + supervision + licences + support + éventuels frais de réservation. Déclarer région, date, devise et conditions.

**Privé (mensuel)**
Coût = C / L + (P × durée_heures × PUE × E) + maintenance + licences + emplacement + réseau + exploitation + assurance + provisions renouvellement.

**Coût par million de tokens utiles**
Coût mensuel total / N.
Il faut publier simultanément TTFT, p95, throughput, taux d'erreurs et mesure de qualité ; sinon un coût/token seul peut pousser à une architecture médiocre.

## Exemple ARITHMÉTIQUE, pas une offre commerciale

4 heures par jour × 22 jours = **88 heures/mois**.
À un tarif **hypothétique** de 3 €/GPU-heure, la seule composante GPU = **264 €** avant réseau, stockage, taxes, licences, frais annexes et arrêts non facturés.

## Énergie

Énergie mensuelle (kWh) = puissance IT moyenne (kW) × durée (h) × PUE.
Émissions opérationnelles = énergie × facteur carbone local daté et sourcé.
Émissions sur cycle de vie = opérationnelles + fabrication/transport/fin de vie, selon méthode explicite d'allocation. Ne pas comparer seulement la consommation instantanée de deux GPU sans mesurer le **travail utile** fourni.

## Mesures à collecter

- GPU utilization et memory used, CPU/RAM, température, puissance réelle ;
- TTFT, inter-token latency, tokens/s, requêtes, p95/p99 ;
- coût par application, tenant, équipe et modèle, budgets et dépassements ;
- taux de cache, quota refusé, taux de routage privé/cloud ;
- localisation/carbone de l'électricité et impacts de la fabrication ;
- coût de l'indisponibilité ou de la capacité inutilisée.

## Décision

Comparer trois scénarios sur un même workload représentatif : privé, cloud GPU, hybride. Simuler charge moyenne, p95/pointe, changement de modèle, hausse tarif, saturation, panne et sortie fournisseur.

**PROJECTION SOURCE [S01] :** l'AIE estime la consommation datacenter mondiale à environ 945 TWh en 2030 dans son scénario central ; cela ne doit pas servir de facteur direct d'émissions d'une requête d'IA.

Utiliser le [modèle CSV](../../templates/finops-estimate.csv) et la [méthode](../00-governance/methodology.md).
