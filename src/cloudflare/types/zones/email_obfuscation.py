# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailObfuscation"]


class EmailObfuscation(BaseModel):
    id: Optional[Literal["email_obfuscation"]] = None
    """Turn on or off **Email Obfuscation**."""

    value: Optional[Literal["on", "off"]] = None
    """The status of Email Obfuscation."""
