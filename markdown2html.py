#!/usr/bin/env python3

import sys
import os

def convert_markdown_to_html(markdown_content):
    lines = markdown_content.split('\n')
    html_lines = []
    
    for line in lines:
        if line.startswith('#'):
            heading_level = len(line.split(' ')[0])
            heading_text = line[heading_level:].strip()
            html_line = f"<h{heading_level}>{heading_text}</h{heading_level}>"
            html_lines.append(html_line)
        else:
            html_lines.append(line)

    return '\n'.join(html_lines)

def main():
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    html_content = convert_markdown_to_html(markdown_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    main()
