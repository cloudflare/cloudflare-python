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
from .advertisements import (
    AdvertisementsResource,
    AsyncAdvertisementsResource,
    AdvertisementsResourceWithRawResponse,
    AsyncAdvertisementsResourceWithRawResponse,
    AdvertisementsResourceWithStreamingResponse,
    AsyncAdvertisementsResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_network_monitoring import rule_edit_params, rule_create_params, rule_update_params
from ....types.magic_network_monitoring.rule_get_response import RuleGetResponse
from ....types.magic_network_monitoring.rule_edit_response import RuleEditResponse
from ....types.magic_network_monitoring.rule_list_response import RuleListResponse
from ....types.magic_network_monitoring.rule_create_response import RuleCreateResponse
from ....types.magic_network_monitoring.rule_delete_response import RuleDeleteResponse
from ....types.magic_network_monitoring.rule_update_response import RuleUpdateResponse

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def advertisements(self) -> AdvertisementsResource:
        return AdvertisementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        duration: str,
        name: str,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleCreateResponse]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    def update(
        self,
        *,
        account_id: str,
        duration: str,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Update network monitoring rules for account.

        Args:
          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          id: The id of the rule. Must be unique.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "id": id,
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
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
    ) -> SyncSinglePage[Optional[RuleListResponse]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page=SyncSinglePage[Optional[RuleListResponse]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RuleListResponse,
        )

    def delete(
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
    ) -> Optional[RuleDeleteResponse]:
        """
        Delete a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleEditResponse]:
        """
        Update a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

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
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=maybe_transform(
                {
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "duration": duration,
                    "name": name,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleEditResponse]], ResultWrapper[RuleEditResponse]),
        )

    def get(
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
    ) -> Optional[RuleGetResponse]:
        """
        List a single network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResource:
        return AsyncAdvertisementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        duration: str,
        name: str,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleCreateResponse]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    async def update(
        self,
        *,
        account_id: str,
        duration: str,
        name: str,
        id: str | NotGiven = NOT_GIVEN,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Update network monitoring rules for account.

        Args:
          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          id: The id of the rule. Must be unique.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                    "id": id,
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
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
    ) -> AsyncPaginator[Optional[RuleListResponse], AsyncSinglePage[Optional[RuleListResponse]]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page=AsyncSinglePage[Optional[RuleListResponse]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RuleListResponse,
        )

    async def delete(
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
    ) -> Optional[RuleDeleteResponse]:
        """
        Delete a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        automatic_advertisement: Optional[bool] | NotGiven = NOT_GIVEN,
        bandwidth: float | NotGiven = NOT_GIVEN,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        packet_threshold: float | NotGiven = NOT_GIVEN,
        prefixes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleEditResponse]:
        """
        Update a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          automatic_advertisement: Toggle on if you would like Cloudflare to automatically advertise the IP
              Prefixes within the rule via Magic Transit when the rule is triggered. Only
              available for users of Magic Transit.

          bandwidth: The number of bits per second for the rule. When this value is exceeded for the
              set duration, an alert notification is sent. Minimum of 1 and no maximum.

          duration: The amount of time that the rule threshold must be exceeded to send an alert
              notification. The final value must be equivalent to one of the following 8
              values ["1m","5m","10m","15m","20m","30m","45m","60m"]. The format is
              AhBmCsDmsEusFns where A, B, C, D, E and F durations are optional; however at
              least one unit must be provided.

          name: The name of the rule. Must be unique. Supports characters A-Z, a-z, 0-9,
              underscore (\\__), dash (-), period (.), and tilde (~). You can’t have a space in
              the rule name. Max 256 characters.

          packet_threshold: The number of packets per second for the rule. When this value is exceeded for
              the set duration, an alert notification is sent. Minimum of 1 and no maximum.

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
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "automatic_advertisement": automatic_advertisement,
                    "bandwidth": bandwidth,
                    "duration": duration,
                    "name": name,
                    "packet_threshold": packet_threshold,
                    "prefixes": prefixes,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleEditResponse]], ResultWrapper[RuleEditResponse]),
        )

    async def get(
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
    ) -> Optional[RuleGetResponse]:
        """
        List a single network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsResourceWithRawResponse:
        return AdvertisementsResourceWithRawResponse(self._rules.advertisements)


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResourceWithRawResponse:
        return AsyncAdvertisementsResourceWithRawResponse(self._rules.advertisements)


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsResourceWithStreamingResponse:
        return AdvertisementsResourceWithStreamingResponse(self._rules.advertisements)


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResourceWithStreamingResponse:
        return AsyncAdvertisementsResourceWithStreamingResponse(self._rules.advertisements)
