# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.zero_trust.dlp.entries import integration_create_params, integration_update_params
from .....types.zero_trust.dlp.entries.integration_create_response import IntegrationCreateResponse
from .....types.zero_trust.dlp.entries.integration_update_response import IntegrationUpdateResponse

__all__ = ["IntegrationResource", "AsyncIntegrationResource"]


class IntegrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IntegrationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        entry_id: str,
        profile_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationCreateResponse]:
        """
        Integration entries can't be created, this will update an existing integration
        entry This is needed for our generated terraform API

        Args:
          profile_id: This field is not actually used as the owning profile for a predefined entry is
              already set to a predefined profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/entries/integration",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "entry_id": entry_id,
                    "profile_id": profile_id,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IntegrationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationCreateResponse]], ResultWrapper[IntegrationCreateResponse]),
        )

    def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._put(
            f"/accounts/{account_id}/dlp/entries/integration/{entry_id}",
            body=maybe_transform({"enabled": enabled}, integration_update_params.IntegrationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IntegrationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        This is a no-op as integration entires can't be deleted but is needed for our
        generated terraform API

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return self._delete(
            f"/accounts/{account_id}/dlp/entries/integration/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncIntegrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIntegrationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        enabled: bool,
        entry_id: str,
        profile_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationCreateResponse]:
        """
        Integration entries can't be created, this will update an existing integration
        entry This is needed for our generated terraform API

        Args:
          profile_id: This field is not actually used as the owning profile for a predefined entry is
              already set to a predefined profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/entries/integration",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "entry_id": entry_id,
                    "profile_id": profile_id,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IntegrationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationCreateResponse]], ResultWrapper[IntegrationCreateResponse]),
        )

    async def update(
        self,
        entry_id: str,
        *,
        account_id: str,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationUpdateResponse]:
        """
        Updates a DLP entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._put(
            f"/accounts/{account_id}/dlp/entries/integration/{entry_id}",
            body=await async_maybe_transform({"enabled": enabled}, integration_update_params.IntegrationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IntegrationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    async def delete(
        self,
        entry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        This is a no-op as integration entires can't be deleted but is needed for our
        generated terraform API

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not entry_id:
            raise ValueError(f"Expected a non-empty value for `entry_id` but received {entry_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/dlp/entries/integration/{entry_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class IntegrationResourceWithRawResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.create = to_raw_response_wrapper(
            integration.create,
        )
        self.update = to_raw_response_wrapper(
            integration.update,
        )
        self.delete = to_raw_response_wrapper(
            integration.delete,
        )


class AsyncIntegrationResourceWithRawResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.create = async_to_raw_response_wrapper(
            integration.create,
        )
        self.update = async_to_raw_response_wrapper(
            integration.update,
        )
        self.delete = async_to_raw_response_wrapper(
            integration.delete,
        )


class IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: IntegrationResource) -> None:
        self._integration = integration

        self.create = to_streamed_response_wrapper(
            integration.create,
        )
        self.update = to_streamed_response_wrapper(
            integration.update,
        )
        self.delete = to_streamed_response_wrapper(
            integration.delete,
        )


class AsyncIntegrationResourceWithStreamingResponse:
    def __init__(self, integration: AsyncIntegrationResource) -> None:
        self._integration = integration

        self.create = async_to_streamed_response_wrapper(
            integration.create,
        )
        self.update = async_to_streamed_response_wrapper(
            integration.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            integration.delete,
        )
