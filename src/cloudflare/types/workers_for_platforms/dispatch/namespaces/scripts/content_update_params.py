# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ContentUpdateParams"]


class ContentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    metadata: Required[object]

    cf_worker_body_part: Annotated[str, PropertyInfo(alias="CF-WORKER-BODY-PART")]

    cf_worker_main_module_part: Annotated[str, PropertyInfo(alias="CF-WORKER-MAIN-MODULE-PART")]
