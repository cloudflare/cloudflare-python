# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AccessRules", "AsyncAccessRules"]


class AccessRules(SyncAPIResource):
    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self)


class AsyncAccessRules(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self)


class AccessRulesWithRawResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._access_rules.rules)


class AsyncAccessRulesWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._access_rules.rules)


class AccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._access_rules.rules)


class AsyncAccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._access_rules.rules)
