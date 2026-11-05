# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel
from ..profiles.pattern import Pattern

__all__ = ["CustomUpdateResponse"]


class CustomUpdateResponse(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None

    validator_ids: Optional[List[str]] = None
    """Validators this entry references, by id, at most 10.

    An empty list means the entry references none.

    Returned by the entry endpoints. Not returned on entries embedded in other
    responses, such as profiles.
    """
