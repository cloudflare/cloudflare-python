# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..._base_client import make_request_options
from .organization_profile import (
    OrganizationProfileResource,
    AsyncOrganizationProfileResource,
    OrganizationProfileResourceWithRawResponse,
    AsyncOrganizationProfileResourceWithRawResponse,
    OrganizationProfileResourceWithStreamingResponse,
    AsyncOrganizationProfileResourceWithStreamingResponse,
)
from ...types.organizations import organization_create_params, organization_update_params
from ...types.organizations.organization import Organization

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def organization_profile(self) -> OrganizationProfileResource:
        return OrganizationProfileResource(self._client)

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
        """
        Create a new organization for a user.

        Args:
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
        name: str,
        parent: organization_update_params.Parent | Omit = omit,
        profile: organization_update_params.Profile | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Modify organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._put(
            f"/organizations/{organization_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                    "profile": profile,
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
    ) -> None:
        """Delete an organization.

        The organization MUST be empty before deleting. It must
        not contain any sub-organizations, accounts, members or users.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            f"/organizations/{organization_id}",
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
    @cached_property
    def organization_profile(self) -> AsyncOrganizationProfileResource:
        return AsyncOrganizationProfileResource(self._client)

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
        """
        Create a new organization for a user.

        Args:
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
        name: str,
        parent: organization_update_params.Parent | Omit = omit,
        profile: organization_update_params.Profile | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organization:
        """
        Modify organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._put(
            f"/organizations/{organization_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent": parent,
                    "profile": profile,
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
    ) -> None:
        """Delete an organization.

        The organization MUST be empty before deleting. It must
        not contain any sub-organizations, accounts, members or users.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
            f"/organizations/{organization_id}",
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
        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )
        self.get = to_raw_response_wrapper(
            organizations.get,
        )

    @cached_property
    def organization_profile(self) -> OrganizationProfileResourceWithRawResponse:
        return OrganizationProfileResourceWithRawResponse(self._organizations.organization_profile)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
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


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
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


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
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
