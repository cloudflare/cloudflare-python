# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RuleDeleteParams"]


class RuleDeleteParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    delete_filter_if_unused: bool
    """
    When true, indicates that Cloudflare should also delete the associated filter if
    there are no other firewall rules referencing the filter.
    """
