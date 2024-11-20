# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["PreviewGetResponse"]


class PreviewGetResponse(BaseModel):
    screenshot: str
    """A base64 encoded PNG image of the email."""
