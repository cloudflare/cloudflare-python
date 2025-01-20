# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from .....types.zero_trust.dlp.email import account_mapping_create_params
from .....types.zero_trust.dlp.email.account_mapping_get_response import AccountMappingGetResponse
from .....types.zero_trust.dlp.email.account_mapping_create_response import AccountMappingCreateResponse

__all__ = ["AccountMappingResource", "AsyncAccountMappingResource"]


class AccountMappingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountMappingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountMappingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountMappingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountMappingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        auth_requirements: account_mapping_create_params.AuthRequirements,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMappingCreateResponse]:
        """
        Create mapping

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dlp/email/account_mapping",
            body=maybe_transform(
                {"auth_requirements": auth_requirements}, account_mapping_create_params.AccountMappingCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountMappingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMappingCreateResponse]], ResultWrapper[AccountMappingCreateResponse]),
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
    ) -> Optional[AccountMappingGetResponse]:
        """
        Get mapping

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dlp/email/account_mapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountMappingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMappingGetResponse]], ResultWrapper[AccountMappingGetResponse]),
        )


class AsyncAccountMappingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountMappingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountMappingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountMappingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountMappingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        auth_requirements: account_mapping_create_params.AuthRequirements,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccountMappingCreateResponse]:
        """
        Create mapping

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dlp/email/account_mapping",
            body=await async_maybe_transform(
                {"auth_requirements": auth_requirements}, account_mapping_create_params.AccountMappingCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountMappingCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMappingCreateResponse]], ResultWrapper[AccountMappingCreateResponse]),
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
    ) -> Optional[AccountMappingGetResponse]:
        """
        Get mapping

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dlp/email/account_mapping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AccountMappingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccountMappingGetResponse]], ResultWrapper[AccountMappingGetResponse]),
        )


class AccountMappingResourceWithRawResponse:
    def __init__(self, account_mapping: AccountMappingResource) -> None:
        self._account_mapping = account_mapping

        self.create = to_raw_response_wrapper(
            account_mapping.create,
        )
        self.get = to_raw_response_wrapper(
            account_mapping.get,
        )


class AsyncAccountMappingResourceWithRawResponse:
    def __init__(self, account_mapping: AsyncAccountMappingResource) -> None:
        self._account_mapping = account_mapping

        self.create = async_to_raw_response_wrapper(
            account_mapping.create,
        )
        self.get = async_to_raw_response_wrapper(
            account_mapping.get,
        )


class AccountMappingResourceWithStreamingResponse:
    def __init__(self, account_mapping: AccountMappingResource) -> None:
        self._account_mapping = account_mapping

        self.create = to_streamed_response_wrapper(
            account_mapping.create,
        )
        self.get = to_streamed_response_wrapper(
            account_mapping.get,
        )


class AsyncAccountMappingResourceWithStreamingResponse:
    def __init__(self, account_mapping: AsyncAccountMappingResource) -> None:
        self._account_mapping = account_mapping

        self.create = async_to_streamed_response_wrapper(
            account_mapping.create,
        )
        self.get = async_to_streamed_response_wrapper(
            account_mapping.get,
        )
