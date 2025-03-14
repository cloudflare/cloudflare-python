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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloudforce_one.scans import config_create_params
from ....types.cloudforce_one.scans.config_list_response import ConfigListResponse
from ....types.cloudforce_one.scans.config_create_response import ConfigCreateResponse

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

    def create(
        self,
        *,
        account_id: str,
        ips: List[str],
        frequency: float | NotGiven = NOT_GIVEN,
        ports: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigCreateResponse]:
        """
        Create a new Scan Config

        Args:
          account_id: Account ID

          ips: A list of IP addresses or CIDR blocks to scan. The maximum number of total IP
              addresses allowed is 5000.

          frequency: The number of days between each scan (0 = no recurring scans).

          ports: A list of ports to scan. Allowed values:"default", "all", or a comma-separated
              list of ports or range of ports (e.g. ["1-80", "443"]). Default will scan the
              100 most commonly open ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/scans/config",
            body=maybe_transform(
                {
                    "ips": ips,
                    "frequency": frequency,
                    "ports": ports,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigCreateResponse]], ResultWrapper[ConfigCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ConfigListResponse]:
        """
        Get the Scan Config for An Account

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/cloudforce-one/scans/config",
            page=SyncSinglePage[ConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ConfigListResponse,
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

    async def create(
        self,
        *,
        account_id: str,
        ips: List[str],
        frequency: float | NotGiven = NOT_GIVEN,
        ports: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigCreateResponse]:
        """
        Create a new Scan Config

        Args:
          account_id: Account ID

          ips: A list of IP addresses or CIDR blocks to scan. The maximum number of total IP
              addresses allowed is 5000.

          frequency: The number of days between each scan (0 = no recurring scans).

          ports: A list of ports to scan. Allowed values:"default", "all", or a comma-separated
              list of ports or range of ports (e.g. ["1-80", "443"]). Default will scan the
              100 most commonly open ports.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/scans/config",
            body=await async_maybe_transform(
                {
                    "ips": ips,
                    "frequency": frequency,
                    "ports": ports,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ConfigCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ConfigCreateResponse]], ResultWrapper[ConfigCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ConfigListResponse, AsyncSinglePage[ConfigListResponse]]:
        """
        Get the Scan Config for An Account

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/cloudforce-one/scans/config",
            page=AsyncSinglePage[ConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ConfigListResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_raw_response_wrapper(
            config.create,
        )
        self.list = to_raw_response_wrapper(
            config.list,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_raw_response_wrapper(
            config.create,
        )
        self.list = async_to_raw_response_wrapper(
            config.list,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_streamed_response_wrapper(
            config.create,
        )
        self.list = to_streamed_response_wrapper(
            config.list,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_streamed_response_wrapper(
            config.create,
        )
        self.list = async_to_streamed_response_wrapper(
            config.list,
        )
