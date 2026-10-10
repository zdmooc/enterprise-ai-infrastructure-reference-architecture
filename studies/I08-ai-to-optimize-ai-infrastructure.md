# I08 — Quel type d'IA pour rendre les infrastructures IA sobres ?

## Principe directeur
**Ne pas mettre une IA générative coûteuse là où une règle, un solveur ou un petit ML suffit.** L'objectif est le **bénéfice net** après l'énergie, le matériel, le coût et les erreurs de l'optimiseur. Sur systèmes physiques et financiers, l'IA conseille/simule avant l'action.

| Use case | Type d'IA candidate | Alternative de contrôle | Données et mesure de succès |
|---|---|---|---|
| Prévoir charge GPU | Séries temporelles, boosting, modèles probabilistes | Seuil fixe / EMA | Erreur forecast, surprovisionnement, kWh net, p95 |
| Détecter GPU inefficaces | Détection d'anomalies Isolation Forest / seuils | Alertes monitoring | Précision alerte, kWh évités **observés** |
| Refroidissement | Optimisation contrainte / RL en simulation | PID et régulation existante | kWh cooling, températures, eau, SLO |
| Optimiser placement | MILP / heuristiques / bandits | Scheduler coût/quota | kWh total, qualité, sous-utilisation |
| Décaler batch | Prévision intensité carbone + solveur | Planification horaire fixe | kgCO2e localisés net, deadlines |
| Router SLM vs LLM | Classificateur calibré / règles | Tout grand modèle | Réponses validées, p95, Wh/réponse |
| Réduire modèles | Quantification, distillation, cache | Serving non optimisé | Qualité, énergie totale training amortie |
| Maintenance | Classification/prognostic | Préventif périodique | Défaillances anticipées vs faux positifs |
| Conseiller exploitant | RAG / agent LLM **lecture seule** | Dashboard/runbook | Décisions utiles, coût de l'agent, audit |

## Cas réel historique : DeepMind pour Google
[DeepMind (20 juillet 2016)](https://deepmind.google/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/) rapporte **jusqu'à 40 % de réduction de l'énergie de refroidissement** sur les sites étudiés. Ce n'est **pas** 40 % de l'énergie datacenter totale ; c'est une revendication d'entreprise et non un rendement universel.

### Design cible d'un contrôleur d'optimisation
```text
Capteurs BMS/PDU/GPU + météo + charge
     ↓ contrôles qualité des séries (horodatage, dérive, lacunes)
Prévision/ML et optimisation sous contraintes
     ↓ simulation / limites déterministes / BIA
Validation humaine & policy engine
     ↓ modification approuvée et réversible
Mesure avant/après -> audit + réentraînement contrôlé
```

**Sûreté physique** : jamais d'accès automatique d'un LLM au contrôleur BMS/UPS/refroidissement critique. Simulation, limites matérielles, arrêt d'urgence et responsabilité de l'opérateur.

## Green Scheduling sous contrainte
Déplacer uniquement les tâches **différables** : batch, indexation documentaire, entraînement, tests, pré-calculs. Exclure règlement de paiement et scoring dans un SLA strict. Déplacement géographique autorisé uniquement si contrat, localisation et risques approuvés. Rendre visible l'empreinte du transfert réseau, le temps d'attente et l'énergie de rechargement du modèle.

## Protocole pour revendiquer une économie
A. Capturer une baseline sans optimiseur sur période comparable.  
B. Fixer charge, qualité, p95, disponibilité, température et eau.  
C. Comparer règles simples, heuristiques, ML et agent ; mesure de l'énergie de l'optimiseur.  
D. Publier kWh et kgCO2e **absolus** et / unité utile, intervalles et coût.  
E. Vérifier fréquence des erreurs, pannes, déplacement/rebond et acceptation métier.  
F. Seule la différence **nette** validée autorise la mention « économie mesurée ».

## Trajectoire 2026–2030 (analyse)
2026–2027 : instrumenter, politiques et modèles de prévision. 2027–2028 : placement/serving adaptatif validé ; sobriété by design. 2029–2030 : contrôle multiobjectif énergie/eau/coût/carbone sous supervision, si données fiables et régulations compatibles. **Scénarios**, non annonces de déploiements garantis.