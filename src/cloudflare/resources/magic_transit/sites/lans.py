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
    LanGetResponse,
    LanListResponse,
    LanCreateResponse,
    LanDeleteResponse,
    LanUpdateResponse,
    lan_create_params,
    lan_update_params,
)

__all__ = ["Lans", "AsyncLans"]


class Lans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LansWithRawResponse:
        return LansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LansWithStreamingResponse:
        return LansWithStreamingResponse(self)

    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan: lan_create_params.Lan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanCreateResponse:
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
            body=maybe_transform({"lan": lan}, lan_create_params.LanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LanCreateResponse], ResultWrapper[LanCreateResponse]),
        )

    def update(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        lan: lan_update_params.Lan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanUpdateResponse:
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
            body=maybe_transform({"lan": lan}, lan_update_params.LanUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LanUpdateResponse], ResultWrapper[LanUpdateResponse]),
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
    ) -> LanListResponse:
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
            cast_to=cast(Type[LanListResponse], ResultWrapper[LanListResponse]),
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
    ) -> LanDeleteResponse:
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
            cast_to=cast(Type[LanDeleteResponse], ResultWrapper[LanDeleteResponse]),
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
    ) -> LanGetResponse:
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
            cast_to=cast(Type[LanGetResponse], ResultWrapper[LanGetResponse]),
        )


class AsyncLans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLansWithRawResponse:
        return AsyncLansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLansWithStreamingResponse:
        return AsyncLansWithStreamingResponse(self)

    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan: lan_create_params.Lan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanCreateResponse:
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
            body=await async_maybe_transform({"lan": lan}, lan_create_params.LanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LanCreateResponse], ResultWrapper[LanCreateResponse]),
        )

    async def update(
        self,
        lan_id: str,
        *,
        account_id: str,
        site_id: str,
        lan: lan_update_params.Lan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanUpdateResponse:
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
            body=await async_maybe_transform({"lan": lan}, lan_update_params.LanUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LanUpdateResponse], ResultWrapper[LanUpdateResponse]),
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
    ) -> LanListResponse:
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
            cast_to=cast(Type[LanListResponse], ResultWrapper[LanListResponse]),
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
    ) -> LanDeleteResponse:
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
            cast_to=cast(Type[LanDeleteResponse], ResultWrapper[LanDeleteResponse]),
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
    ) -> LanGetResponse:
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
            cast_to=cast(Type[LanGetResponse], ResultWrapper[LanGetResponse]),
        )


class LansWithRawResponse:
    def __init__(self, lans: Lans) -> None:
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


class AsyncLansWithRawResponse:
    def __init__(self, lans: AsyncLans) -> None:
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


class LansWithStreamingResponse:
    def __init__(self, lans: Lans) -> None:
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


class AsyncLansWithStreamingResponse:
    def __init__(self, lans: AsyncLans) -> None:
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
