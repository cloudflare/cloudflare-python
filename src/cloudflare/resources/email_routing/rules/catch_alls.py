# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

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
from ...._base_client import make_request_options
from ....types.email_routing.rules import catch_all_update_params
from ....types.email_routing.rules.catch_all_action_param import CatchAllActionParam
from ....types.email_routing.rules.catch_all_get_response import CatchAllGetResponse
from ....types.email_routing.rules.catch_all_matcher_param import CatchAllMatcherParam
from ....types.email_routing.rules.catch_all_update_response import CatchAllUpdateResponse

__all__ = ["CatchAllsResource", "AsyncCatchAllsResource"]


class CatchAllsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatchAllsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CatchAllsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatchAllsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CatchAllsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        actions: Iterable[CatchAllActionParam],
        matchers: Iterable[CatchAllMatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CatchAllUpdateResponse]:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_id: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/email/routing/rules/catch_all",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                },
                catch_all_update_params.CatchAllUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CatchAllUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CatchAllUpdateResponse]], ResultWrapper[CatchAllUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CatchAllGetResponse]:
        """
        Get information on the default catch-all routing rule.

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
            f"/zones/{zone_id}/email/routing/rules/catch_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CatchAllGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CatchAllGetResponse]], ResultWrapper[CatchAllGetResponse]),
        )


class AsyncCatchAllsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatchAllsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCatchAllsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatchAllsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCatchAllsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        actions: Iterable[CatchAllActionParam],
        matchers: Iterable[CatchAllMatcherParam],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CatchAllUpdateResponse]:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_id: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/email/routing/rules/catch_all",
            body=await async_maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                },
                catch_all_update_params.CatchAllUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CatchAllUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CatchAllUpdateResponse]], ResultWrapper[CatchAllUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CatchAllGetResponse]:
        """
        Get information on the default catch-all routing rule.

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
            f"/zones/{zone_id}/email/routing/rules/catch_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CatchAllGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CatchAllGetResponse]], ResultWrapper[CatchAllGetResponse]),
        )


class CatchAllsResourceWithRawResponse:
    def __init__(self, catch_alls: CatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = to_raw_response_wrapper(
            catch_alls.update,
        )
        self.get = to_raw_response_wrapper(
            catch_alls.get,
        )


class AsyncCatchAllsResourceWithRawResponse:
    def __init__(self, catch_alls: AsyncCatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = async_to_raw_response_wrapper(
            catch_alls.update,
        )
        self.get = async_to_raw_response_wrapper(
            catch_alls.get,
        )


class CatchAllsResourceWithStreamingResponse:
    def __init__(self, catch_alls: CatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = to_streamed_response_wrapper(
            catch_alls.update,
        )
        self.get = to_streamed_response_wrapper(
            catch_alls.get,
        )


class AsyncCatchAllsResourceWithStreamingResponse:
    def __init__(self, catch_alls: AsyncCatchAllsResource) -> None:
        self._catch_alls = catch_alls

        self.update = async_to_streamed_response_wrapper(
            catch_alls.update,
        )
        self.get = async_to_streamed_response_wrapper(
            catch_alls.get,
        )
