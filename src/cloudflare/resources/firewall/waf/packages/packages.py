# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .groups import GroupsResource, AsyncGroupsResource

from ....._compat import cached_property

from .rules import RulesResource, AsyncRulesResource

from .....types.firewall.waf.package_list_response import PackageListResponse

from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ....._utils import maybe_transform

from ....._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from .....types.firewall.waf.package_get_response import PackageGetResponse

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
from .....types.firewall.waf import package_list_params
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PackagesResource", "AsyncPackagesResource"]


class PackagesResource(SyncAPIResource):
    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self)

    def list(
        self,
        zone_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[PackageListResponse]:
        """
        Fetches WAF packages for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          direction: The direction used to sort returned packages.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          name: The name of the WAF package.

          order: The field used to sort returned packages.

          page: The page number of paginated results.

          per_page: The number of packages per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/waf/packages",
            page=SyncV4PagePaginationArray[PackageListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    package_list_params.PackageListParams,
                ),
            ),
            model=cast(Any, PackageListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageGetResponse:
        """
        Fetches the details of a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            PackageGetResponse,
            self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PackageGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPackagesResource(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self)

    def list(
        self,
        zone_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["name"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PackageListResponse, AsyncV4PagePaginationArray[PackageListResponse]]:
        """
        Fetches WAF packages for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          direction: The direction used to sort returned packages.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          name: The name of the WAF package.

          order: The field used to sort returned packages.

          page: The page number of paginated results.

          per_page: The number of packages per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/waf/packages",
            page=AsyncV4PagePaginationArray[PackageListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    package_list_params.PackageListParams,
                ),
            ),
            model=cast(Any, PackageListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def get(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageGetResponse:
        """
        Fetches the details of a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            PackageGetResponse,
            await self._get(
                f"/zones/{zone_identifier}/firewall/waf/packages/{identifier}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PackageGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PackagesResourceWithRawResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.list = to_raw_response_wrapper(
            packages.list,
        )
        self.get = to_raw_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._packages.rules)


class AsyncPackagesResourceWithRawResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.list = async_to_raw_response_wrapper(
            packages.list,
        )
        self.get = async_to_raw_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._packages.rules)


class PackagesResourceWithStreamingResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.list = to_streamed_response_wrapper(
            packages.list,
        )
        self.get = to_streamed_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._packages.rules)


class AsyncPackagesResourceWithStreamingResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.list = async_to_streamed_response_wrapper(
            packages.list,
        )
        self.get = async_to_streamed_response_wrapper(
            packages.get,
        )

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._packages.rules)
