import time
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("discordhooker")

def retry_request(func, retries=3, delay=2, backoff=True, exceptions=(Exception,)):
    """
    Retry a function with optional exponential backoff.
    """
    for attempt in range(retries):
        try:
            return func()
        except exceptions as e:
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                sleep_time = delay * (2 ** attempt) if backoff else delay
                time.sleep(sleep_time)
            else:
                raise

def validate_url(url):
    """
    Basic validation to check if URL is a Discord webhook.
    """
    return url.startswith("https://discord.com/api/webhooks/")

def format_timestamp(dt=None):
    """
    Return an ISO8601 timestamp from datetime or current time.
    """
    if not dt:
        dt = datetime.utcnow()
    return dt.isoformat()

def json_pretty_print(data):
    """
    Pretty print a dictionary or JSON string.
    """
    if isinstance(data, str):
        data = json.loads(data)
    return json.dumps(data, indent=4, sort_keys=True)

def truncate_text(text, limit=1024):
    """
    Truncate text to Discord field limits.
    """
    return text if len(text) <= limit else text[:limit-3] + "..."

def sanitize_embed_data(embed):
    """
    Ensures embed fields meet Discord's limits.
    """
    if "fields" in embed:
        embed["fields"] = embed["fields"][:25]
        for field in embed["fields"]:
            field["name"] = truncate_text(field["name"], 256)
            field["value"] = truncate_text(field["value"], 1024)
    return embed