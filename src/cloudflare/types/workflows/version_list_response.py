# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VersionListResponse", "DefaultRetention", "Limits"]


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

    default_retention: Optional[DefaultRetention] = None

    limits: Optional[Limits] = None
