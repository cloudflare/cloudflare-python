# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.mnms.configs import FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Fulls", "AsyncFulls"]


class Fulls(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FullsWithRawResponse:
        return FullsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FullsWithStreamingResponse:
        return FullsWithStreamingResponse(self)

    def magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse],
                ResultWrapper[FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse],
            ),
        )


class AsyncFulls(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFullsWithRawResponse:
        return AsyncFullsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFullsWithStreamingResponse:
        return AsyncFullsWithStreamingResponse(self)

    async def magic_network_monitoring_configuration_list_rules_and_account_configuration(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse],
                ResultWrapper[FullMagicNetworkMonitoringConfigurationListRulesAndAccountConfigurationResponse],
            ),
        )


class FullsWithRawResponse:
    def __init__(self, fulls: Fulls) -> None:
        self._fulls = fulls

        self.magic_network_monitoring_configuration_list_rules_and_account_configuration = to_raw_response_wrapper(
            fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration,
        )


class AsyncFullsWithRawResponse:
    def __init__(self, fulls: AsyncFulls) -> None:
        self._fulls = fulls

        self.magic_network_monitoring_configuration_list_rules_and_account_configuration = (
            async_to_raw_response_wrapper(
                fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration,
            )
        )


class FullsWithStreamingResponse:
    def __init__(self, fulls: Fulls) -> None:
        self._fulls = fulls

        self.magic_network_monitoring_configuration_list_rules_and_account_configuration = to_streamed_response_wrapper(
            fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration,
        )


class AsyncFullsWithStreamingResponse:
    def __init__(self, fulls: AsyncFulls) -> None:
        self._fulls = fulls

        self.magic_network_monitoring_configuration_list_rules_and_account_configuration = (
            async_to_streamed_response_wrapper(
                fulls.magic_network_monitoring_configuration_list_rules_and_account_configuration,
            )
        )
