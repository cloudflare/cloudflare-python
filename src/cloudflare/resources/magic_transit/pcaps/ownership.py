# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.magic_transit.pcaps import ownership_create_params, ownership_validate_params
from ....types.magic_transit.pcaps.ownership_get_response import OwnershipGetResponse
from ....types.magic_transit.pcaps.ownership_create_response import OwnershipCreateResponse
from ....types.magic_transit.pcaps.ownership_validate_response import OwnershipValidateResponse

__all__ = ["OwnershipResource", "AsyncOwnershipResource"]


class OwnershipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OwnershipResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipCreateResponse:
        """
        Adds an AWS or GCP bucket to use with full packet captures.

        Args:
          account_id: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pcaps/ownership",
            body=maybe_transform({"destination_conf": destination_conf}, ownership_create_params.OwnershipCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OwnershipCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OwnershipCreateResponse], ResultWrapper[OwnershipCreateResponse]),
        )

    def delete(
        self,
        ownership_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes buckets added to the packet captures API.

        Args:
          account_id: Identifier

          ownership_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ownership_id:
            raise ValueError(f"Expected a non-empty value for `ownership_id` but received {ownership_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/pcaps/ownership/{ownership_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> Optional[OwnershipGetResponse]:
        """
        List all buckets configured for use with PCAPs API.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/pcaps/ownership",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OwnershipGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipGetResponse]], ResultWrapper[OwnershipGetResponse]),
        )

    def validate(
        self,
        *,
        account_id: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipValidateResponse:
        """
        Validates buckets added to the packet captures API.

        Args:
          account_id: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          ownership_challenge: The ownership challenge filename stored in the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pcaps/ownership/validate",
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
                post_parser=ResultWrapper[OwnershipValidateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OwnershipValidateResponse], ResultWrapper[OwnershipValidateResponse]),
        )


class AsyncOwnershipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOwnershipResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        destination_conf: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipCreateResponse:
        """
        Adds an AWS or GCP bucket to use with full packet captures.

        Args:
          account_id: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pcaps/ownership",
            body=await async_maybe_transform(
                {"destination_conf": destination_conf}, ownership_create_params.OwnershipCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OwnershipCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OwnershipCreateResponse], ResultWrapper[OwnershipCreateResponse]),
        )

    async def delete(
        self,
        ownership_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes buckets added to the packet captures API.

        Args:
          account_id: Identifier

          ownership_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ownership_id:
            raise ValueError(f"Expected a non-empty value for `ownership_id` but received {ownership_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/pcaps/ownership/{ownership_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> Optional[OwnershipGetResponse]:
        """
        List all buckets configured for use with PCAPs API.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pcaps/ownership",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OwnershipGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipGetResponse]], ResultWrapper[OwnershipGetResponse]),
        )

    async def validate(
        self,
        *,
        account_id: str,
        destination_conf: str,
        ownership_challenge: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OwnershipValidateResponse:
        """
        Validates buckets added to the packet captures API.

        Args:
          account_id: Identifier

          destination_conf: The full URI for the bucket. This field only applies to `full` packet captures.

          ownership_challenge: The ownership challenge filename stored in the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pcaps/ownership/validate",
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[OwnershipValidateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OwnershipValidateResponse], ResultWrapper[OwnershipValidateResponse]),
        )


class OwnershipResourceWithRawResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.create = to_raw_response_wrapper(
            ownership.create,
        )
        self.delete = to_raw_response_wrapper(
            ownership.delete,
        )
        self.get = to_raw_response_wrapper(
            ownership.get,
        )
        self.validate = to_raw_response_wrapper(
            ownership.validate,
        )


class AsyncOwnershipResourceWithRawResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.create = async_to_raw_response_wrapper(
            ownership.create,
        )
        self.delete = async_to_raw_response_wrapper(
            ownership.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ownership.get,
        )
        self.validate = async_to_raw_response_wrapper(
            ownership.validate,
        )


class OwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.create = to_streamed_response_wrapper(
            ownership.create,
        )
        self.delete = to_streamed_response_wrapper(
            ownership.delete,
        )
        self.get = to_streamed_response_wrapper(
            ownership.get,
        )
        self.validate = to_streamed_response_wrapper(
            ownership.validate,
        )


class AsyncOwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.create = async_to_streamed_response_wrapper(
            ownership.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            ownership.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ownership.get,
        )
        self.validate = async_to_streamed_response_wrapper(
            ownership.validate,
        )
