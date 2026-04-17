# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RegistrarCheckParams"]


class RegistrarCheckParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    domains: Required[SequenceNotStr[str]]
    """List of fully qualified domain names (FQDNs) to check for availability.

    Each domain must include the extension.

    - Minimum: 1 domain
    - Maximum: 20 domains per request
    - Domains on unsupported extensions are returned with `registrable: false` and a
      `reason` field
    - Malformed domain names (e.g., missing extension) may be omitted from the
      response
    """
