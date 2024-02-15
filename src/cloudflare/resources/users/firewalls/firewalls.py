# File generated from our OpenAPI spec by Stainless.

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
from .access_rules.access_rules import AccessRules, AsyncAccessRules

__all__ = ["Firewalls", "AsyncFirewalls"]


class Firewalls(SyncAPIResource):
    @cached_property
    def access_rules(self) -> AccessRules:
        return AccessRules(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallsWithRawResponse:
        return FirewallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallsWithStreamingResponse:
        return FirewallsWithStreamingResponse(self)


class AsyncFirewalls(AsyncAPIResource):
    @cached_property
    def access_rules(self) -> AsyncAccessRules:
        return AsyncAccessRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallsWithRawResponse:
        return AsyncFirewallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallsWithStreamingResponse:
        return AsyncFirewallsWithStreamingResponse(self)


class FirewallsWithRawResponse:
    def __init__(self, firewalls: Firewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def access_rules(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self._firewalls.access_rules)


class AsyncFirewallsWithRawResponse:
    def __init__(self, firewalls: AsyncFirewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self._firewalls.access_rules)


class FirewallsWithStreamingResponse:
    def __init__(self, firewalls: Firewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def access_rules(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self._firewalls.access_rules)


class AsyncFirewallsWithStreamingResponse:
    def __init__(self, firewalls: AsyncFirewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self._firewalls.access_rules)
