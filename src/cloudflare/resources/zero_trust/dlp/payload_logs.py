# File generated from our OpenAPI spec by Stainless.

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
from ....types.zero_trust.dlp import PayloadLogGetResponse, PayloadLogUpdateResponse, payload_log_update_params

__all__ = ["PayloadLogs", "AsyncPayloadLogs"]


class PayloadLogs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayloadLogsWithRawResponse:
        return PayloadLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayloadLogsWithStreamingResponse:
        return PayloadLogsWithStreamingResponse(self)

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
                post_parser=ResultWrapper._unwrapper,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogGetResponse], ResultWrapper[PayloadLogGetResponse]),
        )


class AsyncPayloadLogs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayloadLogsWithRawResponse:
        return AsyncPayloadLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayloadLogsWithStreamingResponse:
        return AsyncPayloadLogsWithStreamingResponse(self)

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
                post_parser=ResultWrapper._unwrapper,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PayloadLogGetResponse], ResultWrapper[PayloadLogGetResponse]),
        )


class PayloadLogsWithRawResponse:
    def __init__(self, payload_logs: PayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.update = to_raw_response_wrapper(
            payload_logs.update,
        )
        self.get = to_raw_response_wrapper(
            payload_logs.get,
        )


class AsyncPayloadLogsWithRawResponse:
    def __init__(self, payload_logs: AsyncPayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.update = async_to_raw_response_wrapper(
            payload_logs.update,
        )
        self.get = async_to_raw_response_wrapper(
            payload_logs.get,
        )


class PayloadLogsWithStreamingResponse:
    def __init__(self, payload_logs: PayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.update = to_streamed_response_wrapper(
            payload_logs.update,
        )
        self.get = to_streamed_response_wrapper(
            payload_logs.get,
        )


class AsyncPayloadLogsWithStreamingResponse:
    def __init__(self, payload_logs: AsyncPayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.update = async_to_streamed_response_wrapper(
            payload_logs.update,
        )
        self.get = async_to_streamed_response_wrapper(
            payload_logs.get,
        )
