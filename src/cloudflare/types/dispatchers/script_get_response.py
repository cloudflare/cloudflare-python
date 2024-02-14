# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ScriptGetResponse", "Script", "ScriptTailConsumer"]


class ScriptTailConsumer(BaseModel):
    service: str
    """Name of Worker that is to be the consumer."""

    environment: Optional[str] = None
    """Optional environment if the Worker utilizes one."""

    namespace: Optional[str] = None
    """Optional dispatch namespace the script belongs to."""


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

    pipeline_hash: Optional[str] = None
    """Deprecated. Deployment metadata for internal usage."""

    placement_mode: Optional[str] = None
    """Specifies the placement mode for the Worker (e.g. 'smart')."""

    tail_consumers: Optional[List[ScriptTailConsumer]] = None
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Optional[str] = None
    """Specifies the usage model for the Worker (e.g. 'bundled' or 'unbound')."""


class ScriptGetResponse(BaseModel):
    created_on: Optional[datetime] = None
    """When the script was created."""

    dispatch_namespace: Optional[str] = None
    """Name of the Workers for Platforms dispatch namespace."""

    modified_on: Optional[datetime] = None
    """When the script was last modified."""

    script: Optional[Script] = None
