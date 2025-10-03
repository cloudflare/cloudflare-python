# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from ..buckets.provider import Provider

__all__ = [
    "JobCreateParams",
    "Source",
    "SourceR2SlurperS3SourceSchema",
    "SourceR2SlurperS3SourceSchemaSecret",
    "SourceR2SlurperGcsSourceSchema",
    "SourceR2SlurperGcsSourceSchemaSecret",
    "SourceR2SlurperR2SourceSchema",
    "SourceR2SlurperR2SourceSchemaSecret",
    "Target",
    "TargetSecret",
]


class JobCreateParams(TypedDict, total=False):
    account_id: Required[str]

    overwrite: bool

    source: Source

    target: Target


class SourceR2SlurperS3SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]


class SourceR2SlurperS3SourceSchema(TypedDict, total=False):
    bucket: Required[str]

    secret: Required[SourceR2SlurperS3SourceSchemaSecret]

    vendor: Required[Literal["s3"]]

    endpoint: Optional[str]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]

    region: Optional[str]


class SourceR2SlurperGcsSourceSchemaSecret(TypedDict, total=False):
    client_email: Required[Annotated[str, PropertyInfo(alias="clientEmail")]]

    private_key: Required[Annotated[str, PropertyInfo(alias="privateKey")]]


class SourceR2SlurperGcsSourceSchema(TypedDict, total=False):
    bucket: Required[str]

    secret: Required[SourceR2SlurperGcsSourceSchemaSecret]

    vendor: Required[Literal["gcs"]]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]


class SourceR2SlurperR2SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]


class SourceR2SlurperR2SourceSchema(TypedDict, total=False):
    bucket: Required[str]

    secret: Required[SourceR2SlurperR2SourceSchemaSecret]

    vendor: Required[Provider]

    jurisdiction: Literal["default", "eu", "fedramp"]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]


Source: TypeAlias = Union[SourceR2SlurperS3SourceSchema, SourceR2SlurperGcsSourceSchema, SourceR2SlurperR2SourceSchema]


class TargetSecret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]


class Target(TypedDict, total=False):
    bucket: Required[str]

    secret: Required[TargetSecret]

    vendor: Required[Provider]

    jurisdiction: Literal["default", "eu", "fedramp"]
