# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._base_client import make_request_options, AsyncPaginator

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params

__all__ = ["PermissionGroupsResource", "AsyncPermissionGroupsResource"]

class PermissionGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PermissionGroupsResourceWithRawResponse:
        return PermissionGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionGroupsResourceWithStreamingResponse:
        return PermissionGroupsResourceWithStreamingResponse(self)

    def list(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[object]:
        """Find all available permission groups for API Tokens"""
        return self._get_api_list(
            "/user/tokens/permission_groups",
            page = SyncSinglePage[object],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=object,
        )

class AsyncPermissionGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPermissionGroupsResourceWithRawResponse:
        return AsyncPermissionGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionGroupsResourceWithStreamingResponse:
        return AsyncPermissionGroupsResourceWithStreamingResponse(self)

    def list(self,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """Find all available permission groups for API Tokens"""
        return self._get_api_list(
            "/user/tokens/permission_groups",
            page = AsyncSinglePage[object],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=object,
        )

class PermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_raw_response_wrapper(
            permission_groups.list,
        )

class AsyncPermissionGroupsResourceWithRawResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_raw_response_wrapper(
            permission_groups.list,
        )

class PermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: PermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = to_streamed_response_wrapper(
            permission_groups.list,
        )

class AsyncPermissionGroupsResourceWithStreamingResponse:
    def __init__(self, permission_groups: AsyncPermissionGroupsResource) -> None:
        self._permission_groups = permission_groups

        self.list = async_to_streamed_response_wrapper(
            permission_groups.list,
        )