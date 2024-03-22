# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....types import RulesetsRulesetResponse
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)

__all__ = ["ByTag", "AsyncByTag"]


class ByTag(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByTagWithRawResponse:
        return ByTagWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByTagWithStreamingResponse:
        return ByTagWithStreamingResponse(self)

    def get(
        self,
        rule_tag: str,
        *,
        account_id: str,
        ruleset_id: str,
        ruleset_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """
        Fetches the rules of a managed account ruleset version for a given tag.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          rule_tag: A category of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        if not rule_tag:
            raise ValueError(f"Expected a non-empty value for `rule_tag` but received {rule_tag!r}")
        return self._get(
            f"/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )


class AsyncByTag(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByTagWithRawResponse:
        return AsyncByTagWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByTagWithStreamingResponse:
        return AsyncByTagWithStreamingResponse(self)

    async def get(
        self,
        rule_tag: str,
        *,
        account_id: str,
        ruleset_id: str,
        ruleset_version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """
        Fetches the rules of a managed account ruleset version for a given tag.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          rule_tag: A category of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        if not rule_tag:
            raise ValueError(f"Expected a non-empty value for `rule_tag` but received {rule_tag!r}")
        return await self._get(
            f"/accounts/{account_id}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )


class ByTagWithRawResponse:
    def __init__(self, by_tag: ByTag) -> None:
        self._by_tag = by_tag

        self.get = to_raw_response_wrapper(
            by_tag.get,
        )


class AsyncByTagWithRawResponse:
    def __init__(self, by_tag: AsyncByTag) -> None:
        self._by_tag = by_tag

        self.get = async_to_raw_response_wrapper(
            by_tag.get,
        )


class ByTagWithStreamingResponse:
    def __init__(self, by_tag: ByTag) -> None:
        self._by_tag = by_tag

        self.get = to_streamed_response_wrapper(
            by_tag.get,
        )


class AsyncByTagWithStreamingResponse:
    def __init__(self, by_tag: AsyncByTag) -> None:
        self._by_tag = by_tag

        self.get = async_to_streamed_response_wrapper(
            by_tag.get,
        )
