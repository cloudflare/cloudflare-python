# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.magic_network_monitoring.rules import MagicVisibilityMNMRuleAdvertisable

__all__ = ["Advertisements", "AsyncAdvertisements"]


class Advertisements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvertisementsWithRawResponse:
        return AdvertisementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvertisementsWithStreamingResponse:
        return AdvertisementsWithStreamingResponse(self)

    def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicVisibilityMNMRuleAdvertisable]:
        """
        Update advertisement for rule.

        Args:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MagicVisibilityMNMRuleAdvertisable]], ResultWrapper[MagicVisibilityMNMRuleAdvertisable]
            ),
        )


class AsyncAdvertisements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvertisementsWithRawResponse:
        return AsyncAdvertisementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvertisementsWithStreamingResponse:
        return AsyncAdvertisementsWithStreamingResponse(self)

    async def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicVisibilityMNMRuleAdvertisable]:
        """
        Update advertisement for rule.

        Args:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MagicVisibilityMNMRuleAdvertisable]], ResultWrapper[MagicVisibilityMNMRuleAdvertisable]
            ),
        )


class AdvertisementsWithRawResponse:
    def __init__(self, advertisements: Advertisements) -> None:
        self._advertisements = advertisements

        self.edit = to_raw_response_wrapper(
            advertisements.edit,
        )


class AsyncAdvertisementsWithRawResponse:
    def __init__(self, advertisements: AsyncAdvertisements) -> None:
        self._advertisements = advertisements

        self.edit = async_to_raw_response_wrapper(
            advertisements.edit,
        )


class AdvertisementsWithStreamingResponse:
    def __init__(self, advertisements: Advertisements) -> None:
        self._advertisements = advertisements

        self.edit = to_streamed_response_wrapper(
            advertisements.edit,
        )


class AsyncAdvertisementsWithStreamingResponse:
    def __init__(self, advertisements: AsyncAdvertisements) -> None:
        self._advertisements = advertisements

        self.edit = async_to_streamed_response_wrapper(
            advertisements.edit,
        )
