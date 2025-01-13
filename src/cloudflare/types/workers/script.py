# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .scripts.consumer_script import ConsumerScript

__all__ = ["Script", "Placement"]


class Placement(BaseModel):
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


class Script(BaseModel):
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

    placement: Optional[Placement] = None
    """
    Configuration for
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    placement_mode: Optional[Literal["smart"]] = None
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    placement_status: Optional[Literal["SUCCESS", "UNSUPPORTED_APPLICATION", "INSUFFICIENT_INVOCATIONS"]] = None
    """
    Status of
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    """

    tail_consumers: Optional[List[ConsumerScript]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[Literal["standard"]] = None
    """Usage model for the Worker invocations."""
