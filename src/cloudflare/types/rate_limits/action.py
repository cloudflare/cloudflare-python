# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Action"]

Action: TypeAlias = Literal["block", "challenge", "js_challenge", "managed_challenge", "allow", "log", "bypass"]
