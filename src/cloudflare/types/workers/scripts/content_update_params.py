# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..worker_metadata_param import WorkerMetadataParam

__all__ = ["ContentUpdateParams"]


class ContentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    metadata: Required[WorkerMetadataParam]
    """JSON encoded metadata about the uploaded parts and Worker configuration."""

    cf_worker_body_part: Annotated[str, PropertyInfo(alias="CF-WORKER-BODY-PART")]

    cf_worker_main_module_part: Annotated[str, PropertyInfo(alias="CF-WORKER-MAIN-MODULE-PART")]
