# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .lists import (
    Lists,
    AsyncLists,
    ListsWithRawResponse,
    AsyncListsWithRawResponse,
    ListsWithStreamingResponse,
    AsyncListsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .lists.lists import Lists, AsyncLists

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def lists(self) -> Lists:
        return Lists(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)


class AsyncRules(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncLists:
        return AsyncLists(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsWithRawResponse:
        return ListsWithRawResponse(self._rules.lists)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsWithRawResponse:
        return AsyncListsWithRawResponse(self._rules.lists)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsWithStreamingResponse:
        return ListsWithStreamingResponse(self._rules.lists)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsWithStreamingResponse:
        return AsyncListsWithStreamingResponse(self._rules.lists)
