# I11 — DORA, AI Act, RGPD et résilience des infrastructures IA

**Avertissement** : checklist de conception, pas un avis juridique, ni une certification de conformité. Analyse par entité, cas d'usage, prestataire et service.

## Textes et calendrier
- [DORA — ESMA](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora) : applicable depuis **17 janvier 2025**, selon périmètre. Risques TIC, incidents, test de résilience, dépendances et contrats de prestataires.
- [AI Act — article 113 consolidé au 27 juillet 2026](https://ai-act-service-desk.ec.europa.eu/fr/ai-act/article-113) : règles déployées par phases. Haut risque **annexe III** à compter du **2 décembre 2027** et certains systèmes **annexe I** à compter du **2 août 2028** dans le texte consulté. Vérifier l'évolution légale.
- **RGPD** : confidentialité, finalité, conservation, transferts et droits des personnes ; la conformité cloud relève de l'ensemble du traitement.
- [ANSSI SecNumCloud](https://cyber.gouv.fr/offre-de-service/solutions-certifiees-et-qualifiees/services-de-securite-evalue/solutions-en-cours-de-qualification/prestataires-secnumcloud/) : vérifier offre/qualification/périmètre, **pas fournisseur global**.

## Contrôles architecture → preuves
| Risque | Contrôle proposé | Test/évidence attendue |
|---|---|---|
| Service IA externalisé | Registre prestataires, DPA, sous-traitants, exit plan | Contrat, cartographie et test d'export |
| Modèle externe indisponible | Circuit breaker, second modèle **autorisé**, fail-safe | Injection panne modèle et métriques p95 |
| GPU saturé | Quotas admission, répartition, mode dégradé | Montée en charge + refus propre |
| Fuite prompt / context | Classification, minimisation, chiffrements, politiques logs | Test DLP et accès interdit |
| RAG inter-tenant | ACL retrieval côté serveur et isolation index/tenant | Suite de tests négatifs croisés |
| Agent trop privilégié | Approbation, limitation scopes, outil contrôlé, idempotence | Rejeu après timeout sans double paiement |
| Risque AI Act | Inventaire des systèmes, analyse de classification, documentation | Dossier par finalité et version |
| Risque fournisseur GPU/cloud | Évaluation concentration et réversibilité, capacité de secours | Exercice exit / restauration / charge |
| Prise de décision automatisée | Supervision humaine appropriée et explication | Test escalade et contestation selon cas |
| GreenOps déstabilisant | Politique SLO/BIA avant carbone, simulation | Injection variation et vérification sécurité |

## Scénarios de PRA
1. **Défaillance GPU** : nœud perdu, rechargement modèle, disponibilité alternative, backlog. Mesurer reprise réelle, pas un RTO fictif.
2. **Perte fournisseur** : fallback uniquement vers un fournisseur/model/région approuvé ; si aucun, refus sûr.
3. **Défaillance du RAG** : contexte obligatoire absent → refuser réponse risquée, ne pas halluciner contrat.
4. **Agent interrompu après écriture** : système métier dédoublonne via idempotency-key et statut serveur ; aucun replay aveugle.
5. **Défaillance du contrôleur énergétique** : retour aux règles BMS d'origine, arrêt des optimisations autonomes et journalisation.
6. **Perte KMS/identité** : refuser mutations, break-glass dûment contrôlé et audité si prévu.

## Principes de test
La BIA définit le service critique, le RTO/RPO et les concessions possibles ; évaluer SLO en normal, sous charge et durant la panne. Les modèles peuvent nécessiter temps de chargement importants (cold start). Les données AI (poids, métadonnées, index, prompts autorisés) ont des exigences de reprise différentes.

## Éclairage régulateur sectoriel
[EIOPA septembre 2026](https://www.eiopa.europa.eu/publications/scaling-ai-finance-systemic-risks-resilience-and-european-sovereignty_en) met l'accent sur la concentration des prestataires et la nécessité de conserver expertise humaine, capacité de repli et diversité de fournisseurs. La souveraineté **ne garantit pas** la résilience : deux prestataires européens peuvent partager la même dépendance matérielle.

## Green IT compatible conformité
Décaler un **batch autorisé** pour réduire l'empreinte est envisageable ; réduire la latence critique ou contourner résidence/continuité est interdit dans la politique proposée. Les seuils thermiques, power capping et modifications DCIM/BMS sont soumis aux contrôles industriels de sûreté.
