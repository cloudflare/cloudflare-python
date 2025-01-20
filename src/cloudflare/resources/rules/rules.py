# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .lists.lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._rules.lists)


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._rules.lists)


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._rules.lists)


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._rules.lists)
