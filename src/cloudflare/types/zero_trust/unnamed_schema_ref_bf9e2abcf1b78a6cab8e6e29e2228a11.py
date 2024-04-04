# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRefBf9e2abcf1b78a6cab8e6e29e2228a11"]


class UnnamedSchemaRefBf9e2abcf1b78a6cab8e6e29e2228a11(BaseModel):
    id: str

    default: bool
    """Whether the policy is the default for the account"""

    name: str
