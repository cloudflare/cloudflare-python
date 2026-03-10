# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.google_tag_gateway import config_update_params
from ...types.google_tag_gateway.config import Config

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        enabled: bool,
        endpoint: str,
        hide_original_ip: bool,
        measurement_id: str,
        set_up_tag: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Config]:
        """
        Updates the Google Tag Gateway configuration for a zone.

        Args:
          zone_id: Identifier.

          enabled: Enables or disables Google Tag Gateway for this zone.

          endpoint: Specifies the endpoint path for proxying Google Tag Manager requests. Use an
              absolute path starting with '/', with no nested paths and alphanumeric
              characters only (e.g. /metrics).

          hide_original_ip: Hides the original client IP address from Google when enabled.

          measurement_id: Specify the Google Tag Manager container or measurement ID (e.g. GTM-XXXXXXX or
              G-XXXXXXXXXX).

          set_up_tag: Set up the associated Google Tag on the zone automatically when enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/settings/google-tag-gateway/config",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "endpoint": endpoint,
                    "hide_original_ip": hide_original_ip,
                    "measurement_id": measurement_id,
                    "set_up_tag": set_up_tag,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Config]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Config]], ResultWrapper[Config]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Config]:
        """
        Gets the Google Tag Gateway configuration for a zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/google-tag-gateway/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Config]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Config]], ResultWrapper[Config]),
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        enabled: bool,
        endpoint: str,
        hide_original_ip: bool,
        measurement_id: str,
        set_up_tag: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Config]:
        """
        Updates the Google Tag Gateway configuration for a zone.

        Args:
          zone_id: Identifier.

          enabled: Enables or disables Google Tag Gateway for this zone.

          endpoint: Specifies the endpoint path for proxying Google Tag Manager requests. Use an
              absolute path starting with '/', with no nested paths and alphanumeric
              characters only (e.g. /metrics).

          hide_original_ip: Hides the original client IP address from Google when enabled.

          measurement_id: Specify the Google Tag Manager container or measurement ID (e.g. GTM-XXXXXXX or
              G-XXXXXXXXXX).

          set_up_tag: Set up the associated Google Tag on the zone automatically when enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/settings/google-tag-gateway/config",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "endpoint": endpoint,
                    "hide_original_ip": hide_original_ip,
                    "measurement_id": measurement_id,
                    "set_up_tag": set_up_tag,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Config]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Config]], ResultWrapper[Config]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Config]:
        """
        Gets the Google Tag Gateway configuration for a zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/google-tag-gateway/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Config]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Config]], ResultWrapper[Config]),
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
