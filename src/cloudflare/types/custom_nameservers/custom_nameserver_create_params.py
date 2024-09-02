# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CustomNameserverCreateParams"]


class CustomNameserverCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    ns_name: Required[str]
    """The FQDN of the name server."""

    ns_set: float
    """The number of the set that this name server belongs to."""
