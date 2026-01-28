
import os

css_path = 'style.css'

with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find the marker
marker = "th.sortable i {"
idx = content.find(marker)

if idx != -1:
    # Find the closing brace of this block
    brace_idx = content.find("}", idx)
    if brace_idx != -1:
        # Keep everything up to brace
        clean_content = content[:brace_idx+1]
        
        # New CSS
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
        final_content = clean_content + new_css
        
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print("Successfully repaired style.css")
    else:
        print("Closing brace not found")
else:
    print("Marker not found")
