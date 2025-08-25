# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = ["ScriptUpdateResponse", "NamedHandler", "Placement"]


class NamedHandler(BaseModel):
    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the named export."""

    name: Optional[str] = None
    """The name of the export."""


class Placement(BaseModel):
    last_analyzed_at: Optional[datetime] = None
    """
    The last time the script was analyzed for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    mode: Optional[Literal["smart"]] = None
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """


class ScriptUpdateResponse(BaseModel):
    startup_time_ms: int

    id: Optional[str] = None
    """The id of the script in the Workers system. Usually the script name."""

    compatibility_date: Optional[str] = None
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: Optional[List[str]] = None
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    created_on: Optional[datetime] = None
    """When the script was created."""

    etag: Optional[str] = None
    """Hashed script content, can be used in a If-None-Match header when updating."""

    handlers: Optional[List[str]] = None
    """The names of handlers exported as part of the default export."""

    has_assets: Optional[bool] = None
    """Whether a Worker contains assets."""

    has_modules: Optional[bool] = None
    """Whether a Worker contains modules."""

    last_deployed_from: Optional[str] = None
    """The client most recently used to deploy this Worker."""

    logpush: Optional[bool] = None
    """Whether Logpush is turned on for the Worker."""

    migration_tag: Optional[str] = None
    """
    The tag of the Durable Object migration that was most recently applied for this
    Worker.
    """

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    named_handlers: Optional[List[NamedHandler]] = None
    """
    Named exports, such as Durable Object class implementations and named
    entrypoints.
    """

    placement: Optional[Placement] = None
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    placement_mode: Optional[Literal["smart"]] = None

    placement_status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["standard", "bundled", "unbound"]] = None
    """Usage model for the Worker invocations."""
