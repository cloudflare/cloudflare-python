# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import AlwaysUseHTTPUpdateResponse, AlwaysUseHTTPGetResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.settings import always_use_http_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AlwaysUseHTTPs", "AsyncAlwaysUseHTTPs"]


class AlwaysUseHTTPs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlwaysUseHTTPsWithRawResponse:
        return AlwaysUseHTTPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlwaysUseHTTPsWithStreamingResponse:
        return AlwaysUseHTTPsWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AlwaysUseHTTPUpdateResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/always_use_https",
            body=maybe_transform({"value": value}, always_use_http_update_params.AlwaysUseHTTPUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPUpdateResponse]], ResultWrapper[AlwaysUseHTTPUpdateResponse]),
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
    ) -> Optional[AlwaysUseHTTPGetResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPGetResponse]], ResultWrapper[AlwaysUseHTTPGetResponse]),
        )


class AsyncAlwaysUseHTTPs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlwaysUseHTTPsWithRawResponse:
        return AsyncAlwaysUseHTTPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlwaysUseHTTPsWithStreamingResponse:
        return AsyncAlwaysUseHTTPsWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AlwaysUseHTTPUpdateResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/always_use_https",
            body=maybe_transform({"value": value}, always_use_http_update_params.AlwaysUseHTTPUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPUpdateResponse]], ResultWrapper[AlwaysUseHTTPUpdateResponse]),
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
    ) -> Optional[AlwaysUseHTTPGetResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPGetResponse]], ResultWrapper[AlwaysUseHTTPGetResponse]),
        )


class AlwaysUseHTTPsWithRawResponse:
    def __init__(self, always_use_https: AlwaysUseHTTPs) -> None:
        self._always_use_https = always_use_https

        self.update = to_raw_response_wrapper(
            always_use_https.update,
        )
        self.get = to_raw_response_wrapper(
            always_use_https.get,
        )


class AsyncAlwaysUseHTTPsWithRawResponse:
    def __init__(self, always_use_https: AsyncAlwaysUseHTTPs) -> None:
        self._always_use_https = always_use_https

        self.update = async_to_raw_response_wrapper(
            always_use_https.update,
        )
        self.get = async_to_raw_response_wrapper(
            always_use_https.get,
        )


class AlwaysUseHTTPsWithStreamingResponse:
    def __init__(self, always_use_https: AlwaysUseHTTPs) -> None:
        self._always_use_https = always_use_https

        self.update = to_streamed_response_wrapper(
            always_use_https.update,
        )
        self.get = to_streamed_response_wrapper(
            always_use_https.get,
        )


class AsyncAlwaysUseHTTPsWithStreamingResponse:
    def __init__(self, always_use_https: AsyncAlwaysUseHTTPs) -> None:
        self._always_use_https = always_use_https

        self.update = async_to_streamed_response_wrapper(
            always_use_https.update,
        )
        self.get = async_to_streamed_response_wrapper(
            always_use_https.get,
        )
