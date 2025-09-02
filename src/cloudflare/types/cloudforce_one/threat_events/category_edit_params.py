# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CategoryEditParams"]


class CategoryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    kill_chain: Annotated[float, PropertyInfo(alias="killChain")]

    mitre_attack: Annotated[SequenceNotStr[str], PropertyInfo(alias="mitreAttack")]

    name: str

    shortname: str
