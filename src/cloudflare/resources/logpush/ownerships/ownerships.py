# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .validates import Validates, AsyncValidates

from ...._compat import cached_property

from ....types.logpush import OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse

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
from ....types.logpush import ownership_post_accounts_account_identifier_logpush_ownership_params
from .validates import (
    Validates,
    AsyncValidates,
    ValidatesWithRawResponse,
    AsyncValidatesWithRawResponse,
    ValidatesWithStreamingResponse,
    AsyncValidatesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Ownerships", "AsyncOwnerships"]


class Ownerships(SyncAPIResource):
    @cached_property
    def validates(self) -> Validates:
        return Validates(self._client)

    @cached_property
    def with_raw_response(self) -> OwnershipsWithRawResponse:
        return OwnershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipsWithStreamingResponse:
        return OwnershipsWithStreamingResponse(self)

    def post_accounts_account_identifier_logpush_ownership(
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
    ) -> Optional[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse]:
        """
        Gets a new ownership challenge sent to your destination.

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
            f"/{account_or_zone}/{account_or_zone_id}/logpush/ownership",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                ownership_post_accounts_account_identifier_logpush_ownership_params.OwnershipPostAccountsAccountIdentifierLogpushOwnershipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse]],
                ResultWrapper[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse],
            ),
        )


class AsyncOwnerships(AsyncAPIResource):
    @cached_property
    def validates(self) -> AsyncValidates:
        return AsyncValidates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOwnershipsWithRawResponse:
        return AsyncOwnershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipsWithStreamingResponse:
        return AsyncOwnershipsWithStreamingResponse(self)

    async def post_accounts_account_identifier_logpush_ownership(
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
    ) -> Optional[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse]:
        """
        Gets a new ownership challenge sent to your destination.

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
            f"/{account_or_zone}/{account_or_zone_id}/logpush/ownership",
            body=maybe_transform(
                {"destination_conf": destination_conf},
                ownership_post_accounts_account_identifier_logpush_ownership_params.OwnershipPostAccountsAccountIdentifierLogpushOwnershipParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse]],
                ResultWrapper[OwnershipPostAccountsAccountIdentifierLogpushOwnershipResponse],
            ),
        )


class OwnershipsWithRawResponse:
    def __init__(self, ownerships: Ownerships) -> None:
        self._ownerships = ownerships

        self.post_accounts_account_identifier_logpush_ownership = to_raw_response_wrapper(
            ownerships.post_accounts_account_identifier_logpush_ownership,
        )

    @cached_property
    def validates(self) -> ValidatesWithRawResponse:
        return ValidatesWithRawResponse(self._ownerships.validates)


class AsyncOwnershipsWithRawResponse:
    def __init__(self, ownerships: AsyncOwnerships) -> None:
        self._ownerships = ownerships

        self.post_accounts_account_identifier_logpush_ownership = async_to_raw_response_wrapper(
            ownerships.post_accounts_account_identifier_logpush_ownership,
        )

    @cached_property
    def validates(self) -> AsyncValidatesWithRawResponse:
        return AsyncValidatesWithRawResponse(self._ownerships.validates)


class OwnershipsWithStreamingResponse:
    def __init__(self, ownerships: Ownerships) -> None:
        self._ownerships = ownerships

        self.post_accounts_account_identifier_logpush_ownership = to_streamed_response_wrapper(
            ownerships.post_accounts_account_identifier_logpush_ownership,
        )

    @cached_property
    def validates(self) -> ValidatesWithStreamingResponse:
        return ValidatesWithStreamingResponse(self._ownerships.validates)


class AsyncOwnershipsWithStreamingResponse:
    def __init__(self, ownerships: AsyncOwnerships) -> None:
        self._ownerships = ownerships

        self.post_accounts_account_identifier_logpush_ownership = async_to_streamed_response_wrapper(
            ownerships.post_accounts_account_identifier_logpush_ownership,
        )

    @cached_property
    def validates(self) -> AsyncValidatesWithStreamingResponse:
        return AsyncValidatesWithStreamingResponse(self._ownerships.validates)
