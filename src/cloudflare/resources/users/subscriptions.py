# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.users import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionUserSubscriptionGetUserSubscriptionsResponse,
    subscription_update_params,
)

from typing import Iterable, Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.users import subscription_update_params
from ..._wrappers import ResultWrapper
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
        identifier: str,
        *,
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
                    post_parser=ResultWrapper._unwrapper,
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

    def user_subscription_get_user_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse]:
        """Lists all of a user's subscriptions."""
        return self._get(
            "/user/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse]],
                ResultWrapper[SubscriptionUserSubscriptionGetUserSubscriptionsResponse],
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
        identifier: str,
        *,
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

    async def user_subscription_get_user_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse]:
        """Lists all of a user's subscriptions."""
        return await self._get(
            "/user/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse]],
                ResultWrapper[SubscriptionUserSubscriptionGetUserSubscriptionsResponse],
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
        self.user_subscription_get_user_subscriptions = to_raw_response_wrapper(
            subscriptions.user_subscription_get_user_subscriptions,
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
        self.user_subscription_get_user_subscriptions = async_to_raw_response_wrapper(
            subscriptions.user_subscription_get_user_subscriptions,
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
        self.user_subscription_get_user_subscriptions = to_streamed_response_wrapper(
            subscriptions.user_subscription_get_user_subscriptions,
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
        self.user_subscription_get_user_subscriptions = async_to_streamed_response_wrapper(
            subscriptions.user_subscription_get_user_subscriptions,
        )
