class WebhookException(Exception):
    """Raised when the webhook fails to send."""
    pass


class InvalidPayloadException(Exception):
    """Raised when the payload is malformed or missing required fields."""
    pass


class RateLimitException(Exception):
    """Raised when a rate limit is hit and cannot be handled automatically."""
    pass


class FileAttachmentException(Exception):
    """Raised when there's an issue attaching a file."""
    pass
