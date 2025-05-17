# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SecretEditParams"]


class SecretEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    store_id: Required[str]
    """Store Identifier"""

    name: Required[str]
    """The name of the secret"""

    scopes: List[str]
    """The list of services that can use this secret."""

    value: str
    """The value of the secret.

    Note that this is 'write only' - no API reponse will provide this value, it is
    only used to create/modify secrets.
    """
