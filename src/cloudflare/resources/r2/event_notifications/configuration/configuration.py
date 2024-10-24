# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .queues import (
    QueuesResource,
    AsyncQueuesResource,
    QueuesResourceWithRawResponse,
    AsyncQueuesResourceWithRawResponse,
    QueuesResourceWithStreamingResponse,
    AsyncQueuesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import is_given, strip_not_given
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.r2.event_notifications.configuration_get_response import ConfigurationGetResponse

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    @cached_property
    def queues(self) -> QueuesResource:
        return QueuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigurationResourceWithStreamingResponse(self)

    def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationGetResponse:
        """
        List all event notification rules for a bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          cf_r2_jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationGetResponse], ResultWrapper[ConfigurationGetResponse]),
        )


class AsyncConfigurationResource(AsyncAPIResource):
    @cached_property
    def queues(self) -> AsyncQueuesResource:
        return AsyncQueuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigurationResourceWithStreamingResponse(self)

    async def get(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cf_r2_jurisdiction: Literal["default", "eu", "fedramp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationGetResponse:
        """
        List all event notification rules for a bucket.

        Args:
          account_id: Account ID

          bucket_name: Name of the bucket

          cf_r2_jurisdiction: The bucket jurisdiction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given(
                {"cf-r2-jurisdiction": str(cf_r2_jurisdiction) if is_given(cf_r2_jurisdiction) else NOT_GIVEN}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationGetResponse], ResultWrapper[ConfigurationGetResponse]),
        )


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.get = to_raw_response_wrapper(
            configuration.get,
        )

    @cached_property
    def queues(self) -> QueuesResourceWithRawResponse:
        return QueuesResourceWithRawResponse(self._configuration.queues)


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.get = async_to_raw_response_wrapper(
            configuration.get,
        )

    @cached_property
    def queues(self) -> AsyncQueuesResourceWithRawResponse:
        return AsyncQueuesResourceWithRawResponse(self._configuration.queues)


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.get = to_streamed_response_wrapper(
            configuration.get,
        )

    @cached_property
    def queues(self) -> QueuesResourceWithStreamingResponse:
        return QueuesResourceWithStreamingResponse(self._configuration.queues)


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.get = async_to_streamed_response_wrapper(
            configuration.get,
        )

    @cached_property
    def queues(self) -> AsyncQueuesResourceWithStreamingResponse:
        return AsyncQueuesResourceWithStreamingResponse(self._configuration.queues)
