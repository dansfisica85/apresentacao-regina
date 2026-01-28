
import os

css_path = 'style.css'

# Read the file
with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Find the start of corruption. 
# Based on view_file, line 154 is "} / * S t u d e n t..."
# We want to keep up to line 154's closing brace, then append clean CSS.

clean_lines = []
for line in lines:
    if "th.sortable i {" in line:
        clean_lines.append(line)
        # We are near the end of valid content
    elif "opacity: 0.5;" in line:
        clean_lines.append(line)
    elif "t u d e n t" in line: # The corrupted line
        # Split at '}' if it exists on this line
        if '}' in line:
            parts = line.split('}')
            clean_lines.append(parts[0] + '}\n')
        break
    else:
        clean_lines.append(line)

# New CSS to append
new_css = """
/* Student List Modal */
.student-list-container {
    padding-right: 0.5rem;
    /* max-height handled by flexbox in HTML now */
}

.student-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 0.75rem;
    padding: 1rem;
    margin-bottom: 0.75rem;
    transition: all 0.2s;
}

.student-card:hover {
    border-color: #6366f1;
    background: #fff;
    box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.1);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(new_css)
    
print("Fixed style.css")
