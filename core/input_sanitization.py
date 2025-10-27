
# APP_URL INPUT SANITIZATION
def sanitize_url(raw_url):
    raw_url = raw_url.strip()
    if raw_url.startswith("https://"):
        raw_url = raw_url.replace('https://', "")
    elif raw_url.startswith('http://'):
        raw_url = raw_url.replace('http://', "")
    
    full_url = f'https://{raw_url}'
    return full_url