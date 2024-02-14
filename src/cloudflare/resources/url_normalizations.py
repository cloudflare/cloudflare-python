# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
    URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
)

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import url_normalization_url_normalization_update_url_normalization_settings_params
from .._wrappers import ResultWrapper

__all__ = ["URLNormalizations", "AsyncURLNormalizations"]


class URLNormalizations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLNormalizationsWithRawResponse:
        return URLNormalizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLNormalizationsWithStreamingResponse:
        return URLNormalizationsWithStreamingResponse(self)

    def url_normalization_get_url_normalization_settings(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse:
        """
        Fetches the current URL normalization settings.

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
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
        )

    def url_normalization_update_url_normalization_settings(
        self,
        zone_id: str,
        *,
        scope: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse:
        """
        Updates the URL normalization settings.

        Args:
          zone_id: Identifier

          scope: The scope of the URL normalization.

          type: The type of URL normalization performed by Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/url_normalization",
            body=maybe_transform(
                {
                    "scope": scope,
                    "type": type,
                },
                url_normalization_url_normalization_update_url_normalization_settings_params.URLNormalizationURLNormalizationUpdateURLNormalizationSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
        )


class AsyncURLNormalizations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLNormalizationsWithRawResponse:
        return AsyncURLNormalizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLNormalizationsWithStreamingResponse:
        return AsyncURLNormalizationsWithStreamingResponse(self)

    async def url_normalization_get_url_normalization_settings(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse:
        """
        Fetches the current URL normalization settings.

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
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
        )

    async def url_normalization_update_url_normalization_settings(
        self,
        zone_id: str,
        *,
        scope: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse:
        """
        Updates the URL normalization settings.

        Args:
          zone_id: Identifier

          scope: The scope of the URL normalization.

          type: The type of URL normalization performed by Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/url_normalization",
            body=maybe_transform(
                {
                    "scope": scope,
                    "type": type,
                },
                url_normalization_url_normalization_update_url_normalization_settings_params.URLNormalizationURLNormalizationUpdateURLNormalizationSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
        )


class URLNormalizationsWithRawResponse:
    def __init__(self, url_normalizations: URLNormalizations) -> None:
        self._url_normalizations = url_normalizations

        self.url_normalization_get_url_normalization_settings = to_raw_response_wrapper(
            url_normalizations.url_normalization_get_url_normalization_settings,
        )
        self.url_normalization_update_url_normalization_settings = to_raw_response_wrapper(
            url_normalizations.url_normalization_update_url_normalization_settings,
        )


class AsyncURLNormalizationsWithRawResponse:
    def __init__(self, url_normalizations: AsyncURLNormalizations) -> None:
        self._url_normalizations = url_normalizations

        self.url_normalization_get_url_normalization_settings = async_to_raw_response_wrapper(
            url_normalizations.url_normalization_get_url_normalization_settings,
        )
        self.url_normalization_update_url_normalization_settings = async_to_raw_response_wrapper(
            url_normalizations.url_normalization_update_url_normalization_settings,
        )


class URLNormalizationsWithStreamingResponse:
    def __init__(self, url_normalizations: URLNormalizations) -> None:
        self._url_normalizations = url_normalizations

        self.url_normalization_get_url_normalization_settings = to_streamed_response_wrapper(
            url_normalizations.url_normalization_get_url_normalization_settings,
        )
        self.url_normalization_update_url_normalization_settings = to_streamed_response_wrapper(
            url_normalizations.url_normalization_update_url_normalization_settings,
        )


class AsyncURLNormalizationsWithStreamingResponse:
    def __init__(self, url_normalizations: AsyncURLNormalizations) -> None:
        self._url_normalizations = url_normalizations

        self.url_normalization_get_url_normalization_settings = async_to_streamed_response_wrapper(
            url_normalizations.url_normalization_get_url_normalization_settings,
        )
        self.url_normalization_update_url_normalization_settings = async_to_streamed_response_wrapper(
            url_normalizations.url_normalization_update_url_normalization_settings,
        )
