# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

from typing import Dict

__all__ = ["WAFRuleParam"]

WAFRuleParam: TypeAlias = Dict[str, Literal["challenge", "block", "simulate", "disable", "default"]]
