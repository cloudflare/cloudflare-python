# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TenantStructure"]


class TenantStructure(BaseModel):
    id: str
    """Server-assigned UUID"""

    application: Literal["aws", "cloudflare"]
    """Platform this structure models.

    Immutable after creation; determines valid node kinds and identifier formats.
    """

    created_at: datetime

    name: str
    """Human-readable name; unique per account"""

    updated_at: datetime

    import_path: Optional[str] = None
    """Optional unique Rego mount path in the form tenant.<application>.<name>.

    The application segment must match application; omitted when unmounted.
    """
