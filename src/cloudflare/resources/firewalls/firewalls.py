# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .waf import (
    WAF,
    AsyncWAF,
    WAFWithRawResponse,
    AsyncWAFWithRawResponse,
    WAFWithStreamingResponse,
    AsyncWAFWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from .waf.waf import WAF, AsyncWAF
from .ua_rules import (
    UaRules,
    AsyncUaRules,
    UaRulesWithRawResponse,
    AsyncUaRulesWithRawResponse,
    UaRulesWithStreamingResponse,
    AsyncUaRulesWithStreamingResponse,
)
from ..._compat import cached_property
from .lockdowns import (
    Lockdowns,
    AsyncLockdowns,
    LockdownsWithRawResponse,
    AsyncLockdownsWithRawResponse,
    LockdownsWithStreamingResponse,
    AsyncLockdownsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .access_rules import (
    AccessRules,
    AsyncAccessRules,
    AccessRulesWithRawResponse,
    AsyncAccessRulesWithRawResponse,
    AccessRulesWithStreamingResponse,
    AsyncAccessRulesWithStreamingResponse,
)

__all__ = ["Firewalls", "AsyncFirewalls"]


class Firewalls(SyncAPIResource):
    @cached_property
    def lockdowns(self) -> Lockdowns:
        return Lockdowns(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def access_rules(self) -> AccessRules:
        return AccessRules(self._client)

    @cached_property
    def ua_rules(self) -> UaRules:
        return UaRules(self._client)

    @cached_property
    def waf(self) -> WAF:
        return WAF(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallsWithRawResponse:
        return FirewallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallsWithStreamingResponse:
        return FirewallsWithStreamingResponse(self)


class AsyncFirewalls(AsyncAPIResource):
    @cached_property
    def lockdowns(self) -> AsyncLockdowns:
        return AsyncLockdowns(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def access_rules(self) -> AsyncAccessRules:
        return AsyncAccessRules(self._client)

    @cached_property
    def ua_rules(self) -> AsyncUaRules:
        return AsyncUaRules(self._client)

    @cached_property
    def waf(self) -> AsyncWAF:
        return AsyncWAF(self._client)

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
    def lockdowns(self) -> LockdownsWithRawResponse:
        return LockdownsWithRawResponse(self._firewalls.lockdowns)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._firewalls.rules)

    @cached_property
    def access_rules(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self._firewalls.access_rules)

    @cached_property
    def ua_rules(self) -> UaRulesWithRawResponse:
        return UaRulesWithRawResponse(self._firewalls.ua_rules)

    @cached_property
    def waf(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self._firewalls.waf)


class AsyncFirewallsWithRawResponse:
    def __init__(self, firewalls: AsyncFirewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def lockdowns(self) -> AsyncLockdownsWithRawResponse:
        return AsyncLockdownsWithRawResponse(self._firewalls.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._firewalls.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self._firewalls.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUaRulesWithRawResponse:
        return AsyncUaRulesWithRawResponse(self._firewalls.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self._firewalls.waf)


class FirewallsWithStreamingResponse:
    def __init__(self, firewalls: Firewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def lockdowns(self) -> LockdownsWithStreamingResponse:
        return LockdownsWithStreamingResponse(self._firewalls.lockdowns)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._firewalls.rules)

    @cached_property
    def access_rules(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self._firewalls.access_rules)

    @cached_property
    def ua_rules(self) -> UaRulesWithStreamingResponse:
        return UaRulesWithStreamingResponse(self._firewalls.ua_rules)

    @cached_property
    def waf(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self._firewalls.waf)


class AsyncFirewallsWithStreamingResponse:
    def __init__(self, firewalls: AsyncFirewalls) -> None:
        self._firewalls = firewalls

    @cached_property
    def lockdowns(self) -> AsyncLockdownsWithStreamingResponse:
        return AsyncLockdownsWithStreamingResponse(self._firewalls.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._firewalls.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self._firewalls.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUaRulesWithStreamingResponse:
        return AsyncUaRulesWithStreamingResponse(self._firewalls.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self._firewalls.waf)
