# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.networks.subnets import cloudflare_source_update_params
from .....types.zero_trust.networks.subnets.cloudflare_source_update_response import CloudflareSourceUpdateResponse

__all__ = ["CloudflareSourceResource", "AsyncCloudflareSourceResource"]


class CloudflareSourceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CloudflareSourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudflareSourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudflareSourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudflareSourceResourceWithStreamingResponse(self)

    def update(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudflareSourceUpdateResponse:
        """
        Updates the Cloudflare Source subnet of the given address family

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          comment: An optional description of the subnet.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return self._patch(
            f"/accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}",
            body=maybe_transform(
                {
                    "comment": comment,
                    "name": name,
                    "network": network,
                },
                cloudflare_source_update_params.CloudflareSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudflareSourceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudflareSourceUpdateResponse], ResultWrapper[CloudflareSourceUpdateResponse]),
        )


class AsyncCloudflareSourceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCloudflareSourceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudflareSourceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudflareSourceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCloudflareSourceResourceWithStreamingResponse(self)

    async def update(
        self,
        address_family: Literal["v4", "v6"],
        *,
        account_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudflareSourceUpdateResponse:
        """
        Updates the Cloudflare Source subnet of the given address family

        Args:
          account_id: Cloudflare account ID

          address_family: IP address family, either `v4` (IPv4) or `v6` (IPv6)

          comment: An optional description of the subnet.

          name: A user-friendly name for the subnet.

          network: The private IPv4 or IPv6 range defining the subnet, in CIDR notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_family:
            raise ValueError(f"Expected a non-empty value for `address_family` but received {address_family!r}")
        return await self._patch(
            f"/accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "name": name,
                    "network": network,
                },
                cloudflare_source_update_params.CloudflareSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudflareSourceUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudflareSourceUpdateResponse], ResultWrapper[CloudflareSourceUpdateResponse]),
        )


class CloudflareSourceResourceWithRawResponse:
    def __init__(self, cloudflare_source: CloudflareSourceResource) -> None:
        self._cloudflare_source = cloudflare_source

        self.update = to_raw_response_wrapper(
            cloudflare_source.update,
        )


class AsyncCloudflareSourceResourceWithRawResponse:
    def __init__(self, cloudflare_source: AsyncCloudflareSourceResource) -> None:
        self._cloudflare_source = cloudflare_source

        self.update = async_to_raw_response_wrapper(
            cloudflare_source.update,
        )


class CloudflareSourceResourceWithStreamingResponse:
    def __init__(self, cloudflare_source: CloudflareSourceResource) -> None:
        self._cloudflare_source = cloudflare_source

        self.update = to_streamed_response_wrapper(
            cloudflare_source.update,
        )


class AsyncCloudflareSourceResourceWithStreamingResponse:
    def __init__(self, cloudflare_source: AsyncCloudflareSourceResource) -> None:
        self._cloudflare_source = cloudflare_source

        self.update = async_to_streamed_response_wrapper(
            cloudflare_source.update,
        )
