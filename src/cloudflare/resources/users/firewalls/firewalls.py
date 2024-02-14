# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .access_rules.access_rules import AccessRules, AsyncAccessRules

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .access_rules import (
    AccessRules,
    AsyncAccessRules,
    AccessRulesWithRawResponse,
    AsyncAccessRulesWithRawResponse,
    AccessRulesWithStreamingResponse,
    AsyncAccessRulesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

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
