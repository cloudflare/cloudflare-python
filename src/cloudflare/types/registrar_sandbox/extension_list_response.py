# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ExtensionListResponse", "Metadata"]


class Metadata(BaseModel):
    """Extension metadata"""

    name: str
    """The full name of the extension. For example, "co.uk", or "uk" """

    tld: str
    """The tld of the extension.

    For example, for "co.uk", it's "uk". For "uk", it's "uk"
    """


class ExtensionListResponse(BaseModel):
    """
    Extension entry with metadata and JSON Schema documents for the registration operation.
    """

    metadata: Metadata
    """Extension metadata"""

    registration_schema: object
    """
    JSON Schema describing the expected input structure for registration operations
    on this extension.
    """
