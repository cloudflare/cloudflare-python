# File generated from our OpenAPI spec by Stainless.

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
from ....types.mnms.rules import AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse

__all__ = ["Advertisements", "AsyncAdvertisements"]


class Advertisements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvertisementsWithRawResponse:
        return AdvertisementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvertisementsWithStreamingResponse:
        return AdvertisementsWithStreamingResponse(self)

    def magic_network_monitoring_rules_update_advertisement_for_rule(
        self,
        rule_identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse]:
        """
        Update advertisement for rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}/advertisement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse]],
                ResultWrapper[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            ),
        )


class AsyncAdvertisements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvertisementsWithRawResponse:
        return AsyncAdvertisementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvertisementsWithStreamingResponse:
        return AsyncAdvertisementsWithStreamingResponse(self)

    async def magic_network_monitoring_rules_update_advertisement_for_rule(
        self,
        rule_identifier: object,
        *,
        account_identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse]:
        """
        Update advertisement for rule.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}/advertisement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse]],
                ResultWrapper[AdvertisementMagicNetworkMonitoringRulesUpdateAdvertisementForRuleResponse],
            ),
        )


class AdvertisementsWithRawResponse:
    def __init__(self, advertisements: Advertisements) -> None:
        self._advertisements = advertisements

        self.magic_network_monitoring_rules_update_advertisement_for_rule = to_raw_response_wrapper(
            advertisements.magic_network_monitoring_rules_update_advertisement_for_rule,
        )


class AsyncAdvertisementsWithRawResponse:
    def __init__(self, advertisements: AsyncAdvertisements) -> None:
        self._advertisements = advertisements

        self.magic_network_monitoring_rules_update_advertisement_for_rule = async_to_raw_response_wrapper(
            advertisements.magic_network_monitoring_rules_update_advertisement_for_rule,
        )


class AdvertisementsWithStreamingResponse:
    def __init__(self, advertisements: Advertisements) -> None:
        self._advertisements = advertisements

        self.magic_network_monitoring_rules_update_advertisement_for_rule = to_streamed_response_wrapper(
            advertisements.magic_network_monitoring_rules_update_advertisement_for_rule,
        )


class AsyncAdvertisementsWithStreamingResponse:
    def __init__(self, advertisements: AsyncAdvertisements) -> None:
        self._advertisements = advertisements

        self.magic_network_monitoring_rules_update_advertisement_for_rule = async_to_streamed_response_wrapper(
            advertisements.magic_network_monitoring_rules_update_advertisement_for_rule,
        )
