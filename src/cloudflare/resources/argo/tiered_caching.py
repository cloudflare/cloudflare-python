# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...types.argo import tiered_caching_edit_params
from ..._base_client import make_request_options
from ...types.argo.tiered_caching_get_response import TieredCachingGetResponse
from ...types.argo.tiered_caching_edit_response import TieredCachingEditResponse

__all__ = ["TieredCachingResource", "AsyncTieredCachingResource"]


class TieredCachingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TieredCachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TieredCachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TieredCachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TieredCachingResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TieredCachingEditResponse]:
        """
        Tiered Cache works by dividing Cloudflare's data centers into a hierarchy of
        lower-tiers and upper-tiers. If content is not cached in lower-tier data centers
        (generally the ones closest to a visitor), the lower-tier must ask an upper-tier
        to see if it has the content. If the upper-tier does not have the content, only
        the upper-tier can ask the origin for content. This practice improves bandwidth
        efficiency by limiting the number of data centers that can ask the origin for
        content, which reduces origin load and makes websites more cost-effective to
        operate. Additionally, Tiered Cache concentrates connections to origin servers
        so they come from a small number of data centers rather than the full set of
        network locations. This results in fewer open connections using server
        resources.

        Args:
          zone_id: Identifier

          value: Enables Tiered Caching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/argo/tiered_caching",
            body=maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingEditResponse]], ResultWrapper[TieredCachingEditResponse]),
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
    ) -> Optional[TieredCachingGetResponse]:
        """
        Tiered Cache works by dividing Cloudflare's data centers into a hierarchy of
        lower-tiers and upper-tiers. If content is not cached in lower-tier data centers
        (generally the ones closest to a visitor), the lower-tier must ask an upper-tier
        to see if it has the content. If the upper-tier does not have the content, only
        the upper-tier can ask the origin for content. This practice improves bandwidth
        efficiency by limiting the number of data centers that can ask the origin for
        content, which reduces origin load and makes websites more cost-effective to
        operate. Additionally, Tiered Cache concentrates connections to origin servers
        so they come from a small number of data centers rather than the full set of
        network locations. This results in fewer open connections using server
        resources.

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
            f"/zones/{zone_id}/argo/tiered_caching",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingGetResponse]], ResultWrapper[TieredCachingGetResponse]),
        )


class AsyncTieredCachingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTieredCachingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTieredCachingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTieredCachingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTieredCachingResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TieredCachingEditResponse]:
        """
        Tiered Cache works by dividing Cloudflare's data centers into a hierarchy of
        lower-tiers and upper-tiers. If content is not cached in lower-tier data centers
        (generally the ones closest to a visitor), the lower-tier must ask an upper-tier
        to see if it has the content. If the upper-tier does not have the content, only
        the upper-tier can ask the origin for content. This practice improves bandwidth
        efficiency by limiting the number of data centers that can ask the origin for
        content, which reduces origin load and makes websites more cost-effective to
        operate. Additionally, Tiered Cache concentrates connections to origin servers
        so they come from a small number of data centers rather than the full set of
        network locations. This results in fewer open connections using server
        resources.

        Args:
          zone_id: Identifier

          value: Enables Tiered Caching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/argo/tiered_caching",
            body=await async_maybe_transform({"value": value}, tiered_caching_edit_params.TieredCachingEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingEditResponse]], ResultWrapper[TieredCachingEditResponse]),
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
    ) -> Optional[TieredCachingGetResponse]:
        """
        Tiered Cache works by dividing Cloudflare's data centers into a hierarchy of
        lower-tiers and upper-tiers. If content is not cached in lower-tier data centers
        (generally the ones closest to a visitor), the lower-tier must ask an upper-tier
        to see if it has the content. If the upper-tier does not have the content, only
        the upper-tier can ask the origin for content. This practice improves bandwidth
        efficiency by limiting the number of data centers that can ask the origin for
        content, which reduces origin load and makes websites more cost-effective to
        operate. Additionally, Tiered Cache concentrates connections to origin servers
        so they come from a small number of data centers rather than the full set of
        network locations. This results in fewer open connections using server
        resources.

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
            f"/zones/{zone_id}/argo/tiered_caching",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TieredCachingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TieredCachingGetResponse]], ResultWrapper[TieredCachingGetResponse]),
        )


class TieredCachingResourceWithRawResponse:
    def __init__(self, tiered_caching: TieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_raw_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingResourceWithRawResponse:
    def __init__(self, tiered_caching: AsyncTieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_raw_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tiered_caching.get,
        )


class TieredCachingResourceWithStreamingResponse:
    def __init__(self, tiered_caching: TieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = to_streamed_response_wrapper(
            tiered_caching.get,
        )


class AsyncTieredCachingResourceWithStreamingResponse:
    def __init__(self, tiered_caching: AsyncTieredCachingResource) -> None:
        self._tiered_caching = tiered_caching

        self.edit = async_to_streamed_response_wrapper(
            tiered_caching.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tiered_caching.get,
        )
