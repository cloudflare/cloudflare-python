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
from ...._base_client import make_request_options
from ....types.addressing.prefixes import advertisement_status_edit_params
from ....types.addressing.prefixes.advertisement_status_get_response import AdvertisementStatusGetResponse
from ....types.addressing.prefixes.advertisement_status_edit_response import AdvertisementStatusEditResponse

__all__ = ["AdvertisementStatusResource", "AsyncAdvertisementStatusResource"]


class AdvertisementStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvertisementStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AdvertisementStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvertisementStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AdvertisementStatusResourceWithStreamingResponse(self)

    def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementStatusEditResponse]:
        """
        Advertise or withdraw the BGP route for a prefix.

        **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for
        advertising and withdrawing subnets of an IP prefix.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          advertised: Advertisement status of the prefix. If `true`, the BGP route for the prefix is
              advertised to the Internet. If `false`, the BGP route is withdrawn.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            body=maybe_transform(
                {"advertised": advertised}, advertisement_status_edit_params.AdvertisementStatusEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AdvertisementStatusEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AdvertisementStatusEditResponse]], ResultWrapper[AdvertisementStatusEditResponse]
            ),
        )

    def get(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementStatusGetResponse]:
        """
        View the current advertisement state for a prefix.

        **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for
        advertising and withdrawing subnets of an IP prefix.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AdvertisementStatusGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AdvertisementStatusGetResponse]], ResultWrapper[AdvertisementStatusGetResponse]),
        )


class AsyncAdvertisementStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvertisementStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvertisementStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvertisementStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAdvertisementStatusResourceWithStreamingResponse(self)

    async def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementStatusEditResponse]:
        """
        Advertise or withdraw the BGP route for a prefix.

        **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for
        advertising and withdrawing subnets of an IP prefix.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          advertised: Advertisement status of the prefix. If `true`, the BGP route for the prefix is
              advertised to the Internet. If `false`, the BGP route is withdrawn.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            body=await async_maybe_transform(
                {"advertised": advertised}, advertisement_status_edit_params.AdvertisementStatusEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AdvertisementStatusEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AdvertisementStatusEditResponse]], ResultWrapper[AdvertisementStatusEditResponse]
            ),
        )

    async def get(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementStatusGetResponse]:
        """
        View the current advertisement state for a prefix.

        **Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for
        advertising and withdrawing subnets of an IP prefix.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AdvertisementStatusGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AdvertisementStatusGetResponse]], ResultWrapper[AdvertisementStatusGetResponse]),
        )


class AdvertisementStatusResourceWithRawResponse:
    def __init__(self, advertisement_status: AdvertisementStatusResource) -> None:
        self._advertisement_status = advertisement_status

        self.edit = to_raw_response_wrapper(
            advertisement_status.edit,
        )
        self.get = to_raw_response_wrapper(
            advertisement_status.get,
        )


class AsyncAdvertisementStatusResourceWithRawResponse:
    def __init__(self, advertisement_status: AsyncAdvertisementStatusResource) -> None:
        self._advertisement_status = advertisement_status

        self.edit = async_to_raw_response_wrapper(
            advertisement_status.edit,
        )
        self.get = async_to_raw_response_wrapper(
            advertisement_status.get,
        )


class AdvertisementStatusResourceWithStreamingResponse:
    def __init__(self, advertisement_status: AdvertisementStatusResource) -> None:
        self._advertisement_status = advertisement_status

        self.edit = to_streamed_response_wrapper(
            advertisement_status.edit,
        )
        self.get = to_streamed_response_wrapper(
            advertisement_status.get,
        )


class AsyncAdvertisementStatusResourceWithStreamingResponse:
    def __init__(self, advertisement_status: AsyncAdvertisementStatusResource) -> None:
        self._advertisement_status = advertisement_status

        self.edit = async_to_streamed_response_wrapper(
            advertisement_status.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            advertisement_status.get,
        )
