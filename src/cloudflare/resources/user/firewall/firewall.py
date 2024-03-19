# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .access_rules import (
    AccessRules,
    AsyncAccessRules,
    AccessRulesWithRawResponse,
    AsyncAccessRulesWithRawResponse,
    AccessRulesWithStreamingResponse,
    AsyncAccessRulesWithStreamingResponse,
)

__all__ = ["Firewall", "AsyncFirewall"]


class Firewall(SyncAPIResource):
    @cached_property
    def access_rules(self) -> AccessRules:
        return AccessRules(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallWithRawResponse:
        return FirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallWithStreamingResponse:
        return FirewallWithStreamingResponse(self)


class AsyncFirewall(AsyncAPIResource):
    @cached_property
    def access_rules(self) -> AsyncAccessRules:
        return AsyncAccessRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallWithRawResponse:
        return AsyncFirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallWithStreamingResponse:
        return AsyncFirewallWithStreamingResponse(self)


class FirewallWithRawResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

    @cached_property
    def access_rules(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self._firewall.access_rules)


class AsyncFirewallWithRawResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self._firewall.access_rules)


class FirewallWithStreamingResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

    @cached_property
    def access_rules(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self._firewall.access_rules)


class AsyncFirewallWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self._firewall.access_rules)
