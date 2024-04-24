# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zero_trust.dlp import payload_log_update_params
from ....types.zero_trust.dlp.payload_log_get_response import PayloadLogGetResponse
from ....types.zero_trust.dlp.payload_log_update_response import PayloadLogUpdateResponse

__all__ = ["PayloadLogsResource", "AsyncPayloadLogsResource"]


class PayloadLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayloadLogsResourceWithRawResponse:
        return PayloadLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayloadLogsResourceWithStreamingResponse:
        return PayloadLogsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        public_key: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogUpdateResponse:
        """
        Updates the DLP payload log settings for this account.

        Args:
          account_id: Identifier

          public_key: The public key to use when encrypting extracted payloads, as a base64 string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/dlp/payload_log",
            body=maybe_transform({"public_key": public_key}, payload_log_update_params.PayloadLogUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PayloadLogUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogUpdateResponse], ResultWrapper[PayloadLogUpdateResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogGetResponse:
        """
        Gets the current DLP payload log settings for this account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dlp/payload_log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PayloadLogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogGetResponse], ResultWrapper[PayloadLogGetResponse]),
        )


class AsyncPayloadLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayloadLogsResourceWithRawResponse:
        return AsyncPayloadLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayloadLogsResourceWithStreamingResponse:
        return AsyncPayloadLogsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        public_key: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogUpdateResponse:
        """
        Updates the DLP payload log settings for this account.

        Args:
          account_id: Identifier

          public_key: The public key to use when encrypting extracted payloads, as a base64 string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/dlp/payload_log",
            body=await async_maybe_transform(
                {"public_key": public_key}, payload_log_update_params.PayloadLogUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PayloadLogUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogUpdateResponse], ResultWrapper[PayloadLogUpdateResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogGetResponse:
        """
        Gets the current DLP payload log settings for this account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dlp/payload_log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PayloadLogGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogGetResponse], ResultWrapper[PayloadLogGetResponse]),
        )


class PayloadLogsResourceWithRawResponse:
    def __init__(self, payload_logs: PayloadLogsResource) -> None:
        self._payload_logs = payload_logs

        self.update = to_raw_response_wrapper(
            payload_logs.update,
        )
        self.get = to_raw_response_wrapper(
            payload_logs.get,
        )


class AsyncPayloadLogsResourceWithRawResponse:
    def __init__(self, payload_logs: AsyncPayloadLogsResource) -> None:
        self._payload_logs = payload_logs

        self.update = async_to_raw_response_wrapper(
            payload_logs.update,
        )
        self.get = async_to_raw_response_wrapper(
            payload_logs.get,
        )


class PayloadLogsResourceWithStreamingResponse:
    def __init__(self, payload_logs: PayloadLogsResource) -> None:
        self._payload_logs = payload_logs

        self.update = to_streamed_response_wrapper(
            payload_logs.update,
        )
        self.get = to_streamed_response_wrapper(
            payload_logs.get,
        )


class AsyncPayloadLogsResourceWithStreamingResponse:
    def __init__(self, payload_logs: AsyncPayloadLogsResource) -> None:
        self._payload_logs = payload_logs

        self.update = async_to_streamed_response_wrapper(
            payload_logs.update,
        )
        self.get = async_to_streamed_response_wrapper(
            payload_logs.get,
        )
