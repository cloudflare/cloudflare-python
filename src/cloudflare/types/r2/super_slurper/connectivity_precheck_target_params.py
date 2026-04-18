# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..buckets.provider import Provider

__all__ = ["ConnectivityPrecheckTargetParams", "Secret"]


class ConnectivityPrecheckTargetParams(TypedDict, total=False):
    account_id: Required[str]

    bucket: Required[str]

    secret: Required[Secret]

    vendor: Required[Provider]

    jurisdiction: Literal["default", "eu", "fedramp"]


class Secret(TypedDict, total=False):
    access_key_id: Required[Annotated[str, PropertyInfo(alias="accessKeyId")]]

    secret_access_key: Required[Annotated[str, PropertyInfo(alias="secretAccessKey")]]
