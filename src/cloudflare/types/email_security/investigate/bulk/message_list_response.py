# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ....._utils import PropertyInfo
from ....._models import BaseModel

__all__ = ["MessageListResponse", "ActionParams", "ActionParamsMove", "ActionParamsRelease"]


class ActionParamsMove(BaseModel):
    client_recipient: str

    destination: Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]

    type: Literal["MOVE"]

    expected_disposition: Optional[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ] = None


class ActionParamsRelease(BaseModel):
    client_recipient: str

    type: Literal["RELEASE"]


ActionParams: TypeAlias = Annotated[Union[ActionParamsMove, ActionParamsRelease], PropertyInfo(discriminator="type")]


class MessageListResponse(BaseModel):
    action_params: ActionParams

    action_type: Literal["MOVE", "RELEASE"]

    created_at: datetime

    message_id: str

    postfix_id: str

    retry_count: int

    status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]

    alert_id: Optional[str] = None

    email_message_id: Optional[str] = None

    processed_at: Optional[datetime] = None

    retry_after: Optional[datetime] = None
    """When to retry the action if it failed"""

    status_message: Optional[str] = None
