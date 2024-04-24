# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

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
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.registrar import domain_update_params
from ...types.registrar.domain import Domain
from ...types.registrar.domain_get_response import DomainGetResponse
from ...types.registrar.domain_update_response import DomainUpdateResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self)

    def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | NotGiven = NOT_GIVEN,
        locked: bool | NotGiven = NOT_GIVEN,
        privacy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainUpdateResponse]:
        """
        Update individual domain.

        Args:
          account_id: Identifier

          domain_name: Domain name.

          auto_renew: Auto-renew controls whether subscription is automatically renewed upon domain
              expiration.

          locked: Shows whether a registrar lock is in place for a domain.

          privacy: Privacy option controls redacting WHOIS information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainUpdateResponse],
            self._put(
                f"/accounts/{account_id}/registrar/domains/{domain_name}",
                body=maybe_transform(
                    {
                        "auto_renew": auto_renew,
                        "locked": locked,
                        "privacy": privacy,
                    },
                    domain_update_params.DomainUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DomainUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> SyncSinglePage[Domain]:
        """
        List domains handled by Registrar.

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
            f"/accounts/{account_id}/registrar/domains",
            page=SyncSinglePage[Domain],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Domain,
        )

    def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainGetResponse]:
        """
        Show individual domain.

        Args:
          account_id: Identifier

          domain_name: Domain name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainGetResponse],
            self._get(
                f"/accounts/{account_id}/registrar/domains/{domain_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DomainGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | NotGiven = NOT_GIVEN,
        locked: bool | NotGiven = NOT_GIVEN,
        privacy: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainUpdateResponse]:
        """
        Update individual domain.

        Args:
          account_id: Identifier

          domain_name: Domain name.

          auto_renew: Auto-renew controls whether subscription is automatically renewed upon domain
              expiration.

          locked: Shows whether a registrar lock is in place for a domain.

          privacy: Privacy option controls redacting WHOIS information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainUpdateResponse],
            await self._put(
                f"/accounts/{account_id}/registrar/domains/{domain_name}",
                body=await async_maybe_transform(
                    {
                        "auto_renew": auto_renew,
                        "locked": locked,
                        "privacy": privacy,
                    },
                    domain_update_params.DomainUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DomainUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> AsyncPaginator[Domain, AsyncSinglePage[Domain]]:
        """
        List domains handled by Registrar.

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
            f"/accounts/{account_id}/registrar/domains",
            page=AsyncSinglePage[Domain],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Domain,
        )

    async def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainGetResponse]:
        """
        Show individual domain.

        Args:
          account_id: Identifier

          domain_name: Domain name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainGetResponse],
            await self._get(
                f"/accounts/{account_id}/registrar/domains/{domain_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[DomainGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
