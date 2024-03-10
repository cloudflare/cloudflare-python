# File generated from our OpenAPI spec by Stainless.

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
    WanGetResponse,
    WanListResponse,
    WanCreateResponse,
    WanDeleteResponse,
    WanUpdateResponse,
    wan_create_params,
    wan_update_params,
)

__all__ = ["Wans", "AsyncWans"]


class Wans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WansWithRawResponse:
        return WansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WansWithStreamingResponse:
        return WansWithStreamingResponse(self)

    def create(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        wan: wan_create_params.Wan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanCreateResponse:
        """
        Creates a new WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans",
            body=maybe_transform({"wan": wan}, wan_create_params.WanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanCreateResponse], ResultWrapper[WanCreateResponse]),
        )

    def update(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        wan: wan_update_params.Wan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanUpdateResponse:
        """
        Update a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            body=maybe_transform({"wan": wan}, wan_update_params.WanUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanUpdateResponse], ResultWrapper[WanUpdateResponse]),
        )

    def list(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanListResponse:
        """
        Lists WANs associated with an account and site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanListResponse], ResultWrapper[WanListResponse]),
        )

    def delete(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanDeleteResponse:
        """
        Remove a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanDeleteResponse], ResultWrapper[WanDeleteResponse]),
        )

    def get(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanGetResponse:
        """
        Get a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanGetResponse], ResultWrapper[WanGetResponse]),
        )


class AsyncWans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWansWithRawResponse:
        return AsyncWansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWansWithStreamingResponse:
        return AsyncWansWithStreamingResponse(self)

    async def create(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        wan: wan_create_params.Wan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanCreateResponse:
        """
        Creates a new WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans",
            body=await async_maybe_transform({"wan": wan}, wan_create_params.WanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanCreateResponse], ResultWrapper[WanCreateResponse]),
        )

    async def update(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        wan: wan_update_params.Wan | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanUpdateResponse:
        """
        Update a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            body=await async_maybe_transform({"wan": wan}, wan_update_params.WanUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanUpdateResponse], ResultWrapper[WanUpdateResponse]),
        )

    async def list(
        self,
        site_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanListResponse:
        """
        Lists WANs associated with an account and site.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanListResponse], ResultWrapper[WanListResponse]),
        )

    async def delete(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanDeleteResponse:
        """
        Remove a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanDeleteResponse], ResultWrapper[WanDeleteResponse]),
        )

    async def get(
        self,
        wan_identifier: str,
        *,
        account_identifier: str,
        site_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WanGetResponse:
        """
        Get a specific WAN.

        Args:
          account_identifier: Identifier

          site_identifier: Identifier

          wan_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not site_identifier:
            raise ValueError(f"Expected a non-empty value for `site_identifier` but received {site_identifier!r}")
        if not wan_identifier:
            raise ValueError(f"Expected a non-empty value for `wan_identifier` but received {wan_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/sites/{site_identifier}/wans/{wan_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WanGetResponse], ResultWrapper[WanGetResponse]),
        )


class WansWithRawResponse:
    def __init__(self, wans: Wans) -> None:
        self._wans = wans

        self.create = to_raw_response_wrapper(
            wans.create,
        )
        self.update = to_raw_response_wrapper(
            wans.update,
        )
        self.list = to_raw_response_wrapper(
            wans.list,
        )
        self.delete = to_raw_response_wrapper(
            wans.delete,
        )
        self.get = to_raw_response_wrapper(
            wans.get,
        )


class AsyncWansWithRawResponse:
    def __init__(self, wans: AsyncWans) -> None:
        self._wans = wans

        self.create = async_to_raw_response_wrapper(
            wans.create,
        )
        self.update = async_to_raw_response_wrapper(
            wans.update,
        )
        self.list = async_to_raw_response_wrapper(
            wans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wans.delete,
        )
        self.get = async_to_raw_response_wrapper(
            wans.get,
        )


class WansWithStreamingResponse:
    def __init__(self, wans: Wans) -> None:
        self._wans = wans

        self.create = to_streamed_response_wrapper(
            wans.create,
        )
        self.update = to_streamed_response_wrapper(
            wans.update,
        )
        self.list = to_streamed_response_wrapper(
            wans.list,
        )
        self.delete = to_streamed_response_wrapper(
            wans.delete,
        )
        self.get = to_streamed_response_wrapper(
            wans.get,
        )


class AsyncWansWithStreamingResponse:
    def __init__(self, wans: AsyncWans) -> None:
        self._wans = wans

        self.create = async_to_streamed_response_wrapper(
            wans.create,
        )
        self.update = async_to_streamed_response_wrapper(
            wans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wans.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            wans.get,
        )
