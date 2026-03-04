# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workers.observability import (
    destination_list_params,
    destination_create_params,
    destination_update_params,
)
from ....types.workers.observability.destination_list_response import DestinationListResponse
from ....types.workers.observability.destination_create_response import DestinationCreateResponse
from ....types.workers.observability.destination_delete_response import DestinationDeleteResponse
from ....types.workers.observability.destination_update_response import DestinationUpdateResponse

__all__ = ["DestinationsResource", "AsyncDestinationsResource"]


class DestinationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DestinationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        configuration: destination_create_params.Configuration,
        enabled: bool,
        name: str,
        skip_preflight_check: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationCreateResponse:
        """
        Create a new Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/workers/observability/destinations",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "enabled": enabled,
                    "name": name,
                    "skip_preflight_check": skip_preflight_check,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DestinationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DestinationCreateResponse], ResultWrapper[DestinationCreateResponse]),
        )

    def update(
        self,
        slug: str,
        *,
        account_id: str,
        configuration: destination_update_params.Configuration,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationUpdateResponse:
        """
        Update an existing Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._patch(
            f"/accounts/{account_id}/workers/observability/destinations/{slug}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "enabled": enabled,
                },
                destination_update_params.DestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DestinationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DestinationUpdateResponse], ResultWrapper[DestinationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created", "updated"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[DestinationListResponse]:
        """
        List your Workers Observability Telemetry Destinations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/destinations",
            page=SyncSinglePage[DestinationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    destination_list_params.DestinationListParams,
                ),
            ),
            model=DestinationListResponse,
        )

    def delete(
        self,
        slug: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DestinationDeleteResponse]:
        """
        Delete a Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/observability/destinations/{slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DestinationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DestinationDeleteResponse]], ResultWrapper[DestinationDeleteResponse]),
        )


class AsyncDestinationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDestinationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        configuration: destination_create_params.Configuration,
        enabled: bool,
        name: str,
        skip_preflight_check: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationCreateResponse:
        """
        Create a new Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/observability/destinations",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "enabled": enabled,
                    "name": name,
                    "skip_preflight_check": skip_preflight_check,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DestinationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DestinationCreateResponse], ResultWrapper[DestinationCreateResponse]),
        )

    async def update(
        self,
        slug: str,
        *,
        account_id: str,
        configuration: destination_update_params.Configuration,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationUpdateResponse:
        """
        Update an existing Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._patch(
            f"/accounts/{account_id}/workers/observability/destinations/{slug}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "enabled": enabled,
                },
                destination_update_params.DestinationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DestinationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DestinationUpdateResponse], ResultWrapper[DestinationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["created", "updated"] | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DestinationListResponse, AsyncSinglePage[DestinationListResponse]]:
        """
        List your Workers Observability Telemetry Destinations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/destinations",
            page=AsyncSinglePage[DestinationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    destination_list_params.DestinationListParams,
                ),
            ),
            model=DestinationListResponse,
        )

    async def delete(
        self,
        slug: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DestinationDeleteResponse]:
        """
        Delete a Workers Observability Telemetry Destination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/observability/destinations/{slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DestinationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DestinationDeleteResponse]], ResultWrapper[DestinationDeleteResponse]),
        )


class DestinationsResourceWithRawResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_raw_response_wrapper(
            destinations.create,
        )
        self.update = to_raw_response_wrapper(
            destinations.update,
        )
        self.list = to_raw_response_wrapper(
            destinations.list,
        )
        self.delete = to_raw_response_wrapper(
            destinations.delete,
        )


class AsyncDestinationsResourceWithRawResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_raw_response_wrapper(
            destinations.create,
        )
        self.update = async_to_raw_response_wrapper(
            destinations.update,
        )
        self.list = async_to_raw_response_wrapper(
            destinations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            destinations.delete,
        )


class DestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_streamed_response_wrapper(
            destinations.create,
        )
        self.update = to_streamed_response_wrapper(
            destinations.update,
        )
        self.list = to_streamed_response_wrapper(
            destinations.list,
        )
        self.delete = to_streamed_response_wrapper(
            destinations.delete,
        )


class AsyncDestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_streamed_response_wrapper(
            destinations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            destinations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            destinations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            destinations.delete,
        )
