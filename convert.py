import subprocess

# This script uses pandoc to convert the 
# canonical HTML resume to Github-flavored Markdown 
# for better display on GitHub. Requires: Pandoc.

def convert_html_to_gfm() -> None:
    subprocess.run([
        "pandoc",
        "sam_robinson_resume.html", 
        "-f", 
        "html", 
        "-t", 
        "gfm-raw_html", 
        "--wrap=none", 
        "-o", 
        "readme.md"
    ])

convert_html_to_gfm()