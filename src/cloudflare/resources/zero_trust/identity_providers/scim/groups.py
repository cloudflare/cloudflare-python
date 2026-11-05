# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.zero_trust_group import ZeroTrustGroup
from .....types.zero_trust.identity_providers.scim import group_list_params
from .....types.zero_trust.identity_providers.scim.group_get_response import GroupGetResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: SequenceNotStr[str] | Omit = omit,
        idp_resource_id: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ZeroTrustGroup]:
        """
        Lists SCIM Group resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
              "Id". Pass once for a single lookup (`?cf_resource_id=A`) or repeat the
              parameter (`?cf_resource_id=A&cf_resource_id=B`) to look up multiple groups in
              one request, up to 50 values. Mutually exclusive with `idp_resource_id`, `name`,
              `search_contains`, and `search_starts_with`.

          idp_resource_id: The IdP-generated Id of the SCIM Group resource; also known as the "external
              Id". Pass once for a single lookup (`?idp_resource_id=A`) or repeat the
              parameter (`?idp_resource_id=A&idp_resource_id=B`) to look up multiple groups in
              one request, up to 50 values. Mutually exclusive with `cf_resource_id`, `name`,
              `search_contains`, and `search_starts_with`.

          name: The display name of the SCIM Group resource.

          page: Page number of results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
            ),
            page=SyncV4PagePaginationArray[ZeroTrustGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            model=ZeroTrustGroup,
        )

    def delete(
        self,
        group_id: str,
        *,
        account_id: str,
        identity_provider_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a SCIM Group resource from the identity provider's SCIM population.

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          group_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups/{group_id}",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        group_id: str,
        *,
        account_id: str,
        identity_provider_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GroupGetResponse]:
        """
        Returns a SCIM Group resource, including its direct members, synced to
        Cloudflare via the System for Cross-domain Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          group_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups/{group_id}",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GroupGetResponse]], ResultWrapper[GroupGetResponse]),
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: SequenceNotStr[str] | Omit = omit,
        idp_resource_id: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ZeroTrustGroup, AsyncV4PagePaginationArray[ZeroTrustGroup]]:
        """
        Lists SCIM Group resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
              "Id". Pass once for a single lookup (`?cf_resource_id=A`) or repeat the
              parameter (`?cf_resource_id=A&cf_resource_id=B`) to look up multiple groups in
              one request, up to 50 values. Mutually exclusive with `idp_resource_id`, `name`,
              `search_contains`, and `search_starts_with`.

          idp_resource_id: The IdP-generated Id of the SCIM Group resource; also known as the "external
              Id". Pass once for a single lookup (`?idp_resource_id=A`) or repeat the
              parameter (`?idp_resource_id=A&idp_resource_id=B`) to look up multiple groups in
              one request, up to 50 values. Mutually exclusive with `cf_resource_id`, `name`,
              `search_contains`, and `search_starts_with`.

          name: The display name of the SCIM Group resource.

          page: Page number of results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
            ),
            page=AsyncV4PagePaginationArray[ZeroTrustGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            model=ZeroTrustGroup,
        )

    async def delete(
        self,
        group_id: str,
        *,
        account_id: str,
        identity_provider_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a SCIM Group resource from the identity provider's SCIM population.

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          group_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups/{group_id}",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        group_id: str,
        *,
        account_id: str,
        identity_provider_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GroupGetResponse]:
        """
        Returns a SCIM Group resource, including its direct members, synced to
        Cloudflare via the System for Cross-domain Identity Management (SCIM).

        Args:
          account_id: Identifier.

          identity_provider_id: UUID.

          group_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups/{group_id}",
                account_id=account_id,
                identity_provider_id=identity_provider_id,
                group_id=group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GroupGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GroupGetResponse]], ResultWrapper[GroupGetResponse]),
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )
        self.get = to_raw_response_wrapper(
            groups.get,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )
        self.get = async_to_raw_response_wrapper(
            groups.get,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )
        self.get = to_streamed_response_wrapper(
            groups.get,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            groups.get,
        )
