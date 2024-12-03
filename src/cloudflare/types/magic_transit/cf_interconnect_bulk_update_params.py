# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CfInterconnectBulkUpdateParams"]


class CfInterconnectBulkUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[object]

    x_magic_new_hc_target: Annotated[bool, PropertyInfo(alias="x-magic-new-hc-target")]
