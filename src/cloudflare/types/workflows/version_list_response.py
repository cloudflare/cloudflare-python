# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VersionListResponse", "Concurrency", "DefaultRetention", "Limits"]


class Concurrency(BaseModel):
    limit: Optional[int] = None
    """Maximum number of instances of this workflow that can run concurrently.

    Additional instances are queued and started as running instances complete. Must
    not exceed the account concurrency limit.
    """


class DefaultRetention(BaseModel):
    error_retention: Optional[int] = None
    """Default error retention in milliseconds."""

    success_retention: Optional[int] = None
    """Default success retention in milliseconds."""


class Limits(BaseModel):
    steps: Optional[int] = None


class VersionListResponse(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    has_dag: bool

    language: Literal["javascript", "python"]
    """The programming language of the workflow implementation."""

    modified_on: datetime

    workflow_id: str

    concurrency: Optional[Concurrency] = None

    default_retention: Optional[DefaultRetention] = None

    limits: Optional[Limits] = None
