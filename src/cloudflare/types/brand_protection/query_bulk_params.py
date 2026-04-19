# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import TypedDict

__all__ = ["QueryBulkParams"]


class QueryBulkParams(TypedDict, total=False):
    account_id: str

    queries: Iterable[Dict[str, object]]
