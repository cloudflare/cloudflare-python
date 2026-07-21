# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.casb.posture import webhook_create_params, webhook_update_params, webhook_evaluate_params
from ......types.zero_trust.casb.posture.webhook_get_response import WebhookGetResponse
from ......types.zero_trust.casb.posture.webhook_list_response import WebhookListResponse
from ......types.zero_trust.casb.posture.webhook_create_response import WebhookCreateResponse
from ......types.zero_trust.casb.posture.webhook_delete_response import WebhookDeleteResponse
from ......types.zero_trust.casb.posture.webhook_update_response import WebhookUpdateResponse
from ......types.zero_trust.casb.posture.webhook_evaluate_response import WebhookEvaluateResponse
from ......types.zero_trust.casb.posture.webhook_evaluate_existing_response import WebhookEvaluateExistingResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

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

    def create(
        self,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        label: str,
        headers: Iterable[webhook_create_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookCreateResponse]:
        """
        Creates a new webhook configuration for sending finding notifications to
        external endpoints.

        Args:
          authentication_type: Type of authentication used for the webhook.

          destination_url: Target URL for the webhook configuration. Where resulting data will be sent.

          label: Account-specified display label for the webhook configuration.

          headers: List of custom headers to include in webhook requests.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/webhooks", account_id=account_id),
            body=maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "label": label,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookCreateResponse]], ResultWrapper[WebhookCreateResponse]),
        )

    def update(
        self,
        webhook_id: str,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        label: str,
        status: Literal["enabled", "disabled"],
        headers: Iterable[webhook_update_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookUpdateResponse]:
        """
        Updates an existing webhook configuration with new settings.

        Args:
          authentication_type: Type of authentication used for the webhook.

          destination_url: Target URL for the webhook configuration. Where resulting data will be sent.

          label: Account-specified display label for the webhook configuration.

          status: Status of the webhook configuration.

          headers: List of custom headers to include in webhook requests.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

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
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            body=maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "label": label,
                    "status": status,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookUpdateResponse]], ResultWrapper[WebhookUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[WebhookListResponse]:
        """Retrieves all webhook configurations for the authenticated account.

        Returns an
        array of webhook configurations that can be used to send finding notifications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/webhooks", account_id=account_id),
            page=SyncSinglePage[WebhookListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WebhookListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Soft deletes a webhook configuration by its unique identifier.

        The webhook will
        be marked as deleted and will no longer be available for use.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def evaluate(
        self,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        headers: Iterable[webhook_evaluate_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookEvaluateResponse]:
        """
        Sends a test webhook event to the specified destination URL to verify the
        webhook endpoint is reachable and properly configured. This allows customers to
        validate their webhook configuration before creating the actual webhook
        resource.

        The test payload includes:

        - event_type: "webhook.test"
        - timestamp: Current UTC timestamp
        - message: Test message indicating this is from Cloudflare CASB
        - data: Object with test: true

        Args:
          authentication_type: Type of authentication to use for the test webhook request.

          destination_url: Target URL to send the test webhook event to.

          headers: List of custom headers to include in the test webhook request.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/webhooks/evaluate", account_id=account_id),
            body=maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_evaluate_params.WebhookEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookEvaluateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookEvaluateResponse]], ResultWrapper[WebhookEvaluateResponse]),
        )

    def evaluate_existing(
        self,
        webhook_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookEvaluateExistingResponse]:
        """Sends a test webhook event using an existing webhook configuration.

        This allows
        customers to verify their webhook endpoint is still reachable and properly
        configured after creating the webhook resource.

        The test payload includes:

        - event_type: "webhook.test"
        - timestamp: Current UTC timestamp
        - message: Test message indicating this is from Cloudflare CASB
        - data: Object with test: true

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}/evaluate",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookEvaluateExistingResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[WebhookEvaluateExistingResponse]], ResultWrapper[WebhookEvaluateExistingResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookGetResponse]:
        """
        Retrieves a specific webhook configuration by its unique identifier.

        Args:
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
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookGetResponse]], ResultWrapper[WebhookGetResponse]),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

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

    async def create(
        self,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        label: str,
        headers: Iterable[webhook_create_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookCreateResponse]:
        """
        Creates a new webhook configuration for sending finding notifications to
        external endpoints.

        Args:
          authentication_type: Type of authentication used for the webhook.

          destination_url: Target URL for the webhook configuration. Where resulting data will be sent.

          label: Account-specified display label for the webhook configuration.

          headers: List of custom headers to include in webhook requests.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/webhooks", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "label": label,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookCreateResponse]], ResultWrapper[WebhookCreateResponse]),
        )

    async def update(
        self,
        webhook_id: str,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        label: str,
        status: Literal["enabled", "disabled"],
        headers: Iterable[webhook_update_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookUpdateResponse]:
        """
        Updates an existing webhook configuration with new settings.

        Args:
          authentication_type: Type of authentication used for the webhook.

          destination_url: Target URL for the webhook configuration. Where resulting data will be sent.

          label: Account-specified display label for the webhook configuration.

          status: Status of the webhook configuration.

          headers: List of custom headers to include in webhook requests.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

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
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            body=await async_maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "label": label,
                    "status": status,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookUpdateResponse]], ResultWrapper[WebhookUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookListResponse, AsyncSinglePage[WebhookListResponse]]:
        """Retrieves all webhook configurations for the authenticated account.

        Returns an
        array of webhook configurations that can be used to send finding notifications.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/webhooks", account_id=account_id),
            page=AsyncSinglePage[WebhookListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WebhookListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Soft deletes a webhook configuration by its unique identifier.

        The webhook will
        be marked as deleted and will no longer be available for use.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    async def evaluate(
        self,
        *,
        account_id: str,
        authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"],
        destination_url: str,
        headers: Iterable[webhook_evaluate_params.Header] | Omit = omit,
        signing_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookEvaluateResponse]:
        """
        Sends a test webhook event to the specified destination URL to verify the
        webhook endpoint is reachable and properly configured. This allows customers to
        validate their webhook configuration before creating the actual webhook
        resource.

        The test payload includes:

        - event_type: "webhook.test"
        - timestamp: Current UTC timestamp
        - message: Test message indicating this is from Cloudflare CASB
        - data: Object with test: true

        Args:
          authentication_type: Type of authentication to use for the test webhook request.

          destination_url: Target URL to send the test webhook event to.

          headers: List of custom headers to include in the test webhook request.

          signing_secret: Secret key used for HMAC signing when authentication_type is "HMAC-Signing".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/webhooks/evaluate", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "authentication_type": authentication_type,
                    "destination_url": destination_url,
                    "headers": headers,
                    "signing_secret": signing_secret,
                },
                webhook_evaluate_params.WebhookEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookEvaluateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookEvaluateResponse]], ResultWrapper[WebhookEvaluateResponse]),
        )

    async def evaluate_existing(
        self,
        webhook_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookEvaluateExistingResponse]:
        """Sends a test webhook event using an existing webhook configuration.

        This allows
        customers to verify their webhook endpoint is still reachable and properly
        configured after creating the webhook resource.

        The test payload includes:

        - event_type: "webhook.test"
        - timestamp: Current UTC timestamp
        - message: Test message indicating this is from Cloudflare CASB
        - data: Object with test: true

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}/evaluate",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookEvaluateExistingResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[WebhookEvaluateExistingResponse]], ResultWrapper[WebhookEvaluateExistingResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[WebhookGetResponse]:
        """
        Retrieves a specific webhook configuration by its unique identifier.

        Args:
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
            path_template(
                "/accounts/{account_id}/data-security/posture/webhooks/{webhook_id}",
                account_id=account_id,
                webhook_id=webhook_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[WebhookGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[WebhookGetResponse]], ResultWrapper[WebhookGetResponse]),
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.evaluate = to_raw_response_wrapper(
            webhooks.evaluate,
        )
        self.evaluate_existing = to_raw_response_wrapper(
            webhooks.evaluate_existing,
        )
        self.get = to_raw_response_wrapper(
            webhooks.get,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._webhooks.jobs)


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.evaluate = async_to_raw_response_wrapper(
            webhooks.evaluate,
        )
        self.evaluate_existing = async_to_raw_response_wrapper(
            webhooks.evaluate_existing,
        )
        self.get = async_to_raw_response_wrapper(
            webhooks.get,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._webhooks.jobs)


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.evaluate = to_streamed_response_wrapper(
            webhooks.evaluate,
        )
        self.evaluate_existing = to_streamed_response_wrapper(
            webhooks.evaluate_existing,
        )
        self.get = to_streamed_response_wrapper(
            webhooks.get,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._webhooks.jobs)


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.evaluate = async_to_streamed_response_wrapper(
            webhooks.evaluate,
        )
        self.evaluate_existing = async_to_streamed_response_wrapper(
            webhooks.evaluate_existing,
        )
        self.get = async_to_streamed_response_wrapper(
            webhooks.get,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._webhooks.jobs)
