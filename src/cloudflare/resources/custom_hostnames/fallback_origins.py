# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.custom_hostnames import (
    FallbackOriginUpdateResponse,
    FallbackOriginDeleteResponse,
    FallbackOriginGetResponse,
)

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
from ...types.custom_hostnames import fallback_origin_update_params
from ..._wrappers import ResultWrapper
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

__all__ = ["FallbackOrigins", "AsyncFallbackOrigins"]


class FallbackOrigins(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallbackOriginsWithRawResponse:
        return FallbackOriginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallbackOriginsWithStreamingResponse:
        return FallbackOriginsWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        origin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallbackOriginUpdateResponse:
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
        return cast(
            FallbackOriginUpdateResponse,
            self._put(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                body=maybe_transform({"origin": origin}, fallback_origin_update_params.FallbackOriginUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallbackOriginDeleteResponse:
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
        return cast(
            FallbackOriginDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> FallbackOriginGetResponse:
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
        return cast(
            FallbackOriginGetResponse,
            self._get(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncFallbackOrigins(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFallbackOriginsWithRawResponse:
        return AsyncFallbackOriginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallbackOriginsWithStreamingResponse:
        return AsyncFallbackOriginsWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        origin: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallbackOriginUpdateResponse:
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
        return cast(
            FallbackOriginUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                body=maybe_transform({"origin": origin}, fallback_origin_update_params.FallbackOriginUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallbackOriginDeleteResponse:
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
        return cast(
            FallbackOriginDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> FallbackOriginGetResponse:
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
        return cast(
            FallbackOriginGetResponse,
            await self._get(
                f"/zones/{zone_id}/custom_hostnames/fallback_origin",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[FallbackOriginGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class FallbackOriginsWithRawResponse:
    def __init__(self, fallback_origins: FallbackOrigins) -> None:
        self._fallback_origins = fallback_origins

        self.update = to_raw_response_wrapper(
            fallback_origins.update,
        )
        self.delete = to_raw_response_wrapper(
            fallback_origins.delete,
        )
        self.get = to_raw_response_wrapper(
            fallback_origins.get,
        )


class AsyncFallbackOriginsWithRawResponse:
    def __init__(self, fallback_origins: AsyncFallbackOrigins) -> None:
        self._fallback_origins = fallback_origins

        self.update = async_to_raw_response_wrapper(
            fallback_origins.update,
        )
        self.delete = async_to_raw_response_wrapper(
            fallback_origins.delete,
        )
        self.get = async_to_raw_response_wrapper(
            fallback_origins.get,
        )


class FallbackOriginsWithStreamingResponse:
    def __init__(self, fallback_origins: FallbackOrigins) -> None:
        self._fallback_origins = fallback_origins

        self.update = to_streamed_response_wrapper(
            fallback_origins.update,
        )
        self.delete = to_streamed_response_wrapper(
            fallback_origins.delete,
        )
        self.get = to_streamed_response_wrapper(
            fallback_origins.get,
        )


class AsyncFallbackOriginsWithStreamingResponse:
    def __init__(self, fallback_origins: AsyncFallbackOrigins) -> None:
        self._fallback_origins = fallback_origins

        self.update = async_to_streamed_response_wrapper(
            fallback_origins.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            fallback_origins.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            fallback_origins.get,
        )
