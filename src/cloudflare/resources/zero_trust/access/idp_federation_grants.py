# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.zero_trust.access import idp_federation_grant_create_params
from ....types.zero_trust.access.idp_federation_grant import IdPFederationGrant
from ....types.zero_trust.access.idp_federation_grant_list_response import IdPFederationGrantListResponse
from ....types.zero_trust.access.idp_federation_grant_delete_response import IdPFederationGrantDeleteResponse

__all__ = ["IdPFederationGrantsResource", "AsyncIdPFederationGrantsResource"]


class IdPFederationGrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdPFederationGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IdPFederationGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdPFederationGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IdPFederationGrantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        idp_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrant]:
        """
        Creates an IdP federation grant for the specified identity provider, making it
        available for federation to other accounts in the same Cloudflare organization.

        The account must belong to a Cloudflare organization. One-time pin and
        Cloudflare-managed identity providers cannot be federated. An identity provider
        may only have one active grant at a time.

        Args:
          account_id: Identifier.

          idp_id: UID of the identity provider to federate. Must be an existing identity provider
              in this account. One-time pin and Cloudflare-managed identity providers cannot
              be federated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/access/idp_federation_grants", account_id=account_id),
            body=maybe_transform({"idp_id": idp_id}, idp_federation_grant_create_params.IdPFederationGrantCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrant]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrant]], ResultWrapper[IdPFederationGrant]),
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
    ) -> Optional[IdPFederationGrantListResponse]:
        """
        Lists the IdP federation grants owned by the account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/access/idp_federation_grants", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrantListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrantListResponse]], ResultWrapper[IdPFederationGrantListResponse]),
        )

    def delete(
        self,
        grant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrantDeleteResponse]:
        """Deletes an IdP federation grant.

        The identity provider remains in the account,
        but it is no longer available for federation to other accounts.

        Args:
          account_id: Identifier.

          grant_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/access/idp_federation_grants/{grant_id}",
                account_id=account_id,
                grant_id=grant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrantDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IdPFederationGrantDeleteResponse]], ResultWrapper[IdPFederationGrantDeleteResponse]
            ),
        )

    def get(
        self,
        grant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrant]:
        """
        Retrieves a single IdP federation grant by its UID.

        Args:
          account_id: Identifier.

          grant_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/idp_federation_grants/{grant_id}",
                account_id=account_id,
                grant_id=grant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrant]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrant]], ResultWrapper[IdPFederationGrant]),
        )


class AsyncIdPFederationGrantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdPFederationGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdPFederationGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdPFederationGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIdPFederationGrantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        idp_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrant]:
        """
        Creates an IdP federation grant for the specified identity provider, making it
        available for federation to other accounts in the same Cloudflare organization.

        The account must belong to a Cloudflare organization. One-time pin and
        Cloudflare-managed identity providers cannot be federated. An identity provider
        may only have one active grant at a time.

        Args:
          account_id: Identifier.

          idp_id: UID of the identity provider to federate. Must be an existing identity provider
              in this account. One-time pin and Cloudflare-managed identity providers cannot
              be federated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/access/idp_federation_grants", account_id=account_id),
            body=await async_maybe_transform(
                {"idp_id": idp_id}, idp_federation_grant_create_params.IdPFederationGrantCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrant]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrant]], ResultWrapper[IdPFederationGrant]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrantListResponse]:
        """
        Lists the IdP federation grants owned by the account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/access/idp_federation_grants", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrantListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrantListResponse]], ResultWrapper[IdPFederationGrantListResponse]),
        )

    async def delete(
        self,
        grant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrantDeleteResponse]:
        """Deletes an IdP federation grant.

        The identity provider remains in the account,
        but it is no longer available for federation to other accounts.

        Args:
          account_id: Identifier.

          grant_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/access/idp_federation_grants/{grant_id}",
                account_id=account_id,
                grant_id=grant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrantDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IdPFederationGrantDeleteResponse]], ResultWrapper[IdPFederationGrantDeleteResponse]
            ),
        )

    async def get(
        self,
        grant_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IdPFederationGrant]:
        """
        Retrieves a single IdP federation grant by its UID.

        Args:
          account_id: Identifier.

          grant_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not grant_id:
            raise ValueError(f"Expected a non-empty value for `grant_id` but received {grant_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/idp_federation_grants/{grant_id}",
                account_id=account_id,
                grant_id=grant_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IdPFederationGrant]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IdPFederationGrant]], ResultWrapper[IdPFederationGrant]),
        )


class IdPFederationGrantsResourceWithRawResponse:
    def __init__(self, idp_federation_grants: IdPFederationGrantsResource) -> None:
        self._idp_federation_grants = idp_federation_grants

        self.create = to_raw_response_wrapper(
            idp_federation_grants.create,
        )
        self.list = to_raw_response_wrapper(
            idp_federation_grants.list,
        )
        self.delete = to_raw_response_wrapper(
            idp_federation_grants.delete,
        )
        self.get = to_raw_response_wrapper(
            idp_federation_grants.get,
        )


class AsyncIdPFederationGrantsResourceWithRawResponse:
    def __init__(self, idp_federation_grants: AsyncIdPFederationGrantsResource) -> None:
        self._idp_federation_grants = idp_federation_grants

        self.create = async_to_raw_response_wrapper(
            idp_federation_grants.create,
        )
        self.list = async_to_raw_response_wrapper(
            idp_federation_grants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            idp_federation_grants.delete,
        )
        self.get = async_to_raw_response_wrapper(
            idp_federation_grants.get,
        )


class IdPFederationGrantsResourceWithStreamingResponse:
    def __init__(self, idp_federation_grants: IdPFederationGrantsResource) -> None:
        self._idp_federation_grants = idp_federation_grants

        self.create = to_streamed_response_wrapper(
            idp_federation_grants.create,
        )
        self.list = to_streamed_response_wrapper(
            idp_federation_grants.list,
        )
        self.delete = to_streamed_response_wrapper(
            idp_federation_grants.delete,
        )
        self.get = to_streamed_response_wrapper(
            idp_federation_grants.get,
        )


class AsyncIdPFederationGrantsResourceWithStreamingResponse:
    def __init__(self, idp_federation_grants: AsyncIdPFederationGrantsResource) -> None:
        self._idp_federation_grants = idp_federation_grants

        self.create = async_to_streamed_response_wrapper(
            idp_federation_grants.create,
        )
        self.list = async_to_streamed_response_wrapper(
            idp_federation_grants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            idp_federation_grants.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            idp_federation_grants.get,
        )
