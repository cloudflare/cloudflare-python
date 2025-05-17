# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConfigUpdateParams",
    "Origin",
    "OriginPublicDatabase",
    "OriginAccessProtectedDatabaseBehindCloudflareTunnel",
    "Caching",
    "CachingHyperdriveHyperdriveCachingCommon",
    "CachingHyperdriveHyperdriveCachingEnabled",
    "MTLS",
]


class ConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Define configurations using a unique string identifier."""

    name: Required[str]

    origin: Required[Origin]

    caching: Caching

    mtls: MTLS


class OriginPublicDatabase(TypedDict, total=False):
    database: Required[str]
    """Set the name of your origin database."""

    host: Required[str]
    """Defines the host (hostname or IP) of your origin database."""

    password: Required[str]
    """Set the password needed to access your origin database.

    The API never returns this write-only value.
    """

    port: Required[int]
    """Defines the port (default: 5432 for Postgres) of your origin database."""

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    user: Required[str]
    """Set the user of your origin database."""


class OriginAccessProtectedDatabaseBehindCloudflareTunnel(TypedDict, total=False):
    access_client_id: Required[str]
    """
    Defines the Client ID of the Access token to use when connecting to the origin
    database.
    """

    access_client_secret: Required[str]
    """
    Defines the Client Secret of the Access Token to use when connecting to the
    origin database. The API never returns this write-only value.
    """

    database: Required[str]
    """Set the name of your origin database."""

    host: Required[str]
    """Defines the host (hostname or IP) of your origin database."""

    password: Required[str]
    """Set the password needed to access your origin database.

    The API never returns this write-only value.
    """

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    user: Required[str]
    """Set the user of your origin database."""


Origin: TypeAlias = Union[OriginPublicDatabase, OriginAccessProtectedDatabaseBehindCloudflareTunnel]


class CachingHyperdriveHyperdriveCachingCommon(TypedDict, total=False):
    disabled: bool
    """Set to true to disable caching of SQL responses. Default is false."""


class CachingHyperdriveHyperdriveCachingEnabled(TypedDict, total=False):
    disabled: bool
    """Set to true to disable caching of SQL responses. Default is false."""

    max_age: int
    """Specify the maximum duration items should persist in the cache.

    Not returned if set to the default (60).
    """

    stale_while_revalidate: int
    """Specify the number of seconds the cache may serve a stale response.

    Omitted if set to the default (15).
    """


Caching: TypeAlias = Union[CachingHyperdriveHyperdriveCachingCommon, CachingHyperdriveHyperdriveCachingEnabled]


class MTLS(TypedDict, total=False):
    ca_certificate_id: str
    """Define CA certificate ID obtained after uploading CA cert."""

    mtls_certificate_id: str
    """Define mTLS certificate ID obtained after uploading client cert."""

    sslmode: str
    """Set SSL mode to 'require', 'verify-ca', or 'verify-full' to verify the CA."""
