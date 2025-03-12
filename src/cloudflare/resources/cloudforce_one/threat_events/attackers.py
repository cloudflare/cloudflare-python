# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.attacker_list_response import AttackerListResponse

__all__ = ["AttackersResource", "AsyncAttackersResource"]


class AttackersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttackersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AttackersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttackersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AttackersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttackerListResponse:
        """
        Lists attackers

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/attackers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttackerListResponse,
        )


class AsyncAttackersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttackersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttackersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttackersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAttackersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttackerListResponse:
        """
        Lists attackers

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/attackers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttackerListResponse,
        )


class AttackersResourceWithRawResponse:
    def __init__(self, attackers: AttackersResource) -> None:
        self._attackers = attackers

        self.list = to_raw_response_wrapper(
            attackers.list,
        )


class AsyncAttackersResourceWithRawResponse:
    def __init__(self, attackers: AsyncAttackersResource) -> None:
        self._attackers = attackers

        self.list = async_to_raw_response_wrapper(
            attackers.list,
        )


class AttackersResourceWithStreamingResponse:
    def __init__(self, attackers: AttackersResource) -> None:
        self._attackers = attackers

        self.list = to_streamed_response_wrapper(
            attackers.list,
        )


class AsyncAttackersResourceWithStreamingResponse:
    def __init__(self, attackers: AsyncAttackersResource) -> None:
        self._attackers = attackers

        self.list = async_to_streamed_response_wrapper(
            attackers.list,
        )
