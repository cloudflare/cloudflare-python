# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionAccountSubscriptionsCreateSubscriptionResponse,
    SubscriptionAccountSubscriptionsListSubscriptionsResponse,
    SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse,
    subscription_update_params,
    subscription_account_subscriptions_create_subscription_params,
    subscription_zone_subscription_create_zone_subscription_params,
    subscription_zone_subscription_update_zone_subscription_params,
)

from typing import Iterable, Type, Optional

from typing_extensions import Literal

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import subscription_update_params
from ..types import subscription_account_subscriptions_create_subscription_params
from ..types import subscription_zone_subscription_create_zone_subscription_params
from ..types import subscription_zone_subscription_update_zone_subscription_params
from .._wrappers import ResultWrapper
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

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self)

    def update(
        self,
        subscription_identifier: str,
        *,
        account_identifier: str,
        app: subscription_update_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_update_params.ComponentValue] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_update_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_update_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionUpdateResponse:
        """
        Updates an account subscription.

        Args:
          account_identifier: Identifier

          subscription_identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return cast(
            SubscriptionUpdateResponse,
            self._put(
                f"/accounts/{account_identifier}/subscriptions/{subscription_identifier}",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_update_params.SubscriptionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        subscription_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDeleteResponse:
        """
        Deletes an account's subscription.

        Args:
          account_identifier: Identifier

          subscription_identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return self._delete(
            f"/accounts/{account_identifier}/subscriptions/{subscription_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubscriptionDeleteResponse], ResultWrapper[SubscriptionDeleteResponse]),
        )

    def account_subscriptions_create_subscription(
        self,
        account_identifier: str,
        *,
        app: subscription_account_subscriptions_create_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_account_subscriptions_create_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_account_subscriptions_create_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_account_subscriptions_create_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionAccountSubscriptionsCreateSubscriptionResponse:
        """
        Creates an account subscription.

        Args:
          account_identifier: Identifier

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            SubscriptionAccountSubscriptionsCreateSubscriptionResponse,
            self._post(
                f"/accounts/{account_identifier}/subscriptions",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_account_subscriptions_create_subscription_params.SubscriptionAccountSubscriptionsCreateSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionAccountSubscriptionsCreateSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def account_subscriptions_list_subscriptions(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse]:
        """
        Lists all of an account's subscriptions.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse]],
                ResultWrapper[SubscriptionAccountSubscriptionsListSubscriptionsResponse],
            ),
        )

    def zone_subscription_create_zone_subscription(
        self,
        identifier: str,
        *,
        app: subscription_zone_subscription_create_zone_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_zone_subscription_create_zone_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_zone_subscription_create_zone_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_zone_subscription_create_zone_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse:
        """
        Create a zone subscription, either plan or add-ons.

        Args:
          identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse,
            self._post(
                f"/zones/{identifier}/subscription",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_zone_subscription_create_zone_subscription_params.SubscriptionZoneSubscriptionCreateZoneSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def zone_subscription_update_zone_subscription(
        self,
        identifier: str,
        *,
        app: subscription_zone_subscription_update_zone_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_zone_subscription_update_zone_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_zone_subscription_update_zone_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_zone_subscription_update_zone_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse:
        """
        Updates zone subscriptions, either plan or add-ons.

        Args:
          identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse,
            self._put(
                f"/zones/{identifier}/subscription",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_zone_subscription_update_zone_subscription_params.SubscriptionZoneSubscriptionUpdateZoneSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def zone_subscription_zone_subscription_details(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse:
        """
        Lists zone subscription details.

        Args:
          identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse,
            self._get(
                f"/zones/{identifier}/subscription",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSubscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self)

    async def update(
        self,
        subscription_identifier: str,
        *,
        account_identifier: str,
        app: subscription_update_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_update_params.ComponentValue] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_update_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_update_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionUpdateResponse:
        """
        Updates an account subscription.

        Args:
          account_identifier: Identifier

          subscription_identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return cast(
            SubscriptionUpdateResponse,
            await self._put(
                f"/accounts/{account_identifier}/subscriptions/{subscription_identifier}",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_update_params.SubscriptionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        subscription_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDeleteResponse:
        """
        Deletes an account's subscription.

        Args:
          account_identifier: Identifier

          subscription_identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return await self._delete(
            f"/accounts/{account_identifier}/subscriptions/{subscription_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SubscriptionDeleteResponse], ResultWrapper[SubscriptionDeleteResponse]),
        )

    async def account_subscriptions_create_subscription(
        self,
        account_identifier: str,
        *,
        app: subscription_account_subscriptions_create_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_account_subscriptions_create_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_account_subscriptions_create_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_account_subscriptions_create_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionAccountSubscriptionsCreateSubscriptionResponse:
        """
        Creates an account subscription.

        Args:
          account_identifier: Identifier

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            SubscriptionAccountSubscriptionsCreateSubscriptionResponse,
            await self._post(
                f"/accounts/{account_identifier}/subscriptions",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_account_subscriptions_create_subscription_params.SubscriptionAccountSubscriptionsCreateSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionAccountSubscriptionsCreateSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def account_subscriptions_list_subscriptions(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse]:
        """
        Lists all of an account's subscriptions.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse]],
                ResultWrapper[SubscriptionAccountSubscriptionsListSubscriptionsResponse],
            ),
        )

    async def zone_subscription_create_zone_subscription(
        self,
        identifier: str,
        *,
        app: subscription_zone_subscription_create_zone_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_zone_subscription_create_zone_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_zone_subscription_create_zone_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_zone_subscription_create_zone_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse:
        """
        Create a zone subscription, either plan or add-ons.

        Args:
          identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse,
            await self._post(
                f"/zones/{identifier}/subscription",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_zone_subscription_create_zone_subscription_params.SubscriptionZoneSubscriptionCreateZoneSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def zone_subscription_update_zone_subscription(
        self,
        identifier: str,
        *,
        app: subscription_zone_subscription_update_zone_subscription_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_zone_subscription_update_zone_subscription_params.ComponentValue]
        | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_zone_subscription_update_zone_subscription_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_zone_subscription_update_zone_subscription_params.Zone | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse:
        """
        Updates zone subscriptions, either plan or add-ons.

        Args:
          identifier: Subscription identifier tag.

          component_values: The list of add-ons subscribed to.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          zone: A simple zone object. May have null properties if not a zone subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse,
            await self._put(
                f"/zones/{identifier}/subscription",
                body=maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_zone_subscription_update_zone_subscription_params.SubscriptionZoneSubscriptionUpdateZoneSubscriptionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def zone_subscription_zone_subscription_details(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse:
        """
        Lists zone subscription details.

        Args:
          identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse,
            await self._get(
                f"/zones/{identifier}/subscription",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.account_subscriptions_create_subscription = to_raw_response_wrapper(
            subscriptions.account_subscriptions_create_subscription,
        )
        self.account_subscriptions_list_subscriptions = to_raw_response_wrapper(
            subscriptions.account_subscriptions_list_subscriptions,
        )
        self.zone_subscription_create_zone_subscription = to_raw_response_wrapper(
            subscriptions.zone_subscription_create_zone_subscription,
        )
        self.zone_subscription_update_zone_subscription = to_raw_response_wrapper(
            subscriptions.zone_subscription_update_zone_subscription,
        )
        self.zone_subscription_zone_subscription_details = to_raw_response_wrapper(
            subscriptions.zone_subscription_zone_subscription_details,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.account_subscriptions_create_subscription = async_to_raw_response_wrapper(
            subscriptions.account_subscriptions_create_subscription,
        )
        self.account_subscriptions_list_subscriptions = async_to_raw_response_wrapper(
            subscriptions.account_subscriptions_list_subscriptions,
        )
        self.zone_subscription_create_zone_subscription = async_to_raw_response_wrapper(
            subscriptions.zone_subscription_create_zone_subscription,
        )
        self.zone_subscription_update_zone_subscription = async_to_raw_response_wrapper(
            subscriptions.zone_subscription_update_zone_subscription,
        )
        self.zone_subscription_zone_subscription_details = async_to_raw_response_wrapper(
            subscriptions.zone_subscription_zone_subscription_details,
        )


class SubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.account_subscriptions_create_subscription = to_streamed_response_wrapper(
            subscriptions.account_subscriptions_create_subscription,
        )
        self.account_subscriptions_list_subscriptions = to_streamed_response_wrapper(
            subscriptions.account_subscriptions_list_subscriptions,
        )
        self.zone_subscription_create_zone_subscription = to_streamed_response_wrapper(
            subscriptions.zone_subscription_create_zone_subscription,
        )
        self.zone_subscription_update_zone_subscription = to_streamed_response_wrapper(
            subscriptions.zone_subscription_update_zone_subscription,
        )
        self.zone_subscription_zone_subscription_details = to_streamed_response_wrapper(
            subscriptions.zone_subscription_zone_subscription_details,
        )


class AsyncSubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.account_subscriptions_create_subscription = async_to_streamed_response_wrapper(
            subscriptions.account_subscriptions_create_subscription,
        )
        self.account_subscriptions_list_subscriptions = async_to_streamed_response_wrapper(
            subscriptions.account_subscriptions_list_subscriptions,
        )
        self.zone_subscription_create_zone_subscription = async_to_streamed_response_wrapper(
            subscriptions.zone_subscription_create_zone_subscription,
        )
        self.zone_subscription_update_zone_subscription = async_to_streamed_response_wrapper(
            subscriptions.zone_subscription_update_zone_subscription,
        )
        self.zone_subscription_zone_subscription_details = async_to_streamed_response_wrapper(
            subscriptions.zone_subscription_zone_subscription_details,
        )
