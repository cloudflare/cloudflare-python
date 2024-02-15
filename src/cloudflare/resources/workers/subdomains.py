# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.workers import (
    SubdomainWorkerSubdomainCreateSubdomainResponse,
    SubdomainWorkerSubdomainGetSubdomainResponse,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.workers import subdomain_worker_subdomain_create_subdomain_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Subdomains", "AsyncSubdomains"]


class Subdomains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubdomainsWithRawResponse:
        return SubdomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubdomainsWithStreamingResponse:
        return SubdomainsWithStreamingResponse(self)

    def worker_subdomain_create_subdomain(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainWorkerSubdomainCreateSubdomainResponse:
        """
        Creates a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=maybe_transform(
                body, subdomain_worker_subdomain_create_subdomain_params.SubdomainWorkerSubdomainCreateSubdomainParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubdomainWorkerSubdomainCreateSubdomainResponse],
                ResultWrapper[SubdomainWorkerSubdomainCreateSubdomainResponse],
            ),
        )

    def worker_subdomain_get_subdomain(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainWorkerSubdomainGetSubdomainResponse:
        """
        Returns a Workers subdomain for an account.

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
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubdomainWorkerSubdomainGetSubdomainResponse],
                ResultWrapper[SubdomainWorkerSubdomainGetSubdomainResponse],
            ),
        )


class AsyncSubdomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubdomainsWithRawResponse:
        return AsyncSubdomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubdomainsWithStreamingResponse:
        return AsyncSubdomainsWithStreamingResponse(self)

    async def worker_subdomain_create_subdomain(
        self,
        account_id: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainWorkerSubdomainCreateSubdomainResponse:
        """
        Creates a Workers subdomain for an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/subdomain",
            body=maybe_transform(
                body, subdomain_worker_subdomain_create_subdomain_params.SubdomainWorkerSubdomainCreateSubdomainParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubdomainWorkerSubdomainCreateSubdomainResponse],
                ResultWrapper[SubdomainWorkerSubdomainCreateSubdomainResponse],
            ),
        )

    async def worker_subdomain_get_subdomain(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainWorkerSubdomainGetSubdomainResponse:
        """
        Returns a Workers subdomain for an account.

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
            f"/accounts/{account_id}/workers/subdomain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SubdomainWorkerSubdomainGetSubdomainResponse],
                ResultWrapper[SubdomainWorkerSubdomainGetSubdomainResponse],
            ),
        )


class SubdomainsWithRawResponse:
    def __init__(self, subdomains: Subdomains) -> None:
        self._subdomains = subdomains

        self.worker_subdomain_create_subdomain = to_raw_response_wrapper(
            subdomains.worker_subdomain_create_subdomain,
        )
        self.worker_subdomain_get_subdomain = to_raw_response_wrapper(
            subdomains.worker_subdomain_get_subdomain,
        )


class AsyncSubdomainsWithRawResponse:
    def __init__(self, subdomains: AsyncSubdomains) -> None:
        self._subdomains = subdomains

        self.worker_subdomain_create_subdomain = async_to_raw_response_wrapper(
            subdomains.worker_subdomain_create_subdomain,
        )
        self.worker_subdomain_get_subdomain = async_to_raw_response_wrapper(
            subdomains.worker_subdomain_get_subdomain,
        )


class SubdomainsWithStreamingResponse:
    def __init__(self, subdomains: Subdomains) -> None:
        self._subdomains = subdomains

        self.worker_subdomain_create_subdomain = to_streamed_response_wrapper(
            subdomains.worker_subdomain_create_subdomain,
        )
        self.worker_subdomain_get_subdomain = to_streamed_response_wrapper(
            subdomains.worker_subdomain_get_subdomain,
        )


class AsyncSubdomainsWithStreamingResponse:
    def __init__(self, subdomains: AsyncSubdomains) -> None:
        self._subdomains = subdomains

        self.worker_subdomain_create_subdomain = async_to_streamed_response_wrapper(
            subdomains.worker_subdomain_create_subdomain,
        )
        self.worker_subdomain_get_subdomain = async_to_streamed_response_wrapper(
            subdomains.worker_subdomain_get_subdomain,
        )
