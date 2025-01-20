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
from ..._base_client import make_request_options
from ...types.custom_hostnames import fallback_origin_update_params
from ...types.custom_hostnames.fallback_origin_get_response import FallbackOriginGetResponse
from ...types.custom_hostnames.fallback_origin_delete_response import FallbackOriginDeleteResponse
from ...types.custom_hostnames.fallback_origin_update_response import FallbackOriginUpdateResponse

__all__ = ["FallbackOriginResource", "AsyncFallbackOriginResource"]


class FallbackOriginResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallbackOriginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FallbackOriginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallbackOriginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FallbackOriginResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        origin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackOriginUpdateResponse]:
        """
        Update Fallback Origin for Custom Hostnames

        Args:
          zone_id: Identifier

          origin: Your origin hostname that requests to your custom hostnames will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            body=maybe_transform({"origin": origin}, fallback_origin_update_params.FallbackOriginUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginUpdateResponse]], ResultWrapper[FallbackOriginUpdateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackOriginDeleteResponse]:
        """
        Delete Fallback Origin for Custom Hostnames

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginDeleteResponse]], ResultWrapper[FallbackOriginDeleteResponse]),
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
    ) -> Optional[FallbackOriginGetResponse]:
        """
        Get Fallback Origin for Custom Hostnames

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
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginGetResponse]], ResultWrapper[FallbackOriginGetResponse]),
        )


class AsyncFallbackOriginResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFallbackOriginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFallbackOriginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallbackOriginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFallbackOriginResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        origin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackOriginUpdateResponse]:
        """
        Update Fallback Origin for Custom Hostnames

        Args:
          zone_id: Identifier

          origin: Your origin hostname that requests to your custom hostnames will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            body=await async_maybe_transform(
                {"origin": origin}, fallback_origin_update_params.FallbackOriginUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginUpdateResponse]], ResultWrapper[FallbackOriginUpdateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackOriginDeleteResponse]:
        """
        Delete Fallback Origin for Custom Hostnames

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginDeleteResponse]], ResultWrapper[FallbackOriginDeleteResponse]),
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
    ) -> Optional[FallbackOriginGetResponse]:
        """
        Get Fallback Origin for Custom Hostnames

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
            f"/zones/{zone_id}/custom_hostnames/fallback_origin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackOriginGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackOriginGetResponse]], ResultWrapper[FallbackOriginGetResponse]),
        )


class FallbackOriginResourceWithRawResponse:
    def __init__(self, fallback_origin: FallbackOriginResource) -> None:
        self._fallback_origin = fallback_origin

        self.update = to_raw_response_wrapper(
            fallback_origin.update,
        )
        self.delete = to_raw_response_wrapper(
            fallback_origin.delete,
        )
        self.get = to_raw_response_wrapper(
            fallback_origin.get,
        )


class AsyncFallbackOriginResourceWithRawResponse:
    def __init__(self, fallback_origin: AsyncFallbackOriginResource) -> None:
        self._fallback_origin = fallback_origin

        self.update = async_to_raw_response_wrapper(
            fallback_origin.update,
        )
        self.delete = async_to_raw_response_wrapper(
            fallback_origin.delete,
        )
        self.get = async_to_raw_response_wrapper(
            fallback_origin.get,
        )


class FallbackOriginResourceWithStreamingResponse:
    def __init__(self, fallback_origin: FallbackOriginResource) -> None:
        self._fallback_origin = fallback_origin

        self.update = to_streamed_response_wrapper(
            fallback_origin.update,
        )
        self.delete = to_streamed_response_wrapper(
            fallback_origin.delete,
        )
        self.get = to_streamed_response_wrapper(
            fallback_origin.get,
        )


class AsyncFallbackOriginResourceWithStreamingResponse:
    def __init__(self, fallback_origin: AsyncFallbackOriginResource) -> None:
        self._fallback_origin = fallback_origin

        self.update = async_to_streamed_response_wrapper(
            fallback_origin.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            fallback_origin.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            fallback_origin.get,
        )
