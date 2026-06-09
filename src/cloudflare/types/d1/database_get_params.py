# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatabaseGetParams"]


class DatabaseGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    fields: List[
        Literal[
            "uuid",
            "name",
            "created_at",
            "version",
            "jurisdiction",
            "num_tables",
            "file_size",
            "running_in_region",
            "read_replication",
        ]
    ]
    """Comma-separated list of fields to include in the response.

    When omitted, all fields are returned.
    """
