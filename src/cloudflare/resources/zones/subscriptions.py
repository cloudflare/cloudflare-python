# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.zones import subscription_edit_params, subscription_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.user.subscription import Subscription
from ...types.user.rate_plan_param import RatePlanParam
from ...types.user.subscription_zone_param import SubscriptionZoneParam
from ...types.zones.subscription_get_response import SubscriptionGetResponse
from ...types.zones.subscription_edit_response import SubscriptionEditResponse
from ...types.user.subscription_component_param import SubscriptionComponentParam
from ...types.zones.subscription_create_response import SubscriptionCreateResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        app: subscription_create_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[SubscriptionComponentParam] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
        zone: SubscriptionZoneParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionCreateResponse:
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
            SubscriptionCreateResponse,
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
                    subscription_create_params.SubscriptionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> SyncSinglePage[Subscription]:
        """
        Lists all of an account's subscriptions.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/subscriptions",
            page=SyncSinglePage[Subscription],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Subscription,
        )

    def edit(
        self,
        identifier: str,
        *,
        app: subscription_edit_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[SubscriptionComponentParam] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
        zone: SubscriptionZoneParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionEditResponse:
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
            SubscriptionEditResponse,
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
                    subscription_edit_params.SubscriptionEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionGetResponse:
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
            SubscriptionGetResponse,
            self._get(
                f"/zones/{identifier}/subscription",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        identifier: str,
        *,
        app: subscription_create_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[SubscriptionComponentParam] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
        zone: SubscriptionZoneParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionCreateResponse:
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
            SubscriptionCreateResponse,
            await self._post(
                f"/zones/{identifier}/subscription",
                body=await async_maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_create_params.SubscriptionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AsyncPaginator[Subscription, AsyncSinglePage[Subscription]]:
        """
        Lists all of an account's subscriptions.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/subscriptions",
            page=AsyncSinglePage[Subscription],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Subscription,
        )

    async def edit(
        self,
        identifier: str,
        *,
        app: subscription_edit_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[SubscriptionComponentParam] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
        zone: SubscriptionZoneParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionEditResponse:
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
            SubscriptionEditResponse,
            await self._put(
                f"/zones/{identifier}/subscription",
                body=await async_maybe_transform(
                    {
                        "app": app,
                        "component_values": component_values,
                        "frequency": frequency,
                        "rate_plan": rate_plan,
                        "zone": zone,
                    },
                    subscription_edit_params.SubscriptionEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionGetResponse:
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
            SubscriptionGetResponse,
            await self._get(
                f"/zones/{identifier}/subscription",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SubscriptionGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.edit = to_raw_response_wrapper(
            subscriptions.edit,
        )
        self.get = to_raw_response_wrapper(
            subscriptions.get,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.edit = async_to_raw_response_wrapper(
            subscriptions.edit,
        )
        self.get = async_to_raw_response_wrapper(
            subscriptions.get,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.edit = to_streamed_response_wrapper(
            subscriptions.edit,
        )
        self.get = to_streamed_response_wrapper(
            subscriptions.get,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            subscriptions.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            subscriptions.get,
        )
