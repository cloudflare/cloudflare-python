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
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.leaked_credential_checks import detection_create_params, detection_update_params
from ...types.leaked_credential_checks.detection_list_response import DetectionListResponse
from ...types.leaked_credential_checks.detection_create_response import DetectionCreateResponse
from ...types.leaked_credential_checks.detection_update_response import DetectionUpdateResponse

__all__ = ["DetectionsResource", "AsyncDetectionsResource"]


class DetectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DetectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DetectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionCreateResponse:
        """
        Create user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          password: The ruleset expression to use in matching the password in a request

          username: The ruleset expression to use in matching the username in a request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/leaked-credential-checks/detections",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                detection_create_params.DetectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DetectionCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DetectionCreateResponse], ResultWrapper[DetectionCreateResponse]),
        )

    def update(
        self,
        detection_id: str,
        *,
        zone_id: str,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionUpdateResponse:
        """
        Update user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          detection_id: The unique ID for this custom detection

          password: The ruleset expression to use in matching the password in a request

          username: The ruleset expression to use in matching the username in a request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not detection_id:
            raise ValueError(f"Expected a non-empty value for `detection_id` but received {detection_id!r}")
        return self._put(
            f"/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                detection_update_params.DetectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DetectionUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DetectionUpdateResponse], ResultWrapper[DetectionUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DetectionListResponse]:
        """
        List user-defined detection patterns for Leaked Credential Checks

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/leaked-credential-checks/detections",
            page=SyncSinglePage[DetectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DetectionListResponse,
        )

    def delete(
        self,
        detection_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          detection_id: The unique ID for this custom detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not detection_id:
            raise ValueError(f"Expected a non-empty value for `detection_id` but received {detection_id!r}")
        return self._delete(
            f"/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncDetectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDetectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionCreateResponse:
        """
        Create user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          password: The ruleset expression to use in matching the password in a request

          username: The ruleset expression to use in matching the username in a request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/leaked-credential-checks/detections",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                detection_create_params.DetectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DetectionCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DetectionCreateResponse], ResultWrapper[DetectionCreateResponse]),
        )

    async def update(
        self,
        detection_id: str,
        *,
        zone_id: str,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionUpdateResponse:
        """
        Update user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          detection_id: The unique ID for this custom detection

          password: The ruleset expression to use in matching the password in a request

          username: The ruleset expression to use in matching the username in a request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not detection_id:
            raise ValueError(f"Expected a non-empty value for `detection_id` but received {detection_id!r}")
        return await self._put(
            f"/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                detection_update_params.DetectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DetectionUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DetectionUpdateResponse], ResultWrapper[DetectionUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DetectionListResponse, AsyncSinglePage[DetectionListResponse]]:
        """
        List user-defined detection patterns for Leaked Credential Checks

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/leaked-credential-checks/detections",
            page=AsyncSinglePage[DetectionListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DetectionListResponse,
        )

    async def delete(
        self,
        detection_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Remove user-defined detection pattern for Leaked Credential Checks

        Args:
          zone_id: Identifier

          detection_id: The unique ID for this custom detection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not detection_id:
            raise ValueError(f"Expected a non-empty value for `detection_id` but received {detection_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class DetectionsResourceWithRawResponse:
    def __init__(self, detections: DetectionsResource) -> None:
        self._detections = detections

        self.create = to_raw_response_wrapper(
            detections.create,
        )
        self.update = to_raw_response_wrapper(
            detections.update,
        )
        self.list = to_raw_response_wrapper(
            detections.list,
        )
        self.delete = to_raw_response_wrapper(
            detections.delete,
        )


class AsyncDetectionsResourceWithRawResponse:
    def __init__(self, detections: AsyncDetectionsResource) -> None:
        self._detections = detections

        self.create = async_to_raw_response_wrapper(
            detections.create,
        )
        self.update = async_to_raw_response_wrapper(
            detections.update,
        )
        self.list = async_to_raw_response_wrapper(
            detections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            detections.delete,
        )


class DetectionsResourceWithStreamingResponse:
    def __init__(self, detections: DetectionsResource) -> None:
        self._detections = detections

        self.create = to_streamed_response_wrapper(
            detections.create,
        )
        self.update = to_streamed_response_wrapper(
            detections.update,
        )
        self.list = to_streamed_response_wrapper(
            detections.list,
        )
        self.delete = to_streamed_response_wrapper(
            detections.delete,
        )


class AsyncDetectionsResourceWithStreamingResponse:
    def __init__(self, detections: AsyncDetectionsResource) -> None:
        self._detections = detections

        self.create = async_to_streamed_response_wrapper(
            detections.create,
        )
        self.update = async_to_streamed_response_wrapper(
            detections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            detections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            detections.delete,
        )
