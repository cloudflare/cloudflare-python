# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.access.logs.access_request_list_response import AccessRequestListResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Union

from ....._base_client import make_request_options

from typing_extensions import Literal

from datetime import datetime

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.access.logs import access_request_list_params
from typing import cast
from typing import cast

__all__ = ["AccessRequestsResource", "AsyncAccessRequestsResource"]


class AccessRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRequestsResourceWithRawResponse:
        return AccessRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRequestsResourceWithStreamingResponse:
        return AccessRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          account_id: Identifier

          direction: The chronological sorting order for the logs.

          limit: The maximum number of log entries to retrieve.

          since: The earliest event timestamp to query.

          until: The latest event timestamp to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "since": since,
                        "until": until,
                    },
                    access_request_list_params.AccessRequestListParams,
                ),
                post_parser=ResultWrapper[Optional[AccessRequestListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AsyncAccessRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRequestsResourceWithRawResponse:
        return AsyncAccessRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRequestsResourceWithStreamingResponse:
        return AsyncAccessRequestsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          account_id: Identifier

          direction: The chronological sorting order for the logs.

          limit: The maximum number of log entries to retrieve.

          since: The earliest event timestamp to query.

          until: The latest event timestamp to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "since": since,
                        "until": until,
                    },
                    access_request_list_params.AccessRequestListParams,
                ),
                post_parser=ResultWrapper[Optional[AccessRequestListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AccessRequestsResourceWithRawResponse:
    def __init__(self, access_requests: AccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = to_raw_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsResourceWithRawResponse:
    def __init__(self, access_requests: AsyncAccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = async_to_raw_response_wrapper(
            access_requests.list,
        )


class AccessRequestsResourceWithStreamingResponse:
    def __init__(self, access_requests: AccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = to_streamed_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsResourceWithStreamingResponse:
    def __init__(self, access_requests: AsyncAccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = async_to_streamed_response_wrapper(
            access_requests.list,
        )
