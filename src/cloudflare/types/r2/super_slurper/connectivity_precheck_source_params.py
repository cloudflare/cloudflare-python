# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from ..buckets.provider import Provider

__all__ = [
    "ConnectivityPrecheckSourceParams",
    "R2SlurperS3SourceSchema",
    "R2SlurperS3SourceSchemaSecret",
    "R2SlurperGcsSourceSchema",
    "R2SlurperGcsSourceSchemaSecret",
    "R2SlurperR2SourceSchema",
    "R2SlurperR2SourceSchemaSecret",
]


class R2SlurperS3SourceSchema(TypedDict, total=False):
    account_id: Required[str]

    bucket: Required[str]

    secret: Required[R2SlurperS3SourceSchemaSecret]

    vendor: Required[Literal["s3"]]

    endpoint: Optional[str]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]

    region: Optional[str]


class R2SlurperS3SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]


class R2SlurperGcsSourceSchema(TypedDict, total=False):
    account_id: Required[str]

    bucket: Required[str]

    secret: Required[R2SlurperGcsSourceSchemaSecret]

    vendor: Required[Literal["gcs"]]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]


class R2SlurperGcsSourceSchemaSecret(TypedDict, total=False):
    client_email: Required[Annotated[str, PropertyInfo(alias="clientEmail")]]

    private_key: Required[Annotated[str, PropertyInfo(alias="privateKey")]]


class R2SlurperR2SourceSchema(TypedDict, total=False):
    account_id: Required[str]

    bucket: Required[str]

    secret: Required[R2SlurperR2SourceSchemaSecret]

    vendor: Required[Provider]

    jurisdiction: Literal["default", "eu", "fedramp"]

    path_prefix: Annotated[Optional[str], PropertyInfo(alias="pathPrefix")]


class R2SlurperR2SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]


ConnectivityPrecheckSourceParams: TypeAlias = Union[
    R2SlurperS3SourceSchema, R2SlurperGcsSourceSchema, R2SlurperR2SourceSchema
]
