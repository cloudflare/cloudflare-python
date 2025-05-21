# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..buckets.provider import Provider

__all__ = [
    "JobListResponse",
    "Source",
    "SourceS3SourceResponseSchema",
    "SourceGcsSourceResponseSchema",
    "SourceR2SourceResponseSchema",
    "Target",
]


class SourceS3SourceResponseSchema(BaseModel):
    bucket: Optional[str] = None

    endpoint: Optional[str] = None

    path_prefix: Optional[str] = FieldInfo(alias="pathPrefix", default=None)

    vendor: Optional[Literal["s3"]] = None


class SourceGcsSourceResponseSchema(BaseModel):
    bucket: Optional[str] = None

    path_prefix: Optional[str] = FieldInfo(alias="pathPrefix", default=None)

    vendor: Optional[Literal["gcs"]] = None


class SourceR2SourceResponseSchema(BaseModel):
    bucket: Optional[str] = None

    jurisdiction: Optional[Literal["default", "eu", "fedramp"]] = None

    path_prefix: Optional[str] = FieldInfo(alias="pathPrefix", default=None)

    vendor: Optional[Provider] = None


Source: TypeAlias = Union[SourceS3SourceResponseSchema, SourceGcsSourceResponseSchema, SourceR2SourceResponseSchema]


class Target(BaseModel):
    bucket: Optional[str] = None

    jurisdiction: Optional[Literal["default", "eu", "fedramp"]] = None

    vendor: Optional[Provider] = None


class JobListResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    overwrite: Optional[bool] = None

    source: Optional[Source] = None

    status: Optional[Literal["running", "paused", "aborted", "completed"]] = None

    target: Optional[Target] = None
