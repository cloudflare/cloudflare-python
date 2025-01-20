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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dns.zone_transfers import tsig_create_params, tsig_update_params
from ....types.dns.zone_transfers.tsig import TSIG
from ....types.dns.zone_transfers.tsig_delete_response import TSIGDeleteResponse

__all__ = ["TSIGsResource", "AsyncTSIGsResource"]


class TSIGsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TSIGsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TSIGsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TSIGsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TSIGsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
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
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )

    def update(
        self,
        tsig_id: str,
        *,
        account_id: str,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
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
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[TSIG]:
        """
        List TSIGs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            page=SyncSinglePage[TSIG],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TSIG,
        )

    def delete(
        self,
        tsig_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIGDeleteResponse]:
        """
        Delete TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
        return self._delete(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TSIGDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIGDeleteResponse]], ResultWrapper[TSIGDeleteResponse]),
        )

    def get(
        self,
        tsig_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
        """
        Get TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
        return self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )


class AsyncTSIGsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTSIGsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTSIGsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTSIGsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTSIGsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
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
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )

    async def update(
        self,
        tsig_id: str,
        *,
        account_id: str,
        algo: str,
        name: str,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
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
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TSIG, AsyncSinglePage[TSIG]]:
        """
        List TSIGs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secondary_dns/tsigs",
            page=AsyncSinglePage[TSIG],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TSIG,
        )

    async def delete(
        self,
        tsig_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIGDeleteResponse]:
        """
        Delete TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TSIGDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIGDeleteResponse]], ResultWrapper[TSIGDeleteResponse]),
        )

    async def get(
        self,
        tsig_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TSIG]:
        """
        Get TSIG.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tsig_id:
            raise ValueError(f"Expected a non-empty value for `tsig_id` but received {tsig_id!r}")
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TSIG]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TSIG]], ResultWrapper[TSIG]),
        )


class TSIGsResourceWithRawResponse:
    def __init__(self, tsigs: TSIGsResource) -> None:
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


class AsyncTSIGsResourceWithRawResponse:
    def __init__(self, tsigs: AsyncTSIGsResource) -> None:
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


class TSIGsResourceWithStreamingResponse:
    def __init__(self, tsigs: TSIGsResource) -> None:
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


class AsyncTSIGsResourceWithStreamingResponse:
    def __init__(self, tsigs: AsyncTSIGsResource) -> None:
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
