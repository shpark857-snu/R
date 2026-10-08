# BC1 1 L electric kettle LCA — study record

This repository currently contains this README, the [reporting requirements](readme-requirements.md), and the [published classroom BOM](data/kettle-bom.csv). It contains no background-data matches, impact calculation code, decision log, or calculated impact results. The [LCA decision lab](https://tiangong-lca-decision-lab.ecodino73.chatgpt.site/) is the classroom brief and source of the BOM, **not** a generated LCA result.

## 1. Study identity and purpose

| Item | Current record |
| --- | --- |
| Title | BC1 1 L plastic electric kettle LCA (working title from the requirements) |
| Public student/group alias | Unknown; none is recorded |
| Repository | https://github.com/shpark857-snu/R |
| Run ID and study date | Unknown; no run is recorded |
| Goal | Assess one manufactured and packaged kettle at the factory gate, as specified in the [requirements](readme-requirements.md) |
| Intended comparison | Unknown; no baseline or alternative is documented |
| Independent/revised run and Git tag | Unknown; no run output or tag is recorded |

Enter the final 40-character commit SHA in the submission form after committing. It cannot be embedded in this README before that commit exists.

## 2. Product, declared unit and system boundary

The specified declared unit is **one manufactured and packaged BC1 1 L plastic electric kettle at the factory gate**. The [classroom BOM](data/kettle-bom.csv) gives **723 g** for the product and **137.8 g** for packaging. Their sum is **860.8 g**, or **0.8608 kg**, per packaged kettle; the CSV line items reproduce both subtotals. The [European Commission preparatory study PDF](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/3df3f4d6-3717-4261-99e3-a232323111d6/content) confirms BC1 in Section 4, Tables 4-3, 4-4 and 4-8 (printed pp. 26, 27 and 30). Its cover reads **Task 1: Scope, final report, May 2021**, while its publication notice says 2020; the classroom page's “Task 4” label differs from the PDF cover. BC1 is a representative base case, not a named commercial product. The BOM gives finished masses but not polymer grades, yields or assembly electricity.

The intended boundary is factory gate. Included material, conversion, assembly, packaging, and transport processes have not been documented. Exclusions, cut-offs, geography, and reference year are unknown. No use-phase or end-of-life extension is recorded; any future extension should be reported separately from the common factory-gate result.

## 3. Foreground inventory and quantitative assumptions

| Parameter/input | Value | Unit | Evidence/source | Status |
| --- | ---: | --- | --- | --- |
| Product finished mass | 723 | g/kettle | Sum of [BOM](data/kettle-bom.csv) kettle rows | Sourced; CSV sum checked |
| Packaging finished mass | 137.8 | g/kettle | Sum of [BOM](data/kettle-bom.csv) packaging rows | Sourced; CSV sum checked |
| Combined finished mass | 860.8 | g/packaged kettle | Sum of the two BOM subtotals | Calculated; CSV sum checked |
| Component material quantities | See [12 BOM rows](data/kettle-bom.csv) | g/kettle | Classroom BOM, citing 2020 preparatory study | Sourced finished masses; grades not verified |
| Losses, yields, purchased quantities | Unknown | — | No process inventory | Not available |
| Conversion services, assembly electricity | Unknown | — | No process inventory | Not available |
| Transport and scrap | Unknown | — | No process inventory | Not available |
| Prices for monetary estimates | Not applicable currently | — | No monetary estimate is documented | Not used in a recorded calculation |

The 12 finished-mass inputs are stainless steel 186 g, brass 20.25 g, copper 15 g, PP 350.25 g, PVC 43.5 g, nylon 49.5 g, POM 9.75 g, PC 6.75 g, ABS 30 g, silicone 12 g, LDPE foil 6.3 g and cardboard 131.5 g per kettle; see the CSV for part categories. The [interactive assumption report](reports/assumption-scenario.html) uses explicitly provisional values of 5% additional loss for non-PP materials, 0.20 kWh assembly electricity and 100 km additional inbound transport. These values are working assumptions, not measured inventory. Its PP molding candidate already contains 1.034 kg PP resin and 1.79 kWh electricity per 1 kg finished PP part; the report therefore does not add a separate PP loss or molding-electricity assumption. The same candidate includes corrugated-box and transport exchanges that may overlap classroom packaging or additional transport. None of these candidates has yet been accepted as an impact-model provider.

## 4. Background data and matching decisions

The [data manifest](data/data-manifest.csv) records the downloaded classroom BOM and linked source PDF. The [mapping table](data/mapping-decisions.csv) has headers but **no accepted background matches**. A search of the official USLCI GitHub archive produced [nine candidate records](data/uslci-candidates.csv), with dataset names, UUIDs, versions, geographies, 1 kg reference flows, source links and hashes. Their archive path is `downloads/uslci_olca1_5_0_json_ld` at source commit `83f722d2c97ca784e3d258ab51ec4f6804625c1f`; the current-release equivalents and provider closure have not been checked. The PP resin versus injection-molding alternatives and two stainless-steel forms are retained as alternatives, not silently chosen.

The nine archived candidates are marked `UNIT_PROCESS` in their source records. They are **not** cradle-to-gate factors: upstream product inputs require provider linking. No cumulative factor or monetary estimate has been selected, so a monetary sector, currency, price year, price basis and price are not applicable to the current candidate set. Material grades, manufacturing routes and current-release alternatives must be resolved before accepting any match.

## 5. Calculation and impact-assessment methods

The HTML inventory scenario uses `purchased mass = finished mass / (1 − assumed loss)` for non-PP items, scales the archived PP-molding candidate's 1.034 kg resin and 1.79 kWh electricity per kg finished PP part, and converts purchased kg × assumed km / 1,000 to t·km. These are quantity calculations only. No impact-calculation code or method record is present; no process-matrix calculation (such as A s = f; g = B s; h = C g) has been run. Solver, provider linking, allocation/system model, recycling and scrap treatment, credits, characterization method and version, time horizon, biogenic-carbon treatment, and flow matching remain unknown.

Missing upstream providers and uncharacterized flows have not been assessed. Their contributions must not be silently assigned zero.

## 6. How to reproduce the analysis

| Path | Purpose |
| --- | --- |
| [README.md](README.md) | Current study record and known gaps |
| [readme-requirements.md](readme-requirements.md) | Reporting fields and specified mass targets |
| [data/kettle-bom.csv](data/kettle-bom.csv) | Classroom finished-mass inventory, downloaded 2026-10-08; SHA-256 `89b76fbf59a6ab1f3c5825cc6052556b15e1d3e8ea7739121ccb656d00b68f13` |
| [data/data-manifest.csv](data/data-manifest.csv) | Download URL, retrieval date and checksum for the available BOM |
| [data/mapping-decisions.csv](data/mapping-decisions.csv) | Background-match columns; no matches have been accepted |
| [data/uslci-candidates.csv](data/uslci-candidates.csv) | Nine archived USLCI process candidates, including source paths and hashes; none accepted |
| [scripts/validate_bom.R](scripts/validate_bom.R) | Checks CSV schema, positive masses, and both published subtotals |
| [scripts/search_uslci.py](scripts/search_uslci.py) | Searches public Federal LCA Commons metadata after a user-provided API key is available |
| [scripts/build_assumption_report.py](scripts/build_assumption_report.py) | Builds the standalone HTML scenario from the BOM and candidate table |
| [reports/assumption-scenario.html](reports/assumption-scenario.html) | Editable quantity assumptions and current evidence/gaps; no GWP100 result |
| [prompts_and_runs.md](prompts_and_runs.md) | Curated instructions, decisions and verified run status |

The BOM was retrieved from the classroom page's `/classroom/kettle-bom.csv` download. To repeat the **BOM check only**, from the repository root run `Rscript scripts/validate_bom.R`; it should print 723.00 g kettle, 137.80 g packaging and 860.80 g packaged. This uses base R and was run with R 4.5.3 on Debian 13. Run `python scripts/build_assumption_report.py` with Python 3.11+ to regenerate the dependency-free [HTML scenario](reports/assumption-scenario.html), then open that file in a browser. There is no impact-analysis execution command because no accepted complete process network or characterization method is available. The HTML is an inventory scenario, not a generated impact result.

The official TianGong CLI 0.1.27 was checked outside this repository; its `auth status --json` returned `login-required`. Its documented production workflow uses `tiangong-lca auth login` and browser authorization; no TianGong dataset was retrieved. The classroom page points to [USLCI release downloads](https://github.com/FLCAC-admin/uslci-content/blob/dev/docs/release_info/release-downloads.md) and the [Federal LCA Commons API guide](https://www.lcacommons.gov/lca-commons-api-guide); the latter says automated API use needs a user-provided data.gov API key. The search helper reads `USLCI_API_KEY` from the execution environment and can be run from the repository root as `python scripts/search_uslci.py polypropylene --out results/uslci-polypropylene-search.json`. It does not save the key. This command has **not** completed an API search because the key and network proxy are unavailable in the current execution instance. Data permissions, retrieval/caching procedure for background data, and random seeds remain unknown. Restricted data should be obtained through permitted access rather than committed as database dumps. A reproducible impact run requires the permitted inputs or precise retrieval instructions, the model and dependency versions, exact commands, and expected output paths.

## 7. Results, checks and interpretation

**Calculation status: GWP100 not calculated in this repository.** The [HTML scenario](reports/assumption-scenario.html) calculates only provisional material, electricity and freight quantities from sourced masses plus editable assumptions. A GWP100 total in kg CO2-eq per packaged kettle, contribution breakdown, top three contributors, and database/method comparison are unavailable. The BOM line items sum to 723 g product and 137.8 g packaging; this checks the supplied CSV arithmetic, not process mass balance.

The BOM mass subtotals passed. The HTML's default quantity formulas and kg-to-t·km conversion were checked, but their assumptions are not validated measurements. Process mass/balance, supplier closure, contribution sum, and double-counting checks have not been completed; the PP provider's packaging and transport overlap is an identified risk. There are no recorded impact-model passes or failures. Impact drivers and comparison conclusions are unsupported while the model and results are absent; missing contributions are not numerical zeroes.

## 8. Uncertainty and sensitivity

Uncertainty and sensitivity were **not calculated in this repository** because no executable inventory or numerical result exists. Parameters, distributions/ranges and their evidence, correlations, simulation method, draw count, seed, convergence check, mean, median, and P05/P95 are unavailable. Parameter uncertainty, provider/method scenarios, and variation among repeated AI runs cannot be separated without recorded runs. No conditional central 90% interval is reported.

## 9. Codex and human decisions

Codex prepared this repository inspection and README on **2026-10-08 (Korea time)**. The exact model identifier and settings shown to the student are not recorded in the repository and remain unknown. The consequential instruction was to document the actual repository without inventing missing results; see [readme-requirements.md](readme-requirements.md) and the curated [prompt/decision log](prompts_and_runs.md).

The requirements specify the study object and mass targets. Student decisions, accepted or rejected dataset matches, manual edits, error corrections, other assistance, and independently checked outputs are unknown. None are attributed without evidence.

## 10. Independent and revised runs

No preserved independent output or associated Git tag is present. No revision is documented, so prior commit, changed decision, predicted effect, original and revised results, absolute/percentage difference, and explanation are **not applicable to the current record**. If a revised run is made later, preserve the independent result, identify one changed decision, and distinguish a corrected error from a defensible modeling alternative.

## Information needed before final submission

1. Public alias, actual study date, goal, comparison, run ID, and any independent-run tag.
2. Any correction to the classroom BOM and decisions about material grades, yield, electricity, transport, and scrap assumptions.
3. TianGong browser authorization or permitted process exports; USLCI records; complete dataset mapping, selection log, model, method, and provider-closure checks.
4. Actual outputs, figures, validation checks, uncertainty analysis, and curated prompt/decision log, if they exist.

Until those items are available, numerical LCA results and reproducibility remain unverified.
