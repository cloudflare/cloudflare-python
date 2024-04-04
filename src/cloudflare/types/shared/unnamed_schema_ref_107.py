# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..._models import BaseModel
from ..firewall_filter import FirewallFilter

__all__ = ["UnnamedSchemaRef107", "LegacyJhsDeletedFilter"]


class LegacyJhsDeletedFilter(BaseModel):
    id: str
    """The unique identifier of the filter."""

    deleted: bool
    """When true, indicates that the firewall rule was deleted."""


UnnamedSchemaRef107 = Union[FirewallFilter, LegacyJhsDeletedFilter]
