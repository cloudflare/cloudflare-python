# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel
from ....workers.scripts.consumer_script import ConsumerScript

__all__ = ["ScriptUpdateResponse"]


class ScriptUpdateResponse(BaseModel):
    id: Optional[str] = None
    """The id of the script in the Workers system. Usually the script name."""

    created_on: Optional[datetime] = None
    """When the script was created."""

    etag: Optional[str] = None
    """Hashed script content, can be used in a If-None-Match header when updating."""

    has_assets: Optional[bool] = None
    """Whether a Worker contains assets."""

    has_modules: Optional[bool] = None
    """Whether a Worker contains modules."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    placement_mode: Optional[str] = None
    """Specifies the placement mode for the Worker (e.g. 'smart')."""

    startup_time_ms: Optional[int] = None

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["bundled", "unbound"]] = None
    """Usage model for the Worker invocations."""
