# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.logpush.validates.destinations import (
    ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse,
    exist_delete_accounts_account_identifier_logpush_validate_destination_exists_params,
)

__all__ = ["Exists", "AsyncExists"]


class Exists(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExistsWithRawResponse:
        return ExistsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExistsWithStreamingResponse:
        return ExistsWithStreamingResponse(self)

    def delete_accounts_account_identifier_logpush_validate_destination_exists(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse]:
        """
        Checks if there is an existing job with a destination.

        Args:
          account_or_zone_id: Identifier

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/validate/destination/exists",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                exist_delete_accounts_account_identifier_logpush_validate_destination_exists_params.ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse]],
                ResultWrapper[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            ),
        )


class AsyncExists(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExistsWithRawResponse:
        return AsyncExistsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExistsWithStreamingResponse:
        return AsyncExistsWithStreamingResponse(self)

    async def delete_accounts_account_identifier_logpush_validate_destination_exists(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse]:
        """
        Checks if there is an existing job with a destination.

        Args:
          account_or_zone_id: Identifier

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/validate/destination/exists",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                exist_delete_accounts_account_identifier_logpush_validate_destination_exists_params.ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse]],
                ResultWrapper[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            ),
        )


class ExistsWithRawResponse:
    def __init__(self, exists: Exists) -> None:
        self._exists = exists

        self.delete_accounts_account_identifier_logpush_validate_destination_exists = to_raw_response_wrapper(
            exists.delete_accounts_account_identifier_logpush_validate_destination_exists,
        )


class AsyncExistsWithRawResponse:
    def __init__(self, exists: AsyncExists) -> None:
        self._exists = exists

        self.delete_accounts_account_identifier_logpush_validate_destination_exists = async_to_raw_response_wrapper(
            exists.delete_accounts_account_identifier_logpush_validate_destination_exists,
        )


class ExistsWithStreamingResponse:
    def __init__(self, exists: Exists) -> None:
        self._exists = exists

        self.delete_accounts_account_identifier_logpush_validate_destination_exists = to_streamed_response_wrapper(
            exists.delete_accounts_account_identifier_logpush_validate_destination_exists,
        )


class AsyncExistsWithStreamingResponse:
    def __init__(self, exists: AsyncExists) -> None:
        self._exists = exists

        self.delete_accounts_account_identifier_logpush_validate_destination_exists = (
            async_to_streamed_response_wrapper(
                exists.delete_accounts_account_identifier_logpush_validate_destination_exists,
            )
        )
