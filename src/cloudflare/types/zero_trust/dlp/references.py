# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["References", "Entry"]


class Entry(BaseModel):
    """A detection entry that uses a validator."""

    id: str

    name: str

    type: Literal[
        "custom", "custom_prompt_topic", "predefined", "integration", "exact_data", "document_fingerprint", "word_list"
    ]
    """The type of a detection entry."""


class References(BaseModel):
    """What currently uses a validator.

    Deleting a validator that is still in use returns `409`, so
    check this first.

    Read-only. A validator is attached or detached by updating the detection entry that uses it, not
    by writing this back.
    """

    entries: List[Entry]
    """The detection entries using this validator, ordered by name."""

    entry_count: int
    """Number of detection entries this validator is attached to."""
