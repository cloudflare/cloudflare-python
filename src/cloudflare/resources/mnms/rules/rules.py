# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .advertisements import Advertisements, AsyncAdvertisements

from ...._compat import cached_property

from ....types.mnms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleGetResponse,
    RuleMagicNetworkMonitoringRulesCreateRulesResponse,
    RuleMagicNetworkMonitoringRulesListRulesResponse,
    RuleMagicNetworkMonitoringRulesUpdateRulesResponse,
)

from typing import Type, Optional

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
from .advertisements import (
    Advertisements,
    AsyncAdvertisements,
    AdvertisementsWithRawResponse,
    AsyncAdvertisementsWithRawResponse,
    AdvertisementsWithStreamingResponse,
    AsyncAdvertisementsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def advertisements(self) -> Advertisements:
        return Advertisements(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def update(
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
    ) -> Optional[RuleUpdateResponse]:
        """
        Update a network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(
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
    ) -> Optional[RuleDeleteResponse]:
        """
        Delete a network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def get(
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
    ) -> Optional[RuleGetResponse]:
        """
        List a single network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
        )

    def magic_network_monitoring_rules_create_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesCreateRulesResponse],
            ),
        )

    def magic_network_monitoring_rules_list_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesListRulesResponse]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesListRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesListRulesResponse],
            ),
        )

    def magic_network_monitoring_rules_update_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesUpdateRulesResponse],
            ),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def advertisements(self) -> AsyncAdvertisements:
        return AsyncAdvertisements(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def update(
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
    ) -> Optional[RuleUpdateResponse]:
        """
        Update a network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(
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
    ) -> Optional[RuleDeleteResponse]:
        """
        Delete a network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def get(
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
    ) -> Optional[RuleGetResponse]:
        """
        List a single network monitoring rule for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/mnm/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
        )

    async def magic_network_monitoring_rules_create_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesCreateRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesCreateRulesResponse],
            ),
        )

    async def magic_network_monitoring_rules_list_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesListRulesResponse]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesListRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesListRulesResponse],
            ),
        )

    async def magic_network_monitoring_rules_update_rules(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_identifier}/mnm/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleMagicNetworkMonitoringRulesUpdateRulesResponse]],
                ResultWrapper[RuleMagicNetworkMonitoringRulesUpdateRulesResponse],
            ),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )
        self.magic_network_monitoring_rules_create_rules = to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_create_rules,
        )
        self.magic_network_monitoring_rules_list_rules = to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_list_rules,
        )
        self.magic_network_monitoring_rules_update_rules = to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_update_rules,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsWithRawResponse:
        return AdvertisementsWithRawResponse(self._rules.advertisements)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )
        self.magic_network_monitoring_rules_create_rules = async_to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_create_rules,
        )
        self.magic_network_monitoring_rules_list_rules = async_to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_list_rules,
        )
        self.magic_network_monitoring_rules_update_rules = async_to_raw_response_wrapper(
            rules.magic_network_monitoring_rules_update_rules,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsWithRawResponse:
        return AsyncAdvertisementsWithRawResponse(self._rules.advertisements)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )
        self.magic_network_monitoring_rules_create_rules = to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_create_rules,
        )
        self.magic_network_monitoring_rules_list_rules = to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_list_rules,
        )
        self.magic_network_monitoring_rules_update_rules = to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_update_rules,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsWithStreamingResponse:
        return AdvertisementsWithStreamingResponse(self._rules.advertisements)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
        self.magic_network_monitoring_rules_create_rules = async_to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_create_rules,
        )
        self.magic_network_monitoring_rules_list_rules = async_to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_list_rules,
        )
        self.magic_network_monitoring_rules_update_rules = async_to_streamed_response_wrapper(
            rules.magic_network_monitoring_rules_update_rules,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsWithStreamingResponse:
        return AsyncAdvertisementsWithStreamingResponse(self._rules.advertisements)
