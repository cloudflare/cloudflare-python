# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

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
from ....types.dns.zone_transfers import incoming_create_params, incoming_update_params
from ....types.dns.zone_transfers.incoming_get_response import IncomingGetResponse
from ....types.dns.zone_transfers.incoming_create_response import IncomingCreateResponse
from ....types.dns.zone_transfers.incoming_delete_response import IncomingDeleteResponse
from ....types.dns.zone_transfers.incoming_update_response import IncomingUpdateResponse

__all__ = ["IncomingResource", "AsyncIncomingResource"]


class IncomingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncomingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IncomingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncomingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IncomingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        auto_refresh_seconds: float,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncomingCreateResponse]:
        """
        Create secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_create_params.IncomingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingCreateResponse]], ResultWrapper[IncomingCreateResponse]),
        )

    def update(
        self,
        *,
        zone_id: str,
        auto_refresh_seconds: float,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncomingUpdateResponse]:
        """
        Update secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_update_params.IncomingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingUpdateResponse]], ResultWrapper[IncomingUpdateResponse]),
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
    ) -> Optional[IncomingDeleteResponse]:
        """
        Delete secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingDeleteResponse]], ResultWrapper[IncomingDeleteResponse]),
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
    ) -> Optional[IncomingGetResponse]:
        """
        Get secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingGetResponse]], ResultWrapper[IncomingGetResponse]),
        )


class AsyncIncomingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncomingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIncomingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncomingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIncomingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        auto_refresh_seconds: float,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncomingCreateResponse]:
        """
        Create secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=await async_maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_create_params.IncomingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingCreateResponse]], ResultWrapper[IncomingCreateResponse]),
        )

    async def update(
        self,
        *,
        zone_id: str,
        auto_refresh_seconds: float,
        name: str,
        peers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncomingUpdateResponse]:
        """
        Update secondary zone configuration for incoming zone transfers.

        Args:
          auto_refresh_seconds: How often should a secondary zone auto refresh regardless of DNS NOTIFY. Not
              applicable for primary zones.

          name: Zone name.

          peers: A list of peer tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/secondary_dns/incoming",
            body=await async_maybe_transform(
                {
                    "auto_refresh_seconds": auto_refresh_seconds,
                    "name": name,
                    "peers": peers,
                },
                incoming_update_params.IncomingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingUpdateResponse]], ResultWrapper[IncomingUpdateResponse]),
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
    ) -> Optional[IncomingDeleteResponse]:
        """
        Delete secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingDeleteResponse]], ResultWrapper[IncomingDeleteResponse]),
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
    ) -> Optional[IncomingGetResponse]:
        """
        Get secondary zone configuration for incoming zone transfers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/secondary_dns/incoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IncomingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncomingGetResponse]], ResultWrapper[IncomingGetResponse]),
        )


class IncomingResourceWithRawResponse:
    def __init__(self, incoming: IncomingResource) -> None:
        self._incoming = incoming

        self.create = to_raw_response_wrapper(
            incoming.create,
        )
        self.update = to_raw_response_wrapper(
            incoming.update,
        )
        self.delete = to_raw_response_wrapper(
            incoming.delete,
        )
        self.get = to_raw_response_wrapper(
            incoming.get,
        )


class AsyncIncomingResourceWithRawResponse:
    def __init__(self, incoming: AsyncIncomingResource) -> None:
        self._incoming = incoming

        self.create = async_to_raw_response_wrapper(
            incoming.create,
        )
        self.update = async_to_raw_response_wrapper(
            incoming.update,
        )
        self.delete = async_to_raw_response_wrapper(
            incoming.delete,
        )
        self.get = async_to_raw_response_wrapper(
            incoming.get,
        )


class IncomingResourceWithStreamingResponse:
    def __init__(self, incoming: IncomingResource) -> None:
        self._incoming = incoming

        self.create = to_streamed_response_wrapper(
            incoming.create,
        )
        self.update = to_streamed_response_wrapper(
            incoming.update,
        )
        self.delete = to_streamed_response_wrapper(
            incoming.delete,
        )
        self.get = to_streamed_response_wrapper(
            incoming.get,
        )


class AsyncIncomingResourceWithStreamingResponse:
    def __init__(self, incoming: AsyncIncomingResource) -> None:
        self._incoming = incoming

        self.create = async_to_streamed_response_wrapper(
            incoming.create,
        )
        self.update = async_to_streamed_response_wrapper(
            incoming.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            incoming.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            incoming.get,
        )
