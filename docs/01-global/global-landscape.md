# Paysage mondial IA 2026–2030

**Statut :** faits publics et scénarios distincts. **Date d'arrêt :** 2026-10-10.

## Taxonomie de l'infrastructure

| Niveau | Usage | Architecture et contraintes |
|---|---|---|
| Poste de travail | Prototype, test d'inférence locale | VRAM, RAM, acoustique, coût initial |
| Serveur GPU | Serving, petits fine-tunings, RAG | Partage GPU, réservation, support |
| Cluster privé | Multi-équipes, données sensibles | Réseau rapide, placement, quotas, HA |
| GPU cloud | Bursts, essais, entraînement ponctuel | Disponibilité, engagement, trafic, sortie |
| AI Factory | Calcul partagé et écosystème | Ordonnancement, allocation, gouvernance |
| Hyperscale / Gigafactory | Grands modèles, entraînement massif | Énergie, refroidissement, interconnexions, CAPEX |

## Principales zones

### États-Unis
Écosystème hyperscaler, GPU clouds spécialisés, développeurs de puces et opérateurs de datacenters. **Analyse :** chercher les économies d'échelle, les intégrations verticales puce/réseau/logiciel et la diversité des accélérateurs. Ne pas assimiler annonce d'investissement et capacité livrée.

### Chine
Écosystème propre d'accélérateurs, de modèles et de plateformes, sous contraintes géopolitiques et de semi-conducteurs. **Analyse :** suivre les piles logicielles alternatives et les compromis performance/portabilité. Une revue fournisseur primaire est requise avant tout chiffre.

### Europe
EuroHPC, AI Factories, projet AI Gigafactories, opérateurs européens et hyperscalers présents localement. **Analyse :** dissocier quantité de calcul, souveraineté et facilité d'accès industriel.

### Inde, Moyen-Orient et Asie du Sud-Est
Marchés potentiels de nouvelles zones de calcul. **Analyse :** pertinence du réseau électrique, du refroidissement, des chaînes logistiques, de la connectivité et de la réglementation locale.

## Énergie : cas AIE

**PROJECTION SOURCE [S01] :** AIE Energy and AI (2025), scénario central, consommation électrique des **datacenters tous usages confondus** d'environ 945 TWh en 2030. Ce chiffre n'est **pas** l'énergie consommée par la seule IA. L'AIE souligne une forte sensibilité à la vitesse d'adoption de l'IA, aux gains d'efficience et aux contraintes énergétiques.

## Tendances structurantes 2026–2030

1. **Intégration rack-scale :** CPU, HBM, réseau d'accélérateurs et refroidissement comme système.
2. **Séparation des profils de calcul :** modèles généraux, petits modèles spécialisés, calcul classique non génératif.
3. **Serving économique :** batching, quantification, speculative decoding lorsque pertinent, caches, allocation automatique des GPU.
4. **Distribution de l'inférence :** répartition cloud / privé / edge guidée par classification, latence et coûts.
5. **Gestion de la dépendance :** modèle, framework, accélérateur, fournisseur, énergie et contrats.
6. **Exploitation agentique :** journal des outils et actions, permissions minimales, supervision et sécurité du runtime.

## Trois scénarios proposés

- **Capacité contrainte :** composants/électricité rares → quota, ordonnancement et sobriété prioritaires.
- **Croissance maîtrisée :** cloud + privé coexistants → routeur de modèles, portefeuille d'applications et FinOps.
- **Accélération industrielle :** inférence très volumique → automatisation GPU et energy-aware placement.

Ces trois scénarios sont des **hypothèses stratégiques**, pas des prévisions probabilisées.

## Mesures de veille

Livraison effective vs projet ; puissance IT et puissance raccordée ; cartes GPU utilisables ; performances par workload ; prix unitaire complet ; adoption en production ; impact carbone ; services officiellement qualifiés.

**Sources :** [S01], [S02], [S03] du [registre](../09-strategy/sources-register.md).
