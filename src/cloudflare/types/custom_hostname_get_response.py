# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .ssl import SSL
from .._models import BaseModel

__all__ = ["CustomHostnameGetResponse"]


class CustomHostnameGetResponse(BaseModel):
    id: str
    """Identifier"""

    hostname: str
    """The custom hostname that will point to your hostname via CNAME."""

    ssl: SSL
    """SSL properties for the custom hostname."""
