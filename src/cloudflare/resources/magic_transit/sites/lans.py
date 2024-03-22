# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ....types.magic_transit.sites import (
    LANGetResponse,
    LANListResponse,
    LANCreateResponse,
    LANDeleteResponse,
    LANUpdateResponse,
    lan_create_params,
    lan_update_params,
)

__all__ = ["LANs", "AsyncLANs"]


class LANs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LANsWithRawResponse:
        return LANsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LANsWithStreamingResponse:
        return LANsWithStreamingResponse(self)

    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan: lan_create_params.LAN | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANCreateResponse:
        """Creates a new LAN.

        If the site is in high availability mode, static_addressing
        is required along with secondary and virtual address.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            body=maybe_transform({"lan": lan}, lan_create_params.LANCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANCreateResponse], ResultWrapper[LANCreateResponse]),
        )

    def update(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        lan: lan_update_params.LAN | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANUpdateResponse:
        """
        Update a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=maybe_transform({"lan": lan}, lan_update_params.LANUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANUpdateResponse], ResultWrapper[LANUpdateResponse]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANListResponse:
        """
        Lists LANs associated with an account and site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANListResponse], ResultWrapper[LANListResponse]),
        )

    def delete(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANDeleteResponse:
        """
        Remove a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANDeleteResponse], ResultWrapper[LANDeleteResponse]),
        )

    def get(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANGetResponse:
        """
        Get a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANGetResponse], ResultWrapper[LANGetResponse]),
        )


class AsyncLANs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLANsWithRawResponse:
        return AsyncLANsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLANsWithStreamingResponse:
        return AsyncLANsWithStreamingResponse(self)

    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan: lan_create_params.LAN | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANCreateResponse:
        """Creates a new LAN.

        If the site is in high availability mode, static_addressing
        is required along with secondary and virtual address.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            body=await async_maybe_transform({"lan": lan}, lan_create_params.LANCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANCreateResponse], ResultWrapper[LANCreateResponse]),
        )

    async def update(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        lan: lan_update_params.LAN | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANUpdateResponse:
        """
        Update a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            body=await async_maybe_transform({"lan": lan}, lan_update_params.LANUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANUpdateResponse], ResultWrapper[LANUpdateResponse]),
        )

    async def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANListResponse:
        """
        Lists LANs associated with an account and site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANListResponse], ResultWrapper[LANListResponse]),
        )

    async def delete(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANDeleteResponse:
        """
        Remove a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANDeleteResponse], ResultWrapper[LANDeleteResponse]),
        )

    async def get(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LANGetResponse:
        """
        Get a specific LAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          lan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not lan_id:
            raise ValueError(f"Expected a non-empty value for `lan_id` but received {lan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LANGetResponse], ResultWrapper[LANGetResponse]),
        )


class LANsWithRawResponse:
    def __init__(self, lans: LANs) -> None:
        self._lans = lans

        self.create = to_raw_response_wrapper(
            lans.create,
        )
        self.update = to_raw_response_wrapper(
            lans.update,
        )
        self.list = to_raw_response_wrapper(
            lans.list,
        )
        self.delete = to_raw_response_wrapper(
            lans.delete,
        )
        self.get = to_raw_response_wrapper(
            lans.get,
        )


class AsyncLANsWithRawResponse:
    def __init__(self, lans: AsyncLANs) -> None:
        self._lans = lans

        self.create = async_to_raw_response_wrapper(
            lans.create,
        )
        self.update = async_to_raw_response_wrapper(
            lans.update,
        )
        self.list = async_to_raw_response_wrapper(
            lans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            lans.delete,
        )
        self.get = async_to_raw_response_wrapper(
            lans.get,
        )


class LANsWithStreamingResponse:
    def __init__(self, lans: LANs) -> None:
        self._lans = lans

        self.create = to_streamed_response_wrapper(
            lans.create,
        )
        self.update = to_streamed_response_wrapper(
            lans.update,
        )
        self.list = to_streamed_response_wrapper(
            lans.list,
        )
        self.delete = to_streamed_response_wrapper(
            lans.delete,
        )
        self.get = to_streamed_response_wrapper(
            lans.get,
        )


class AsyncLANsWithStreamingResponse:
    def __init__(self, lans: AsyncLANs) -> None:
        self._lans = lans

        self.create = async_to_streamed_response_wrapper(
            lans.create,
        )
        self.update = async_to_streamed_response_wrapper(
            lans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            lans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            lans.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            lans.get,
        )
