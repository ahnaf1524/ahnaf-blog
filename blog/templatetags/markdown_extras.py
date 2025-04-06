import markdown
from django import template
import re

register = template.Library()

# Markdownify function to convert markdown to HTML
@register.filter(name='markdownify')
def markdownify(text):
    return markdown.markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])

# Truncate content until the first heading (h1, h2, etc.)
@register.filter(name='truncate_until_heading')
def truncate_until_heading(text):
    match = re.search(r'(^|\n)(# .+?)(?=\n|$)', text) 
    if match:
        return text[:match.start()].strip()
    return text

@register.filter(name='truncate_and_markdownify')
def truncate_and_markdownify(text):
    truncated_text = truncate_until_heading(text)  
    return markdownify(truncated_text) 