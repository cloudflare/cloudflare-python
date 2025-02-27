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
]


class OriginPublicDatabase(BaseModel):
    database: str
    """The name of your origin database."""

    host: str
    """The host (hostname or IP) of your origin database."""

    port: int
    """The port (default: 5432 for Postgres) of your origin database."""

    scheme: Literal["postgres", "postgresql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """The user of your origin database."""


class OriginAccessProtectedDatabaseBehindCloudflareTunnel(BaseModel):
    access_client_id: str
    """
    The Client ID of the Access token to use when connecting to the origin database.
    """

    database: str
    """The name of your origin database."""

    host: str
    """The host (hostname or IP) of your origin database."""

    scheme: Literal["postgres", "postgresql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """The user of your origin database."""


Origin: TypeAlias = Union[OriginPublicDatabase, OriginAccessProtectedDatabaseBehindCloudflareTunnel]


class CachingHyperdriveHyperdriveCachingCommon(BaseModel):
    disabled: Optional[bool] = None
    """When set to true, disables the caching of SQL responses. (Default: false)"""


class CachingHyperdriveHyperdriveCachingEnabled(BaseModel):
    disabled: Optional[bool] = None
    """When set to true, disables the caching of SQL responses. (Default: false)"""

    max_age: Optional[int] = None
    """When present, specifies max duration for which items should persist in the
    cache.

    Not returned if set to default. (Default: 60)
    """

    stale_while_revalidate: Optional[int] = None
    """
    When present, indicates the number of seconds cache may serve the response after
    it becomes stale. Not returned if set to default. (Default: 15)
    """


Caching: TypeAlias = Union[CachingHyperdriveHyperdriveCachingCommon, CachingHyperdriveHyperdriveCachingEnabled]


class Hyperdrive(BaseModel):
    id: str
    """Identifier"""

    name: str

    origin: Origin

    caching: Optional[Caching] = None

    created_on: Optional[datetime] = None
    """When the Hyperdrive configuration was created."""

    modified_on: Optional[datetime] = None
    """When the Hyperdrive configuration was last modified."""
