# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .word import Word
from ....._models import BaseModel
from ..references import References

__all__ = ["ProximityWordValidator"]


class ProximityWordValidator(BaseModel):
    """A reusable list of weighted words.

    Attaching it to a detection entry raises the confidence of
    that entry's matches when one of the words appears nearby, and lowers it when none do.
    """

    id: str

    created_at: datetime

    name: str
    """A name for this validator, at most 50 characters."""

    referenced_by: References
    """What currently uses a validator.

    Deleting a validator that is still in use returns `409`, so check this first.

    Read-only. A validator is attached or detached by updating the detection entry
    that uses it, not by writing this back.
    """

    updated_at: datetime

    words: List[Word]
    """The words that raise confidence when found near a match."""
