# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatabaseExportParams", "DumpOptions"]


class DatabaseExportParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    output_format: Required[Literal["polling"]]
    """Specifies that you will poll this endpoint until the export completes"""

    current_bookmark: str
    """
    To poll an in-progress export, provide the current bookmark (returned by your
    first polling response)
    """

    dump_options: DumpOptions


class DumpOptions(TypedDict, total=False):
    no_data: bool
    """Export only the table definitions, not their contents"""

    no_schema: bool
    """Export only each table's contents, not its definition"""

    tables: List[str]
    """Filter the export to just one or more tables.

    Passing an empty array is the same as not passing anything and means: export all
    tables.
    """
