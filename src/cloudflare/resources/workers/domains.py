# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.workers import (
    DomainGetResponse,
    DomainWorkerDomainListDomainsResponse,
    DomainWorkerDomainAttachToDomainResponse,
    domain_worker_domain_list_domains_params,
    domain_worker_domain_attach_to_domain_params,
)

__all__ = ["Domains", "AsyncDomains"]


class Domains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self)

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
    ) -> DomainGetResponse:
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
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )

    def worker_domain_attach_to_domain(
        self,
        account_id: object,
        *,
        environment: str,
        hostname: str,
        service: str,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainWorkerDomainAttachToDomainResponse:
        """
        Attaches a Worker to a zone and hostname.

        Args:
          environment: Worker environment associated with the zone and hostname.

          hostname: Hostname of the Worker Domain.

          service: Worker service associated with the zone and hostname.

          zone_id: Identifier of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/workers/domains",
            body=maybe_transform(
                {
                    "environment": environment,
                    "hostname": hostname,
                    "service": service,
                    "zone_id": zone_id,
                },
                domain_worker_domain_attach_to_domain_params.DomainWorkerDomainAttachToDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainWorkerDomainAttachToDomainResponse], ResultWrapper[DomainWorkerDomainAttachToDomainResponse]
            ),
        )

    def worker_domain_list_domains(
        self,
        account_id: object,
        *,
        environment: str | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        service: str | NotGiven = NOT_GIVEN,
        zone_id: object | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainWorkerDomainListDomainsResponse:
        """
        Lists all Worker Domains for an account.

        Args:
          environment: Worker environment associated with the zone and hostname.

          hostname: Hostname of the Worker Domain.

          service: Worker service associated with the zone and hostname.

          zone_id: Identifier of the zone.

          zone_name: Name of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/workers/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "hostname": hostname,
                        "service": service,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    domain_worker_domain_list_domains_params.DomainWorkerDomainListDomainsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainWorkerDomainListDomainsResponse], ResultWrapper[DomainWorkerDomainListDomainsResponse]
            ),
        )


class AsyncDomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self)

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
    ) -> DomainGetResponse:
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
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )

    async def worker_domain_attach_to_domain(
        self,
        account_id: object,
        *,
        environment: str,
        hostname: str,
        service: str,
        zone_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainWorkerDomainAttachToDomainResponse:
        """
        Attaches a Worker to a zone and hostname.

        Args:
          environment: Worker environment associated with the zone and hostname.

          hostname: Hostname of the Worker Domain.

          service: Worker service associated with the zone and hostname.

          zone_id: Identifier of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/workers/domains",
            body=maybe_transform(
                {
                    "environment": environment,
                    "hostname": hostname,
                    "service": service,
                    "zone_id": zone_id,
                },
                domain_worker_domain_attach_to_domain_params.DomainWorkerDomainAttachToDomainParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainWorkerDomainAttachToDomainResponse], ResultWrapper[DomainWorkerDomainAttachToDomainResponse]
            ),
        )

    async def worker_domain_list_domains(
        self,
        account_id: object,
        *,
        environment: str | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        service: str | NotGiven = NOT_GIVEN,
        zone_id: object | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainWorkerDomainListDomainsResponse:
        """
        Lists all Worker Domains for an account.

        Args:
          environment: Worker environment associated with the zone and hostname.

          hostname: Hostname of the Worker Domain.

          service: Worker service associated with the zone and hostname.

          zone_id: Identifier of the zone.

          zone_name: Name of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/workers/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "hostname": hostname,
                        "service": service,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    domain_worker_domain_list_domains_params.DomainWorkerDomainListDomainsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainWorkerDomainListDomainsResponse], ResultWrapper[DomainWorkerDomainListDomainsResponse]
            ),
        )


class DomainsWithRawResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )
        self.worker_domain_attach_to_domain = to_raw_response_wrapper(
            domains.worker_domain_attach_to_domain,
        )
        self.worker_domain_list_domains = to_raw_response_wrapper(
            domains.worker_domain_list_domains,
        )


class AsyncDomainsWithRawResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )
        self.worker_domain_attach_to_domain = async_to_raw_response_wrapper(
            domains.worker_domain_attach_to_domain,
        )
        self.worker_domain_list_domains = async_to_raw_response_wrapper(
            domains.worker_domain_list_domains,
        )


class DomainsWithStreamingResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )
        self.worker_domain_attach_to_domain = to_streamed_response_wrapper(
            domains.worker_domain_attach_to_domain,
        )
        self.worker_domain_list_domains = to_streamed_response_wrapper(
            domains.worker_domain_list_domains,
        )


class AsyncDomainsWithStreamingResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
        self.worker_domain_attach_to_domain = async_to_streamed_response_wrapper(
            domains.worker_domain_attach_to_domain,
        )
        self.worker_domain_list_domains = async_to_streamed_response_wrapper(
            domains.worker_domain_list_domains,
        )
