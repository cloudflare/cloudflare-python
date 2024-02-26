# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.logpush import (
    OwnershipCreateResponse,
    OwnershipValidateResponse,
    ownership_create_params,
    ownership_validate_params,
)

__all__ = ["Ownership", "AsyncOwnership"]


class Ownership(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OwnershipWithRawResponse:
        return OwnershipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipWithStreamingResponse:
        return OwnershipWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipCreateResponse]:
        """
        Gets a new ownership challenge sent to your destination.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/{account_id}/{zone_id}/logpush/ownership",
            body=maybe_transform({"destination_conf": destination_conf}, ownership_create_params.OwnershipCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipCreateResponse]], ResultWrapper[OwnershipCreateResponse]),
        )

    def validate(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipValidateResponse]:
        """
        Validates ownership challenge of the destination.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/{account_id}/{zone_id}/logpush/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                ownership_validate_params.OwnershipValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipValidateResponse]], ResultWrapper[OwnershipValidateResponse]),
        )


class AsyncOwnership(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOwnershipWithRawResponse:
        return AsyncOwnershipWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipWithStreamingResponse:
        return AsyncOwnershipWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipCreateResponse]:
        """
        Gets a new ownership challenge sent to your destination.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/{account_id}/{zone_id}/logpush/ownership",
            body=maybe_transform({"destination_conf": destination_conf}, ownership_create_params.OwnershipCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipCreateResponse]], ResultWrapper[OwnershipCreateResponse]),
        )

    async def validate(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipValidateResponse]:
        """
        Validates ownership challenge of the destination.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/{account_id}/{zone_id}/logpush/ownership/validate",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "ownership_challenge": ownership_challenge,
                },
                ownership_validate_params.OwnershipValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipValidateResponse]], ResultWrapper[OwnershipValidateResponse]),
        )


class OwnershipWithRawResponse:
    def __init__(self, ownership: Ownership) -> None:
        self._ownership = ownership

        self.create = to_raw_response_wrapper(
            ownership.create,
        )
        self.validate = to_raw_response_wrapper(
            ownership.validate,
        )


class AsyncOwnershipWithRawResponse:
    def __init__(self, ownership: AsyncOwnership) -> None:
        self._ownership = ownership

        self.create = async_to_raw_response_wrapper(
            ownership.create,
        )
        self.validate = async_to_raw_response_wrapper(
            ownership.validate,
        )


class OwnershipWithStreamingResponse:
    def __init__(self, ownership: Ownership) -> None:
        self._ownership = ownership

        self.create = to_streamed_response_wrapper(
            ownership.create,
        )
        self.validate = to_streamed_response_wrapper(
            ownership.validate,
        )


class AsyncOwnershipWithStreamingResponse:
    def __init__(self, ownership: AsyncOwnership) -> None:
        self._ownership = ownership

        self.create = async_to_streamed_response_wrapper(
            ownership.create,
        )
        self.validate = async_to_streamed_response_wrapper(
            ownership.validate,
        )
