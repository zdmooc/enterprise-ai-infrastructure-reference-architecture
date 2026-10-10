# Modèle carbone documentaire (sans GPU ni cloud)

Ce calculateur Python standard (sans dépendance) **ne mesure aucune consommation**. Il réalise uniquement l'arithmétique des facteurs **fournis par l'utilisateur**. À ne jamais utiliser comme preuve d'ACV fournisseur ou d'émissions réelles sans données instrumentées et contrôlées.

## Usage
```bash
python tools/estimate_lca.py examples/hypothetical_private_lca.json
python -m unittest discover -s tests -v
```

**Champs requis :** status, system_boundary, factor_source, factor_method, model_or_workload, it_energy_kwh, pue (>=1), grid_intensity_kgco2e_per_kwh, allocated_embodied_kgco2e, valid_results (>0).

**Sortie :** énergie site calculée, émissions opérationnelles théoriques, fabrication allouée déclarée, kgCO2e totaux inclus, kgCO2e/1 000 résultats valides. Le flag `measured_footprint` reflète **uniquement le statut déclaré par l'utilisateur** : il ne prouve aucune mesure réelle. Par défaut, exemple `ILLUSTRATIVE`.

Exclusions : eau, émissions infrastructure hors périmètre fourni, training partagé et allocation du matériel, réseau interrégions, effets rebond et norme comptable scopes. Voir [méthode ACV](../studies/I06-lca-hardware-and-ai-service.md).
