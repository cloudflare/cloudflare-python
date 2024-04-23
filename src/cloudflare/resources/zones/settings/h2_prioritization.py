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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import H2Prioritization, h2_prioritization_edit_params
from ....types.zones.settings.h2_prioritization import H2Prioritization
from ....types.zones.settings.h2_prioritization_param import H2PrioritizationParam

__all__ = ["H2PrioritizationResource", "AsyncH2PrioritizationResource"]


class H2PrioritizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> H2PrioritizationResourceWithRawResponse:
        return H2PrioritizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> H2PrioritizationResourceWithStreamingResponse:
        return H2PrioritizationResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: H2PrioritizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2Prioritization]:
        """
        Gets HTTP/2 Edge Prioritization setting.

        Args:
          zone_id: Identifier

          value: HTTP/2 Edge Prioritization optimises the delivery of resources served through
              HTTP/2 to improve page load performance. It also supports fine control of
              content delivery when used in conjunction with Workers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/h2_prioritization",
            body=maybe_transform({"value": value}, h2_prioritization_edit_params.H2PrioritizationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[H2Prioritization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2Prioritization]], ResultWrapper[H2Prioritization]),
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
    ) -> Optional[H2Prioritization]:
        """
        Gets HTTP/2 Edge Prioritization setting.

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
            f"/zones/{zone_id}/settings/h2_prioritization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[H2Prioritization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2Prioritization]], ResultWrapper[H2Prioritization]),
        )


class AsyncH2PrioritizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncH2PrioritizationResourceWithRawResponse:
        return AsyncH2PrioritizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncH2PrioritizationResourceWithStreamingResponse:
        return AsyncH2PrioritizationResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: H2PrioritizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2Prioritization]:
        """
        Gets HTTP/2 Edge Prioritization setting.

        Args:
          zone_id: Identifier

          value: HTTP/2 Edge Prioritization optimises the delivery of resources served through
              HTTP/2 to improve page load performance. It also supports fine control of
              content delivery when used in conjunction with Workers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/h2_prioritization",
            body=await async_maybe_transform(
                {"value": value}, h2_prioritization_edit_params.H2PrioritizationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[H2Prioritization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2Prioritization]], ResultWrapper[H2Prioritization]),
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
    ) -> Optional[H2Prioritization]:
        """
        Gets HTTP/2 Edge Prioritization setting.

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
            f"/zones/{zone_id}/settings/h2_prioritization",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[H2Prioritization]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2Prioritization]], ResultWrapper[H2Prioritization]),
        )


class H2PrioritizationResourceWithRawResponse:
    def __init__(self, h2_prioritization: H2PrioritizationResource) -> None:
        self._h2_prioritization = h2_prioritization

        self.edit = to_raw_response_wrapper(
            h2_prioritization.edit,
        )
        self.get = to_raw_response_wrapper(
            h2_prioritization.get,
        )


class AsyncH2PrioritizationResourceWithRawResponse:
    def __init__(self, h2_prioritization: AsyncH2PrioritizationResource) -> None:
        self._h2_prioritization = h2_prioritization

        self.edit = async_to_raw_response_wrapper(
            h2_prioritization.edit,
        )
        self.get = async_to_raw_response_wrapper(
            h2_prioritization.get,
        )


class H2PrioritizationResourceWithStreamingResponse:
    def __init__(self, h2_prioritization: H2PrioritizationResource) -> None:
        self._h2_prioritization = h2_prioritization

        self.edit = to_streamed_response_wrapper(
            h2_prioritization.edit,
        )
        self.get = to_streamed_response_wrapper(
            h2_prioritization.get,
        )


class AsyncH2PrioritizationResourceWithStreamingResponse:
    def __init__(self, h2_prioritization: AsyncH2PrioritizationResource) -> None:
        self._h2_prioritization = h2_prioritization

        self.edit = async_to_streamed_response_wrapper(
            h2_prioritization.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            h2_prioritization.get,
        )
