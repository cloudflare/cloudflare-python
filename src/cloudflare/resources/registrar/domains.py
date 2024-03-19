# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.registrar import DomainGetResponse, DomainListResponse, DomainUpdateResponse, domain_update_params

__all__ = ["Domains", "AsyncDomains"]


class Domains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self)

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
                    post_parser=ResultWrapper._unwrapper,
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
    ) -> Optional[DomainListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/registrar/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainListResponse]], ResultWrapper[DomainListResponse]),
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncDomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self)

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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/registrar/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainListResponse]], ResultWrapper[DomainListResponse]),
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class DomainsWithRawResponse:
    def __init__(self, domains: Domains) -> None:
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


class AsyncDomainsWithRawResponse:
    def __init__(self, domains: AsyncDomains) -> None:
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


class DomainsWithStreamingResponse:
    def __init__(self, domains: Domains) -> None:
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


class AsyncDomainsWithStreamingResponse:
    def __init__(self, domains: AsyncDomains) -> None:
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
