"""Build a standalone HTML inventory scenario from sourced BOM and candidate metadata."""

import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOM = list(csv.DictReader((ROOT / "data/kettle-bom.csv").open()))
CANDIDATES = list(csv.DictReader((ROOT / "data/uslci-candidates.csv").open()))


def cell(value):
    return html.escape(str(value), quote=True)


bom_rows = "\n".join(
    f"<tr><td>{cell(row['material'])}</td><td>{cell(row['scope'])}</td>"
    f"<td class='num'>{float(row['finished_mass_g']):.2f}</td></tr>"
    for row in BOM
)
candidate_rows = "\n".join(
    "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><a href='{}'>source</a></td></tr>".format(
        *(cell(row[k]) for k in ("foreground_input", "dataset_name", "geography", "reason_or_gap")),
        cell(row["source_url"]),
    )
    for row in CANDIDATES
)

template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>BC1 kettle — exploratory inventory scenario</title>
<style>
:root{font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:#172736;background:#f4f7f8}
*{box-sizing:border-box}body{margin:0}header{background:#123d46;color:white;padding:2rem max(1.2rem,calc((100vw - 1100px)/2))}
h1{font-size:clamp(1.8rem,4vw,3rem);margin:.3rem 0}.subtitle{max-width:55rem;line-height:1.5}
main{max-width:1100px;margin:auto;padding:1.3rem}.badge{display:inline-block;background:#dff3e9;color:#12533b;padding:.4rem .7rem;border-radius:999px;font-weight:700;font-size:.85rem}
.warning{background:#fff0d8;color:#5b3900;padding:1rem;border-left:5px solid #d7881b;border-radius:.4rem;margin:1.2rem 0;line-height:1.5}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1rem;margin:1.2rem 0}.card,section{background:white;border:1px solid #d9e3e6;border-radius:.8rem;padding:1.2rem;box-shadow:0 2px 8px #18333a0b}
.card strong{display:block;font-size:1.5rem;color:#125a63;margin-top:.4rem}section{margin:1.2rem 0}h2{margin-top:0;font-size:1.3rem}p,li{line-height:1.55}
.controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}label{display:block;font-weight:700;margin-bottom:.45rem}input{width:100%;padding:.6rem;border:1px solid #9ab1b7;border-radius:.4rem;font:inherit}
.hint{font-size:.86rem;color:#425b63}.outputs{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.8rem;margin-top:1rem}.output{background:#eaf5f5;padding:1rem;border-radius:.5rem}.output b{display:block;font-size:1.25rem;color:#125a63}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.92rem}th,td{text-align:left;padding:.6rem;border-bottom:1px solid #d9e3e6;vertical-align:top}th{background:#ecf2f4}.num{text-align:right;font-variant-numeric:tabular-nums}
a{color:#075e84}footer{font-size:.88rem;color:#4b626a;padding:1rem 0 3rem}
</style>
</head>
<body>
<header><span class="badge">Source checked · assumptions editable</span><h1>BC1 kettle inventory scenario</h1>
<p class="subtitle">One manufactured and packaged 1 L plastic kettle at the factory gate. This report separates the published finished-mass BOM, archived USLCI search candidates, and provisional quantity assumptions.</p></header>
<main>
<div class="warning"><strong>GWP100: not calculated.</strong> The candidate processes have not been accepted or linked to complete upstream providers and a characterized climate method. The quantities below are an exploratory inventory, not kg CO₂-eq and not a submitted footprint.</div>
<div class="cards">
<div class="card">Kettle finished mass<strong>723.00 g</strong></div>
<div class="card">Packaging finished mass<strong>137.80 g</strong></div>
<div class="card">Total finished mass<strong>860.80 g</strong></div>
<div class="card">USLCI archived candidates<strong>9</strong><span class="hint">0 accepted matches</span></div>
</div>
<section><h2>1. Provisional quantities</h2>
<p>Change these values to inspect their effect on required material and activity quantities. Default values are <strong>working assumptions only</strong>; they are not measurements from the kettle study.</p>
<div class="controls">
<div><label for="loss">Additional material loss for non-PP items (%)</label><input id="loss" type="number" min="0" max="50" step="0.5" value="5"><p class="hint">Assumed 5%. Purchased mass = finished mass / (1 − loss). Remove where a selected provider already includes losses.</p></div>
<div><label for="assembly">Assembly electricity (kWh/kettle)</label><input id="assembly" type="number" min="0" max="5" step="0.05" value="0.20"><p class="hint">Assumed 0.20 kWh. No measured factory electricity was provided.</p></div>
<div><label for="distance">Additional inbound transport (km)</label><input id="distance" type="number" min="0" max="5000" step="10" value="100"><p class="hint">Assumed 100 km. Add only for routes not already included in a selected background process.</p></div>
</div>
<div class="outputs">
<div class="output">Trial material input<b id="purchase"></b><span class="hint">kg/kettle; includes PP resin within PP molding candidate</span></div>
<div class="output">PP resin within molding<b id="ppresin"></b><span class="hint">1.034 kg resin per kg finished PP part, archived candidate</span></div>
<div class="output">PP molding electricity<b id="ppelectricity"></b><span class="hint">1.79 kWh per kg finished PP part, already in candidate</span></div>
<div class="output">Extra assembly electricity<b id="assemblyout"></b><span class="hint">Assumption; separate from PP molding electricity</span></div>
<div class="output">Additional freight activity<b id="freight"></b><span class="hint">t·km; provisional, provider overlap not checked</span></div>
</div>
<p class="hint">PP molding is a <em>candidate</em> unit process, not an accepted provider. Its recorded resin and electricity inputs are shown for double-counting review. It also contains 0.1 kg converted corrugated box per kg part and transport exchanges, which may overlap the classroom packaging and the extra freight assumption. If a different PP provider is selected, recalculate these quantities.</p>
</section>
<section><h2>2. Published finished-mass BOM</h2><p>The <a href="../data/kettle-bom.csv">classroom CSV</a> sums to 723.00 g product and 137.80 g packaging. The linked <a href="https://publica-rest.fraunhofer.de/server/api/core/bitstreams/3df3f4d6-3717-4261-99e3-a232323111d6/content">European Commission source PDF</a> confirms BC1 in Section 4. Its cover says Task 1: Scope, final report, May 2021; the publication notice says 2020.</p>
<div class="scroll"><table><thead><tr><th>Material</th><th>Scope</th><th class="num">Finished mass (g)</th></tr></thead><tbody>__BOM_ROWS__</tbody></table></div></section>
<section><h2>3. USLCI search candidates</h2><p>These nine records were found in the official USLCI GitHub archive path <code>downloads/uslci_olca1_5_0_json_ld</code> at source commit <code>83f722d2c97ca784e3d258ab51ec4f6804625c1f</code>. They are older archived records; a current release and provider closure must be checked before selecting matches. See the <a href="../data/uslci-candidates.csv">full candidate table</a> for IDs, versions, units, links and hashes.</p>
<div class="scroll"><table><thead><tr><th>Foreground input</th><th>Candidate process</th><th>Geography</th><th>Reason or gap</th><th>Record</th></tr></thead><tbody>__CANDIDATE_ROWS__</tbody></table></div>
<p class="hint">No confirmed candidates yet for brass, copper, nylon, POM, PC or silicone. Resin-only records do not cover component manufacture. Corrugated containerboard is only a proxy for unspecified cardboard packaging.</p></section>
<section><h2>4. What prevents a climate result</h2><ol><li>Confirm material grades, part-forming routes, geography and reference year.</li><li>Search current TianGong and USLCI releases, compare alternatives and accept provider matches.</li><li>Resolve upstream suppliers, allocation, recycling, transport overlap and missing flows.</li><li>Select and document a GWP100 characterization method and calculate contributions. Then check their sum, mass balance and sensitivity.</li></ol>
<p>Current TianGong CLI status is <code>login-required</code>. The Federal LCA Commons API key was not available in this execution instance when this report was built. The archived candidate list was obtained from the public USLCI GitHub repository without a private key.</p></section>
<footer>Generated from repository data using <code>python scripts/build_assumption_report.py</code>. Inputs and calculations are inspectable in the repository. No credentials or restricted database dump are embedded.</footer>
</main>
<script>
const bom = __BOM_JSON__;
const ppFinished = bom.filter(x => x.material === "Polypropylene (PP)").reduce((a,x)=>a+Number(x.finished_mass_g),0)/1000;
const nonPpFinished = bom.filter(x => x.material !== "Polypropylene (PP)").reduce((a,x)=>a+Number(x.finished_mass_g),0)/1000;
function update(){
  const loss = Math.min(50,Math.max(0,Number(document.getElementById("loss").value)||0))/100;
  const assembly = Math.max(0,Number(document.getElementById("assembly").value)||0);
  const distance = Math.max(0,Number(document.getElementById("distance").value)||0);
  const ppResin = ppFinished*1.034;
  const purchase = ppResin + nonPpFinished/(1-loss);
  document.getElementById("purchase").textContent = purchase.toFixed(4)+" kg";
  document.getElementById("ppresin").textContent = ppResin.toFixed(4)+" kg";
  document.getElementById("ppelectricity").textContent = (ppFinished*1.79).toFixed(4)+" kWh";
  document.getElementById("assemblyout").textContent = assembly.toFixed(2)+" kWh";
  document.getElementById("freight").textContent = (purchase*distance/1000).toFixed(4)+" t·km";
}
for(const id of ["loss","assembly","distance"]) document.getElementById(id).addEventListener("input",update);
update();
</script>
</body></html>
"""
rendered = (
    template.replace("__BOM_ROWS__", bom_rows)
    .replace("__CANDIDATE_ROWS__", candidate_rows)
    .replace("__BOM_JSON__", json.dumps(BOM, ensure_ascii=False).replace("<", "\\u003c"))
)
output = ROOT / "reports/assumption-scenario.html"
output.parent.mkdir(exist_ok=True)
output.write_text(rendered)
print(output)
