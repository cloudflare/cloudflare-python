# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    SubscriptionGetResponse,
    SubscriptionListResponse,
    SubscriptionCreateResponse,
    SubscriptionDeleteResponse,
    SubscriptionUpdateResponse,
    subscription_create_params,
    subscription_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self)

    def create(
        self,
        identifier: str,
        *,
        app: subscription_create_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_create_params.ComponentValue] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_create_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_create_params.Zone | NotGiven = NOT_GIVEN,
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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

    def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionListResponse]:
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
            cast_to=cast(Type[Optional[SubscriptionListResponse]], ResultWrapper[SubscriptionListResponse]),
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionGetResponse]
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

    async def create(
        self,
        identifier: str,
        *,
        app: subscription_create_params.App | NotGiven = NOT_GIVEN,
        component_values: Iterable[subscription_create_params.ComponentValue] | NotGiven = NOT_GIVEN,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: subscription_create_params.RatePlan | NotGiven = NOT_GIVEN,
        zone: subscription_create_params.Zone | NotGiven = NOT_GIVEN,
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionListResponse]:
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
            cast_to=cast(Type[Optional[SubscriptionListResponse]], ResultWrapper[SubscriptionListResponse]),
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SubscriptionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.get = to_raw_response_wrapper(
            subscriptions.get,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subscriptions.get,
        )


class SubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.get = to_streamed_response_wrapper(
            subscriptions.get,
        )


class AsyncSubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscriptions.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subscriptions.get,
        )
