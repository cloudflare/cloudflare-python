# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LogEditParams"]


class LogEditParams(TypedDict, total=False):
    account_id: Required[str]

    gateway_id: Required[str]
    """gateway id"""

    feedback: Optional[float]

    metadata: Optional[Dict[str, Union[str, float, bool]]]

    score: Optional[float]
