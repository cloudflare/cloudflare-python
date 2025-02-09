# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventNotificationGetResponse", "Queue", "QueueRule"]


class QueueRule(BaseModel):
    actions: List[Literal["PutObject", "CopyObject", "DeleteObject", "CompleteMultipartUpload", "LifecycleDeletion"]]
    """Array of R2 object actions that will trigger notifications"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the rule was created"""

    description: Optional[str] = None
    """
    A description that can be used to identify the event notification rule after
    creation
    """

    prefix: Optional[str] = None
    """Notifications will be sent only for objects with this prefix"""

    rule_id: Optional[str] = FieldInfo(alias="ruleId", default=None)
    """Rule ID"""

    suffix: Optional[str] = None
    """Notifications will be sent only for objects with this suffix"""


class Queue(BaseModel):
    queue_id: Optional[str] = FieldInfo(alias="queueId", default=None)
    """Queue ID"""

    queue_name: Optional[str] = FieldInfo(alias="queueName", default=None)
    """Name of the queue"""

    rules: Optional[List[QueueRule]] = None


class EventNotificationGetResponse(BaseModel):
    bucket_name: Optional[str] = FieldInfo(alias="bucketName", default=None)
    """Name of the bucket."""

    queues: Optional[List[Queue]] = None
    """List of queues associated with the bucket."""
