# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .weight import Weight
from ....._models import BaseModel

__all__ = ["Word"]


class Word(BaseModel):
    """A word that raises a match's confidence when it appears near the match."""

    weight: Weight
    """How much a word contributes to a match's confidence when it is found nearby.

    Separate from a profile's high/medium/low confidence threshold: this describes
    how telling the word is, not how confident the resulting match is.
    """

    word: str
    """The word or phrase to look for.

    Must contain 1–128 characters and is matched case-insensitively.
    """
