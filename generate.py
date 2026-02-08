#!/usr/bin/env python3
"""
Rakuichi HP Generator
Simple static site generator that concatenates HTML sections.
"""

import os
from pathlib import Path

def main():
    """Main function to generate index.html"""
    base_dir = Path(__file__).parent
    src_dir = base_dir / 'src'
    sections_dir = src_dir / 'sections'
    output_path = base_dir / 'index.html'

    print("--- Rakuichi HP Generator ---")

    # 1. Load Base Template
    base_html_path = src_dir / 'base.html'
    if not base_html_path.exists():
        print(f"Error: Base template not found at {base_html_path}")
        return

    with open(base_html_path, 'r', encoding='utf-8') as f:
        base_html = f.read()
    print(f"Loaded base template: {base_html_path.name}")

    # 2. Load and Concatenate Sections
    sections_html = ""
    # Glob all .html files in sections/ and sort them by filename (01_..., 02_...)
    section_files = sorted(sections_dir.glob('*.html'))
    
    if not section_files:
        print("Warning: No section files found in src/sections/")

    for section_file in section_files:
        print(f"Processing section: {section_file.name}")
        with open(section_file, 'r', encoding='utf-8') as f:
            sections_html += f.read() + "\n"

    # 3. Inject Content into Base Template
    final_html = base_html.replace('{{content}}', sections_html)

    # 4. Write Output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"✓ Generated: {output_path}")
    print("Done! The website has been rebuilt from source sections.")

if __name__ == '__main__':
    main()
