# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "Hyperdrive",
    "Origin",
    "OriginPublicDatabase",
    "OriginAccessProtectedDatabaseBehindCloudflareTunnel",
    "Caching",
    "CachingHyperdriveHyperdriveCachingCommon",
    "CachingHyperdriveHyperdriveCachingEnabled",
    "MTLS",
]


class OriginPublicDatabase(BaseModel):
    database: str
    """Set the name of your origin database."""

    host: str
    """Defines the host (hostname or IP) of your origin database."""

    port: int
    """Defines the port (default: 5432 for Postgres) of your origin database."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """Set the user of your origin database."""


class OriginAccessProtectedDatabaseBehindCloudflareTunnel(BaseModel):
    access_client_id: str
    """
    Defines the Client ID of the Access token to use when connecting to the origin
    database.
    """

    database: str
    """Set the name of your origin database."""

    host: str
    """Defines the host (hostname or IP) of your origin database."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """Set the user of your origin database."""


Origin: TypeAlias = Union[OriginPublicDatabase, OriginAccessProtectedDatabaseBehindCloudflareTunnel]


class CachingHyperdriveHyperdriveCachingCommon(BaseModel):
    disabled: Optional[bool] = None
    """Set to true to disable caching of SQL responses. Default is false."""


class CachingHyperdriveHyperdriveCachingEnabled(BaseModel):
    disabled: Optional[bool] = None
    """Set to true to disable caching of SQL responses. Default is false."""

    max_age: Optional[int] = None
    """Specify the maximum duration items should persist in the cache.

    Not returned if set to the default (60).
    """

    stale_while_revalidate: Optional[int] = None
    """Specify the number of seconds the cache may serve a stale response.

    Omitted if set to the default (15).
    """


Caching: TypeAlias = Union[CachingHyperdriveHyperdriveCachingCommon, CachingHyperdriveHyperdriveCachingEnabled]


class MTLS(BaseModel):
    ca_certificate_id: Optional[str] = None
    """Define CA certificate ID obtained after uploading CA cert."""

    mtls_certificate_id: Optional[str] = None
    """Define mTLS certificate ID obtained after uploading client cert."""

    sslmode: Optional[str] = None
    """Set SSL mode to 'require', 'verify-ca', or 'verify-full' to verify the CA."""


class Hyperdrive(BaseModel):
    id: str
    """Define configurations using a unique string identifier."""

    name: str

    origin: Origin

    caching: Optional[Caching] = None

    created_on: Optional[datetime] = None
    """Defines the creation time of the Hyperdrive configuration."""

    modified_on: Optional[datetime] = None
    """Defines the last modified time of the Hyperdrive configuration."""

    mtls: Optional[MTLS] = None
