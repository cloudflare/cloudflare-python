# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ActiveSessionCreatePollResponse", "Data", "DataPoll", "DataPollOption", "DataPollOptionVote"]


class DataPollOptionVote(BaseModel):
    id: str

    name: str


class DataPollOption(BaseModel):
    count: float

    text: str
    """Text of the answer option"""

    votes: List[DataPollOptionVote]


class DataPoll(BaseModel):
    id: str
    """ID of the poll"""

    options: List[DataPollOption]
    """Answer options"""

    question: str
    """Question asked by the poll"""

    anonymous: Optional[bool] = None

    created_by: Optional[str] = None

    hide_votes: Optional[bool] = None

    voted: Optional[List[str]] = None


class Data(BaseModel):
    action: Optional[str] = None

    poll: Optional[DataPoll] = None


class ActiveSessionCreatePollResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
