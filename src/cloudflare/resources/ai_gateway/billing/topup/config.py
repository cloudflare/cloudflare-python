# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import overload

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.ai_gateway.billing.topup import config_create_params
from .....types.ai_gateway.billing.topup.config_get_response import ConfigGetResponse
from .....types.ai_gateway.billing.topup.config_create_response import ConfigCreateResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        threshold: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Configure auto top-up with a balance threshold and top-up amount.

        Requests that
        add a payment method first return authentication details. The configuration is
        saved only after the authenticated setup is submitted. Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          amount: Auto top-up amount in cents (min 1000).

          threshold: Balance threshold in cents that triggers auto top-up (min 500).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        consent_version: str,
        payment_method_id: str,
        setup_idempotency_key: str,
        threshold: int,
        setup_intent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Configure auto top-up with a balance threshold and top-up amount.

        Requests that
        add a payment method first return authentication details. The configuration is
        saved only after the authenticated setup is submitted. Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          amount: Auto top-up amount in cents (min 1000).

          consent_version: Version of the off-session auto-top-up consent accepted by the user.

          payment_method_id: Card to authenticate for future automatic top-ups.

          setup_idempotency_key: Client-generated UUID that makes payment-method setup safe to retry.

          threshold: Balance threshold in cents that triggers auto top-up (min 500).

          setup_intent_id: Successfully confirmed payment-method setup identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "amount", "threshold"],
        ["account_id", "amount", "consent_version", "payment_method_id", "setup_idempotency_key", "threshold"],
    )
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        threshold: int,
        consent_version: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        setup_idempotency_key: str | Omit = omit,
        setup_intent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ConfigCreateResponse,
            self._post(
                path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
                body=maybe_transform(
                    {
                        "amount": amount,
                        "threshold": threshold,
                        "consent_version": consent_version,
                        "payment_method_id": payment_method_id,
                        "setup_idempotency_key": setup_idempotency_key,
                        "setup_intent_id": setup_intent_id,
                    },
                    config_create_params.ConfigCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ConfigCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigCreateResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Remove the auto top-up configuration for the account.

        Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """
        Retrieve the current auto top-up threshold, amount, and any error state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        threshold: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Configure auto top-up with a balance threshold and top-up amount.

        Requests that
        add a payment method first return authentication details. The configuration is
        saved only after the authenticated setup is submitted. Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          amount: Auto top-up amount in cents (min 1000).

          threshold: Balance threshold in cents that triggers auto top-up (min 500).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        consent_version: str,
        payment_method_id: str,
        setup_idempotency_key: str,
        threshold: int,
        setup_intent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Configure auto top-up with a balance threshold and top-up amount.

        Requests that
        add a payment method first return authentication details. The configuration is
        saved only after the authenticated setup is submitted. Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          amount: Auto top-up amount in cents (min 1000).

          consent_version: Version of the off-session auto-top-up consent accepted by the user.

          payment_method_id: Card to authenticate for future automatic top-ups.

          setup_idempotency_key: Client-generated UUID that makes payment-method setup safe to retry.

          threshold: Balance threshold in cents that triggers auto top-up (min 500).

          setup_intent_id: Successfully confirmed payment-method setup identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "amount", "threshold"],
        ["account_id", "amount", "consent_version", "payment_method_id", "setup_idempotency_key", "threshold"],
    )
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        threshold: int,
        consent_version: str | Omit = omit,
        payment_method_id: str | Omit = omit,
        setup_idempotency_key: str | Omit = omit,
        setup_intent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            ConfigCreateResponse,
            await self._post(
                path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
                body=await async_maybe_transform(
                    {
                        "amount": amount,
                        "threshold": threshold,
                        "consent_version": consent_version,
                        "payment_method_id": payment_method_id,
                        "setup_idempotency_key": setup_idempotency_key,
                        "setup_intent_id": setup_intent_id,
                    },
                    config_create_params.ConfigCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[ConfigCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigCreateResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Remove the auto top-up configuration for the account.

        Dashboard sessions only:
        API token, OAuth, and service credentials are rejected with 403.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """
        Retrieve the current auto top-up threshold, amount, and any error state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/config", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_raw_response_wrapper(
            config.create,
        )
        self.delete = to_raw_response_wrapper(
            config.delete,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_raw_response_wrapper(
            config.create,
        )
        self.delete = async_to_raw_response_wrapper(
            config.delete,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_streamed_response_wrapper(
            config.create,
        )
        self.delete = to_streamed_response_wrapper(
            config.delete,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_streamed_response_wrapper(
            config.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            config.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
