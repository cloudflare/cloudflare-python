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

    bucket: str

    endpoint: Optional[str]

    secret: R2SlurperS3SourceSchemaSecret

    vendor: Literal["s3"]


class R2SlurperS3SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]


class R2SlurperGcsSourceSchema(TypedDict, total=False):
    account_id: Required[str]

    bucket: str

    secret: R2SlurperGcsSourceSchemaSecret

    vendor: Literal["gcs"]


class R2SlurperGcsSourceSchemaSecret(TypedDict, total=False):
    client_email: Annotated[str, PropertyInfo(alias="clientEmail")]

    private_key: Annotated[str, PropertyInfo(alias="privateKey")]


class R2SlurperR2SourceSchema(TypedDict, total=False):
    account_id: Required[str]

    bucket: str

    jurisdiction: Literal["default", "eu", "fedramp"]

    secret: R2SlurperR2SourceSchemaSecret

    vendor: Provider


class R2SlurperR2SourceSchemaSecret(TypedDict, total=False):
    access_key_id: Annotated[str, PropertyInfo(alias="accessKeyId")]

    secret_access_key: Annotated[str, PropertyInfo(alias="secretAccessKey")]


ConnectivityPrecheckSourceParams: TypeAlias = Union[
    R2SlurperS3SourceSchema, R2SlurperGcsSourceSchema, R2SlurperR2SourceSchema
]
