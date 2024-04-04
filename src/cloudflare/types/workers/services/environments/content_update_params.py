# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .....types import shared_params
from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = ["ContentUpdateParams"]


class ContentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    service_name: Required[str]
    """Name of Worker to bind to"""

    any_part_name: Annotated[List[FileTypes], PropertyInfo(alias="<any part name>")]
    """A module comprising a Worker script, often a javascript file.

    Multiple modules may be provided as separate named parts, but at least one
    module must be present. This should be referenced either in the metadata as
    `main_module` (esm)/`body_part` (service worker) or as a header
    `CF-WORKER-MAIN-MODULE-PART` (esm) /`CF-WORKER-BODY-PART` (service worker) by
    part name.
    """

    metadata: shared_params.UnnamedSchemaRef51
    """JSON encoded metadata about the uploaded parts and Worker configuration."""
