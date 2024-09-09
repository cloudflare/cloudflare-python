# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = ["Script"]


class Script(BaseModel):
    id: Optional[str] = None
    """The id of the script in the Workers system. Usually the script name."""

    created_on: Optional[datetime] = None
    """When the script was created."""

    etag: Optional[str] = None
    """Hashed script content, can be used in a If-None-Match header when updating."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    placement_mode: Optional[str] = None
    """Specifies the placement mode for the Worker (e.g. 'smart')."""

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""
