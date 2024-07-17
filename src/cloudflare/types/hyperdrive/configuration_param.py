# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationParam"]


class ConfigurationParam(TypedDict, total=False):
    database: Required[str]
    """The name of your origin database."""

    host: Required[str]
    """The host (hostname or IP) of your origin database."""

    scheme: Required[Literal["postgres", "postgresql", "mysql"]]
    """Specifies the URL scheme used to connect to your origin database."""

    user: Required[str]
    """The user of your origin database."""

    access_client_id: str
    """The Client ID of the Access token to use when connecting to the origin database"""

    port: int
    """The port (default: 5432 for Postgres) of your origin database."""
