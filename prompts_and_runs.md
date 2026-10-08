# Curated decisions and run status

## 2026-10-08 — repository inspection and BOM check

- Instruction: document the actual kettle LCA repository in all ten required README sections, without inventing missing inputs or results.
- Instruction: use the linked LCA decision lab and publish completed repository changes to GitHub.
- Codex action: retrieved the classroom BOM CSV and checked the 12 positive finished masses and two scope subtotals with base R.
- Verified output: 723.00 g kettle, 137.80 g packaging, 860.80 g packaged.
- Source check: the linked European Commission PDF confirms the BC1 BOM in Section 4, but its cover identifies Task 1, not the classroom page's Task 4 label.
- Data decision: retained the classroom BOM's stated material labels. No polymer grade, yield, geography, process energy, background provider, or impact factor was selected.
- TianGong CLI 0.1.27 local authentication status: `login-required`; no dataset search was performed. USLCI dataset retrieval and matching are also pending.
- Calculation decision: report impact calculation as not calculated. A mass sum cannot establish GWP100.
- Human modeling choices and independent validation: not recorded in the repository.

## 2026-10-08 — exploratory HTML inventory scenario

- User authorized provisional assumptions for missing data and requested an HTML artifact.
- Codex searched the official USLCI public GitHub archive and recorded nine process candidates. None was accepted as a complete background match.
- The HTML starts with 5% additional material loss for non-PP inputs, 0.20 kWh/kettle assembly electricity, and 100 km additional inbound transport. These are editable illustrative assumptions, not sourced measurements.
- The archived PP injection-molding candidate already lists 1.034 kg resin and 1.79 kWh electricity per kg finished PP part. The scenario does not add a second PP resin-loss or molding-electricity burden.
- No GWP100 result was calculated: current-release matches, provider closure and characterization remain unresolved. TianGong authentication and a working Federal LCA Commons API key were not available in this execution instance.
