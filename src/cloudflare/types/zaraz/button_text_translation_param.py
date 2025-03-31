# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ButtonTextTranslationParam"]


class ButtonTextTranslationParam(TypedDict, total=False):
    accept_all: Required[Dict[str, str]]
    """Object where keys are language codes"""

    confirm_my_choices: Required[Dict[str, str]]
    """Object where keys are language codes"""

    reject_all: Required[Dict[str, str]]
    """Object where keys are language codes"""
