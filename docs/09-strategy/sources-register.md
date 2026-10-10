# Registre des sources primaires et statut des affirmations

**Dernière vérification : 2026-10-10.** Les URL sont des sources à examiner périodiquement. Il ne faut pas confondre date de publication et date de consultation.

| ID | Source et lien | Date source | Assertion utilisable / statut |
|---|---|---|---|
| S01 | [AIE, Energy and AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) | 2025 | PROJECTION SOURCE : ~945 TWh/an datacenters monde en 2030, scénario central, pas « IA seule » |
| S02 | [Commission européenne, AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories) | Page évolutive, consultée 2026-10-10 | FAIT PUBLIC : 19 AI Factories et 13 antennes **en cours de création** |
| S03 | [AIE, Energy Supply for AI](https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai) | 2025 | PROJECTION SOURCE : besoins énergétiques et contraintes sur la chaîne électrique |
| S04 | [EIOPA, Scaling AI in Finance](https://www.eiopa.europa.eu/publications/scaling-ai-finance-systemic-risks-resilience-and-european-sovereignty_en) | 2026-09-16 | FAIT PUBLIC : enquête 347 assureurs/25 pays, 65 % utilisent GenAI et 23 % envisagent ; adoption inclut des POC |
| S05 | [ESMA, DORA](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora) | Page évolutive, consultée 2026-10-10 | FAIT PUBLIC : DORA applicable depuis 2025-01-17 |
| S06 | [Commission, AI Act, article 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113) | Version consolidée 2026-07-27 | FAIT PUBLIC : application échelonnée, annexe III haut risque à compter du 2027-12-02 selon texte consolidé |
| S07 | [ANSSI, Cloud / SecNumCloud](https://cyber.gouv.fr/enjeux-technologiques/cloud/) | Page évolutive, consultée 2026-10-10 | FAIT PUBLIC : qualification d'offres/serv. précis et non de toutes les applications du client |
| S08 | [BNP Paribas, LLM-as-a-Service](https://group.bnpparibas/communique-de-presse/bnp-paribas-met-a-disposition-de-ses-metiers-une-plateforme-de-llm-as-a-service-pour-accelerer-lindustrialisation-de-cas-dusage-dia-generative) | 2025 | DÉCLARATION FOURNISSEUR : GPU mutualisés dans datacenters du Groupe |
| S09 | [AXA, Global AI Hub](https://www.axa.com/press/press-releases/axa-and-publicis-sapient-collaborate-to-deploy-global-ai-hub-at-scale) | 2026-09-08 | DÉCLARATION ENTREPRISE : hub agentique commun, gouvernance, FinOps et sécurité |
| S10 | [Red Hat, OpenShift AI serving](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.2/html-single/configuring_your_model-serving_platform/index) | Documentation produit, version 3.2 | TECHNIQUE : vLLM et KServe GPU ; vérifier correspondance avec version déployée |
| S11 | [Groupe BPCE, MAiA](https://www.digital-payments.groupebpce.com/le-groupe-bpce-accelere-adoption-intelligence-artificielle/) | 2025 | DÉCLARATION ENTREPRISE : MAiA et >2 M prompts/mois ; pas de détails publics sur les GPU |


| S12 | [Green Software Foundation, SCI for AI](https://greensoftware.foundation/standards/sci-ai/) et [spécification](https://github.com/Green-Software-Foundation/sci-ai/blob/main/SPEC.md) | Spécification publiée, page consultée 2026-10-10 | MÉTHODE : SCI = (O + M) / R, mesure IA de conception à inférence, unités fonctionnelles et frontières |
| S13 | [ADEME, IA générative : comment quantifier les impacts ?](https://www.ademe.fr/presse/communique-national/ia-generative-comment-quantifier-les-impacts/) | 2026-07-22 | FAIT PUBLIC : analyse des impacts environnementaux directs/indirects, attention sobriété et effets rebond |
| S14 | [UE, règlement délégué 2024/1364](https://eur-lex.europa.eu/eli/reg_del/2024/1364/oj?locale=eng) | 2024 | RÉGLEMENTATION : méthode indicateurs durabilité datacenters, PUE, WUE, ERF, REF |
| S15 | [Boavizta, méthode impacts incorporés](https://doc.api.boavizta.org/Explanations/embedded_methodology/) | Documentation évolutive, consultée 2026-10-10 | MÉTHODE : estimation d'impacts matériels avec limites, fin de vie pas toujours incluse |
| S16 | [RTE, éCO2mix](https://www.rte-france.com/donnees-publications/eco2mix-donnees-temps-reel) | Données évolutives, consultées 2026-10-10 | DONNÉES RÉSEAU FR : production et émissions électriques ; ne mesure pas directement les datacenters |
| S17 | [DeepMind, datacenter cooling](https://deepmind.google/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/) | 2016 | DÉCLARATION ENTREPRISE HISTORIQUE : jusqu'à 40 % sur **énergie refroidissement**, non énergie totale |
| S18 | [Green Software Foundation, Carbon Aware SDK](https://carbon-aware-sdk.greensoftware.foundation/docs/overview) | Documentation consultée 2026-10-10 | OUTIL : placement temporel/géographique des tâches différables selon intensité prévue |
| S19 | [Hugging Face, AI Energy Score](https://huggingface.github.io/AIEnergyScore/) | Documentation consultée 2026-10-10 | BENCHMARK : énergie GPU sur tâches IA ; autres composants à ajouter avant ACV complète |

| S20 | [NVIDIA GB300 NVL72](https://www.nvidia.com/fr-fr/data-center/gb300-nvl72/) | Fiche consultée 2026-10-10 | CONSTRUCTEUR : rack 72 Blackwell Ultra + 36 Grace, refroidissement liquide, mémoire agrégée |
| S21 | [AMD MI355X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html) | Fiche consultée 2026-10-10 | CONSTRUCTEUR : 288 GB HBM3E, bande passante 8 TB/s, TBP 1400 W |
| S22 | [Google TPU7x Ironwood](https://docs.cloud.google.com/tpu/docs/tpu7x) | Documentation consultée 2026-10-10 | FOURNISSEUR : 192 GiB HBM par puce, 9 216 puces/pod, limites frameworks |
| S23 | [AWS EC2 P6-B200](https://aws.amazon.com/ec2/instance-types/p6/) | Fiche consultée 2026-10-10 | FOURNISSEUR : instances 8 B200, mémoire annoncée ~1440 GB ; disponibilité régionale non garantie |
| S24 | [Microsoft Azure ND-GB200 v6](https://learn.microsoft.com/fr-fr/azure/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series) | Documentation consultée 2026-10-10 | FOURNISSEUR : configuration 4 Blackwell GPU + 2 Grace |
| S25 | [Google Cloud A4 / B200](https://docs.cloud.google.com/compute/docs/gpus) | Documentation consultée 2026-10-10 | FOURNISSEUR : 8 B200 et 1 440 GB HBM ; réserver/quota selon zone |
| S26 | [BNP Paribas LLM-as-a-Service, 05/06/2025](https://group.bnpparibas/communique-de-presse/bnp-paribas-met-a-disposition-de-ses-metiers-une-plateforme-de-llm-as-a-service-pour-accelerer-lindustrialisation-de-cas-dusage-dia-generative) | 2025-06-05 | DÉCLARATION ÉTABLISSEMENT : plateforme interne GPU, pas de capacité HW chiffrée |
| S27 | [BPCE MAiA, 19/11/2025](https://www.digital-payments.groupebpce.com/le-groupe-bpce-accelere-adoption-intelligence-artificielle/) | 2025-11-19 | DÉCLARATION ÉTABLISSEMENT : >2 M prompts/mois, modèles externes, hardware non public |
| S28 | [AXA Global AI Hub, 08/09/2026](https://www.axa.com/press/press-releases/axa-and-publicis-sapient-collaborate-to-deploy-global-ai-hub-at-scale) | 2026-09-08 | DÉCLARATION ÉTABLISSEMENT : hub agentique, cinq entités, infrastructure physique non précisée |

## Politique de correction

- Si une source change, indiquer la version/date, ne pas effacer l'historique.
- Les communiqués prouvent qu'une entreprise **a déclaré** un dispositif, pas sa performance observée.
- Les estimations énergétiques, prévisions de dépenses, nombres de GPU et tarifs commerciaux exigent une référence et des hypothèses séparées.
- N'ajouter **aucun** chiffre de puissance, coût, part de marché ou délai sans preuve.
