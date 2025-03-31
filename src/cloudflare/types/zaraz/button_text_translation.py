# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ButtonTextTranslation"]


class ButtonTextTranslation(BaseModel):
    accept_all: Dict[str, str]
    """Object where keys are language codes"""

    confirm_my_choices: Dict[str, str]
    """Object where keys are language codes"""

    reject_all: Dict[str, str]
    """Object where keys are language codes"""
