# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .word_param import WordParam

__all__ = ["ProximityWordCreateParams"]


class ProximityWordCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """A name for this validator, at most 50 characters."""

    words: Required[Iterable[WordParam]]
    """
    The words that raise confidence when found near a match, at most 100 per
    validator. Matching ignores case, so the list may not contain the same word
    twice with different capitalisation. Words are stored as sent.

    For example, a validator for medical record numbers might use
    `[{"word": "patient", "weight": "strong"}, {"word": "diagnosis", "weight": "moderate"}, {"word": "mrn", "weight": "weak"}]`.
    """
