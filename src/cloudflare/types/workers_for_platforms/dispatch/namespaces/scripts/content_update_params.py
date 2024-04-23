# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ......_types import FileTypes
from ......_utils import PropertyInfo
from .....workers.worker_metadata_param import WorkerMetadataParam

__all__ = ["ContentUpdateParams"]


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
    part name. Source maps may also be included using the `application/source-map`
    content type.
    """

    metadata: WorkerMetadataParam
    """JSON encoded metadata about the uploaded parts and Worker configuration."""
