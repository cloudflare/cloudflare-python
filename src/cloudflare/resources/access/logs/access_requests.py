# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.access.logs import AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["AccessRequests", "AsyncAccessRequests"]


class AccessRequests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRequestsWithRawResponse:
        return AccessRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRequestsWithStreamingResponse:
        return AccessRequestsWithStreamingResponse(self)

    def access_authentication_logs_get_access_authentication_logs(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{identifier}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse]],
                ResultWrapper[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            ),
        )


class AsyncAccessRequests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRequestsWithRawResponse:
        return AsyncAccessRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRequestsWithStreamingResponse:
        return AsyncAccessRequestsWithStreamingResponse(self)

    async def access_authentication_logs_get_access_authentication_logs(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{identifier}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse]],
                ResultWrapper[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            ),
        )


class AccessRequestsWithRawResponse:
    def __init__(self, access_requests: AccessRequests) -> None:
        self._access_requests = access_requests

        self.access_authentication_logs_get_access_authentication_logs = to_raw_response_wrapper(
            access_requests.access_authentication_logs_get_access_authentication_logs,
        )


class AsyncAccessRequestsWithRawResponse:
    def __init__(self, access_requests: AsyncAccessRequests) -> None:
        self._access_requests = access_requests

        self.access_authentication_logs_get_access_authentication_logs = async_to_raw_response_wrapper(
            access_requests.access_authentication_logs_get_access_authentication_logs,
        )


class AccessRequestsWithStreamingResponse:
    def __init__(self, access_requests: AccessRequests) -> None:
        self._access_requests = access_requests

        self.access_authentication_logs_get_access_authentication_logs = to_streamed_response_wrapper(
            access_requests.access_authentication_logs_get_access_authentication_logs,
        )


class AsyncAccessRequestsWithStreamingResponse:
    def __init__(self, access_requests: AsyncAccessRequests) -> None:
        self._access_requests = access_requests

        self.access_authentication_logs_get_access_authentication_logs = async_to_streamed_response_wrapper(
            access_requests.access_authentication_logs_get_access_authentication_logs,
        )
