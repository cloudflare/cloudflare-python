# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.alerting.v3s.destinations import (
    WebhookUpdateResponse,
    WebhookDeleteResponse,
    WebhookGetResponse,
    WebhookNotificationWebhooksCreateAWebhookResponse,
    WebhookNotificationWebhooksListWebhooksResponse,
)

from typing import Type, Optional

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.alerting.v3s.destinations import webhook_update_params
from .....types.alerting.v3s.destinations import webhook_notification_webhooks_create_a_webhook_params
from ....._wrappers import ResultWrapper
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
        webhook_id: str,
        *,
        account_id: str,
        name: str,
        url: str,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          name: The name of the webhook destination. This will be included in the request body
              when you receive a webhook notification.

          url: The POST endpoint to call when dispatching a notification.

          secret: Optional secret that will be passed in the `cf-webhook-auth` header when
              dispatching generic webhook notifications or formatted for supported
              destinations. Secrets are not returned in any API response body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._put(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "secret": secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WebhookUpdateResponse], ResultWrapper[WebhookUpdateResponse]),
        )

    def delete(
        self,
        webhook_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebhookDeleteResponse]:
        """
        Delete a configured webhook destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return cast(
            Optional[WebhookDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
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
        webhook_id: str,
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
        Get details for a single webhooks destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WebhookGetResponse], ResultWrapper[WebhookGetResponse]),
        )

    def notification_webhooks_create_a_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookNotificationWebhooksCreateAWebhookResponse:
        """
        Creates a new webhook destination.

        Args:
          account_id: The account id

          name: The name of the webhook destination. This will be included in the request body
              when you receive a webhook notification.

          url: The POST endpoint to call when dispatching a notification.

          secret: Optional secret that will be passed in the `cf-webhook-auth` header when
              dispatching generic webhook notifications or formatted for supported
              destinations. Secrets are not returned in any API response body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "secret": secret,
                },
                webhook_notification_webhooks_create_a_webhook_params.WebhookNotificationWebhooksCreateAWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WebhookNotificationWebhooksCreateAWebhookResponse],
                ResultWrapper[WebhookNotificationWebhooksCreateAWebhookResponse],
            ),
        )

    def notification_webhooks_list_webhooks(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebhookNotificationWebhooksListWebhooksResponse]:
        """
        Gets a list of all configured webhook destinations.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[WebhookNotificationWebhooksListWebhooksResponse]],
                ResultWrapper[WebhookNotificationWebhooksListWebhooksResponse],
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
        webhook_id: str,
        *,
        account_id: str,
        name: str,
        url: str,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookUpdateResponse:
        """
        Update a webhook destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          name: The name of the webhook destination. This will be included in the request body
              when you receive a webhook notification.

          url: The POST endpoint to call when dispatching a notification.

          secret: Optional secret that will be passed in the `cf-webhook-auth` header when
              dispatching generic webhook notifications or formatted for supported
              destinations. Secrets are not returned in any API response body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._put(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "secret": secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WebhookUpdateResponse], ResultWrapper[WebhookUpdateResponse]),
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebhookDeleteResponse]:
        """
        Delete a configured webhook destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return cast(
            Optional[WebhookDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
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
        webhook_id: str,
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
        Get details for a single webhooks destination.

        Args:
          account_id: The account id

          webhook_id: The unique identifier of a webhook

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WebhookGetResponse], ResultWrapper[WebhookGetResponse]),
        )

    async def notification_webhooks_create_a_webhook(
        self,
        account_id: str,
        *,
        name: str,
        url: str,
        secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookNotificationWebhooksCreateAWebhookResponse:
        """
        Creates a new webhook destination.

        Args:
          account_id: The account id

          name: The name of the webhook destination. This will be included in the request body
              when you receive a webhook notification.

          url: The POST endpoint to call when dispatching a notification.

          secret: Optional secret that will be passed in the `cf-webhook-auth` header when
              dispatching generic webhook notifications or formatted for supported
              destinations. Secrets are not returned in any API response body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "secret": secret,
                },
                webhook_notification_webhooks_create_a_webhook_params.WebhookNotificationWebhooksCreateAWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[WebhookNotificationWebhooksCreateAWebhookResponse],
                ResultWrapper[WebhookNotificationWebhooksCreateAWebhookResponse],
            ),
        )

    async def notification_webhooks_list_webhooks(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WebhookNotificationWebhooksListWebhooksResponse]:
        """
        Gets a list of all configured webhook destinations.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/webhooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[WebhookNotificationWebhooksListWebhooksResponse]],
                ResultWrapper[WebhookNotificationWebhooksListWebhooksResponse],
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
        self.notification_webhooks_create_a_webhook = to_raw_response_wrapper(
            webhooks.notification_webhooks_create_a_webhook,
        )
        self.notification_webhooks_list_webhooks = to_raw_response_wrapper(
            webhooks.notification_webhooks_list_webhooks,
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
        self.notification_webhooks_create_a_webhook = async_to_raw_response_wrapper(
            webhooks.notification_webhooks_create_a_webhook,
        )
        self.notification_webhooks_list_webhooks = async_to_raw_response_wrapper(
            webhooks.notification_webhooks_list_webhooks,
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
        self.notification_webhooks_create_a_webhook = to_streamed_response_wrapper(
            webhooks.notification_webhooks_create_a_webhook,
        )
        self.notification_webhooks_list_webhooks = to_streamed_response_wrapper(
            webhooks.notification_webhooks_list_webhooks,
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
        self.notification_webhooks_create_a_webhook = async_to_streamed_response_wrapper(
            webhooks.notification_webhooks_create_a_webhook,
        )
        self.notification_webhooks_list_webhooks = async_to_streamed_response_wrapper(
            webhooks.notification_webhooks_list_webhooks,
        )
