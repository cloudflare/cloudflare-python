# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SchemaListParams"]


class SchemaListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]]
    """Add feature(s) to the results.

    The feature name that is given here corresponds to the resulting feature object.
    Have a look at the top-level object description for more details on the specific
    meaning.
    """

    host: List[str]
    """Receive schema only for the given host(s)."""
