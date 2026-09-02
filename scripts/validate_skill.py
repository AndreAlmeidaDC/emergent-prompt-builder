#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
REQ=["SKILL.md","README.md","CHANGELOG.md","metadata.json","references/vibecode-core.md","references/platform-emergent.md","references/version-check.md","references/archetypes.md","references/accessibility-web.md","references/accessibility-mobile.md"]
def fail(x): print("FAIL:",x); raise SystemExit(1)
def main():
    missing=[p for p in REQ if not (ROOT/p).exists()]
    if missing: fail("missing: "+", ".join(missing))
    meta=json.loads((ROOT/"metadata.json").read_text()); version=str(meta.get("version",""))
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}",version): fail("bad version")
    if meta.get("origin_url")!="https://github.com/AndreAlmeidaDC/emergent-prompt-builder": fail("wrong origin")
    text="\n".join((ROOT/p).read_text() for p in REQ if p.endswith(".md"))
    for token in [version,"E1.5","E2","Prototype","Mobile","forking","GitHub","MCP","stop conditions","independent"]:
        if token.lower() not in text.lower(): fail("missing concept: "+token)
    stale=["São cinco agentes coordenados","máximo 4 prompts","regra das 2 tentativas","deploy ativo ~50 créditos/mês","harness-engineering-coding-agent/main/metadata.json"]
    for value in stale:
        if value.lower() in text.lower(): fail("stale claim: "+value)
    print(f"Validation passed. version={version}")
if __name__=="__main__": main()
