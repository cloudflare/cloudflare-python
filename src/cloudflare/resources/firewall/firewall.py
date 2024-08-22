# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .lockdowns import LockdownsResource, AsyncLockdownsResource

from ..._compat import cached_property

from .rules import RulesResource, AsyncRulesResource

from .access_rules import AccessRulesResource, AsyncAccessRulesResource

from .ua_rules import UARulesResource, AsyncUARulesResource

from .waf.waf import WAFResource, AsyncWAFResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .lockdowns import LockdownsResource, AsyncLockdownsResource, LockdownsResourceWithRawResponse, AsyncLockdownsResourceWithRawResponse, LockdownsResourceWithStreamingResponse, AsyncLockdownsResourceWithStreamingResponse
from .rules import RulesResource, AsyncRulesResource, RulesResourceWithRawResponse, AsyncRulesResourceWithRawResponse, RulesResourceWithStreamingResponse, AsyncRulesResourceWithStreamingResponse
from .access_rules import AccessRulesResource, AsyncAccessRulesResource, AccessRulesResourceWithRawResponse, AsyncAccessRulesResourceWithRawResponse, AccessRulesResourceWithStreamingResponse, AsyncAccessRulesResourceWithStreamingResponse
from .ua_rules import UARulesResource, AsyncUARulesResource, UARulesResourceWithRawResponse, AsyncUARulesResourceWithRawResponse, UARulesResourceWithStreamingResponse, AsyncUARulesResourceWithStreamingResponse
from .waf import WAFResource, AsyncWAFResource, WAFResourceWithRawResponse, AsyncWAFResourceWithRawResponse, WAFResourceWithStreamingResponse, AsyncWAFResourceWithStreamingResponse

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
        return FirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallResourceWithStreamingResponse:
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
        return AsyncFirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallResourceWithStreamingResponse:
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