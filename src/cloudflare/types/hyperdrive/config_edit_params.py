# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .configuration_param import ConfigurationParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ConfigEditParams", "Caching"]


class ConfigEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    caching: Caching

    name: str

    origin: ConfigurationParam


class Caching(TypedDict, total=False):
    disabled: bool
    """When set to true, disables the caching of SQL responses. (Default: false)"""

    max_age: int
    """When present, specifies max duration for which items should persist in the
    cache.

    (Default: 60)
    """

    stale_while_revalidate: int
    """
    When present, indicates the number of seconds cache may serve the response after
    it becomes stale. (Default: 15)
    """
