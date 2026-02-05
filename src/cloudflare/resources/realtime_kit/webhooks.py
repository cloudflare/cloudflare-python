# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.realtime_kit import (
    webhook_edit_webhook_params,
    webhook_create_webhook_params,
    webhook_replace_webhook_params,
)
from ...types.realtime_kit.webhook_edit_webhook_response import WebhookEditWebhookResponse
from ...types.realtime_kit.webhook_get_webhooks_response import WebhookGetWebhooksResponse
from ...types.realtime_kit.webhook_create_webhook_response import WebhookCreateWebhookResponse
from ...types.realtime_kit.webhook_delete_webhook_response import WebhookDeleteWebhookResponse
from ...types.realtime_kit.webhook_replace_webhook_response import WebhookReplaceWebhookResponse
from ...types.realtime_kit.webhook_get_webhook_by_id_response import WebhookGetWebhookByIDResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create_webhook(
        self,
        app_id: str,
        *,
        account_id: str,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ]
        ],
        name: str,
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateWebhookResponse:
        """
        Adds a new webhook to an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that this webhook will get triggered by

          name: Name of the webhook

          url: URL this webhook will send events to

          enabled: Set whether or not the webhook should be active when created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks",
            body=maybe_transform(
                {
                    "events": events,
                    "name": name,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_create_webhook_params.WebhookCreateWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateWebhookResponse,
        )

    def delete_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteWebhookResponse:
        """
        Removes a webhook for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteWebhookResponse,
        )

    def edit_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.chatSynced",
                "meeting.transcript",
                "meeting.summary",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEditWebhookResponse:
        """
        Edits the webhook details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that the webhook will get triggered by

          name: Name of the webhook

          url: URL the webhook will send events to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "events": events,
                    "name": name,
                    "url": url,
                },
                webhook_edit_webhook_params.WebhookEditWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEditWebhookResponse,
        )

    def get_webhook_by_id(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetWebhookByIDResponse:
        """
        Returns webhook details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetWebhookByIDResponse,
        )

    def get_webhooks(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetWebhooksResponse:
        """
        Returns details of all webhooks for an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetWebhooksResponse,
        )

    def replace_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ]
        ],
        name: str,
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookReplaceWebhookResponse:
        """
        Replace all details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that this webhook will get triggered by

          name: Name of the webhook

          url: URL this webhook will send events to

          enabled: Set whether or not the webhook should be active when created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            body=maybe_transform(
                {
                    "events": events,
                    "name": name,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_replace_webhook_params.WebhookReplaceWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReplaceWebhookResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create_webhook(
        self,
        app_id: str,
        *,
        account_id: str,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ]
        ],
        name: str,
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateWebhookResponse:
        """
        Adds a new webhook to an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that this webhook will get triggered by

          name: Name of the webhook

          url: URL this webhook will send events to

          enabled: Set whether or not the webhook should be active when created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks",
            body=await async_maybe_transform(
                {
                    "events": events,
                    "name": name,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_create_webhook_params.WebhookCreateWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateWebhookResponse,
        )

    async def delete_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteWebhookResponse:
        """
        Removes a webhook for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteWebhookResponse,
        )

    async def edit_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.chatSynced",
                "meeting.transcript",
                "meeting.summary",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEditWebhookResponse:
        """
        Edits the webhook details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that the webhook will get triggered by

          name: Name of the webhook

          url: URL the webhook will send events to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "events": events,
                    "name": name,
                    "url": url,
                },
                webhook_edit_webhook_params.WebhookEditWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEditWebhookResponse,
        )

    async def get_webhook_by_id(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetWebhookByIDResponse:
        """
        Returns webhook details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetWebhookByIDResponse,
        )

    async def get_webhooks(
        self,
        app_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookGetWebhooksResponse:
        """
        Returns details of all webhooks for an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookGetWebhooksResponse,
        )

    async def replace_webhook(
        self,
        webhook_id: str,
        *,
        account_id: str,
        app_id: str,
        events: List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ]
        ],
        name: str,
        url: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookReplaceWebhookResponse:
        """
        Replace all details for the given webhook ID.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          events: Events that this webhook will get triggered by

          name: Name of the webhook

          url: URL this webhook will send events to

          enabled: Set whether or not the webhook should be active when created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._put(
            f"/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}",
            body=await async_maybe_transform(
                {
                    "events": events,
                    "name": name,
                    "url": url,
                    "enabled": enabled,
                },
                webhook_replace_webhook_params.WebhookReplaceWebhookParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReplaceWebhookResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_webhook = to_raw_response_wrapper(
            webhooks.create_webhook,
        )
        self.delete_webhook = to_raw_response_wrapper(
            webhooks.delete_webhook,
        )
        self.edit_webhook = to_raw_response_wrapper(
            webhooks.edit_webhook,
        )
        self.get_webhook_by_id = to_raw_response_wrapper(
            webhooks.get_webhook_by_id,
        )
        self.get_webhooks = to_raw_response_wrapper(
            webhooks.get_webhooks,
        )
        self.replace_webhook = to_raw_response_wrapper(
            webhooks.replace_webhook,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_webhook = async_to_raw_response_wrapper(
            webhooks.create_webhook,
        )
        self.delete_webhook = async_to_raw_response_wrapper(
            webhooks.delete_webhook,
        )
        self.edit_webhook = async_to_raw_response_wrapper(
            webhooks.edit_webhook,
        )
        self.get_webhook_by_id = async_to_raw_response_wrapper(
            webhooks.get_webhook_by_id,
        )
        self.get_webhooks = async_to_raw_response_wrapper(
            webhooks.get_webhooks,
        )
        self.replace_webhook = async_to_raw_response_wrapper(
            webhooks.replace_webhook,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_webhook = to_streamed_response_wrapper(
            webhooks.create_webhook,
        )
        self.delete_webhook = to_streamed_response_wrapper(
            webhooks.delete_webhook,
        )
        self.edit_webhook = to_streamed_response_wrapper(
            webhooks.edit_webhook,
        )
        self.get_webhook_by_id = to_streamed_response_wrapper(
            webhooks.get_webhook_by_id,
        )
        self.get_webhooks = to_streamed_response_wrapper(
            webhooks.get_webhooks,
        )
        self.replace_webhook = to_streamed_response_wrapper(
            webhooks.replace_webhook,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create_webhook = async_to_streamed_response_wrapper(
            webhooks.create_webhook,
        )
        self.delete_webhook = async_to_streamed_response_wrapper(
            webhooks.delete_webhook,
        )
        self.edit_webhook = async_to_streamed_response_wrapper(
            webhooks.edit_webhook,
        )
        self.get_webhook_by_id = async_to_streamed_response_wrapper(
            webhooks.get_webhook_by_id,
        )
        self.get_webhooks = async_to_streamed_response_wrapper(
            webhooks.get_webhooks,
        )
        self.replace_webhook = async_to_streamed_response_wrapper(
            webhooks.replace_webhook,
        )
