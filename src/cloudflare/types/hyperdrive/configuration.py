# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Configuration"]


class Configuration(BaseModel):
    database: str
    """The name of your origin database."""

    host: str
    """The host (hostname or IP) of your origin database."""

    scheme: Literal["postgres", "postgresql", "mysql"]
    """Specifies the URL scheme used to connect to your origin database."""

    user: str
    """The user of your origin database."""

    access_client_id: Optional[str] = None
    """The Client ID of the Access token to use when connecting to the origin database"""

    port: Optional[int] = None
    """The port (default: 5432 for Postgres) of your origin database."""
