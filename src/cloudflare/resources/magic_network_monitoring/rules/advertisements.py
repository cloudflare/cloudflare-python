# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.magic_network_monitoring.rules import advertisement_edit_params
from ....types.magic_network_monitoring.rules.advertisement import Advertisement

__all__ = ["AdvertisementsResource", "AsyncAdvertisementsResource"]


class AdvertisementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvertisementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AdvertisementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvertisementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AdvertisementsResourceWithStreamingResponse(self)

    def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Advertisement]:
        """Update advertisement for rule.

        Args:
          rule_id: The id of the rule.

        Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}/advertisement",
            body=maybe_transform(body, advertisement_edit_params.AdvertisementEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Advertisement]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Advertisement]], ResultWrapper[Advertisement]),
        )


class AsyncAdvertisementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvertisementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvertisementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvertisementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAdvertisementsResourceWithStreamingResponse(self)

    async def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Advertisement]:
        """Update advertisement for rule.

        Args:
          rule_id: The id of the rule.

        Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}/advertisement",
            body=await async_maybe_transform(body, advertisement_edit_params.AdvertisementEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Advertisement]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Advertisement]], ResultWrapper[Advertisement]),
        )


class AdvertisementsResourceWithRawResponse:
    def __init__(self, advertisements: AdvertisementsResource) -> None:
        self._advertisements = advertisements

        self.edit = to_raw_response_wrapper(
            advertisements.edit,
        )


class AsyncAdvertisementsResourceWithRawResponse:
    def __init__(self, advertisements: AsyncAdvertisementsResource) -> None:
        self._advertisements = advertisements

        self.edit = async_to_raw_response_wrapper(
            advertisements.edit,
        )


class AdvertisementsResourceWithStreamingResponse:
    def __init__(self, advertisements: AdvertisementsResource) -> None:
        self._advertisements = advertisements

        self.edit = to_streamed_response_wrapper(
            advertisements.edit,
        )


class AsyncAdvertisementsResourceWithStreamingResponse:
    def __init__(self, advertisements: AsyncAdvertisementsResource) -> None:
        self._advertisements = advertisements

        self.edit = async_to_streamed_response_wrapper(
            advertisements.edit,
        )
