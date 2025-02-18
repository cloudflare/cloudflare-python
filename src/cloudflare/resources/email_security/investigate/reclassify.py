# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.email_security.investigate import reclassify_create_params

__all__ = ["ReclassifyResource", "AsyncReclassifyResource"]


class ReclassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReclassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReclassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReclassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReclassifyResourceWithStreamingResponse(self)

    def create(
        self,
        postfix_id: str,
        *,
        account_id: str,
        expected_disposition: Literal["NONE", "BULK", "MALICIOUS", "SPAM", "SPOOF", "SUSPICIOUS"],
        eml_content: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Change email classfication

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          eml_content: Base64 encoded content of the EML file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return self._post(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify",
            body=maybe_transform(
                {
                    "expected_disposition": expected_disposition,
                    "eml_content": eml_content,
                },
                reclassify_create_params.ReclassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncReclassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReclassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReclassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReclassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReclassifyResourceWithStreamingResponse(self)

    async def create(
        self,
        postfix_id: str,
        *,
        account_id: str,
        expected_disposition: Literal["NONE", "BULK", "MALICIOUS", "SPAM", "SPOOF", "SUSPICIOUS"],
        eml_content: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Change email classfication

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          eml_content: Base64 encoded content of the EML file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return await self._post(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify",
            body=await async_maybe_transform(
                {
                    "expected_disposition": expected_disposition,
                    "eml_content": eml_content,
                },
                reclassify_create_params.ReclassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class ReclassifyResourceWithRawResponse:
    def __init__(self, reclassify: ReclassifyResource) -> None:
        self._reclassify = reclassify

        self.create = to_raw_response_wrapper(
            reclassify.create,
        )


class AsyncReclassifyResourceWithRawResponse:
    def __init__(self, reclassify: AsyncReclassifyResource) -> None:
        self._reclassify = reclassify

        self.create = async_to_raw_response_wrapper(
            reclassify.create,
        )


class ReclassifyResourceWithStreamingResponse:
    def __init__(self, reclassify: ReclassifyResource) -> None:
        self._reclassify = reclassify

        self.create = to_streamed_response_wrapper(
            reclassify.create,
        )


class AsyncReclassifyResourceWithStreamingResponse:
    def __init__(self, reclassify: AsyncReclassifyResource) -> None:
        self._reclassify = reclassify

        self.create = async_to_streamed_response_wrapper(
            reclassify.create,
        )
