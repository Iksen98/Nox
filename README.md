# CIS Hiring Location Advisor Agent

## Overview

The CIS Hiring Location Advisor Agent is designed to support Managers and Directors in making structured, defensible decisions about **where to hire** within the approved CIS COE framework.

The agent provides governance-aligned recommendations based strictly on approved COE locations and authoritative data.

This tool helps ensure hiring decisions are:
- Consistent
- Data-driven
- Risk-aware
- Aligned with the CIS operating model

---

## Scope

This agent operates in a **strict closed-world model**.

Only approved CIS COE locations are considered.

No external locations or assumptions are permitted beyond the authorized dataset.

---

## Authoritative Data Source

All recommendations are derived exclusively from: COEMatrix.csv


This is the single source of truth for:
- COE maturity
- Cost profile
- Talent availability
- Ramp readiness
- Attrition indicators
- Governance risks
- CIS Lead ownership

No external inference or general knowledge is permitted.

---

## What the Agent Does

The agent:

- Collects required hiring inputs from the user
- Reviews and confirms provided inputs
- Applies structured reasoning based on the COE dataset
- Recommends the most suitable COE location
- Explains the rationale clearly
- Highlights key risks and governance considerations
- Can optionally provide a ranked Top 3 recommendation

---

## Required Inputs

Before recommending, the agent must clarify:

- Working language
- Cost sensitivity
- Minimum time-zone overlap

If inputs are incomplete, the agent will:
- Request clarification
- If declined, state explicit assumptions
- Confirm whether to proceed

---

## Governance & Version Control

All changes to:
- Dataset (COEMatrix.csv)
- Agent logic
- Operational rules

Must be managed via Pull Request.

The repository is the authoritative reference for this tool.

---

## Intended Audience

- CIS Managers
- CIS Directors
- Workforce Planning stakeholders

---

## Objective

Enable confident, transparent, and defensible hiring location decisions aligned with long-term CIS strategy.
