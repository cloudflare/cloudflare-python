# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ......_types import FileTypes
from ......_utils import PropertyInfo

__all__ = ["ContentUpdateParams", "Metadata"]


class ContentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    any_part_name: Annotated[List[FileTypes], PropertyInfo(alias="<any part name>")]
    """A module comprising a Worker script, often a javascript file.

    Multiple modules may be provided as separate named parts, but at least one
    module must be present. This should be referenced either in the metadata as
    `main_module` (esm)/`body_part` (service worker) or as a header
    `CF-WORKER-MAIN-MODULE-PART` (esm) /`CF-WORKER-BODY-PART` (service worker) by
    part name.
    """

    metadata: Metadata
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


class Metadata(TypedDict, total=False):
    body_part: str
    """Name of the part in the multipart request that contains the script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
    """

    main_module: str
    """Name of the part in the multipart request that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """
