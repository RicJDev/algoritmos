#!/usr/bin/env python3

import glob
import subprocess
import os

gabo_files = glob.glob("**/*.gabo", recursive=True)

with open("combined.md", "a", encoding="utf-8") as outfile:
    _ = outfile.write("## Pseudocódigo \n```\n")
    for filename in gabo_files:
        if os.path.exists(filename):
            with open(filename, "+r", encoding="utf-8") as infile:
                _ = outfile.write(infile.read())
                _ = outfile.write("\n")
    _ = outfile.write("```")

_ = subprocess.run(
    [
        "pandoc",
        "combined.md",
        "-o",
        "pseudocodigo.docx",
        "--reference-doc",
        "../../../../__ideas__/reference.docx",
    ]
)

os.remove("combined.md")

