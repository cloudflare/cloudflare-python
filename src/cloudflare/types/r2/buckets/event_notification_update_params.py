# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EventNotificationUpdateParams", "Rule"]


class EventNotificationUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    bucket_name: Required[str]
    """Name of the bucket"""

    rules: Iterable[Rule]
    """Array of rules to drive notifications"""

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """The bucket jurisdiction"""


class Rule(TypedDict, total=False):
    actions: Required[
        List[Literal["PutObject", "CopyObject", "DeleteObject", "CompleteMultipartUpload", "LifecycleDeletion"]]
    ]
    """Array of R2 object actions that will trigger notifications"""

    description: str
    """
    A description that can be used to identify the event notification rule after
    creation
    """

    prefix: str
    """Notifications will be sent only for objects with this prefix"""

    suffix: str
    """Notifications will be sent only for objects with this suffix"""
