import re

def sanitize_name(name):
    """Convert a human-readable name to a sanitized ID."""
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
