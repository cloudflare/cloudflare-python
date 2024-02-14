# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import WorkerDomainGetResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["WorkerDomains", "AsyncWorkerDomains"]


class WorkerDomains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkerDomainsWithRawResponse:
        return WorkerDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkerDomainsWithStreamingResponse:
        return WorkerDomainsWithStreamingResponse(self)

    def delete(
        self,
        domain_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Detaches a Worker from a zone and hostname.

        Args:
          domain_id: Identifer of the Worker Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        domain_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerDomainGetResponse:
        """
        Gets a Worker domain.

        Args:
          domain_id: Identifer of the Worker Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkerDomainGetResponse], ResultWrapper[WorkerDomainGetResponse]),
        )


class AsyncWorkerDomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkerDomainsWithRawResponse:
        return AsyncWorkerDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkerDomainsWithStreamingResponse:
        return AsyncWorkerDomainsWithStreamingResponse(self)

    async def delete(
        self,
        domain_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Detaches a Worker from a zone and hostname.

        Args:
          domain_id: Identifer of the Worker Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        domain_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerDomainGetResponse:
        """
        Gets a Worker domain.

        Args:
          domain_id: Identifer of the Worker Domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkerDomainGetResponse], ResultWrapper[WorkerDomainGetResponse]),
        )


class WorkerDomainsWithRawResponse:
    def __init__(self, worker_domains: WorkerDomains) -> None:
        self._worker_domains = worker_domains

        self.delete = to_raw_response_wrapper(
            worker_domains.delete,
        )
        self.get = to_raw_response_wrapper(
            worker_domains.get,
        )


class AsyncWorkerDomainsWithRawResponse:
    def __init__(self, worker_domains: AsyncWorkerDomains) -> None:
        self._worker_domains = worker_domains

        self.delete = async_to_raw_response_wrapper(
            worker_domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            worker_domains.get,
        )


class WorkerDomainsWithStreamingResponse:
    def __init__(self, worker_domains: WorkerDomains) -> None:
        self._worker_domains = worker_domains

        self.delete = to_streamed_response_wrapper(
            worker_domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            worker_domains.get,
        )


class AsyncWorkerDomainsWithStreamingResponse:
    def __init__(self, worker_domains: AsyncWorkerDomains) -> None:
        self._worker_domains = worker_domains

        self.delete = async_to_streamed_response_wrapper(
            worker_domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            worker_domains.get,
        )
