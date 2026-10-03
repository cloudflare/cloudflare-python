# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ConfigCreateResponse",
    "Caching",
    "Origin",
    "OriginPublicDatabase",
    "OriginAccessProtectedDatabaseBehindCloudflareTunnel",
    "OriginDatabaseReachableThroughAWorkersVPC",
    "Integration",
    "MTLS",
]


class Caching(BaseModel):
    disabled: bool
    """Defines whether caching is disabled."""

    max_age: Optional[int] = None
    """Defines the maximum duration (in seconds) items persist in the cache."""

    stale_while_revalidate: Optional[int] = None
    """Defines the number of seconds the cache may serve a stale response."""


class OriginPublicDatabase(BaseModel):
    database: str
    """Set the name of your origin database."""

    host: str
    """Defines the publicly reachable hostname or IP of your origin database.

    Private, loopback, and link-local IP addresses are not allowed.
    """

    port: int
    """Defines the port of your origin database.

    Defaults to 5432 for PostgreSQL or 3306 for MySQL if not specified.
    """

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


class OriginDatabaseReachableThroughAWorkersVPC(BaseModel):
    database: str
    """Set the name of your origin database."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    service_id: str
    """The identifier of the Workers VPC Service to connect through.

    Hyperdrive will egress through the specified VPC Service to reach the origin
    database.
    """

    user: str
    """Set the user of your origin database."""


Origin: TypeAlias = Union[
    OriginPublicDatabase, OriginAccessProtectedDatabaseBehindCloudflareTunnel, OriginDatabaseReachableThroughAWorkersVPC
]


class Integration(BaseModel):
    """Connects to a PlanetScale database using credentials managed by Cloudflare.

    The Cloudflare account must already be linked to PlanetScale in the Hyperdrive dashboard.
    """

    database_branch_name: str
    """The name of the PlanetScale database branch."""

    database_name: str
    """The name of the PlanetScale database."""

    organization_name: str
    """The name of the PlanetScale organization."""

    provider: Literal["planetscale"]
    """The database integration provider used by this operation."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    custom_database_name: Optional[str] = None
    """The database name to use when connecting.

    Defaults to `postgres` for PostgreSQL and `mysql` for MySQL.
    """


class MTLS(BaseModel):
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    ca_certificate_id: Optional[str] = None
    """Define CA certificate ID obtained after uploading CA cert."""

    mtls_certificate_id: Optional[str] = None
    """Define mTLS certificate ID obtained after uploading client cert."""

    sslmode: Optional[str] = None
    """PostgreSQL accepts `require`, `verify-ca`, and `verify-full`.

    MySQL accepts `REQUIRED`, `VERIFY_CA`, and `VERIFY_IDENTITY`. The verify modes
    require a CA certificate; the require modes cannot be used with a CA
    certificate.
    """


class ConfigCreateResponse(BaseModel):
    id: str
    """Define configurations using a unique string identifier."""

    caching: Caching

    name: str
    """The name of the Hyperdrive configuration.

    Used to identify the configuration in the Cloudflare dashboard and API.
    """

    origin: Origin
    """
    Combines database connection fields with exactly one supported network location.
    """

    created_on: Optional[datetime] = None
    """Defines the creation time of the Hyperdrive configuration."""

    integration: Optional[Integration] = None
    """Connects to a PlanetScale database using credentials managed by Cloudflare.

    The Cloudflare account must already be linked to PlanetScale in the Hyperdrive
    dashboard.
    """

    modified_on: Optional[datetime] = None
    """Defines the last modified time of the Hyperdrive configuration."""

    mtls: Optional[MTLS] = None
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    origin_connection_limit: Optional[int] = None
    """
    The (soft) maximum number of connections the Hyperdrive is allowed to make to
    the origin database.

    Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
    specified, defaults to 20 for free tier and 60 for paid tier. Certain
    Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
    if you need a higher limit.
    """

    restarted_on: Optional[datetime] = None
    """
    Defines the last time the Hyperdrive connection pool was explicitly restarted
    via the restart endpoint. Omitted if the pool has never been explicitly
    restarted.
    """
