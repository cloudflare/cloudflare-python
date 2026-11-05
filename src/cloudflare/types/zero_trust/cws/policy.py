# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Policy"]


class Policy(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    entrypoint: str
    """Non-function rule declared in rego_source.

    Evaluation uses data.<package_path>.<entrypoint>.
    """

    filter: str
    """Filter expression that determines whether this policy applies.

    Maximum 4096 UTF-8 bytes.
    """

    name: str
    """Human-readable name; unique per account"""

    package_path: str
    """Dotted path derived from rego_source.

    Begins with policy. and is unique per account.
    """

    rego_source: str
    """
    Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
    bytes.
    """

    tags: Dict[str, str]
    """Tags attached to this policy"""

    updated_at: datetime

    description: Optional[str] = None
    """Optional free-form description."""
