# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["UniqueDeviceListParams"]


class UniqueDeviceListParams(TypedDict, total=False):
    account_id: Required[str]

    device_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="deviceId")]
    """Optionally filter result stats to a specific device(s).

    Cannot be used in combination with colo param.
    """

    test_name: Annotated[str, PropertyInfo(alias="testName")]
    """Optionally filter results by test name"""
