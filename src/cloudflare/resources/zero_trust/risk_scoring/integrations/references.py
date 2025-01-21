# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.zero_trust.risk_scoring.integrations.reference_get_response import ReferenceGetResponse

__all__ = ["ReferencesResource", "AsyncReferencesResource"]


class ReferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReferencesResourceWithStreamingResponse(self)

    def get(
        self,
        reference_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceGetResponse]:
        """
        Get risk score integration by reference id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not reference_id:
            raise ValueError(f"Expected a non-empty value for `reference_id` but received {reference_id!r}")
        return self._get(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReferenceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReferenceGetResponse]], ResultWrapper[ReferenceGetResponse]),
        )


class AsyncReferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReferencesResourceWithStreamingResponse(self)

    async def get(
        self,
        reference_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceGetResponse]:
        """
        Get risk score integration by reference id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not reference_id:
            raise ValueError(f"Expected a non-empty value for `reference_id` but received {reference_id!r}")
        return await self._get(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ReferenceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReferenceGetResponse]], ResultWrapper[ReferenceGetResponse]),
        )


class ReferencesResourceWithRawResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.get = to_raw_response_wrapper(
            references.get,
        )


class AsyncReferencesResourceWithRawResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.get = async_to_raw_response_wrapper(
            references.get,
        )


class ReferencesResourceWithStreamingResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.get = to_streamed_response_wrapper(
            references.get,
        )


class AsyncReferencesResourceWithStreamingResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.get = async_to_streamed_response_wrapper(
            references.get,
        )
