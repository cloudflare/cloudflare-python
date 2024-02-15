# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.secondary_dns import (
    TsigGetResponse,
    TsigDeleteResponse,
    TsigUpdateResponse,
    TsigSecondaryDNSTsigListTsiGsResponse,
    TsigSecondaryDNSTsigCreateTsigResponse,
    tsig_update_params,
    tsig_secondary_dns_tsig_create_tsig_params,
)

__all__ = ["Tsigs", "AsyncTsigs"]


class Tsigs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TsigsWithRawResponse:
        return TsigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TsigsWithStreamingResponse:
        return TsigsWithStreamingResponse(self)

    def update(
        self,
        tsig_id: object,
        *,
        account_id: object,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigUpdateResponse:
        """
        Modify TSIG.

        Args:
          algo: TSIG algorithm.

          name: TSIG key name.

          secret: TSIG secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            body=maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_update_params.TsigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigUpdateResponse], ResultWrapper[TsigUpdateResponse]),
        )

    def delete(
        self,
        tsig_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigDeleteResponse:
        """
        Delete TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigDeleteResponse], ResultWrapper[TsigDeleteResponse]),
        )

    def get(
        self,
        tsig_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigGetResponse:
        """
        Get TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigGetResponse], ResultWrapper[TsigGetResponse]),
        )

    def secondary_dns_tsig_create_tsig(
        self,
        account_id: object,
        *,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigSecondaryDNSTsigCreateTsigResponse:
        """
        Create TSIG.

        Args:
          algo: TSIG algorithm.

          name: TSIG key name.

          secret: TSIG secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            body=maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_secondary_dns_tsig_create_tsig_params.TsigSecondaryDNSTsigCreateTsigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TsigSecondaryDNSTsigCreateTsigResponse], ResultWrapper[TsigSecondaryDNSTsigCreateTsigResponse]
            ),
        )

    def secondary_dns_tsig_list_tsi_gs(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TsigSecondaryDNSTsigListTsiGsResponse]:
        """
        List TSIGs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TsigSecondaryDNSTsigListTsiGsResponse]],
                ResultWrapper[TsigSecondaryDNSTsigListTsiGsResponse],
            ),
        )


class AsyncTsigs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTsigsWithRawResponse:
        return AsyncTsigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTsigsWithStreamingResponse:
        return AsyncTsigsWithStreamingResponse(self)

    async def update(
        self,
        tsig_id: object,
        *,
        account_id: object,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigUpdateResponse:
        """
        Modify TSIG.

        Args:
          algo: TSIG algorithm.

          name: TSIG key name.

          secret: TSIG secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            body=maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_update_params.TsigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigUpdateResponse], ResultWrapper[TsigUpdateResponse]),
        )

    async def delete(
        self,
        tsig_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigDeleteResponse:
        """
        Delete TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigDeleteResponse], ResultWrapper[TsigDeleteResponse]),
        )

    async def get(
        self,
        tsig_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigGetResponse:
        """
        Get TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TsigGetResponse], ResultWrapper[TsigGetResponse]),
        )

    async def secondary_dns_tsig_create_tsig(
        self,
        account_id: object,
        *,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TsigSecondaryDNSTsigCreateTsigResponse:
        """
        Create TSIG.

        Args:
          algo: TSIG algorithm.

          name: TSIG key name.

          secret: TSIG secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            body=maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_secondary_dns_tsig_create_tsig_params.TsigSecondaryDNSTsigCreateTsigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TsigSecondaryDNSTsigCreateTsigResponse], ResultWrapper[TsigSecondaryDNSTsigCreateTsigResponse]
            ),
        )

    async def secondary_dns_tsig_list_tsi_gs(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TsigSecondaryDNSTsigListTsiGsResponse]:
        """
        List TSIGs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TsigSecondaryDNSTsigListTsiGsResponse]],
                ResultWrapper[TsigSecondaryDNSTsigListTsiGsResponse],
            ),
        )


class TsigsWithRawResponse:
    def __init__(self, tsigs: Tsigs) -> None:
        self._tsigs = tsigs

        self.update = to_raw_response_wrapper(
            tsigs.update,
        )
        self.delete = to_raw_response_wrapper(
            tsigs.delete,
        )
        self.get = to_raw_response_wrapper(
            tsigs.get,
        )
        self.secondary_dns_tsig_create_tsig = to_raw_response_wrapper(
            tsigs.secondary_dns_tsig_create_tsig,
        )
        self.secondary_dns_tsig_list_tsi_gs = to_raw_response_wrapper(
            tsigs.secondary_dns_tsig_list_tsi_gs,
        )


class AsyncTsigsWithRawResponse:
    def __init__(self, tsigs: AsyncTsigs) -> None:
        self._tsigs = tsigs

        self.update = async_to_raw_response_wrapper(
            tsigs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            tsigs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tsigs.get,
        )
        self.secondary_dns_tsig_create_tsig = async_to_raw_response_wrapper(
            tsigs.secondary_dns_tsig_create_tsig,
        )
        self.secondary_dns_tsig_list_tsi_gs = async_to_raw_response_wrapper(
            tsigs.secondary_dns_tsig_list_tsi_gs,
        )


class TsigsWithStreamingResponse:
    def __init__(self, tsigs: Tsigs) -> None:
        self._tsigs = tsigs

        self.update = to_streamed_response_wrapper(
            tsigs.update,
        )
        self.delete = to_streamed_response_wrapper(
            tsigs.delete,
        )
        self.get = to_streamed_response_wrapper(
            tsigs.get,
        )
        self.secondary_dns_tsig_create_tsig = to_streamed_response_wrapper(
            tsigs.secondary_dns_tsig_create_tsig,
        )
        self.secondary_dns_tsig_list_tsi_gs = to_streamed_response_wrapper(
            tsigs.secondary_dns_tsig_list_tsi_gs,
        )


class AsyncTsigsWithStreamingResponse:
    def __init__(self, tsigs: AsyncTsigs) -> None:
        self._tsigs = tsigs

        self.update = async_to_streamed_response_wrapper(
            tsigs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            tsigs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tsigs.get,
        )
        self.secondary_dns_tsig_create_tsig = async_to_streamed_response_wrapper(
            tsigs.secondary_dns_tsig_create_tsig,
        )
        self.secondary_dns_tsig_list_tsi_gs = async_to_streamed_response_wrapper(
            tsigs.secondary_dns_tsig_list_tsi_gs,
        )
