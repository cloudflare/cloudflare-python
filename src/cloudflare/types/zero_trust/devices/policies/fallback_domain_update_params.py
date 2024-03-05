# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .teams_devices_fallback_domain_param import TeamsDevicesFallbackDomainParam

__all__ = ["FallbackDomainUpdateParams"]


class FallbackDomainUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    body: Required[Iterable[TeamsDevicesFallbackDomainParam]]
