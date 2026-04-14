# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.registrar import domain_update_params
from ...types.registrar.domain import Domain

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
    )
    def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | Omit = omit,
        locked: bool | Omit = omit,
        privacy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update individual domain.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
        return self._put(
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
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Show individual domain.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._get(
            f"/accounts/{account_id}/registrar/domains/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
    )
    async def update(
        self,
        domain_name: str,
        *,
        account_id: str,
        auto_renew: bool | Omit = omit,
        locked: bool | Omit = omit,
        privacy: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update individual domain.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

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
        return await self._put(
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
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated(
        "This operation is deprecated and will be removed in a future release. A replacement Registrar API will be announced separately."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Show individual domain.

        Args:
          account_id: Identifier

          domain_name: Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
              `mybrand.app`). The domain name uniquely identifies a registration — the same
              domain cannot be registered twice, making it a natural idempotency key for
              registration requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._get(
            f"/accounts/{account_id}/registrar/domains/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                domains.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                domains.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                domains.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                domains.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                domains.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                domains.get,  # pyright: ignore[reportDeprecated],
            )
        )


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                domains.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                domains.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                domains.get,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                domains.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                domains.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                domains.get,  # pyright: ignore[reportDeprecated],
            )
        )
