# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.caches import (
    VariantListResponse,
    VariantDeleteResponse,
    VariantZoneCacheSettingsChangeVariantsSettingResponse,
    variant_zone_cache_settings_change_variants_setting_params,
)

from typing import Type

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
from ...types.caches import variant_zone_cache_settings_change_variants_setting_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Variants", "AsyncVariants"]


class Variants(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self)

    def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantListResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantListResponse], ResultWrapper[VariantListResponse]),
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
    ) -> VariantDeleteResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantDeleteResponse], ResultWrapper[VariantDeleteResponse]),
        )

    def zone_cache_settings_change_variants_setting(
        self,
        zone_id: str,
        *,
        value: variant_zone_cache_settings_change_variants_setting_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantZoneCacheSettingsChangeVariantsSettingResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            body=maybe_transform(
                {"value": value},
                variant_zone_cache_settings_change_variants_setting_params.VariantZoneCacheSettingsChangeVariantsSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VariantZoneCacheSettingsChangeVariantsSettingResponse],
                ResultWrapper[VariantZoneCacheSettingsChangeVariantsSettingResponse],
            ),
        )


class AsyncVariants(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self)

    async def list(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantListResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantListResponse], ResultWrapper[VariantListResponse]),
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
    ) -> VariantDeleteResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/cache/variants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VariantDeleteResponse], ResultWrapper[VariantDeleteResponse]),
        )

    async def zone_cache_settings_change_variants_setting(
        self,
        zone_id: str,
        *,
        value: variant_zone_cache_settings_change_variants_setting_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantZoneCacheSettingsChangeVariantsSettingResponse:
        """
        Variant support enables caching variants of images with certain file extensions
        in addition to the original. This only applies when the origin server sends the
        'Vary: Accept' response header. If the origin server sends 'Vary: Accept' but
        does not serve the variant requested, the response will not be cached. This will
        be indicated with BYPASS cache status in the response headers.

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
            f"/zones/{zone_id}/cache/variants",
            body=maybe_transform(
                {"value": value},
                variant_zone_cache_settings_change_variants_setting_params.VariantZoneCacheSettingsChangeVariantsSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VariantZoneCacheSettingsChangeVariantsSettingResponse],
                ResultWrapper[VariantZoneCacheSettingsChangeVariantsSettingResponse],
            ),
        )


class VariantsWithRawResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.list = to_raw_response_wrapper(
            variants.list,
        )
        self.delete = to_raw_response_wrapper(
            variants.delete,
        )
        self.zone_cache_settings_change_variants_setting = to_raw_response_wrapper(
            variants.zone_cache_settings_change_variants_setting,
        )


class AsyncVariantsWithRawResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.list = async_to_raw_response_wrapper(
            variants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            variants.delete,
        )
        self.zone_cache_settings_change_variants_setting = async_to_raw_response_wrapper(
            variants.zone_cache_settings_change_variants_setting,
        )


class VariantsWithStreamingResponse:
    def __init__(self, variants: Variants) -> None:
        self._variants = variants

        self.list = to_streamed_response_wrapper(
            variants.list,
        )
        self.delete = to_streamed_response_wrapper(
            variants.delete,
        )
        self.zone_cache_settings_change_variants_setting = to_streamed_response_wrapper(
            variants.zone_cache_settings_change_variants_setting,
        )


class AsyncVariantsWithStreamingResponse:
    def __init__(self, variants: AsyncVariants) -> None:
        self._variants = variants

        self.list = async_to_streamed_response_wrapper(
            variants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            variants.delete,
        )
        self.zone_cache_settings_change_variants_setting = async_to_streamed_response_wrapper(
            variants.zone_cache_settings_change_variants_setting,
        )
