# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
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
from ...types.organizations import organization_profile_update_params
from ...types.organizations.organization_profile_get_params import Result

__all__ = ["OrganizationProfileResource", "AsyncOrganizationProfileResource"]


class OrganizationProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OrganizationProfileResourceWithStreamingResponse(self)

    def update(
        self,
        organization_id: str,
        *,
        business_address: str,
        business_email: str,
        business_name: str,
        business_phone: str,
        external_metadata: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Modify organization profile.

        (Currently in Closed Beta - see
        https://developers.cloudflare.com/fundamentals/organizations/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/organizations/{organization_id}/profile",
            body=maybe_transform(
                {
                    "business_address": business_address,
                    "business_email": business_email,
                    "business_name": business_name,
                    "business_phone": business_phone,
                    "external_metadata": external_metadata,
                },
                organization_profile_update_params.OrganizationProfileUpdateParams,
            ),
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
    ) -> Result:
        """Get an organizations profile if it exists.

        (Currently in Closed Beta - see
        https://developers.cloudflare.com/fundamentals/organizations/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/organizations/{organization_id}/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Result]._unwrapper,
            ),
            cast_to=cast(Type[Result], ResultWrapper[Result]),
        )


class AsyncOrganizationProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOrganizationProfileResourceWithStreamingResponse(self)

    async def update(
        self,
        organization_id: str,
        *,
        business_address: str,
        business_email: str,
        business_name: str,
        business_phone: str,
        external_metadata: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Modify organization profile.

        (Currently in Closed Beta - see
        https://developers.cloudflare.com/fundamentals/organizations/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/organizations/{organization_id}/profile",
            body=await async_maybe_transform(
                {
                    "business_address": business_address,
                    "business_email": business_email,
                    "business_name": business_name,
                    "business_phone": business_phone,
                    "external_metadata": external_metadata,
                },
                organization_profile_update_params.OrganizationProfileUpdateParams,
            ),
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
    ) -> Result:
        """Get an organizations profile if it exists.

        (Currently in Closed Beta - see
        https://developers.cloudflare.com/fundamentals/organizations/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/organizations/{organization_id}/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Result]._unwrapper,
            ),
            cast_to=cast(Type[Result], ResultWrapper[Result]),
        )


class OrganizationProfileResourceWithRawResponse:
    def __init__(self, organization_profile: OrganizationProfileResource) -> None:
        self._organization_profile = organization_profile

        self.update = to_raw_response_wrapper(
            organization_profile.update,
        )
        self.get = to_raw_response_wrapper(
            organization_profile.get,
        )


class AsyncOrganizationProfileResourceWithRawResponse:
    def __init__(self, organization_profile: AsyncOrganizationProfileResource) -> None:
        self._organization_profile = organization_profile

        self.update = async_to_raw_response_wrapper(
            organization_profile.update,
        )
        self.get = async_to_raw_response_wrapper(
            organization_profile.get,
        )


class OrganizationProfileResourceWithStreamingResponse:
    def __init__(self, organization_profile: OrganizationProfileResource) -> None:
        self._organization_profile = organization_profile

        self.update = to_streamed_response_wrapper(
            organization_profile.update,
        )
        self.get = to_streamed_response_wrapper(
            organization_profile.get,
        )


class AsyncOrganizationProfileResourceWithStreamingResponse:
    def __init__(self, organization_profile: AsyncOrganizationProfileResource) -> None:
        self._organization_profile = organization_profile

        self.update = async_to_streamed_response_wrapper(
            organization_profile.update,
        )
        self.get = async_to_streamed_response_wrapper(
            organization_profile.get,
        )
