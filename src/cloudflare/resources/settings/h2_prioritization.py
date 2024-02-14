# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import (
    H2PrioritizationUpdateResponse,
    H2PrioritizationGetResponse,
    h2_prioritization_update_params,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import h2_prioritization_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["H2Prioritization", "AsyncH2Prioritization"]


class H2Prioritization(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> H2PrioritizationWithRawResponse:
        return H2PrioritizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> H2PrioritizationWithStreamingResponse:
        return H2PrioritizationWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: h2_prioritization_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2PrioritizationUpdateResponse]:
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
            body=maybe_transform({"value": value}, h2_prioritization_update_params.H2PrioritizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2PrioritizationUpdateResponse]], ResultWrapper[H2PrioritizationUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2PrioritizationGetResponse]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2PrioritizationGetResponse]], ResultWrapper[H2PrioritizationGetResponse]),
        )


class AsyncH2Prioritization(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncH2PrioritizationWithRawResponse:
        return AsyncH2PrioritizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncH2PrioritizationWithStreamingResponse:
        return AsyncH2PrioritizationWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: h2_prioritization_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2PrioritizationUpdateResponse]:
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
            body=maybe_transform({"value": value}, h2_prioritization_update_params.H2PrioritizationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2PrioritizationUpdateResponse]], ResultWrapper[H2PrioritizationUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[H2PrioritizationGetResponse]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[H2PrioritizationGetResponse]], ResultWrapper[H2PrioritizationGetResponse]),
        )


class H2PrioritizationWithRawResponse:
    def __init__(self, h2_prioritization: H2Prioritization) -> None:
        self._h2_prioritization = h2_prioritization

        self.update = to_raw_response_wrapper(
            h2_prioritization.update,
        )
        self.get = to_raw_response_wrapper(
            h2_prioritization.get,
        )


class AsyncH2PrioritizationWithRawResponse:
    def __init__(self, h2_prioritization: AsyncH2Prioritization) -> None:
        self._h2_prioritization = h2_prioritization

        self.update = async_to_raw_response_wrapper(
            h2_prioritization.update,
        )
        self.get = async_to_raw_response_wrapper(
            h2_prioritization.get,
        )


class H2PrioritizationWithStreamingResponse:
    def __init__(self, h2_prioritization: H2Prioritization) -> None:
        self._h2_prioritization = h2_prioritization

        self.update = to_streamed_response_wrapper(
            h2_prioritization.update,
        )
        self.get = to_streamed_response_wrapper(
            h2_prioritization.get,
        )


class AsyncH2PrioritizationWithStreamingResponse:
    def __init__(self, h2_prioritization: AsyncH2Prioritization) -> None:
        self._h2_prioritization = h2_prioritization

        self.update = async_to_streamed_response_wrapper(
            h2_prioritization.update,
        )
        self.get = async_to_streamed_response_wrapper(
            h2_prioritization.get,
        )
