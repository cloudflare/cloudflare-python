# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.logpush.ownerships import ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.logpush.ownerships import validate_post_accounts_account_identifier_logpush_ownership_validate_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Validates", "AsyncValidates"]


class Validates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self)

    def post_accounts_account_identifier_logpush_ownership_validate(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse]:
        """
        Validates ownership challenge of the destination.

        Args:
          account_or_zone_id: Identifier

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          ownership_challenge: Ownership challenge token to prove destination ownership.

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
            f"/{account_or_zone}/{account_or_zone_id}/logpush/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                validate_post_accounts_account_identifier_logpush_ownership_validate_params.ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse]],
                ResultWrapper[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse],
            ),
        )


class AsyncValidates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self)

    async def post_accounts_account_identifier_logpush_ownership_validate(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse]:
        """
        Validates ownership challenge of the destination.

        Args:
          account_or_zone_id: Identifier

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          ownership_challenge: Ownership challenge token to prove destination ownership.

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
            f"/{account_or_zone}/{account_or_zone_id}/logpush/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                validate_post_accounts_account_identifier_logpush_ownership_validate_params.ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse]],
                ResultWrapper[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse],
            ),
        )


class ValidatesWithRawResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.post_accounts_account_identifier_logpush_ownership_validate = to_raw_response_wrapper(
            validates.post_accounts_account_identifier_logpush_ownership_validate,
        )


class AsyncValidatesWithRawResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.post_accounts_account_identifier_logpush_ownership_validate = async_to_raw_response_wrapper(
            validates.post_accounts_account_identifier_logpush_ownership_validate,
        )


class ValidatesWithStreamingResponse:
    def __init__(self, validates: Validates) -> None:
        self._validates = validates

        self.post_accounts_account_identifier_logpush_ownership_validate = to_streamed_response_wrapper(
            validates.post_accounts_account_identifier_logpush_ownership_validate,
        )


class AsyncValidatesWithStreamingResponse:
    def __init__(self, validates: AsyncValidates) -> None:
        self._validates = validates

        self.post_accounts_account_identifier_logpush_ownership_validate = async_to_streamed_response_wrapper(
            validates.post_accounts_account_identifier_logpush_ownership_validate,
        )
