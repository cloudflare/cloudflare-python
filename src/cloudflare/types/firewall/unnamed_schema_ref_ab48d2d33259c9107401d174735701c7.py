# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..._models import BaseModel
from ..firewall_filter import FirewallFilter

__all__ = ["UnnamedSchemaRefAb48d2d33259c9107401d174735701c7", "LegacyJhsDeletedFilter"]


class LegacyJhsDeletedFilter(BaseModel):
    id: str
    """The unique identifier of the filter."""

    deleted: bool
    """When true, indicates that the firewall rule was deleted."""


UnnamedSchemaRefAb48d2d33259c9107401d174735701c7 = Union[FirewallFilter, LegacyJhsDeletedFilter]
