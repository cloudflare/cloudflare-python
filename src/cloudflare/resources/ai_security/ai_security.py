# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .custom_topics import (
    CustomTopicsResource,
    AsyncCustomTopicsResource,
    CustomTopicsResourceWithRawResponse,
    AsyncCustomTopicsResourceWithRawResponse,
    CustomTopicsResourceWithStreamingResponse,
    AsyncCustomTopicsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.ai_security import ai_security_update_params
from ...types.ai_security.ai_security_get_response import AISecurityGetResponse
from ...types.ai_security.ai_security_update_response import AISecurityUpdateResponse

__all__ = ["AISecurityResource", "AsyncAISecurityResource"]


class AISecurityResource(SyncAPIResource):
    @cached_property
    def custom_topics(self) -> CustomTopicsResource:
        return CustomTopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AISecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AISecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AISecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AISecurityResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISecurityUpdateResponse:
        """
        Enable or disable AI Security for Apps for a zone.

        Changes can take up to a minute to propagate to the zone.

        Args:
          zone_id: Defines the zone.

          enabled: Whether AI Security for Apps is enabled on the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            path_template("/zones/{zone_id}/ai-security/settings", zone_id=zone_id),
            body=maybe_transform({"enabled": enabled}, ai_security_update_params.AISecurityUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AISecurityUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AISecurityUpdateResponse], ResultWrapper[AISecurityUpdateResponse]),
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
    ) -> AISecurityGetResponse:
        """
        Get whether AI Security for Apps is enabled or disabled for a zone.

        Args:
          zone_id: Defines the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/ai-security/settings", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AISecurityGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AISecurityGetResponse], ResultWrapper[AISecurityGetResponse]),
        )


class AsyncAISecurityResource(AsyncAPIResource):
    @cached_property
    def custom_topics(self) -> AsyncCustomTopicsResource:
        return AsyncCustomTopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAISecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAISecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAISecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAISecurityResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AISecurityUpdateResponse:
        """
        Enable or disable AI Security for Apps for a zone.

        Changes can take up to a minute to propagate to the zone.

        Args:
          zone_id: Defines the zone.

          enabled: Whether AI Security for Apps is enabled on the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            path_template("/zones/{zone_id}/ai-security/settings", zone_id=zone_id),
            body=await async_maybe_transform({"enabled": enabled}, ai_security_update_params.AISecurityUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AISecurityUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[AISecurityUpdateResponse], ResultWrapper[AISecurityUpdateResponse]),
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
    ) -> AISecurityGetResponse:
        """
        Get whether AI Security for Apps is enabled or disabled for a zone.

        Args:
          zone_id: Defines the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/ai-security/settings", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AISecurityGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AISecurityGetResponse], ResultWrapper[AISecurityGetResponse]),
        )


class AISecurityResourceWithRawResponse:
    def __init__(self, ai_security: AISecurityResource) -> None:
        self._ai_security = ai_security

        self.update = to_raw_response_wrapper(
            ai_security.update,
        )
        self.get = to_raw_response_wrapper(
            ai_security.get,
        )

    @cached_property
    def custom_topics(self) -> CustomTopicsResourceWithRawResponse:
        return CustomTopicsResourceWithRawResponse(self._ai_security.custom_topics)


class AsyncAISecurityResourceWithRawResponse:
    def __init__(self, ai_security: AsyncAISecurityResource) -> None:
        self._ai_security = ai_security

        self.update = async_to_raw_response_wrapper(
            ai_security.update,
        )
        self.get = async_to_raw_response_wrapper(
            ai_security.get,
        )

    @cached_property
    def custom_topics(self) -> AsyncCustomTopicsResourceWithRawResponse:
        return AsyncCustomTopicsResourceWithRawResponse(self._ai_security.custom_topics)


class AISecurityResourceWithStreamingResponse:
    def __init__(self, ai_security: AISecurityResource) -> None:
        self._ai_security = ai_security

        self.update = to_streamed_response_wrapper(
            ai_security.update,
        )
        self.get = to_streamed_response_wrapper(
            ai_security.get,
        )

    @cached_property
    def custom_topics(self) -> CustomTopicsResourceWithStreamingResponse:
        return CustomTopicsResourceWithStreamingResponse(self._ai_security.custom_topics)


class AsyncAISecurityResourceWithStreamingResponse:
    def __init__(self, ai_security: AsyncAISecurityResource) -> None:
        self._ai_security = ai_security

        self.update = async_to_streamed_response_wrapper(
            ai_security.update,
        )
        self.get = async_to_streamed_response_wrapper(
            ai_security.get,
        )

    @cached_property
    def custom_topics(self) -> AsyncCustomTopicsResourceWithStreamingResponse:
        return AsyncCustomTopicsResourceWithStreamingResponse(self._ai_security.custom_topics)
