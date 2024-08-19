# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyListParams"]


class KeyListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cursor: str
    """
    Opaque token indicating the position from which to continue when requesting the
    next set of records if the amount of list results was limited by the limit
    parameter. A valid value for the cursor can be obtained from the `cursors`
    object in the `result_info` structure.
    """

    limit: float
    """The number of keys to return.

    The cursor attribute may be used to iterate over the next batch of keys if there
    are more than the limit.
    """

    prefix: str
    """A string prefix used to filter down which keys will be returned.

    Exact matches and any key names that begin with the prefix will be returned.
    """
