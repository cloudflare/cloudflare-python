# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegoModule"]


class RegoModule(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    name: str
    """Human-readable name; unique per account"""

    package_path: str
    """Dotted path derived from rego_source.

    Begins with lib. and is unique per account.
    """

    rego_source: str
    """
    Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
    bytes.
    """

    updated_at: datetime
