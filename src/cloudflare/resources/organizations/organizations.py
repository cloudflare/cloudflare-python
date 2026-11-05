# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .logs.logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
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
from .billing.billing import (
    BillingResource,
    AsyncBillingResource,
    BillingResourceWithRawResponse,
    AsyncBillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
    AsyncBillingResourceWithStreamingResponse,
)
from .organization_profile import (
    OrganizationProfileResource,
    AsyncOrganizationProfileResource,
    OrganizationProfileResourceWithRawResponse,
    AsyncOrganizationProfileResourceWithRawResponse,
    OrganizationProfileResourceWithStreamingResponse,
    AsyncOrganizationProfileResourceWithStreamingResponse,
)
from ...types.organizations import organization_list_params, organization_create_params, organization_update_params
from ...types.organizations.organization import Organization
from ...types.organizations.organization_delete_response import OrganizationDeleteResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    """
    User API tokens can list and create Organizations, but reading, updating, or deleting an Organization requires a Global API key and your registered email address. The `cloudflare_organization` Terraform resource therefore requires a Global API key for its full lifecycle.

    See [Organizations authentication limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/#api-authentication) for credential compatibility by operation. Each endpoint’s **Security** section lists its supported authentication methods, with **Accepted Permissions** where applicable.
    """

    @cached_property
    def organization_profile(self) -> OrganizationProfileResource:
        return OrganizationProfileResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent: organization_create_params.Parent | Omit = omit,
        profile: organization_create_params.Profile | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """Create a new organization for a user.

        Sub-organization creation availability
        depends on the organization's capabilities. The optional `profile` object
        accepts partial profile details; its individual fields are not required.
        Organization names are limited to 65 UTF-8 bytes. Each profile field is limited
        to 1,000 UTF-8 bytes, and a non-empty business email must be valid. At least one
        of business name, address, phone, or email must be non-empty to persist a
        profile.

        Args:
          name: The Organization name, limited to 65 UTF-8 bytes.

          profile: Optional profile fields, each limited to 1,000 UTF-8 bytes. An empty profile is
              ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organizations",
            body=maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                    "profile": profile,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )

    def update(
        self,
        organization_id: str,
        *,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """Update an organization's name.

        Supplying `parent_id` verifies the current
        parent; this endpoint cannot move an organization. Organization names are
        limited to 65 UTF-8 bytes.

        Args:
          name: The Organization's display name, limited to 65 UTF-8 bytes. An omitted, empty,
              or unchanged value is a no-op.

          parent_id: The current parent Organization ID. A different value is rejected; this endpoint
              cannot move an Organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._put(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        containing: organization_list_params.Containing | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        member: organization_list_params.Member | Omit = omit,
        name: organization_list_params.Name | Omit = omit,
        order_by: Literal["name"] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        parent: organization_list_params.Parent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Organization]:
        """Retrieve a list of organizations a particular user has access to.

        At most one of
        `containing.account`, `containing.user`, or `containing.organization` may be
        provided.

        Args:
          id: Only return organizations with the specified IDs (ex. id=foo&id=bar). Send
              multiple elements by repeating the query value.

          direction: Sort direction for the `order_by` field. Defaults to `asc` when `order_by` is
              specified.

          order_by: Field to order results by. Currently supported values: `name`. When not
              specified, results are ordered by hierarchy.

          page_size: The amount of items to return. Defaults to 10.

          page_token: An opaque token returned from the last list response that when provided will
              retrieve the next page.

              Parameters used to filter the retrieved list must remain in subsequent requests
              with a page token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organizations",
            page=SyncSinglePage[Organization],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "containing": containing,
                        "direction": direction,
                        "member": member,
                        "name": name,
                        "order_by": order_by,
                        "page_size": page_size,
                        "page_token": page_token,
                        "parent": parent,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=Organization,
        )

    def delete(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDeleteResponse:
        """Delete an organization.

        It must not contain active sub-organizations or
        accounts. A root organization must also have no active managed users.
        Sub-organization deletion availability depends on the organization's
        capabilities.

        **Access Control:** Root deletion is restricted to enterprise organizations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._delete(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OrganizationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OrganizationDeleteResponse], ResultWrapper[OrganizationDeleteResponse]),
        )

    def get(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Retrieve the details of a certain organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    """
    User API tokens can list and create Organizations, but reading, updating, or deleting an Organization requires a Global API key and your registered email address. The `cloudflare_organization` Terraform resource therefore requires a Global API key for its full lifecycle.

    See [Organizations authentication limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/#api-authentication) for credential compatibility by operation. Each endpoint’s **Security** section lists its supported authentication methods, with **Accepted Permissions** where applicable.
    """

    @cached_property
    def organization_profile(self) -> AsyncOrganizationProfileResource:
        return AsyncOrganizationProfileResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent: organization_create_params.Parent | Omit = omit,
        profile: organization_create_params.Profile | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """Create a new organization for a user.

        Sub-organization creation availability
        depends on the organization's capabilities. The optional `profile` object
        accepts partial profile details; its individual fields are not required.
        Organization names are limited to 65 UTF-8 bytes. Each profile field is limited
        to 1,000 UTF-8 bytes, and a non-empty business email must be valid. At least one
        of business name, address, phone, or email must be non-empty to persist a
        profile.

        Args:
          name: The Organization name, limited to 65 UTF-8 bytes.

          profile: Optional profile fields, each limited to 1,000 UTF-8 bytes. An empty profile is
              ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organizations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                    "profile": profile,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )

    async def update(
        self,
        organization_id: str,
        *,
        name: str | Omit = omit,
        parent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """Update an organization's name.

        Supplying `parent_id` verifies the current
        parent; this endpoint cannot move an organization. Organization names are
        limited to 65 UTF-8 bytes.

        Args:
          name: The Organization's display name, limited to 65 UTF-8 bytes. An omitted, empty,
              or unchanged value is a no-op.

          parent_id: The current parent Organization ID. A different value is rejected; this endpoint
              cannot move an Organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._put(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        containing: organization_list_params.Containing | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        member: organization_list_params.Member | Omit = omit,
        name: organization_list_params.Name | Omit = omit,
        order_by: Literal["name"] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        parent: organization_list_params.Parent | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Organization, AsyncSinglePage[Organization]]:
        """Retrieve a list of organizations a particular user has access to.

        At most one of
        `containing.account`, `containing.user`, or `containing.organization` may be
        provided.

        Args:
          id: Only return organizations with the specified IDs (ex. id=foo&id=bar). Send
              multiple elements by repeating the query value.

          direction: Sort direction for the `order_by` field. Defaults to `asc` when `order_by` is
              specified.

          order_by: Field to order results by. Currently supported values: `name`. When not
              specified, results are ordered by hierarchy.

          page_size: The amount of items to return. Defaults to 10.

          page_token: An opaque token returned from the last list response that when provided will
              retrieve the next page.

              Parameters used to filter the retrieved list must remain in subsequent requests
              with a page token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organizations",
            page=AsyncSinglePage[Organization],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "containing": containing,
                        "direction": direction,
                        "member": member,
                        "name": name,
                        "order_by": order_by,
                        "page_size": page_size,
                        "page_token": page_token,
                        "parent": parent,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=Organization,
        )

    async def delete(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDeleteResponse:
        """Delete an organization.

        It must not contain active sub-organizations or
        accounts. A root organization must also have no active managed users.
        Sub-organization deletion availability depends on the organization's
        capabilities.

        **Access Control:** Root deletion is restricted to enterprise organizations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._delete(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OrganizationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OrganizationDeleteResponse], ResultWrapper[OrganizationDeleteResponse]),
        )

    async def get(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Retrieve the details of a certain organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            path_template("/organizations/{organization_id}", organization_id=organization_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Organization]._unwrapper,
            ),
            cast_to=cast(Type[Organization], ResultWrapper[Organization]),
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )
        self.get = to_raw_response_wrapper(
            organizations.get,
        )

    @cached_property
    def organization_profile(self) -> OrganizationProfileResourceWithRawResponse:
        return OrganizationProfileResourceWithRawResponse(self._organizations.organization_profile)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._organizations.logs)

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organizations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            organizations.get,
        )

    @cached_property
    def organization_profile(self) -> AsyncOrganizationProfileResourceWithRawResponse:
        return AsyncOrganizationProfileResourceWithRawResponse(self._organizations.organization_profile)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._organizations.logs)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._organizations.billing)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = to_streamed_response_wrapper(
            organizations.delete,
        )
        self.get = to_streamed_response_wrapper(
            organizations.get,
        )

    @cached_property
    def organization_profile(self) -> OrganizationProfileResourceWithStreamingResponse:
        return OrganizationProfileResourceWithStreamingResponse(self._organizations.organization_profile)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._organizations.logs)

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._organizations.billing)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organizations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            organizations.get,
        )

    @cached_property
    def organization_profile(self) -> AsyncOrganizationProfileResourceWithStreamingResponse:
        return AsyncOrganizationProfileResourceWithStreamingResponse(self._organizations.organization_profile)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._organizations.logs)

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._organizations.billing)
