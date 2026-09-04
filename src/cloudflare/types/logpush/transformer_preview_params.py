# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TransformerPreviewParams"]


class TransformerPreviewParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    input: Required[Dict[str, object]]
    """A single log record to transform (JSON object)."""

    sql: Required[str]
    """The SQL transformer query.

    Maximum 32 KB. The query must contain a FROM clause referencing a valid logpush
    dataset.
    """
