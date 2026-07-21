# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_transit.connectors import interrupt_create_params
from ....types.magic_transit.connectors.interrupt_list_response import InterruptListResponse
from ....types.magic_transit.connectors.interrupt_create_response import InterruptCreateResponse

__all__ = ["InterruptsResource", "AsyncInterruptsResource"]


class InterruptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterruptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InterruptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterruptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InterruptsResourceWithStreamingResponse(self)

    def create(
        self,
        connector_id: str,
        *,
        account_id: str,
        reboot: interrupt_create_params.Reboot | Omit = omit,
        restart: interrupt_create_params.Restart | Omit = omit,
        shutdown: interrupt_create_params.Shutdown | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterruptCreateResponse:
        """
        Creates an interrupt for a Magic WAN Connector.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/magic/connectors/{connector_id}/interrupts",
                account_id=account_id,
                connector_id=connector_id,
            ),
            body=maybe_transform(
                {
                    "reboot": reboot,
                    "restart": restart,
                    "shutdown": shutdown,
                },
                interrupt_create_params.InterruptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InterruptCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InterruptCreateResponse], ResultWrapper[InterruptCreateResponse]),
        )

    def list(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[InterruptListResponse]:
        """
        Lists interrupts for a Magic WAN Connector.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/connectors/{connector_id}/interrupts",
                account_id=account_id,
                connector_id=connector_id,
            ),
            page=SyncSinglePage[InterruptListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=InterruptListResponse,
        )


class AsyncInterruptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterruptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterruptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterruptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInterruptsResourceWithStreamingResponse(self)

    async def create(
        self,
        connector_id: str,
        *,
        account_id: str,
        reboot: interrupt_create_params.Reboot | Omit = omit,
        restart: interrupt_create_params.Restart | Omit = omit,
        shutdown: interrupt_create_params.Shutdown | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterruptCreateResponse:
        """
        Creates an interrupt for a Magic WAN Connector.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/magic/connectors/{connector_id}/interrupts",
                account_id=account_id,
                connector_id=connector_id,
            ),
            body=await async_maybe_transform(
                {
                    "reboot": reboot,
                    "restart": restart,
                    "shutdown": shutdown,
                },
                interrupt_create_params.InterruptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InterruptCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[InterruptCreateResponse], ResultWrapper[InterruptCreateResponse]),
        )

    def list(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InterruptListResponse, AsyncSinglePage[InterruptListResponse]]:
        """
        Lists interrupts for a Magic WAN Connector.

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/connectors/{connector_id}/interrupts",
                account_id=account_id,
                connector_id=connector_id,
            ),
            page=AsyncSinglePage[InterruptListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=InterruptListResponse,
        )


class InterruptsResourceWithRawResponse:
    def __init__(self, interrupts: InterruptsResource) -> None:
        self._interrupts = interrupts

        self.create = to_raw_response_wrapper(
            interrupts.create,
        )
        self.list = to_raw_response_wrapper(
            interrupts.list,
        )


class AsyncInterruptsResourceWithRawResponse:
    def __init__(self, interrupts: AsyncInterruptsResource) -> None:
        self._interrupts = interrupts

        self.create = async_to_raw_response_wrapper(
            interrupts.create,
        )
        self.list = async_to_raw_response_wrapper(
            interrupts.list,
        )


class InterruptsResourceWithStreamingResponse:
    def __init__(self, interrupts: InterruptsResource) -> None:
        self._interrupts = interrupts

        self.create = to_streamed_response_wrapper(
            interrupts.create,
        )
        self.list = to_streamed_response_wrapper(
            interrupts.list,
        )


class AsyncInterruptsResourceWithStreamingResponse:
    def __init__(self, interrupts: AsyncInterruptsResource) -> None:
        self._interrupts = interrupts

        self.create = async_to_streamed_response_wrapper(
            interrupts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            interrupts.list,
        )
