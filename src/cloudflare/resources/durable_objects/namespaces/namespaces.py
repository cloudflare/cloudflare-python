# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .objects import ObjectsResource, AsyncObjectsResource

from ...._compat import cached_property

from ....types.durable_objects.namespace import Namespace

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._base_client import make_request_options, AsyncPaginator

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
from ....types import shared_params
from .objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Namespace]:
        """
        Returns the Durable Object namespaces owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/durable_objects/namespaces",
            page=SyncSinglePage[Namespace],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Namespace,
        )


class AsyncNamespacesResource(AsyncAPIResource):
    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Namespace, AsyncSinglePage[Namespace]]:
        """
        Returns the Durable Object namespaces owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/durable_objects/namespaces",
            page=AsyncSinglePage[Namespace],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Namespace,
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._namespaces.objects)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._namespaces.objects)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._namespaces.objects)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._namespaces.objects)
