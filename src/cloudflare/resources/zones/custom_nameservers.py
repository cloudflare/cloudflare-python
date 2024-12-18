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
from ...types.zones import custom_nameserver_update_params
from ..._base_client import make_request_options
from ...types.zones.custom_nameserver_get_response import CustomNameserverGetResponse
from ...types.zones.custom_nameserver_update_response import CustomNameserverUpdateResponse

__all__ = ["CustomNameserversResource", "AsyncCustomNameserversResource"]


class CustomNameserversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomNameserversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNameserversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomNameserversResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverUpdateResponse]:
        """
        Set metadata for account-level custom nameservers on a zone.

        If you would like new zones in the account to use account custom nameservers by
        default, use PUT /accounts/:identifier to set the account setting
        use_account_custom_ns_by_default to true.

        Deprecated in favor of
        [Update DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-update-dns-settings).

        Args:
          zone_id: Identifier

          enabled: Whether zone uses account-level custom nameservers.

          ns_set: The number of the name server set to assign to the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/custom_ns",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "ns_set": ns_set,
                },
                custom_nameserver_update_params.CustomNameserverUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomNameserverUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNameserverUpdateResponse]], ResultWrapper[CustomNameserverUpdateResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomNameserverGetResponse:
        """
        Get metadata for account-level custom nameservers on a zone.

        Deprecated in favor of
        [Show DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-list-dns-settings).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/custom_ns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomNameserverGetResponse,
        )


class AsyncCustomNameserversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomNameserversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNameserversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomNameserversResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserverUpdateResponse]:
        """
        Set metadata for account-level custom nameservers on a zone.

        If you would like new zones in the account to use account custom nameservers by
        default, use PUT /accounts/:identifier to set the account setting
        use_account_custom_ns_by_default to true.

        Deprecated in favor of
        [Update DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-update-dns-settings).

        Args:
          zone_id: Identifier

          enabled: Whether zone uses account-level custom nameservers.

          ns_set: The number of the name server set to assign to the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/custom_ns",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "ns_set": ns_set,
                },
                custom_nameserver_update_params.CustomNameserverUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomNameserverUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNameserverUpdateResponse]], ResultWrapper[CustomNameserverUpdateResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomNameserverGetResponse:
        """
        Get metadata for account-level custom nameservers on a zone.

        Deprecated in favor of
        [Show DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-list-dns-settings).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/custom_ns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomNameserverGetResponse,
        )


class CustomNameserversResourceWithRawResponse:
    def __init__(self, custom_nameservers: CustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = to_raw_response_wrapper(
            custom_nameservers.update,
        )
        self.get = to_raw_response_wrapper(
            custom_nameservers.get,
        )


class AsyncCustomNameserversResourceWithRawResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = async_to_raw_response_wrapper(
            custom_nameservers.update,
        )
        self.get = async_to_raw_response_wrapper(
            custom_nameservers.get,
        )


class CustomNameserversResourceWithStreamingResponse:
    def __init__(self, custom_nameservers: CustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = to_streamed_response_wrapper(
            custom_nameservers.update,
        )
        self.get = to_streamed_response_wrapper(
            custom_nameservers.get,
        )


class AsyncCustomNameserversResourceWithStreamingResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.update = async_to_streamed_response_wrapper(
            custom_nameservers.update,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_nameservers.get,
        )
