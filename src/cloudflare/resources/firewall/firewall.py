# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    UARules,
    AsyncUARules,
    UARulesWithRawResponse,
    AsyncUARulesWithRawResponse,
    UARulesWithStreamingResponse,
    AsyncUARulesWithStreamingResponse,
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

__all__ = ["Firewall", "AsyncFirewall"]


class Firewall(SyncAPIResource):
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
    def ua_rules(self) -> UARules:
        return UARules(self._client)

    @cached_property
    def waf(self) -> WAF:
        return WAF(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallWithRawResponse:
        return FirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallWithStreamingResponse:
        return FirewallWithStreamingResponse(self)


class AsyncFirewall(AsyncAPIResource):
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
    def ua_rules(self) -> AsyncUARules:
        return AsyncUARules(self._client)

    @cached_property
    def waf(self) -> AsyncWAF:
        return AsyncWAF(self._client)

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
    def lockdowns(self) -> LockdownsWithRawResponse:
        return LockdownsWithRawResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> UARulesWithRawResponse:
        return UARulesWithRawResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> WAFWithRawResponse:
        return WAFWithRawResponse(self._firewall.waf)


class AsyncFirewallWithRawResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> AsyncLockdownsWithRawResponse:
        return AsyncLockdownsWithRawResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUARulesWithRawResponse:
        return AsyncUARulesWithRawResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFWithRawResponse:
        return AsyncWAFWithRawResponse(self._firewall.waf)


class FirewallWithStreamingResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> LockdownsWithStreamingResponse:
        return LockdownsWithStreamingResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> UARulesWithStreamingResponse:
        return UARulesWithStreamingResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> WAFWithStreamingResponse:
        return WAFWithStreamingResponse(self._firewall.waf)


class AsyncFirewallWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> AsyncLockdownsWithStreamingResponse:
        return AsyncLockdownsWithStreamingResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUARulesWithStreamingResponse:
        return AsyncUARulesWithStreamingResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFWithStreamingResponse:
        return AsyncWAFWithStreamingResponse(self._firewall.waf)
