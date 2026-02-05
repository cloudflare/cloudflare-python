# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["NamespaceGetResponse"]


class NamespaceGetResponse(BaseModel):
    created_by: Optional[str] = None
    """Identifier."""

    created_on: Optional[datetime] = None
    """When the script was created."""

    modified_by: Optional[str] = None
    """Identifier."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    namespace_id: Optional[str] = None
    """API Resource UUID tag."""

    namespace_name: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""

    script_count: Optional[int] = None
    """The current number of scripts in this Dispatch Namespace."""

    trusted_workers: Optional[bool] = None
    """Whether the Workers in the namespace are executed in a "trusted" manner.

    When a Worker is trusted, it has access to the shared caches for the zone in the
    Cache API, and has access to the `request.cf` object on incoming Requests. When
    a Worker is untrusted, caches are not shared across the zone, and `request.cf`
    is undefined. By default, Workers in a namespace are "untrusted".
    """
