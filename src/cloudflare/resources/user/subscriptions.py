# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
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
from ...types.user import subscription_edit_params, subscription_update_params
from ..._base_client import make_request_options
from ...types.user.rate_plan_param import RatePlanParam
from ...types.user.subscription_zone_param import SubscriptionZoneParam
from ...types.user.subscription_get_response import SubscriptionGetResponse
from ...types.user.subscription_edit_response import SubscriptionEditResponse
from ...types.user.subscription_component_param import SubscriptionComponentParam
from ...types.user.subscription_delete_response import SubscriptionDeleteResponse
from ...types.user.subscription_update_response import SubscriptionUpdateResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        app: subscription_update_params.App | NotGiven = NOT_GIVEN,
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
    ) -> SubscriptionUpdateResponse:
        """
        Updates a user's subscriptions.

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
            SubscriptionUpdateResponse,
            self._put(
                f"/user/subscriptions/{identifier}",
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
                    post_parser=ResultWrapper[SubscriptionUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDeleteResponse:
        """
        Deletes a user's subscription.

        Args:
          identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._delete(
            f"/user/subscriptions/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
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
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionGetResponse]:
        """Lists all of a user's subscriptions."""
        return self._get(
            "/user/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubscriptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubscriptionGetResponse]], ResultWrapper[SubscriptionGetResponse]),
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        app: subscription_update_params.App | NotGiven = NOT_GIVEN,
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
    ) -> SubscriptionUpdateResponse:
        """
        Updates a user's subscriptions.

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
            SubscriptionUpdateResponse,
            await self._put(
                f"/user/subscriptions/{identifier}",
                body=await async_maybe_transform(
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
                    post_parser=ResultWrapper[SubscriptionUpdateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionDeleteResponse:
        """
        Deletes a user's subscription.

        Args:
          identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._delete(
            f"/user/subscriptions/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
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
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionGetResponse]:
        """Lists all of a user's subscriptions."""
        return await self._get(
            "/user/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubscriptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubscriptionGetResponse]], ResultWrapper[SubscriptionGetResponse]),
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
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

        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
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

        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
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

        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            subscriptions.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            subscriptions.get,
        )
