# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AIGatewayCreateParams"]


class AIGatewayCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """gateway id"""

    cache_invalidate_on_update: Required[bool]

    cache_ttl: Required[Optional[int]]

    collect_logs: Required[bool]

    rate_limiting_interval: Required[Optional[int]]

    rate_limiting_limit: Required[Optional[int]]

    rate_limiting_technique: Required[Literal["fixed", "sliding"]]
