# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable, List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["QueueUpdateParams", "Rule"]

class QueueUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    bucket_name: Required[str]
    """Identifier."""

    rules: Iterable[Rule]
    """Array of rules to drive notifications"""

class Rule(TypedDict, total=False):
    actions: Required[List[Literal["PutObject", "CopyObject", "DeleteObject", "CompleteMultipartUpload", "AbortMultipartUpload"]]]
    """Array of R2 object actions that will trigger notifications"""

    prefix: str
    """Notifications will be sent only for objects with this prefix"""

    suffix: str
    """Notifications will be sent only for objects with this suffix"""