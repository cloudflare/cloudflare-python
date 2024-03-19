# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....workers import WorkersScript
from ....._models import BaseModel

__all__ = ["WorkersNamespaceScript"]


class WorkersNamespaceScript(BaseModel):
    created_on: Optional[datetime] = None
    """When the script was created."""

    dispatch_namespace: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    script: Optional[WorkersScript] = None
