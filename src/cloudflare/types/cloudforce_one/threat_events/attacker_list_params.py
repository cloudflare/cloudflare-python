# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AttackerListParams"]


class AttackerListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """Array of dataset IDs to query attackers from.

    If not provided, returns all attackers from Event DO tables.
    """
