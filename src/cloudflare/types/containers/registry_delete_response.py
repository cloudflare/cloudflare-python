# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RegistryDeleteResponse"]


class RegistryDeleteResponse(BaseModel):
    """Result of deleting an image registry from a Containers account."""

    domain: str
    """A string representation of a domain name.

    See RFC-1034 (https://www.ietf.org/rfc/rfc1034.txt). Consider that the limit of
    a domain name is min 3 and max 253 ASCII characters.
    """
