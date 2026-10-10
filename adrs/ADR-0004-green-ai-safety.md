# ADR-0004 — Pilotage GreenOps par IA sous garde-fous

**Date :** 2026-10-10. **Statut : PROPOSED**.

## Problème
Optimiser énergie et carbone sans dégrader l'intégrité, la disponibilité, la température ni les obligations banque/assurance.

## Proposition
Privilégier premièrement mesure, right-sizing et règles simples. Utiliser ML pour prédire et suggérer. Carbon-aware scheduling uniquement pour tâches différables ; ML/RL de refroidissement d'abord simulé et avec contraintes déterministes. Agents LLM en lecture seule par défaut. Toute décision à conséquence physique ou métier requiert validation humaine ou autorisations pré-approuvées explicites.

## Critères
Baseline sans IA, émissions/énergie nettes incluant le coût de l'optimiseur, p95 et qualité, limites thermiques, sécurité, résidence, audit, plan d'arrêt.

## Alternatives
Optimisation statique, ML supervisé, solveur mathématique, RL contrôlé ; retenir la moins complexe apportant un bénéfice net objectivé.

## Statut d'évidence
Concept et protocole, **aucune optimisation mesurée**.
