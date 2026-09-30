# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConfigCreateParams",
    "HyperdriveHyperdriveConfigCreateWithOrigin",
    "HyperdriveHyperdriveConfigCreateWithOriginOrigin",
    "HyperdriveHyperdriveConfigCreateWithOriginOriginPublicDatabase",
    "HyperdriveHyperdriveConfigCreateWithOriginOriginAccessProtectedDatabaseBehindCloudflareTunnel",
    "HyperdriveHyperdriveConfigCreateWithOriginOriginDatabaseReachableThroughAWorkersVPC",
    "HyperdriveHyperdriveConfigCreateWithOriginCaching",
    "HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateDisabled",
    "HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateEnabled",
    "HyperdriveHyperdriveConfigCreateWithOriginMTLS",
    "HyperdriveHyperdriveConfigCreateWithIntegration",
    "HyperdriveHyperdriveConfigCreateWithIntegrationIntegration",
    "HyperdriveHyperdriveConfigCreateWithIntegrationCaching",
    "HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateDisabled",
    "HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateEnabled",
    "HyperdriveHyperdriveConfigCreateWithIntegrationMTLS",
]


class HyperdriveHyperdriveConfigCreateWithOrigin(TypedDict, total=False):
    account_id: Required[str]
    """Define configurations using a unique string identifier."""

    name: Required[str]
    """The name of the Hyperdrive configuration.

    Used to identify the configuration in the Cloudflare dashboard and API.
    """

    origin: Required[HyperdriveHyperdriveConfigCreateWithOriginOrigin]
    """
    Combines database connection fields with exactly one supported network location.
    """

    caching: HyperdriveHyperdriveConfigCreateWithOriginCaching

    integration: Optional[object]

    mtls: HyperdriveHyperdriveConfigCreateWithOriginMTLS
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    origin_connection_limit: int
    """
    The (soft) maximum number of connections the Hyperdrive is allowed to make to
    the origin database.

    Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
    specified, defaults to 20 for free tier and 60 for paid tier. Certain
    Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
    if you need a higher limit.
    """


class HyperdriveHyperdriveConfigCreateWithOriginOriginPublicDatabase(TypedDict, total=False):
    database: Required[str]
    """Set the name of your origin database."""

    host: Required[str]
    """Defines the publicly reachable hostname or IP of your origin database.

    Private, loopback, and link-local IP addresses are not allowed.
    """

    password: Required[str]
    """Set the password needed to access your origin database.

    The API never returns this write-only value.
    """

    port: Required[int]
    """Defines the port of your origin database.

    Defaults to 5432 for PostgreSQL or 3306 for MySQL if not specified.
    """

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    user: Required[str]
    """Set the user of your origin database."""


class HyperdriveHyperdriveConfigCreateWithOriginOriginAccessProtectedDatabaseBehindCloudflareTunnel(
    TypedDict, total=False
):
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


class HyperdriveHyperdriveConfigCreateWithOriginOriginDatabaseReachableThroughAWorkersVPC(TypedDict, total=False):
    database: Required[str]
    """Set the name of your origin database."""

    password: Required[str]
    """Set the password needed to access your origin database.

    The API never returns this write-only value.
    """

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    service_id: Required[str]
    """The identifier of the Workers VPC Service to connect through.

    Hyperdrive will egress through the specified VPC Service to reach the origin
    database.
    """

    user: Required[str]
    """Set the user of your origin database."""


HyperdriveHyperdriveConfigCreateWithOriginOrigin: TypeAlias = Union[
    HyperdriveHyperdriveConfigCreateWithOriginOriginPublicDatabase,
    HyperdriveHyperdriveConfigCreateWithOriginOriginAccessProtectedDatabaseBehindCloudflareTunnel,
    HyperdriveHyperdriveConfigCreateWithOriginOriginDatabaseReachableThroughAWorkersVPC,
]


class HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateDisabled(
    TypedDict, total=False
):
    disabled: Required[Literal[True]]

    max_age: Optional[int]

    stale_while_revalidate: Optional[int]


class HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateEnabled(TypedDict, total=False):
    disabled: Literal[False]

    max_age: Optional[int]
    """Specify the maximum duration (in seconds) items should persist in the cache.

    Defaults to 60 seconds if not specified.
    """

    stale_while_revalidate: Optional[int]
    """Specify the number of seconds the cache may serve a stale response.

    Defaults to 15 seconds if not specified.
    """


