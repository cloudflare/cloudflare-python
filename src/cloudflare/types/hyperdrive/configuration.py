# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Configuration"]


class Configuration(BaseModel):
    database: str
    """The name of your origin database."""

    host: str
    """The host (hostname or IP) of your origin database."""

    port: int
    """The port (default: 5432 for Postgres) of your origin database."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """The user of your origin database."""
