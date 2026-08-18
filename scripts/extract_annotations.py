"""
Extract PDF annotations (comments, highlights, sticky notes) from a file in
data/raw/<deal>/ into a text file in data/working/<deal>/.

Usage:
    python scripts/extract_annotations.py <deal-slug> "<filename.pdf>"
"""

import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent

ANNOT_TYPE_NAMES = {
    0: "Text", 1: "Link", 2: "FreeText", 3: "Line", 4: "Square",
    5: "Circle", 6: "Polygon", 7: "PolyLine", 8: "Highlight",
    9: "Underline", 10: "Squiggly", 11: "StrikeOut", 12: "Stamp",
    13: "Caret", 14: "Ink", 15: "Popup", 16: "FileAttachment",
}


def main():
    if len(sys.argv) != 3:
        print('Usage: python scripts/extract_annotations.py <deal-slug> "<filename.pdf>"')
        sys.exit(1)

    deal, filename = sys.argv[1], sys.argv[2]
    src = ROOT / "data" / "raw" / deal / filename
    out_dir = ROOT / "data" / "working" / deal
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(src)
    lines = []
    for i, page in enumerate(doc, start=1):
        for annot in page.annots() or []:
            atype = ANNOT_TYPE_NAMES.get(annot.type[0], f"Type{annot.type[0]}")
            content = (annot.info.get("content") or "").strip()
            author = (annot.info.get("title") or "").strip()

            covered_text = ""
            if atype in ("Highlight", "Underline", "Squiggly", "StrikeOut"):
                try:
                    covered_text = page.get_textbox(annot.rect).strip()
                except Exception:
                    covered_text = ""

            if not content and not covered_text:
                continue

            entry = f"[page {i}] ({atype})"
            if author:
                entry += f" by {author}"
            if covered_text:
                entry += f"\n  marked text: {covered_text}"
            if content:
                entry += f"\n  comment: {content}"
            lines.append(entry)

    out_path = out_dir / (Path(filename).stem + "_ANNOTATIONS.txt")
    out_path.write_text("\n\n".join(lines), encoding="utf-8")
    print(f"extracted {len(lines)} annotations -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