HyperdriveHyperdriveConfigCreateWithOriginCaching: TypeAlias = Union[
    HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateDisabled,
    HyperdriveHyperdriveConfigCreateWithOriginCachingHyperdriveHyperdriveCachingCreateEnabled,
]


class HyperdriveHyperdriveConfigCreateWithOriginMTLS(TypedDict, total=False):
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    ca_certificate_id: str
    """Define CA certificate ID obtained after uploading CA cert."""

    mtls_certificate_id: str
    """Define mTLS certificate ID obtained after uploading client cert."""

    sslmode: str
    """PostgreSQL accepts `require`, `verify-ca`, and `verify-full`.

    MySQL accepts `REQUIRED`, `VERIFY_CA`, and `VERIFY_IDENTITY`. The verify modes
    require a CA certificate; the require modes cannot be used with a CA
    certificate.
    """


class HyperdriveHyperdriveConfigCreateWithIntegration(TypedDict, total=False):
    account_id: Required[str]
    """Define configurations using a unique string identifier."""

    integration: Required[HyperdriveHyperdriveConfigCreateWithIntegrationIntegration]
    """Connects to a PlanetScale database using credentials managed by Cloudflare.

    The Cloudflare account must already be linked to PlanetScale in the Hyperdrive
    dashboard.
    """

    name: Required[str]
    """The name of the Hyperdrive configuration.

    Used to identify the configuration in the Cloudflare dashboard and API.
    """

    caching: HyperdriveHyperdriveConfigCreateWithIntegrationCaching

    mtls: HyperdriveHyperdriveConfigCreateWithIntegrationMTLS
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    origin: Optional[object]

    origin_connection_limit: int
    """
    The (soft) maximum number of connections the Hyperdrive is allowed to make to
    the origin database.

    Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
    specified, defaults to 20 for free tier and 60 for paid tier. Certain
    Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
    if you need a higher limit.
    """


class HyperdriveHyperdriveConfigCreateWithIntegrationIntegration(TypedDict, total=False):
    """Connects to a PlanetScale database using credentials managed by Cloudflare.

    The Cloudflare account must already be linked to PlanetScale in the Hyperdrive dashboard.
    """

    database_branch_name: Required[str]
    """The name of the PlanetScale database branch."""

    database_name: Required[str]
    """The name of the PlanetScale database."""

    organization_name: Required[str]
    """The name of the PlanetScale organization."""

    provider: Required[Literal["planetscale"]]
    """The database integration provider used by this operation."""

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    custom_database_name: str
    """The database name to use when connecting.

    Defaults to `postgres` for PostgreSQL and `mysql` for MySQL.
    """


class HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateDisabled(
    TypedDict, total=False
):
    disabled: Required[Literal[True]]

    max_age: Optional[int]

    stale_while_revalidate: Optional[int]


class HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateEnabled(
    TypedDict, total=False
):
    disabled: Literal[False]

    max_age: Optional[int]
    """Specify the maximum duration (in seconds) items should persist in the cache.

    Defaults to 60 seconds if not specified.
    """

    stale_while_revalidate: Optional[int]
    """Specify the number of seconds the cache may serve a stale response.

    Defaults to 15 seconds if not specified.
    """


HyperdriveHyperdriveConfigCreateWithIntegrationCaching: TypeAlias = Union[
    HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateDisabled,
    HyperdriveHyperdriveConfigCreateWithIntegrationCachingHyperdriveHyperdriveCachingCreateEnabled,
]


class HyperdriveHyperdriveConfigCreateWithIntegrationMTLS(TypedDict, total=False):
    """mTLS configuration for the origin connection.

    Cannot be used with VPC Service origins; TLS must be managed on the VPC Service.
    """

    ca_certificate_id: str
    """Define CA certificate ID obtained after uploading CA cert."""

    mtls_certificate_id: str
    """Define mTLS certificate ID obtained after uploading client cert."""

    sslmode: str
    """PostgreSQL accepts `require`, `verify-ca`, and `verify-full`.

    MySQL accepts `REQUIRED`, `VERIFY_CA`, and `VERIFY_IDENTITY`. The verify modes
    require a CA certificate; the require modes cannot be used with a CA
    certificate.
    """


ConfigCreateParams: TypeAlias = Union[
    HyperdriveHyperdriveConfigCreateWithOrigin, HyperdriveHyperdriveConfigCreateWithIntegration
]
