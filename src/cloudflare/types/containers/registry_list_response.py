# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegistryListResponse"]


class RegistryListResponse(BaseModel):
    """An image registry added in a customer account."""

    created_at: str
    """UTC timestamp string in ISO 8601 format."""

    domain: str
    """A string representation of a domain name.

    See RFC-1034 (https://www.ietf.org/rfc/rfc1034.txt). Consider that the limit of
    a domain name is min 3 and max 253 ASCII characters.
    """

    kind: Optional[Literal["ECR", "DockerHub", "GAR", "default"]] = None
    """The type of registry that is being configured."""

    public_key: Optional[str] = None
    """Public component of the registry credentials.

    For managed registries this is a base64-encoded public key; for external
    registries the format depends on the registry provider.
    """
