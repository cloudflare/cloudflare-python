# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.pages.projects import (
    DomainUpdateResponse,
    DomainGetResponse,
    DomainPagesDomainsAddDomainResponse,
    DomainPagesDomainsGetDomainsResponse,
)

from typing import Optional, Type

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
from ....types.pages.projects import domain_pages_domains_add_domain_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainUpdateResponse]:
        """
        Retry the validation status of a single domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainUpdateResponse],
            self._patch(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
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

    def delete(
        self,
        domain_name: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a Pages project's domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainGetResponse]:
        """
        Fetch a single domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainGetResponse],
            self._get(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
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

    def pages_domains_add_domain(
        self,
        project_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainPagesDomainsAddDomainResponse]:
        """
        Add a new domain for the Pages project.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return cast(
            Optional[DomainPagesDomainsAddDomainResponse],
            self._post(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains",
                body=maybe_transform(body, domain_pages_domains_add_domain_params.DomainPagesDomainsAddDomainParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainPagesDomainsAddDomainResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def pages_domains_get_domains(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainPagesDomainsGetDomainsResponse:
        """
        Fetch a list of all domains associated with a Pages project.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainPagesDomainsGetDomainsResponse], ResultWrapper[DomainPagesDomainsGetDomainsResponse]
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
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainUpdateResponse]:
        """
        Retry the validation status of a single domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainUpdateResponse],
            await self._patch(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
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

    async def delete(
        self,
        domain_name: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a Pages project's domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return await self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        domain_name: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainGetResponse]:
        """
        Fetch a single domain.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          domain_name: Name of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not domain_name:
            raise ValueError(f"Expected a non-empty value for `domain_name` but received {domain_name!r}")
        return cast(
            Optional[DomainGetResponse],
            await self._get(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}",
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

    async def pages_domains_add_domain(
        self,
        project_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DomainPagesDomainsAddDomainResponse]:
        """
        Add a new domain for the Pages project.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return cast(
            Optional[DomainPagesDomainsAddDomainResponse],
            await self._post(
                f"/accounts/{account_id}/pages/projects/{project_name}/domains",
                body=maybe_transform(body, domain_pages_domains_add_domain_params.DomainPagesDomainsAddDomainParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DomainPagesDomainsAddDomainResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def pages_domains_get_domains(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainPagesDomainsGetDomainsResponse:
        """
        Fetch a list of all domains associated with a Pages project.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return await self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainPagesDomainsGetDomainsResponse], ResultWrapper[DomainPagesDomainsGetDomainsResponse]
            ),
        )


class DomainsWithRawResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )
        self.pages_domains_add_domain = to_raw_response_wrapper(
            domains.pages_domains_add_domain,
        )
        self.pages_domains_get_domains = to_raw_response_wrapper(
            domains.pages_domains_get_domains,
        )


class AsyncDomainsWithRawResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )
        self.pages_domains_add_domain = async_to_raw_response_wrapper(
            domains.pages_domains_add_domain,
        )
        self.pages_domains_get_domains = async_to_raw_response_wrapper(
            domains.pages_domains_get_domains,
        )


class DomainsWithStreamingResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )
        self.pages_domains_add_domain = to_streamed_response_wrapper(
            domains.pages_domains_add_domain,
        )
        self.pages_domains_get_domains = to_streamed_response_wrapper(
            domains.pages_domains_get_domains,
        )


class AsyncDomainsWithStreamingResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
        self.pages_domains_add_domain = async_to_streamed_response_wrapper(
            domains.pages_domains_add_domain,
        )
        self.pages_domains_get_domains = async_to_streamed_response_wrapper(
            domains.pages_domains_get_domains,
        )
