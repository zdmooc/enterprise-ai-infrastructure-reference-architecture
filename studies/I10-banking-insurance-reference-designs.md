# I10 — HLD IA Banque & Assurance : architecture fonctionnelle, technique et Green IT

**Statut** : ARCHITECTURE PROPOSÉE. Aucun schéma de SI bancaire/assurantiel interne confidentiel.

## Pourquoi des plateformes communes ?

**Source publique BNP Paribas [2025]** : LLM-as-a-Service dans les datacenters du Groupe, GPU mutualisés, interface standardisée sécurisée, modèles ouverts/Mistral ; le nombre de GPU, réseau, TCO et empreinte restent non publics. [Communiqué](https://group.bnpparibas/communique-de-presse/bnp-paribas-met-a-disposition-de-ses-metiers-une-plateforme-de-llm-as-a-service-pour-accelerer-lindustrialisation-de-cas-dusage-dia-generative)

**Source publique BPCE [19/11/2025]** : MAiA fondée sur plusieurs modèles externes, plus de 2 millions de prompts mensuels annoncés ; **cette source n'établit pas de topologie GPU privée**. [Communiqué](https://www.digital-payments.groupebpce.com/le-groupe-bpce-accelere-adoption-intelligence-artificielle/)

**Source publique AXA [08/09/2026]** : Global AI Hub fournisseur-agnostique, agents sécurisés, gouvernance/FinOps/SafetyOps/human oversight, cinq entités utilisatrices selon AXA ; configuration hardware non publique. [Communiqué](https://www.axa.com/press/press-releases/axa-and-publicis-sapient-collaborate-to-deploy-global-ai-hub-at-scale)

Ces exemples montrent **trois trajectoires publiquement déclarées**, non une architecture uniforme entre établissements.

## Architecture HLD banque — IA d'assistance et de recherche

```text
Conseiller / Compliance / IT Ops / Analyste
            │ SSO + contexte de rôle
       API Gateway / AI Gateway
            │ classification, quotas et rétention
       Orchestrateur d'assistants
         ├─ Recherche RAG avec ACL/ABAC sur document
         ├─ Catalogue modèles / version / évaluations
         └─ Model Router "policy first"
             ├─ modèle privé sur GPU/CPU, versionnée et journalisée
             ├─ modèle EU admissible contractuellement
             └─ API cloud **uniquement** si autorisée
            │
       Validation de sortie / sources / garde-fous
            │
       Restitution en lecture seule
```

**Séparer le système transactionnel** : toute initiation de paiement/crédit passe dans une API métier distincte avec validateur déterministe, idempotency-key, journal opposable si applicable et approbation selon risque. L'IA n'établit pas seule la vérité transactionnelle.

### Domaines bancaires et architectures adaptées
| Domaine | Solution candidate | Risques majeurs | Optimisation Green |
|---|---|---|---|
| Fraude instant payments | ML scoring **hors** LLM sync si non indispensable | Faux négatifs, p99, disponibilité | CPU/ML spécialisé, modèle compact |
| Recherche procédures réglementaires | RAG et SLM/LLM selon difficulté | ACL, prompt injection, hallucination | Cache, routage SLM, fin de contexte |
| Assistance conseiller | Agent consultatif | Données personnelles, justification | Réutilisation de réponses, quotas |
| IT incidents et exploitation | RAG lecture seule + outil diagnostic | Actions trop privilégiées | Alerting ML léger et pas grand LLM systématique |
| Market research | Classification + RAG + synthèse | Licence données, fuite d'information | Batch hors temps critique |

## Architecture HLD assurance

```text
Gestionnaires sinistres / souscripteurs / service client
       │
  Identity + accès dossier / consentement
       │
  AI Gateway + modèle policy-aware
       ├─ OCR / extraction spécialisée
       ├─ recherche contrats RAG / droits
       ├─ ML fraude et tarification (selon autorisation)
       └─ LLM génération brouillon / synthèse sous contrôle
       │
  Résultat qualifié et traçable / intervention gestionnaire
       │
  SI indemnisation / souscription (source d'autorité)
```

**Données santé en assurance :** évaluer obligations renforcées, transferts, hébergement, minimisation et droits. Ne pas assimiler tout assistant assureur à un système haut risque : classement dépend de la finalité réelle.

## NFR communs à dériver BIA
Disponibilité, p95/p99/TTFT, débit, saturation, RTO/RPO **non inventés**, protection modèle, monitoring des hallucinations, data lineage, souveraineté, validation d'agent, exit plan, DORA fournisseur, coût/réponse, kWh/CO2e/résultat métier validé.

## Composition du Green Control Plane
**Observe** : KPI IT, GPU, tickets, énergie, eau. **Estimate** : E et M allouées, facteurs électriques. **Decide** : policy souveraineté et criticité, modèle dimensionné. **Act** : optimisation de workloads batch ou requêtes basse criticité, contrôle humain. **Audit** : résultat, coût, empreinte nette, non-régression métier.

## Mesure indépendante des fournisseurs
Requêtes métier complétées et correctes, pourcentage servi par CPU/SLM/LLM, temps et énergie de chaque route, coûts, région, rejet, retries, valeur carbone par service **avec incertitude**. Ne pas affirmer « architecture décarbonée » sur la seule base du siège du fournisseur.
