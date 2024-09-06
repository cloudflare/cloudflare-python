# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import List, Iterable

from ...._types import FileTypes

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["VersionCreateParams", "Metadata", "MetadataAnnotations"]


class VersionCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    any_part_name: Annotated[List[FileTypes], PropertyInfo(alias="<any part name>")]
    """A module comprising a Worker script, often a javascript file.

    Multiple modules may be provided as separate named parts, but at least one
    module must be present and referenced in the metadata as `main_module`.
    """

    metadata: Metadata
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


class MetadataAnnotations(TypedDict, total=False):
    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the version."""

    workers_tag: Annotated[str, PropertyInfo(alias="workers/tag")]
    """User-provided identifier for the version."""


class Metadata(TypedDict, total=False):
    annotations: MetadataAnnotations

    bindings: Iterable[object]
    """List of bindings available to the worker."""

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: List[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    keep_bindings: List[str]
    """List of binding types to keep from previous_upload."""

    main_module: str
    """Name of the part in the multipart request that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """

    usage_model: Literal["standard"]
    """Usage model to apply to invocations."""
