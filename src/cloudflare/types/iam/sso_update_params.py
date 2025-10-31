# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSOUpdateParams"]


class SSOUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    enabled: bool
    """SSO Connector enabled state"""

    use_fedramp_language: bool
    """Controls the display of FedRAMP language to the user during SSO login"""
