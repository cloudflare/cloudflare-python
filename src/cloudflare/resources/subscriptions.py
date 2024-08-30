# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal

import httpx

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
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.subscriptions import subscription_create_params, subscription_update_params
from ..types.user.subscription import Subscription
from ..types.user.rate_plan_param import RatePlanParam
from ..types.subscriptions.subscription_get_response import SubscriptionGetResponse
from ..types.subscriptions.subscription_create_response import SubscriptionCreateResponse
from ..types.subscriptions.subscription_delete_response import SubscriptionDeleteResponse
from ..types.subscriptions.subscription_update_response import SubscriptionUpdateResponse

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
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
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

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

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
                        "frequency": frequency,
                        "rate_plan": rate_plan,
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

    def update(
        self,
        subscription_identifier: str,
        *,
        account_id: str,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
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
          account_id: Identifier

          subscription_identifier: Subscription identifier tag.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return cast(
            SubscriptionUpdateResponse,
            self._put(
                f"/accounts/{account_id}/subscriptions/{subscription_identifier}",
                body=maybe_transform(
                    {
                        "frequency": frequency,
                        "rate_plan": rate_plan,
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

    def delete(
        self,
        subscription_identifier: str,
        *,
        account_id: str,
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
          account_id: Identifier

          subscription_identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return self._delete(
            f"/accounts/{account_id}/subscriptions/{subscription_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SubscriptionDeleteResponse]._unwrapper,
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
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
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

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

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
                        "frequency": frequency,
                        "rate_plan": rate_plan,
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

    async def update(
        self,
        subscription_identifier: str,
        *,
        account_id: str,
        frequency: Literal["weekly", "monthly", "quarterly", "yearly"] | NotGiven = NOT_GIVEN,
        rate_plan: RatePlanParam | NotGiven = NOT_GIVEN,
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
          account_id: Identifier

          subscription_identifier: Subscription identifier tag.

          frequency: How often the subscription is renewed automatically.

          rate_plan: The rate plan applied to the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return cast(
            SubscriptionUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/subscriptions/{subscription_identifier}",
                body=await async_maybe_transform(
                    {
                        "frequency": frequency,
                        "rate_plan": rate_plan,
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

    async def delete(
        self,
        subscription_identifier: str,
        *,
        account_id: str,
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
          account_id: Identifier

          subscription_identifier: Subscription identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not subscription_identifier:
            raise ValueError(
                f"Expected a non-empty value for `subscription_identifier` but received {subscription_identifier!r}"
            )
        return await self._delete(
            f"/accounts/{account_id}/subscriptions/{subscription_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SubscriptionDeleteResponse]._unwrapper,
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


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
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


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
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


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
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
