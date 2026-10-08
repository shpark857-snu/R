"""Search public Federal LCA Commons metadata without recording the API key."""

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="material or process term")
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--page-size", type=int, default=25)
    parser.add_argument("--out", type=pathlib.Path, required=True)
    args = parser.parse_args()
    if args.page < 1 or not 1 <= args.page_size <= 100:
        parser.error("page must be positive and page-size must be 1..100")

    key = os.environ.get("USLCI_API_KEY")
    if not key:
        print("USLCI_API_KEY is unavailable in this environment.", file=sys.stderr)
        return 2

    url = "https://api.nal.usda.gov/FederalLCACommonsapi/search/?" + urllib.parse.urlencode(
        {
            "query": args.query,
            "page": args.page,
            "pageSize": args.page_size,
            "api_key": key,
        }
    )
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        print(f"Federal LCA Commons returned HTTP {error.code}.", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, ValueError):
        print("Federal LCA Commons request or JSON parsing failed.", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Saved public search response to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
