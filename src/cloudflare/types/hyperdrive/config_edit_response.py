# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .hyperdrive import Hyperdrive

__all__ = ["ConfigEditResponse"]


class ConfigEditResponse(Hyperdrive):
    created_on: Optional[datetime] = None
    """When the Hyperdrive configuration was created."""

    modified_on: Optional[datetime] = None
    """When the Hyperdrive configuration was last modified."""
