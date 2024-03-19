# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
    SecondaryDNSTSIG,
    TSIGListResponse,
    TSIGDeleteResponse,
    tsig_create_params,
    tsig_update_params,
)

__all__ = ["TSIGs", "AsyncTSIGs"]


class TSIGs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TSIGsWithRawResponse:
        return TSIGsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TSIGsWithStreamingResponse:
        return TSIGsWithStreamingResponse(self)

    def create(
        self,
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
    ) -> SecondaryDNSTSIG:
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
                tsig_create_params.TSIGCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )

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
    ) -> SecondaryDNSTSIG:
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
                tsig_update_params.TSIGUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIGListResponse]:
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
            cast_to=cast(Type[Optional[TSIGListResponse]], ResultWrapper[TSIGListResponse]),
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
    ) -> TSIGDeleteResponse:
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
            cast_to=cast(Type[TSIGDeleteResponse], ResultWrapper[TSIGDeleteResponse]),
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
    ) -> SecondaryDNSTSIG:
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
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )


class AsyncTSIGs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTSIGsWithRawResponse:
        return AsyncTSIGsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTSIGsWithStreamingResponse:
        return AsyncTSIGsWithStreamingResponse(self)

    async def create(
        self,
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
    ) -> SecondaryDNSTSIG:
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
            body=await async_maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_create_params.TSIGCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )

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
    ) -> SecondaryDNSTSIG:
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
            body=await async_maybe_transform(
                {
                    "algo": algo,
                    "name": name,
                    "secret": secret,
                },
                tsig_update_params.TSIGUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIGListResponse]:
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
            cast_to=cast(Type[Optional[TSIGListResponse]], ResultWrapper[TSIGListResponse]),
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
    ) -> TSIGDeleteResponse:
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
            cast_to=cast(Type[TSIGDeleteResponse], ResultWrapper[TSIGDeleteResponse]),
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
    ) -> SecondaryDNSTSIG:
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
            cast_to=cast(Type[SecondaryDNSTSIG], ResultWrapper[SecondaryDNSTSIG]),
        )


class TSIGsWithRawResponse:
    def __init__(self, tsigs: TSIGs) -> None:
        self._tsigs = tsigs

        self.create = to_raw_response_wrapper(
            tsigs.create,
        )
        self.update = to_raw_response_wrapper(
            tsigs.update,
        )
        self.list = to_raw_response_wrapper(
            tsigs.list,
        )
        self.delete = to_raw_response_wrapper(
            tsigs.delete,
        )
        self.get = to_raw_response_wrapper(
            tsigs.get,
        )


class AsyncTSIGsWithRawResponse:
    def __init__(self, tsigs: AsyncTSIGs) -> None:
        self._tsigs = tsigs

        self.create = async_to_raw_response_wrapper(
            tsigs.create,
        )
        self.update = async_to_raw_response_wrapper(
            tsigs.update,
        )
        self.list = async_to_raw_response_wrapper(
            tsigs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tsigs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            tsigs.get,
        )


class TSIGsWithStreamingResponse:
    def __init__(self, tsigs: TSIGs) -> None:
        self._tsigs = tsigs

        self.create = to_streamed_response_wrapper(
            tsigs.create,
        )
        self.update = to_streamed_response_wrapper(
            tsigs.update,
        )
        self.list = to_streamed_response_wrapper(
            tsigs.list,
        )
        self.delete = to_streamed_response_wrapper(
            tsigs.delete,
        )
        self.get = to_streamed_response_wrapper(
            tsigs.get,
        )


class AsyncTSIGsWithStreamingResponse:
    def __init__(self, tsigs: AsyncTSIGs) -> None:
        self._tsigs = tsigs

        self.create = async_to_streamed_response_wrapper(
            tsigs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tsigs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tsigs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tsigs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            tsigs.get,
        )
