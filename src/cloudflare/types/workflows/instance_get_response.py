# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InstanceGetResponse",
    "Error",
    "Step",
    "StepUnionMember0",
    "StepUnionMember0Attempt",
    "StepUnionMember0AttemptError",
    "StepUnionMember0Config",
    "StepUnionMember0ConfigRetries",
    "StepUnionMember1",
    "StepUnionMember1Error",
    "StepUnionMember2",
    "StepUnionMember2Trigger",
    "Trigger",
]


class Error(BaseModel):
    message: str

    name: str


class StepUnionMember0AttemptError(BaseModel):
    message: str

    name: str


class StepUnionMember0Attempt(BaseModel):
    end: Optional[datetime] = None

    error: Optional[StepUnionMember0AttemptError] = None

    start: datetime

    success: Optional[bool] = None


class StepUnionMember0ConfigRetries(BaseModel):
    delay: Union[str, float]

    limit: float

    backoff: Optional[Literal["constant", "linear", "exponential"]] = None


class StepUnionMember0Config(BaseModel):
    retries: StepUnionMember0ConfigRetries

    timeout: Union[str, float]


class StepUnionMember0(BaseModel):
    attempts: List[StepUnionMember0Attempt]

    config: StepUnionMember0Config

    end: Optional[datetime] = None

    name: str

    output: object

    start: datetime

    success: Optional[bool] = None

    type: Literal["step"]


class StepUnionMember1Error(BaseModel):
    message: str

    name: str


class StepUnionMember1(BaseModel):
    end: datetime

    error: Optional[StepUnionMember1Error] = None

    finished: bool

    name: str

    start: datetime

    type: Literal["sleep"]


class StepUnionMember2Trigger(BaseModel):
    source: str


class StepUnionMember2(BaseModel):
    trigger: StepUnionMember2Trigger

    type: Literal["termination"]


Step: TypeAlias = Union[StepUnionMember0, StepUnionMember1, StepUnionMember2]


class Trigger(BaseModel):
    source: Literal["unknown", "api", "binding", "event", "cron"]


class InstanceGetResponse(BaseModel):
    end: Optional[datetime] = None

    error: Optional[Error] = None

    output: Union[str, float]

    params: object

    queued: datetime

    start: Optional[datetime] = None

    status: Literal[
        "queued", "running", "paused", "errored", "terminated", "complete", "waitingForPause", "waiting", "unknown"
    ]

    steps: List[Step]

    success: Optional[bool] = None

    trigger: Trigger

    version_id: str = FieldInfo(alias="versionId")
