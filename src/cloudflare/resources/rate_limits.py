# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ..types import (
    RateLimitGetResponse,
    RateLimitEditResponse,
    RateLimitListResponse,
    RateLimitCreateResponse,
    RateLimitDeleteResponse,
    rate_limit_edit_params,
    rate_limit_list_params,
    rate_limit_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["RateLimits", "AsyncRateLimits"]


class RateLimits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateLimitsWithRawResponse:
        return RateLimitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateLimitsWithStreamingResponse:
        return RateLimitsWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitCreateResponse]:
        """Creates a new rate limit for a zone.

        Refer to the object definition for a list
        of required attributes.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            Optional[RateLimitCreateResponse],
            self._post(
                f"/zones/{zone_identifier}/rate_limits",
                body=maybe_transform(body, rate_limit_create_params.RateLimitCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[RateLimitListResponse]:
        """
        Fetches the rate limits for a zone.

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/rate_limits",
            page=SyncV4PagePaginationArray[RateLimitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    rate_limit_list_params.RateLimitListParams,
                ),
            ),
            model=RateLimitListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitDeleteResponse]:
        """
        Deletes an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/rate_limits/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RateLimitDeleteResponse]], ResultWrapper[RateLimitDeleteResponse]),
        )

    def edit(
        self,
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitEditResponse]:
        """
        Updates an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[RateLimitEditResponse],
            self._put(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                body=maybe_transform(body, rate_limit_edit_params.RateLimitEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitGetResponse]:
        """
        Fetches the details of a rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[RateLimitGetResponse],
            self._get(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRateLimits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateLimitsWithRawResponse:
        return AsyncRateLimitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateLimitsWithStreamingResponse:
        return AsyncRateLimitsWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitCreateResponse]:
        """Creates a new rate limit for a zone.

        Refer to the object definition for a list
        of required attributes.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            Optional[RateLimitCreateResponse],
            await self._post(
                f"/zones/{zone_identifier}/rate_limits",
                body=await async_maybe_transform(body, rate_limit_create_params.RateLimitCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RateLimitListResponse, AsyncV4PagePaginationArray[RateLimitListResponse]]:
        """
        Fetches the rate limits for a zone.

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/rate_limits",
            page=AsyncV4PagePaginationArray[RateLimitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    rate_limit_list_params.RateLimitListParams,
                ),
            ),
            model=RateLimitListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitDeleteResponse]:
        """
        Deletes an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/rate_limits/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RateLimitDeleteResponse]], ResultWrapper[RateLimitDeleteResponse]),
        )

    async def edit(
        self,
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitEditResponse]:
        """
        Updates an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[RateLimitEditResponse],
            await self._put(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                body=await async_maybe_transform(body, rate_limit_edit_params.RateLimitEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RateLimitGetResponse]:
        """
        Fetches the details of a rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[RateLimitGetResponse],
            await self._get(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RateLimitsWithRawResponse:
    def __init__(self, rate_limits: RateLimits) -> None:
        self._rate_limits = rate_limits

        self.create = to_raw_response_wrapper(
            rate_limits.create,
        )
        self.list = to_raw_response_wrapper(
            rate_limits.list,
        )
        self.delete = to_raw_response_wrapper(
            rate_limits.delete,
        )
        self.edit = to_raw_response_wrapper(
            rate_limits.edit,
        )
        self.get = to_raw_response_wrapper(
            rate_limits.get,
        )


class AsyncRateLimitsWithRawResponse:
    def __init__(self, rate_limits: AsyncRateLimits) -> None:
        self._rate_limits = rate_limits

        self.create = async_to_raw_response_wrapper(
            rate_limits.create,
        )
        self.list = async_to_raw_response_wrapper(
            rate_limits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rate_limits.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            rate_limits.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rate_limits.get,
        )


class RateLimitsWithStreamingResponse:
    def __init__(self, rate_limits: RateLimits) -> None:
        self._rate_limits = rate_limits

        self.create = to_streamed_response_wrapper(
            rate_limits.create,
        )
        self.list = to_streamed_response_wrapper(
            rate_limits.list,
        )
        self.delete = to_streamed_response_wrapper(
            rate_limits.delete,
        )
        self.edit = to_streamed_response_wrapper(
            rate_limits.edit,
        )
        self.get = to_streamed_response_wrapper(
            rate_limits.get,
        )


class AsyncRateLimitsWithStreamingResponse:
    def __init__(self, rate_limits: AsyncRateLimits) -> None:
        self._rate_limits = rate_limits

        self.create = async_to_streamed_response_wrapper(
            rate_limits.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rate_limits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rate_limits.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            rate_limits.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rate_limits.get,
        )
