# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretUpdateParams"]


class SecretUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: str
    """
    The name of this secret, this is what will be used to access it inside the
    Worker.
    """

    text: str
    """The value of the secret."""

    type: Literal["secret_text"]
    """The type of secret to put."""
