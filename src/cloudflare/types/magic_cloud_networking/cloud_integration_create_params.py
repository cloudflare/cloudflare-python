# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CloudIntegrationCreateParams"]


class CloudIntegrationCreateParams(TypedDict, total=False):
    account_id: Required[str]

    cloud_type: Required[Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"]]

    friendly_name: Required[str]

    description: str

    forwarded: str
