#!/usr/bin/env python3
"""Update nav links consistently across all html files to include Enterprise + Pricing + Security."""
from pathlib import Path
import re

ROOT = Path("/Users/keyscales/Documents/Key's Touch/Website")

NEW_NAV = '''<ul class="nav-links" id="nav-menu">
                <li><a href="/#what-we-do">Services</a></li>
                <li><a href="/services/enterprise.html">Enterprise</a></li>
                <li><a href="/pricing.html">Pricing</a></li>
                <li><a href="/case-studies.html">Case Studies</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/?audit=open" class="nav-cta">Free High-Value Audit</a></li>
            </ul>'''

# Match the existing nav-links block
pattern = re.compile(r'<ul class="nav-links" id="nav-menu">.*?</ul>', re.DOTALL)

files = list(ROOT.glob("*.html")) + list((ROOT / "services").glob("*.html"))
for f in files:
    content = f.read_text()
    if 'nav-links' not in content:
        continue
    new_content = pattern.sub(NEW_NAV, content)
    if new_content != content:
        f.write_text(new_content)
        print(f"Updated nav: {f.relative_to(ROOT)}")
    else:
        print(f"No change:   {f.relative_to(ROOT)}")
