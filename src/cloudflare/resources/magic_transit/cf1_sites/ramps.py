# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform
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
from ....types.magic_transit.cf1_sites import ramp_create_params
from ....types.magic_transit.cf1_sites.ramp import Ramp

__all__ = ["RampsResource", "AsyncRampsResource"]


class RampsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RampsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RampsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RampsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RampsResourceWithStreamingResponse(self)

    def create(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        body: Iterable[ramp_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Ramp]:
        """
        Creates ramps (network connections) for a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
            ),
            page=SyncSinglePage[Ramp],
            body=maybe_transform(body, Iterable[ramp_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ramp,
            method="post",
        )

    def list(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Ramp]:
        """Lists ramps (network connections) associated with a CF1 Site.

        Ramps represent
        GRE tunnels, IPsec tunnels, interconnects, or MCONN links.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
            ),
            page=SyncSinglePage[Ramp],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ramp,
        )

    def delete(
        self,
        ramp_id: str,
        *,
        account_id: str,
        cf1_site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ramp:
        """
        Deletes a specific ramp from a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          ramp_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        if not ramp_id:
            raise ValueError(f"Expected a non-empty value for `ramp_id` but received {ramp_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
                ramp_id=ramp_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Ramp]._unwrapper,
            ),
            cast_to=cast(Type[Ramp], ResultWrapper[Ramp]),
        )

    def get(
        self,
        ramp_id: str,
        *,
        account_id: str,
        cf1_site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ramp:
        """
        Gets a specific ramp for a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          ramp_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        if not ramp_id:
            raise ValueError(f"Expected a non-empty value for `ramp_id` but received {ramp_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
                ramp_id=ramp_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Ramp]._unwrapper,
            ),
            cast_to=cast(Type[Ramp], ResultWrapper[Ramp]),
        )


class AsyncRampsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRampsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRampsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRampsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRampsResourceWithStreamingResponse(self)

    def create(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        body: Iterable[ramp_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Ramp, AsyncSinglePage[Ramp]]:
        """
        Creates ramps (network connections) for a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
            ),
            page=AsyncSinglePage[Ramp],
            body=maybe_transform(body, Iterable[ramp_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ramp,
            method="post",
        )

    def list(
        self,
        cf1_site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Ramp, AsyncSinglePage[Ramp]]:
        """Lists ramps (network connections) associated with a CF1 Site.

        Ramps represent
        GRE tunnels, IPsec tunnels, interconnects, or MCONN links.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
            ),
            page=AsyncSinglePage[Ramp],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Ramp,
        )

    async def delete(
        self,
        ramp_id: str,
        *,
        account_id: str,
        cf1_site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ramp:
        """
        Deletes a specific ramp from a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          ramp_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        if not ramp_id:
            raise ValueError(f"Expected a non-empty value for `ramp_id` but received {ramp_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
                ramp_id=ramp_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Ramp]._unwrapper,
            ),
            cast_to=cast(Type[Ramp], ResultWrapper[Ramp]),
        )

    async def get(
        self,
        ramp_id: str,
        *,
        account_id: str,
        cf1_site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Ramp:
        """
        Gets a specific ramp for a CF1 Site.

        Args:
          account_id: Identifier

          cf1_site_id: Identifier

          ramp_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not cf1_site_id:
            raise ValueError(f"Expected a non-empty value for `cf1_site_id` but received {cf1_site_id!r}")
        if not ramp_id:
            raise ValueError(f"Expected a non-empty value for `ramp_id` but received {ramp_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/magic/cf1_sites/{cf1_site_id}/ramps/{ramp_id}",
                account_id=account_id,
                cf1_site_id=cf1_site_id,
                ramp_id=ramp_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Ramp]._unwrapper,
            ),
            cast_to=cast(Type[Ramp], ResultWrapper[Ramp]),
        )


class RampsResourceWithRawResponse:
    def __init__(self, ramps: RampsResource) -> None:
        self._ramps = ramps

        self.create = to_raw_response_wrapper(
            ramps.create,
        )
        self.list = to_raw_response_wrapper(
            ramps.list,
        )
        self.delete = to_raw_response_wrapper(
            ramps.delete,
        )
        self.get = to_raw_response_wrapper(
            ramps.get,
        )


class AsyncRampsResourceWithRawResponse:
    def __init__(self, ramps: AsyncRampsResource) -> None:
        self._ramps = ramps

        self.create = async_to_raw_response_wrapper(
            ramps.create,
        )
        self.list = async_to_raw_response_wrapper(
            ramps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ramps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ramps.get,
        )


class RampsResourceWithStreamingResponse:
    def __init__(self, ramps: RampsResource) -> None:
        self._ramps = ramps

        self.create = to_streamed_response_wrapper(
            ramps.create,
        )
        self.list = to_streamed_response_wrapper(
            ramps.list,
        )
        self.delete = to_streamed_response_wrapper(
            ramps.delete,
        )
        self.get = to_streamed_response_wrapper(
            ramps.get,
        )


class AsyncRampsResourceWithStreamingResponse:
    def __init__(self, ramps: AsyncRampsResource) -> None:
        self._ramps = ramps

        self.create = async_to_streamed_response_wrapper(
            ramps.create,
        )
        self.list = async_to_streamed_response_wrapper(
            ramps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ramps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ramps.get,
        )
