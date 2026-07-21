# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmailRoutingUpdateParams"]


class EmailRoutingUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    enabled: Literal[True, False]
    """State of your zone Email Routing settings.

    No-op on this endpoint - use `POST`/`DELETE /zones/{zone_id}/email/routing/dns`.
    """

    skip_wizard: Literal[True, False]
    """Flag to check if the user skipped the configuration wizard."""

    support_subaddress: Literal[True, False]
    """
    Whether subaddressing (plus-addressing) is honored when matching incoming mail
    against routing rules.
    """
