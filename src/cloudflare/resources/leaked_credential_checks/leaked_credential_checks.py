# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .detections import (
    DetectionsResource,
    AsyncDetectionsResource,
    DetectionsResourceWithRawResponse,
    AsyncDetectionsResourceWithRawResponse,
    DetectionsResourceWithStreamingResponse,
    AsyncDetectionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.leaked_credential_checks import leaked_credential_check_create_params
from ...types.leaked_credential_checks.leaked_credential_check_get_response import LeakedCredentialCheckGetResponse
from ...types.leaked_credential_checks.leaked_credential_check_create_response import (
    LeakedCredentialCheckCreateResponse,
)

__all__ = ["LeakedCredentialChecksResource", "AsyncLeakedCredentialChecksResource"]


class LeakedCredentialChecksResource(SyncAPIResource):
    @cached_property
    def detections(self) -> DetectionsResource:
        return DetectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LeakedCredentialChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LeakedCredentialChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeakedCredentialChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LeakedCredentialChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakedCredentialCheckCreateResponse:
        """
        Updates the current status of Leaked Credential Checks

        Args:
          zone_id: Identifier

          enabled: Whether or not Leaked Credential Checks are enabled

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/leaked-credential-checks",
            body=maybe_transform(
                {"enabled": enabled}, leaked_credential_check_create_params.LeakedCredentialCheckCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LeakedCredentialCheckCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialCheckCreateResponse], ResultWrapper[LeakedCredentialCheckCreateResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakedCredentialCheckGetResponse:
        """
        Retrieves the current status of Leaked Credential Checks

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/leaked-credential-checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LeakedCredentialCheckGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialCheckGetResponse], ResultWrapper[LeakedCredentialCheckGetResponse]),
        )


class AsyncLeakedCredentialChecksResource(AsyncAPIResource):
    @cached_property
    def detections(self) -> AsyncDetectionsResource:
        return AsyncDetectionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLeakedCredentialChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeakedCredentialChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeakedCredentialChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLeakedCredentialChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakedCredentialCheckCreateResponse:
        """
        Updates the current status of Leaked Credential Checks

        Args:
          zone_id: Identifier

          enabled: Whether or not Leaked Credential Checks are enabled

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/leaked-credential-checks",
            body=await async_maybe_transform(
                {"enabled": enabled}, leaked_credential_check_create_params.LeakedCredentialCheckCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LeakedCredentialCheckCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialCheckCreateResponse], ResultWrapper[LeakedCredentialCheckCreateResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeakedCredentialCheckGetResponse:
        """
        Retrieves the current status of Leaked Credential Checks

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/leaked-credential-checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LeakedCredentialCheckGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[LeakedCredentialCheckGetResponse], ResultWrapper[LeakedCredentialCheckGetResponse]),
        )


class LeakedCredentialChecksResourceWithRawResponse:
    def __init__(self, leaked_credential_checks: LeakedCredentialChecksResource) -> None:
        self._leaked_credential_checks = leaked_credential_checks

        self.create = to_raw_response_wrapper(
            leaked_credential_checks.create,
        )
        self.get = to_raw_response_wrapper(
            leaked_credential_checks.get,
        )

    @cached_property
    def detections(self) -> DetectionsResourceWithRawResponse:
        return DetectionsResourceWithRawResponse(self._leaked_credential_checks.detections)


class AsyncLeakedCredentialChecksResourceWithRawResponse:
    def __init__(self, leaked_credential_checks: AsyncLeakedCredentialChecksResource) -> None:
        self._leaked_credential_checks = leaked_credential_checks

        self.create = async_to_raw_response_wrapper(
            leaked_credential_checks.create,
        )
        self.get = async_to_raw_response_wrapper(
            leaked_credential_checks.get,
        )

    @cached_property
    def detections(self) -> AsyncDetectionsResourceWithRawResponse:
        return AsyncDetectionsResourceWithRawResponse(self._leaked_credential_checks.detections)


class LeakedCredentialChecksResourceWithStreamingResponse:
    def __init__(self, leaked_credential_checks: LeakedCredentialChecksResource) -> None:
        self._leaked_credential_checks = leaked_credential_checks

        self.create = to_streamed_response_wrapper(
            leaked_credential_checks.create,
        )
        self.get = to_streamed_response_wrapper(
            leaked_credential_checks.get,
        )

    @cached_property
    def detections(self) -> DetectionsResourceWithStreamingResponse:
        return DetectionsResourceWithStreamingResponse(self._leaked_credential_checks.detections)


class AsyncLeakedCredentialChecksResourceWithStreamingResponse:
    def __init__(self, leaked_credential_checks: AsyncLeakedCredentialChecksResource) -> None:
        self._leaked_credential_checks = leaked_credential_checks

        self.create = async_to_streamed_response_wrapper(
            leaked_credential_checks.create,
        )
        self.get = async_to_streamed_response_wrapper(
            leaked_credential_checks.get,
        )

    @cached_property
    def detections(self) -> AsyncDetectionsResourceWithStreamingResponse:
        return AsyncDetectionsResourceWithStreamingResponse(self._leaked_credential_checks.detections)
