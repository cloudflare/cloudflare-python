# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from .._compat import cached_property

from ..types.rate_limits.rate_limit_create_response import RateLimitCreateResponse

from .._wrappers import ResultWrapper

from .._utils import maybe_transform, async_maybe_transform

from .._base_client import make_request_options, AsyncPaginator

from ..types.rate_limits.rate_limit import RateLimit

from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ..types.rate_limits.rate_limit_delete_response import RateLimitDeleteResponse

from typing import Type

from ..types.rate_limits.rate_limit_edit_response import RateLimitEditResponse

from ..types.rate_limits.rate_limit_get_response import RateLimitGetResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ..types.rate_limits import rate_limit_create_params, rate_limit_edit_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types.rate_limits import rate_limit_create_params
from ..types.rate_limits import rate_limit_list_params
from ..types.rate_limits import rate_limit_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RateLimitsResource", "AsyncRateLimitsResource"]


class RateLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RateLimitsResourceWithRawResponse:
        return RateLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateLimitsResourceWithStreamingResponse:
        return RateLimitsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
    )
    def create(
        self,
        zone_identifier: str,
        *,
        action: rate_limit_create_params.Action,
        match: rate_limit_create_params.Match,
        period: float,
        threshold: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitCreateResponse:
        """Creates a new rate limit for a zone.

        Refer to the object definition for a list
        of required attributes.

        Args:
          zone_identifier: Identifier

          action: The action to perform when the threshold of matched traffic within the
              configured period is exceeded.

          match: Determines which traffic the rate limit counts towards the threshold.

          period: The time in seconds (an integer value) to count matching traffic. If the count
              exceeds the configured threshold within this period, Cloudflare will perform the
              configured action.

          threshold: The threshold that will trigger the configured mitigation action. Configure this
              value along with the `period` property to establish a threshold per period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            RateLimitCreateResponse,
            self._post(
                f"/zones/{zone_identifier}/rate_limits",
                body=maybe_transform(
                    {
                        "action": action,
                        "match": match,
                        "period": period,
                        "threshold": threshold,
                    },
                    rate_limit_create_params.RateLimitCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> SyncV4PagePaginationArray[RateLimit]:
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
            page=SyncV4PagePaginationArray[RateLimit],
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
            model=RateLimit,
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> RateLimitDeleteResponse:
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
                post_parser=ResultWrapper[RateLimitDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RateLimitDeleteResponse], ResultWrapper[RateLimitDeleteResponse]),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
    )
    def edit(
        self,
        id: str,
        *,
        zone_identifier: str,
        action: rate_limit_edit_params.Action,
        match: rate_limit_edit_params.Match,
        period: float,
        threshold: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitEditResponse:
        """
        Updates an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          action: The action to perform when the threshold of matched traffic within the
              configured period is exceeded.

          match: Determines which traffic the rate limit counts towards the threshold.

          period: The time in seconds (an integer value) to count matching traffic. If the count
              exceeds the configured threshold within this period, Cloudflare will perform the
              configured action.

          threshold: The threshold that will trigger the configured mitigation action. Configure this
              value along with the `period` property to establish a threshold per period.

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
            RateLimitEditResponse,
            self._put(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                body=maybe_transform(
                    {
                        "action": action,
                        "match": match,
                        "period": period,
                        "threshold": threshold,
                    },
                    rate_limit_edit_params.RateLimitEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> RateLimitGetResponse:
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
            RateLimitGetResponse,
            self._get(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRateLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRateLimitsResourceWithRawResponse:
        return AsyncRateLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateLimitsResourceWithStreamingResponse:
        return AsyncRateLimitsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
    )
    async def create(
        self,
        zone_identifier: str,
        *,
        action: rate_limit_create_params.Action,
        match: rate_limit_create_params.Match,
        period: float,
        threshold: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitCreateResponse:
        """Creates a new rate limit for a zone.

        Refer to the object definition for a list
        of required attributes.

        Args:
          zone_identifier: Identifier

          action: The action to perform when the threshold of matched traffic within the
              configured period is exceeded.

          match: Determines which traffic the rate limit counts towards the threshold.

          period: The time in seconds (an integer value) to count matching traffic. If the count
              exceeds the configured threshold within this period, Cloudflare will perform the
              configured action.

          threshold: The threshold that will trigger the configured mitigation action. Configure this
              value along with the `period` property to establish a threshold per period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            RateLimitCreateResponse,
            await self._post(
                f"/zones/{zone_identifier}/rate_limits",
                body=await async_maybe_transform(
                    {
                        "action": action,
                        "match": match,
                        "period": period,
                        "threshold": threshold,
                    },
                    rate_limit_create_params.RateLimitCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> AsyncPaginator[RateLimit, AsyncV4PagePaginationArray[RateLimit]]:
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
            page=AsyncV4PagePaginationArray[RateLimit],
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
            model=RateLimit,
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> RateLimitDeleteResponse:
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
                post_parser=ResultWrapper[RateLimitDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RateLimitDeleteResponse], ResultWrapper[RateLimitDeleteResponse]),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
    )
    async def edit(
        self,
        id: str,
        *,
        zone_identifier: str,
        action: rate_limit_edit_params.Action,
        match: rate_limit_edit_params.Match,
        period: float,
        threshold: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateLimitEditResponse:
        """
        Updates an existing rate limit.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the rate limit.

          action: The action to perform when the threshold of matched traffic within the
              configured period is exceeded.

          match: Determines which traffic the rate limit counts towards the threshold.

          period: The time in seconds (an integer value) to count matching traffic. If the count
              exceeds the configured threshold within this period, Cloudflare will perform the
              configured action.

          threshold: The threshold that will trigger the configured mitigation action. Configure this
              value along with the `period` property to establish a threshold per period.

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
            RateLimitEditResponse,
            await self._put(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                body=await async_maybe_transform(
                    {
                        "action": action,
                        "match": match,
                        "period": period,
                        "threshold": threshold,
                    },
                    rate_limit_edit_params.RateLimitEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @typing_extensions.deprecated(
        "Rate limiting API is deprecated in favour of using the Ruleset Engine. See https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#rate-limiting-api-previous-version for full details."
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
    ) -> RateLimitGetResponse:
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
            RateLimitGetResponse,
            await self._get(
                f"/zones/{zone_identifier}/rate_limits/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RateLimitGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RateLimitGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RateLimitsResourceWithRawResponse:
    def __init__(self, rate_limits: RateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                rate_limits.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                rate_limits.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                rate_limits.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                rate_limits.edit  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                rate_limits.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRateLimitsResourceWithRawResponse:
    def __init__(self, rate_limits: AsyncRateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                rate_limits.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                rate_limits.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                rate_limits.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                rate_limits.edit  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                rate_limits.get  # pyright: ignore[reportDeprecated],
            )
        )


class RateLimitsResourceWithStreamingResponse:
    def __init__(self, rate_limits: RateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                rate_limits.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                rate_limits.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                rate_limits.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                rate_limits.edit  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                rate_limits.get  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncRateLimitsResourceWithStreamingResponse:
    def __init__(self, rate_limits: AsyncRateLimitsResource) -> None:
        self._rate_limits = rate_limits

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                rate_limits.create  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                rate_limits.list  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                rate_limits.delete  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                rate_limits.edit  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                rate_limits.get  # pyright: ignore[reportDeprecated],
            )
        )
