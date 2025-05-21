# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["D1", "ReadReplication"]


class ReadReplication(BaseModel):
    mode: Literal["auto", "disabled"]
    """The read replication mode for the database.

    Use 'auto' to create replicas and allow D1 automatically place them around the
    world, or 'disabled' to not use any database replicas (it can take a few hours
    for all replicas to be deleted).
    """


class D1(BaseModel):
    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    file_size: Optional[float] = None
    """The D1 database's size, in bytes."""

    name: Optional[str] = None
    """D1 database name."""

    num_tables: Optional[float] = None

    read_replication: Optional[ReadReplication] = None
    """Configuration for D1 read replication."""

    uuid: Optional[str] = None
    """D1 database identifier (UUID)."""

    version: Optional[str] = None
