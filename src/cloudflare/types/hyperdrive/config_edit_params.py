# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConfigEditParams",
    "Caching",
    "CachingHyperdriveHyperdriveCachingCommon",
    "CachingHyperdriveHyperdriveCachingEnabled",
    "Origin",
    "OriginHyperdriveHyperdriveDatabase",
    "OriginHyperdriveInternetOrigin",
    "OriginHyperdriveOverAccessOrigin",
]


class ConfigEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    caching: Caching

    name: str

    origin: Origin


class CachingHyperdriveHyperdriveCachingCommon(TypedDict, total=False):
    disabled: bool
    """When set to true, disables the caching of SQL responses. (Default: false)"""


class CachingHyperdriveHyperdriveCachingEnabled(TypedDict, total=False):
    disabled: bool
    """When set to true, disables the caching of SQL responses. (Default: false)"""

    max_age: int
    """When present, specifies max duration for which items should persist in the
    cache.

    Not returned if set to default. (Default: 60)
    """

    stale_while_revalidate: int
    """
    When present, indicates the number of seconds cache may serve the response after
    it becomes stale. Not returned if set to default. (Default: 15)
    """


Caching: TypeAlias = Union[CachingHyperdriveHyperdriveCachingCommon, CachingHyperdriveHyperdriveCachingEnabled]


class OriginHyperdriveHyperdriveDatabase(TypedDict, total=False):
    database: str
    """The name of your origin database."""

    password: str
    """The password required to access your origin database.

    This value is write-only and never returned by the API.
    """

    scheme: Literal["postgres", "postgresql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """The user of your origin database."""


class OriginHyperdriveInternetOrigin(TypedDict, total=False):
    host: Required[str]
    """The host (hostname or IP) of your origin database."""

    port: Required[int]
    """The port (default: 5432 for Postgres) of your origin database."""


class OriginHyperdriveOverAccessOrigin(TypedDict, total=False):
    access_client_id: Required[str]
    """
    The Client ID of the Access token to use when connecting to the origin database.
    """

    access_client_secret: Required[str]
    """
    The Client Secret of the Access token to use when connecting to the origin
    database. This value is write-only and never returned by the API.
    """

    host: Required[str]
    """The host (hostname or IP) of your origin database."""


Origin: TypeAlias = Union[
    OriginHyperdriveHyperdriveDatabase, OriginHyperdriveInternetOrigin, OriginHyperdriveOverAccessOrigin
]
