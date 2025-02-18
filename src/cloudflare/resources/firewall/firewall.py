# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .waf.waf import (
    WAFResource,
    AsyncWAFResource,
    WAFResourceWithRawResponse,
    AsyncWAFResourceWithRawResponse,
    WAFResourceWithStreamingResponse,
    AsyncWAFResourceWithStreamingResponse,
)
from .ua_rules import (
    UARulesResource,
    AsyncUARulesResource,
    UARulesResourceWithRawResponse,
    AsyncUARulesResourceWithRawResponse,
    UARulesResourceWithStreamingResponse,
    AsyncUARulesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .lockdowns import (
    LockdownsResource,
    AsyncLockdownsResource,
    LockdownsResourceWithRawResponse,
    AsyncLockdownsResourceWithRawResponse,
    LockdownsResourceWithStreamingResponse,
    AsyncLockdownsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .access_rules import (
    AccessRulesResource,
    AsyncAccessRulesResource,
    AccessRulesResourceWithRawResponse,
    AsyncAccessRulesResourceWithRawResponse,
    AccessRulesResourceWithStreamingResponse,
    AsyncAccessRulesResourceWithStreamingResponse,
)

__all__ = ["FirewallResource", "AsyncFirewallResource"]


class FirewallResource(SyncAPIResource):
    @cached_property
    def lockdowns(self) -> LockdownsResource:
        return LockdownsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def access_rules(self) -> AccessRulesResource:
        return AccessRulesResource(self._client)

    @cached_property
    def ua_rules(self) -> UARulesResource:
        return UARulesResource(self._client)

    @cached_property
    def waf(self) -> WAFResource:
        return WAFResource(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FirewallResourceWithStreamingResponse(self)


class AsyncFirewallResource(AsyncAPIResource):
    @cached_property
    def lockdowns(self) -> AsyncLockdownsResource:
        return AsyncLockdownsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesResource:
        return AsyncAccessRulesResource(self._client)

    @cached_property
    def ua_rules(self) -> AsyncUARulesResource:
        return AsyncUARulesResource(self._client)

    @cached_property
    def waf(self) -> AsyncWAFResource:
        return AsyncWAFResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFirewallResourceWithStreamingResponse(self)


class FirewallResourceWithRawResponse:
    def __init__(self, firewall: FirewallResource) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> LockdownsResourceWithRawResponse:
        return LockdownsResourceWithRawResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AccessRulesResourceWithRawResponse:
        return AccessRulesResourceWithRawResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> UARulesResourceWithRawResponse:
        return UARulesResourceWithRawResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> WAFResourceWithRawResponse:
        return WAFResourceWithRawResponse(self._firewall.waf)


class AsyncFirewallResourceWithRawResponse:
    def __init__(self, firewall: AsyncFirewallResource) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> AsyncLockdownsResourceWithRawResponse:
        return AsyncLockdownsResourceWithRawResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesResourceWithRawResponse:
        return AsyncAccessRulesResourceWithRawResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUARulesResourceWithRawResponse:
        return AsyncUARulesResourceWithRawResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFResourceWithRawResponse:
        return AsyncWAFResourceWithRawResponse(self._firewall.waf)


class FirewallResourceWithStreamingResponse:
    def __init__(self, firewall: FirewallResource) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> LockdownsResourceWithStreamingResponse:
        return LockdownsResourceWithStreamingResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AccessRulesResourceWithStreamingResponse:
        return AccessRulesResourceWithStreamingResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> UARulesResourceWithStreamingResponse:
        return UARulesResourceWithStreamingResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> WAFResourceWithStreamingResponse:
        return WAFResourceWithStreamingResponse(self._firewall.waf)


class AsyncFirewallResourceWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewallResource) -> None:
        self._firewall = firewall

    @cached_property
    def lockdowns(self) -> AsyncLockdownsResourceWithStreamingResponse:
        return AsyncLockdownsResourceWithStreamingResponse(self._firewall.lockdowns)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._firewall.rules)

    @cached_property
    def access_rules(self) -> AsyncAccessRulesResourceWithStreamingResponse:
        return AsyncAccessRulesResourceWithStreamingResponse(self._firewall.access_rules)

    @cached_property
    def ua_rules(self) -> AsyncUARulesResourceWithStreamingResponse:
        return AsyncUARulesResourceWithStreamingResponse(self._firewall.ua_rules)

    @cached_property
    def waf(self) -> AsyncWAFResourceWithStreamingResponse:
        return AsyncWAFResourceWithStreamingResponse(self._firewall.waf)
