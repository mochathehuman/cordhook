# Cordhook

Cordhook is a clean, lightweight Python wrapper around the Discord Webhook API.  
It provides a developer-friendly way to send rich messages, embeds, and file attachments with built-in validation, retry logic, and error handling.

---

[PyPi Project Page](https://pypi.org/project/cordhook/)

## Features

- Simple interface for sending messages and embeds  
- Full support for Discord embed customization  
- File attachment support  
- Auto retry logic with exponential backoff  
- Custom exception handling for common issues  
- Utility functions for formatting, truncating, and validating payloads  

---

## Quick Start
```bash
pip install cordhook
```
```py
from cordhook import Webhook

wh = Webhook("https://discord.com/api/webhooks/...")
wh.set_content("Hello, world!")\\
  .add_embed("Embed Title", "This is a test")\\
  .send()
```
---

## Embed Creation

You can use the create_embed() helper for more control:
```py
from cordhook import create_embed

embed = create_embed(
    title="Sample Embed",
    description="Generated with Cordhook",
    footer_text="Sent via Python",
    timestamp=True
)
```
---

## Utilities

- retry_request(func, retries=3) – retries any function with optional backoff  
- validate_url(url) – checks if a webhook URL is valid  
- json_pretty_print(obj) – nicely formats any JSON or dict  
- truncate_text(text, limit=1024) – prevents hitting Discord text limits  

---

## Exceptions

Cordhook raises specific exceptions so you can catch and handle errors cleanly:

- WebhookException  
- InvalidPayloadException  
- RateLimitException  
- FileAttachmentException  

---

## Example with File
```py
Webhook("url")  
    .set_content("With a file!")  
    .attach_file("cat.png")  
    .send()
```
---

## License

MIT License — free to use, modify, and distribute  

---

## Feedback or Contributions

Open an issue or PR to suggest improvements or fix bugs.