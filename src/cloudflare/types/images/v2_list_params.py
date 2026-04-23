# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V2ListParams", "Meta"]


class V2ListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    continuation_token: Optional[str]
    """Continuation token to fetch next page.

    Passed as a query param when requesting List V2 api endpoint.
    """

    creator: Optional[str]
    """Internal user ID set within the creator field.

    Setting to empty string "" will return images where creator field is not set
    """

    meta: Meta

    per_page: float
    """Number of items per page"""

    sort_order: Literal["asc", "desc"]
    """Sorting order by upload time"""


class Meta(TypedDict, total=False):
    field_operator: Annotated[str, PropertyInfo(alias="<field>[<operator>]")]
    """Optional metadata filter(s). Multiple filters can be combined with AND logic.

    **Operators:**

    - `eq`, `eq:string`, `eq:number`, `eq:boolean` - Exact match
    - `in`, `in:string`, `in:number` - Match any value in pipe-separated list

    **Examples:**

    - `meta.status[eq]=active`
    - `meta.priority[eq:number]=5`
    - `meta.enabled[eq:boolean]=true`
    - `meta.region[in]=us-east|us-west|eu-west`
    """
