# I09 — Green AI by Design : modèles, workloads bancaires et assurance

## Séquence d'arbitrage métier
1. Règles déterministes / recherche indexée simple : le besoin peut-il être couvert **sans IA** ?
2. ML supervisé classifiant/régression CPU si efficacité et auditabilité suffisantes ?
3. Petit modèle / SLM quantifié, avec benchmark de qualité métier ?
4. RAG / outil métier qui fournit des faits plutôt que LLM seul ?
5. Grand LLM nécessaire pour les requêtes réellement complexes ?
6. Fine-tuning justifié plutôt que prompt gigantesque et contexte non borné ?

L'**énergie par token** seule est insuffisante si le petit modèle échoue souvent. Optimiser : kgCO2e/1 000 **résultats corrects** avec mêmes contraintes de confidentialité et disponibilité.

## Classes de charge
| Charge | Risque si routeur « bas carbone » privilégie un modèle inadapté | Politique recommandée |
|---|---|---|
| Fraude paiement instantané | Faux négatif/faux positif, dérive p99 | Modèle métier validé, ne pas appeler LLM synchrone sans nécessité |
| Génération de courrier assurance | Problème de qualité et divulgation | SLM/RAG possible avec relecture selon risque |
| Recherche procédures contrôle interne | Source non autorisée, hallucination | ACL retrieval + citations + seuil qualité |
| Classification dossiers sinistres | Mauvais règlement et impact client | Classification contrôlée, escalade humaine |
| Agent d'exploitation IT | Action irréversible | Tools read-only par défaut, approbation requise |
| Traitement batch réglementaire | Retard d'échéance | Carbon-aware scheduling dans fenêtre validée |

## Paramètres d'efficience
- **Système** : idle GPU, multi-tenancy maîtrisé, right-sizing, auto-scaling prudent, cache modèles, quantification avec mesure qualité.
- **Modèle** : petite taille justifiée, topologie dense/MoE et actifs, vocabulaire, contexte, précision, distillation sous vérification.
- **Application** : prompts brefs mais suffisants, retrieval filtré, cache sémantique prudent, limites d'appels outils/retries, budget tokens par tâche.
- **Portefeuille** : éviter duplication du même modèle dans 20 silos ; mutualisation sous isolation tenant.

## Exemple de comparaison fictive **non mesurée**
Workload : 1 000 dossiers documentaires correctement traités (jeu de test identique), les requêtes ratées incluses.
- Solution A : 1 200 appels LLM ; qualité 1 000/1 000 ; énergie fictive 15 kWh.
- Solution B : 1 300 appels SLM + 100 escalades LLM ; qualité 1 000/1 000 ; énergie fictive 8 kWh.
Le gain de 7 kWh est **une simple arithmétique sur valeurs inventées** ; il ne prouve rien tant que le coût d'hébergement, le RAG, la fabrication, l'entraînement/distillation et les changements de latence ne sont pas évalués.

## Architecture de routage
```text
requête & classification ──► policy données / modèle / résidence
  ├─ règles ou recherche classique
  ├─ ML / petit modèle validé
  └─ grand modèle approuvé si complexité/qualité l'impose
                   ↓
     évaluation qualité + journal minimal + coût + kWh + carbone
```

## Conditions Green AI banque/assurance
Ne pas faire passer l'empreinte avant la BIA, DORA/AI Act/RGPD, sécurité des agents, souveraineté, droits des assurés ou la qualité décisionnelle. La meilleure option peut être « ne pas utiliser de GPU ». Les modèles du fournisseur restent des données manquantes tant que leur ACV n'est pas publiée.

## Livrables de conseil
Matrice qualité/risques/latence/TCO/ACV ; diagramme HLD ; périmètre ACV ; décision justifiée et hypothèses ; plan de tests de non-régression ; stratégie de retrait d'un modèle.

Méthodes : [SCI for AI](https://github.com/Green-Software-Foundation/sci-ai/blob/main/SPEC.md), [ADEME](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/).