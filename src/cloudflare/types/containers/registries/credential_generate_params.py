# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CredentialGenerateParams"]


class CredentialGenerateParams(TypedDict, total=False):
    account_id: Required[str]

    expiration_minutes: int
    """The number of minutes Cloudflare managed registry credentials stay valid.

    Required for managed registries and must remain positive. Cloudflare ignores
    this value for external registries.
    """

    permissions: List[Literal["pull", "push", "list"]]
    """The permissions for Cloudflare managed registry credentials.

    Required for managed registries. Cloudflare ignores this value for external
    registries.
    """
