# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegoMetadata"]


class RegoMetadata(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    data: object

    import_path: str
    """
    Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
    underscore segment. Reference it as data.<import_path>.
    """

    name: str
    """Human-readable name; unique per account"""

    updated_at: datetime
