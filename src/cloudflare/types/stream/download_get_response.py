# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DownloadGetResponse", "Audio", "Default"]


class Audio(BaseModel):
    """The audio-only download. Only present if this download type has been created."""

    percent_complete: Optional[float] = FieldInfo(alias="percentComplete", default=None)
    """Indicates the progress as a percentage between 0 and 100."""

    status: Optional[Literal["ready", "inprogress", "error"]] = None
    """The status of a generated download."""

    url: Optional[str] = None
    """The URL to access the generated download."""


class Default(BaseModel):
    """The default video download.

    Only present if this download type has been created.
    """

    percent_complete: Optional[float] = FieldInfo(alias="percentComplete", default=None)
    """Indicates the progress as a percentage between 0 and 100."""

    status: Optional[Literal["ready", "inprogress", "error"]] = None
    """The status of a generated download."""

    url: Optional[str] = None
    """The URL to access the generated download."""


class DownloadGetResponse(BaseModel):
    """An object with download type keys.

    Each key is optional and only present if that download type has been created.
    """

    audio: Optional[Audio] = None
    """The audio-only download. Only present if this download type has been created."""

    default: Optional[Default] = None
    """The default video download.

    Only present if this download type has been created.
    """
