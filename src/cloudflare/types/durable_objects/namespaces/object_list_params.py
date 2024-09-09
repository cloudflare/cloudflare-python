# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cursor: str
    """
    Opaque token indicating the position from which to continue when requesting the
    next set of records. A valid value for the cursor can be obtained from the
    cursors object in the result_info structure.
    """

    limit: float
    """The number of objects to return.

    The cursor attribute may be used to iterate over the next batch of objects if
    there are more than the limit.
    """
