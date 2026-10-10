# Méthode, preuve et contrôle qualité

**Référence : 2026-10-10.** Ce dépôt est une base de connaissance d'architecture, pas une certification, une étude de capacité contractuelle ni un audit de conformité.

## Classification des affirmations

| Marqueur | Condition minimale |
|---|---|
| FAIT PUBLIC | Source primaire, URL, date de publication ou de consultation, contexte |
| PROJECTION SOURCE | Auteur du scénario, horizon, scénario précis, hypothèses |
| HYPOTHÈSE | Proposition interne et méthode de falsification |
| DÉCISION | ADR, critères, alternatives, risques, réexamen |
| LAB PLANIFIÉ | Pré-requis et protocole documentés mais pas exécutés |
| LAB VALIDÉ | Commandes, versions, sortie horodatée, métriques, erreurs, rollback |

Aucune annonce de fournisseur, offre de presse ou étude commerciale ne doit être présentée comme preuve indépendante de performance. Les fiches des banques/assurances décrivent **uniquement les éléments rendus publics**.

## Matrice de sources

Priorité : textes juridiques consolidés, superviseurs, régulateurs, organismes statistiques, documentations officielles, communiqués des entreprises (pour leur propre stratégie), presse et études commerciales (avec attribution). Chaque source doit disposer d'un identifiant [Sxx] du [registre](../09-strategy/sources-register.md).

## Règles de comparaison

- Distinction impérative : entraînement, fine-tuning, batch inference, online inference, RAG, agents.
- Unité de calcul : GPU-heures **et** tokens utiles/seconde et par euro, pas « nombre de GPU » isolé.
- Coût : devise, pays/région, date, engagement, stockage, réseau, licence, exploitation, refroidissement, TVA éventuelle.
- Souveraineté : résidence des données ≠ contrôle juridique ≠ exploitation ≠ indépendance matérielle.
- Résilience : RTO/RPO/SLO à dériver d'une BIA. Ne jamais inventer un « 99,99 % » ou « RTO 60 s ».
- Empreinte : mesurer ou estimer explicitement fabrication GPU/HBM/CPU/serveurs/réseau/bâtiments selon frontière, électricité opérationnelle, PUE/WUE, intensité carbone locale datée, fin de vie, allocation et incertitudes. Conserver unité fonctionnelle et qualité métier équivalentes ; intégrer coût environnemental de l'optimiseur lui-même. Méthode [SCI for AI](../07-finops-green-it/lifecycle-environmental-footprint.md).
- Green AI : comparer l'optimisation ML/agentique contre règles simples et baseline ; aucune économie garantie ou émission évitée non mesurée. Les actions touchant refroidissement et workloads critiques restent soumises à garde-fous et validation humaine.
- Rapport externe : isoler les informations publiques des preuves de laboratoire et des projections.

## Cadence

Revue mensuelle du [registre des sources](../09-strategy/sources-register.md) et trimestrielle de la [roadmap](../09-strategy/roadmap-2026-2030.md). Revue ponctuelle obligatoire après une nouvelle loi, version majeure de plateforme ou benchmark invalidant une hypothèse.

## Definition of Done documentaire

1. Question d'architecture explicite.
2. Alternative et compromis, y compris « ne pas employer de GPU/LLM ».
3. Sources datées, statut d'évidence.
4. Hypothèses et limites.
5. Mesures et décision de validation.
6. Liens vers ADR, modèle de coût ou lab lorsque pertinent.

## Contrôles avant publication

Pas de secrets, données personnelles, captures clients, informations confidentielles, résultats inventés ou affirmation de conformité automatique. Ni noms de clients finaux inférés, ni architectures internes non publiées.
