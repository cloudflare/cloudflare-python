# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

from ...._types import SequenceNotStr

__all__ = ["SettingValueParam"]

SettingValueParam: TypeAlias = Union[Literal["1.0", "1.1", "1.2", "1.3", "on", "off"], SequenceNotStr[str]]
