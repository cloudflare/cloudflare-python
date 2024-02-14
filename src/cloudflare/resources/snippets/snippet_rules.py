# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.snippets import SnippetRuleListResponse, SnippetRuleUpdateResponse, snippet_rule_update_params

__all__ = ["SnippetRules", "AsyncSnippetRules"]


class SnippetRules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SnippetRulesWithRawResponse:
        return SnippetRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SnippetRulesWithStreamingResponse:
        return SnippetRulesWithStreamingResponse(self)

    def update(
        self,
        zone_identifier: str,
        *,
        rules: Iterable[snippet_rule_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetRuleUpdateResponse:
        """
        Put Rules

        Args:
          zone_identifier: Identifier

          rules: List of snippet rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/snippets/snippet_rules",
            body=maybe_transform({"rules": rules}, snippet_rule_update_params.SnippetRuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetRuleUpdateResponse], ResultWrapper[SnippetRuleUpdateResponse]),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetRuleListResponse:
        """
        Rules

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/snippets/snippet_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetRuleListResponse], ResultWrapper[SnippetRuleListResponse]),
        )


class AsyncSnippetRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSnippetRulesWithRawResponse:
        return AsyncSnippetRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSnippetRulesWithStreamingResponse:
        return AsyncSnippetRulesWithStreamingResponse(self)

    async def update(
        self,
        zone_identifier: str,
        *,
        rules: Iterable[snippet_rule_update_params.Rule] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetRuleUpdateResponse:
        """
        Put Rules

        Args:
          zone_identifier: Identifier

          rules: List of snippet rules

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/snippets/snippet_rules",
            body=maybe_transform({"rules": rules}, snippet_rule_update_params.SnippetRuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetRuleUpdateResponse], ResultWrapper[SnippetRuleUpdateResponse]),
        )

    async def list(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SnippetRuleListResponse:
        """
        Rules

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/snippets/snippet_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SnippetRuleListResponse], ResultWrapper[SnippetRuleListResponse]),
        )


class SnippetRulesWithRawResponse:
    def __init__(self, snippet_rules: SnippetRules) -> None:
        self._snippet_rules = snippet_rules

        self.update = to_raw_response_wrapper(
            snippet_rules.update,
        )
        self.list = to_raw_response_wrapper(
            snippet_rules.list,
        )


class AsyncSnippetRulesWithRawResponse:
    def __init__(self, snippet_rules: AsyncSnippetRules) -> None:
        self._snippet_rules = snippet_rules

        self.update = async_to_raw_response_wrapper(
            snippet_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            snippet_rules.list,
        )


class SnippetRulesWithStreamingResponse:
    def __init__(self, snippet_rules: SnippetRules) -> None:
        self._snippet_rules = snippet_rules

        self.update = to_streamed_response_wrapper(
            snippet_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            snippet_rules.list,
        )


class AsyncSnippetRulesWithStreamingResponse:
    def __init__(self, snippet_rules: AsyncSnippetRules) -> None:
        self._snippet_rules = snippet_rules

        self.update = async_to_streamed_response_wrapper(
            snippet_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            snippet_rules.list,
        )
