# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.mtls_certificates import AssociationGetResponse

__all__ = ["Associations", "AsyncAssociations"]


class Associations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssociationsWithRawResponse:
        return AssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsWithStreamingResponse:
        return AssociationsWithStreamingResponse(self)

    def get(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssociationGetResponse]:
        """
        Lists all active associations between the certificate and Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssociationGetResponse]], ResultWrapper[AssociationGetResponse]),
        )


class AsyncAssociations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssociationsWithRawResponse:
        return AsyncAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsWithStreamingResponse:
        return AsyncAssociationsWithStreamingResponse(self)

    async def get(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssociationGetResponse]:
        """
        Lists all active associations between the certificate and Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssociationGetResponse]], ResultWrapper[AssociationGetResponse]),
        )


class AssociationsWithRawResponse:
    def __init__(self, associations: Associations) -> None:
        self._associations = associations

        self.get = to_raw_response_wrapper(
            associations.get,
        )


class AsyncAssociationsWithRawResponse:
    def __init__(self, associations: AsyncAssociations) -> None:
        self._associations = associations

        self.get = async_to_raw_response_wrapper(
            associations.get,
        )


class AssociationsWithStreamingResponse:
    def __init__(self, associations: Associations) -> None:
        self._associations = associations

        self.get = to_streamed_response_wrapper(
            associations.get,
        )


class AsyncAssociationsWithStreamingResponse:
    def __init__(self, associations: AsyncAssociations) -> None:
        self._associations = associations

        self.get = async_to_streamed_response_wrapper(
            associations.get,
        )
