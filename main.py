#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a front page drawn
from the verified world news of Tuesday 17 November 2026 (Kerch Bridge
struck again, Iran drones at the U.S. radar in Bahrain, Trump in Manila
with the Xi-Trump-Putin summit set for Shenzhen, tankers mined near
Hormuz, Japan scrambling jets, Houthis advancing on Aden). The program
copies it byte for byte to /output/entry.png, so both graded runs write
the same bytes. The gate takes a whole PNG or JPEG of at most 1 MiB and
1024 by 1024 pixels; this file is a 1024x1024 PNG of about 115 KiB.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

DST.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
print(f"wrote {DST} ({DST.stat().st_size} bytes)")
sys.exit(0)
