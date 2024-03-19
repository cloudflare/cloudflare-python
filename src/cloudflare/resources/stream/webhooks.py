# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.stream import WebhookGetResponse, WebhookDeleteResponse, WebhookUpdateResponse, webhook_update_params

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksWithRawResponse:
        return WebhooksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksWithStreamingResponse:
        return WebhooksWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        notification_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Creates a webhook notification.

        Args:
          account_id: The account identifier tag.

          notification_url: The URL where webhooks will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookUpdateResponse,
            self._put(
                f"/accounts/{account_id}/stream/webhook",
                body=maybe_transform({"notification_url": notification_url}, webhook_update_params.WebhookUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeleteResponse:
        """
        Deletes a webhook.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/webhook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookGetResponse:
        """
        Retrieves a list of webhooks.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookGetResponse,
            self._get(
                f"/accounts/{account_id}/stream/webhook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncWebhooks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksWithRawResponse:
        return AsyncWebhooksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksWithStreamingResponse:
        return AsyncWebhooksWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        notification_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Creates a webhook notification.

        Args:
          account_id: The account identifier tag.

          notification_url: The URL where webhooks will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/stream/webhook",
                body=await async_maybe_transform(
                    {"notification_url": notification_url}, webhook_update_params.WebhookUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeleteResponse:
        """
        Deletes a webhook.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/webhook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookGetResponse:
        """
        Retrieves a list of webhooks.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            WebhookGetResponse,
            await self._get(
                f"/accounts/{account_id}/stream/webhook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[WebhookGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class WebhooksWithRawResponse:
    def __init__(self, webhooks: Webhooks) -> None:
        self._webhooks = webhooks

        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.get = to_raw_response_wrapper(
            webhooks.get,
        )


class AsyncWebhooksWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooks) -> None:
        self._webhooks = webhooks

        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            webhooks.get,
        )


class WebhooksWithStreamingResponse:
    def __init__(self, webhooks: Webhooks) -> None:
        self._webhooks = webhooks

        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.get = to_streamed_response_wrapper(
            webhooks.get,
        )


class AsyncWebhooksWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooks) -> None:
        self._webhooks = webhooks

        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            webhooks.get,
        )
