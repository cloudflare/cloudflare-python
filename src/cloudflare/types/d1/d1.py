# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["D1", "ReadReplication"]


class ReadReplication(BaseModel):
    """Configuration for D1 read replication."""

    mode: Literal["auto", "disabled"]
    """The read replication mode for the database.

    Mode 'auto' denotes that D1 creates replicas and automatically places them
    around the world. Mode 'disabled' denotes that no database replicas are used.
    """


class D1(BaseModel):
    """The details of the D1 database."""

    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    file_size: Optional[float] = None
    """The D1 database's size, in bytes."""

    jurisdiction: Optional[Literal["eu", "fedramp"]] = None
    """Specify the location to restrict the D1 database to run and store data.

    If this option is present, the location hint is ignored.
    """

    name: Optional[str] = None
    """D1 database name."""

    num_tables: Optional[float] = None

    read_replication: Optional[ReadReplication] = None
    """Configuration for D1 read replication."""

    uuid: Optional[str] = None
    """D1 database identifier (UUID)."""

    version: Optional[str] = None
