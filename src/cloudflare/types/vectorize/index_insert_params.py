# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IndexInsertParams"]


class IndexInsertParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[FileTypes]
    """ndjson file containing vectors to insert."""

    unparsable_behavior: Annotated[Literal["error", "discard"], PropertyInfo(alias="unparsable-behavior")]
    """Behavior for ndjson parse failures."""