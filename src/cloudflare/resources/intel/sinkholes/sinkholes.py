# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from .ingresses import (
    IngressesResource,
    AsyncIngressesResource,
    IngressesResourceWithRawResponse,
    AsyncIngressesResourceWithRawResponse,
    IngressesResourceWithStreamingResponse,
    AsyncIngressesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ....types.intel import sinkhole_create_params, sinkhole_update_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.intel.sinkhole import Sinkhole

__all__ = ["SinkholesResource", "AsyncSinkholesResource"]


class SinkholesResource(SyncAPIResource):
    @cached_property
    def ingresses(self) -> IngressesResource:
        return IngressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SinkholesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SinkholesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SinkholesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        r2_bucket: str | Omit = omit,
        r2_id: str | Omit = omit,
        r2_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Sinkhole]:
        """Create a new sinkhole.

        Logs of large request bodies will be truncated, but the
        full request body can be recorded in R2. If you wish to record large request
        bodies in R2, include the R2 key ID, key secret, and bucket name in the request
        body.

        Args:
          account_id: An identifier for the resource.

          name: The name of the sinkhole.

          r2_bucket: The name of the R2 bucket to store results. Required if you want to store large
              request bodies in R2.

          r2_id: The id of the R2 instance. Required if you want to store large request bodies in
              R2.

          r2_secret: The secret key for the R2 API token. Required if you want to store large request
              bodies in R2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/intel/sinkholes", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "r2_bucket": r2_bucket,
                    "r2_id": r2_id,
                    "r2_secret": r2_secret,
                },
                sinkhole_create_params.SinkholeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Sinkhole]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Sinkhole]], ResultWrapper[Sinkhole]),
        )

    def update(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        name: str,
        r2_bucket: str | Omit = omit,
        r2_id: str | Omit = omit,
        r2_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Replaces the name or R2 configuration of the specified sinkhole.

        This is a full
        replacement. All fields, including r2_secret, must be re-supplied. Omitting
        r2_secret overwrites the stored value with an empty string.

        Args:
          account_id: An identifier for the resource.

          name: The name of the sinkhole.

          r2_bucket: The name of the R2 bucket to store results. Required if you want to store large
              request bodies in R2.

          r2_id: The id of the R2 instance. Required if you want to store large request bodies in
              R2.

          r2_secret: The secret key for the R2 API token. Required if you want to store large request
              bodies in R2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "r2_bucket": r2_bucket,
                    "r2_id": r2_id,
                    "r2_secret": r2_secret,
                },
                sinkhole_update_params.SinkholeUpdateParams,
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
    ) -> SyncSinglePage[Sinkhole]:
        """
        Lists sinkholes owned by the account for redirecting malicious traffic.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/intel/sinkholes", account_id=account_id),
            page=SyncSinglePage[Sinkhole],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Sinkhole,
        )

    def delete(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete the specified sinkhole.

        The sinkhole must not have any active ingress
        rules defined. A 409 response code indicates that this condition is not met.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
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

    def get(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Sinkhole]:
        """
        Get the specified sinkhole by its unique identifier.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Sinkhole]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Sinkhole]], ResultWrapper[Sinkhole]),
        )


class AsyncSinkholesResource(AsyncAPIResource):
    @cached_property
    def ingresses(self) -> AsyncIngressesResource:
        return AsyncIngressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSinkholesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSinkholesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSinkholesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        r2_bucket: str | Omit = omit,
        r2_id: str | Omit = omit,
        r2_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Sinkhole]:
        """Create a new sinkhole.

        Logs of large request bodies will be truncated, but the
        full request body can be recorded in R2. If you wish to record large request
        bodies in R2, include the R2 key ID, key secret, and bucket name in the request
        body.

        Args:
          account_id: An identifier for the resource.

          name: The name of the sinkhole.

          r2_bucket: The name of the R2 bucket to store results. Required if you want to store large
              request bodies in R2.

          r2_id: The id of the R2 instance. Required if you want to store large request bodies in
              R2.

          r2_secret: The secret key for the R2 API token. Required if you want to store large request
              bodies in R2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/intel/sinkholes", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "r2_bucket": r2_bucket,
                    "r2_id": r2_id,
                    "r2_secret": r2_secret,
                },
                sinkhole_create_params.SinkholeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Sinkhole]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Sinkhole]], ResultWrapper[Sinkhole]),
        )

    async def update(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        name: str,
        r2_bucket: str | Omit = omit,
        r2_id: str | Omit = omit,
        r2_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Replaces the name or R2 configuration of the specified sinkhole.

        This is a full
        replacement. All fields, including r2_secret, must be re-supplied. Omitting
        r2_secret overwrites the stored value with an empty string.

        Args:
          account_id: An identifier for the resource.

          name: The name of the sinkhole.

          r2_bucket: The name of the R2 bucket to store results. Required if you want to store large
              request bodies in R2.

          r2_id: The id of the R2 instance. Required if you want to store large request bodies in
              R2.

          r2_secret: The secret key for the R2 API token. Required if you want to store large request
              bodies in R2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "r2_bucket": r2_bucket,
                    "r2_id": r2_id,
                    "r2_secret": r2_secret,
                },
                sinkhole_update_params.SinkholeUpdateParams,
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
    ) -> AsyncPaginator[Sinkhole, AsyncSinglePage[Sinkhole]]:
        """
        Lists sinkholes owned by the account for redirecting malicious traffic.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/intel/sinkholes", account_id=account_id),
            page=AsyncSinglePage[Sinkhole],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Sinkhole,
        )

    async def delete(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete the specified sinkhole.

        The sinkhole must not have any active ingress
        rules defined. A 409 response code indicates that this condition is not met.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
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

    async def get(
        self,
        sinkhole_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Sinkhole]:
        """
        Get the specified sinkhole by its unique identifier.

        Args:
          account_id: An identifier for the resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/intel/sinkholes/{sinkhole_id}", account_id=account_id, sinkhole_id=sinkhole_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Sinkhole]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Sinkhole]], ResultWrapper[Sinkhole]),
        )


class SinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.create = to_raw_response_wrapper(
            sinkholes.create,
        )
        self.update = to_raw_response_wrapper(
            sinkholes.update,
        )
        self.list = to_raw_response_wrapper(
            sinkholes.list,
        )
        self.delete = to_raw_response_wrapper(
            sinkholes.delete,
        )
        self.get = to_raw_response_wrapper(
            sinkholes.get,
        )

    @cached_property
    def ingresses(self) -> IngressesResourceWithRawResponse:
        return IngressesResourceWithRawResponse(self._sinkholes.ingresses)


class AsyncSinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.create = async_to_raw_response_wrapper(
            sinkholes.create,
        )
        self.update = async_to_raw_response_wrapper(
            sinkholes.update,
        )
        self.list = async_to_raw_response_wrapper(
            sinkholes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sinkholes.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sinkholes.get,
        )

    @cached_property
    def ingresses(self) -> AsyncIngressesResourceWithRawResponse:
        return AsyncIngressesResourceWithRawResponse(self._sinkholes.ingresses)


class SinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.create = to_streamed_response_wrapper(
            sinkholes.create,
        )
        self.update = to_streamed_response_wrapper(
            sinkholes.update,
        )
        self.list = to_streamed_response_wrapper(
            sinkholes.list,
        )
        self.delete = to_streamed_response_wrapper(
            sinkholes.delete,
        )
        self.get = to_streamed_response_wrapper(
            sinkholes.get,
        )

    @cached_property
    def ingresses(self) -> IngressesResourceWithStreamingResponse:
        return IngressesResourceWithStreamingResponse(self._sinkholes.ingresses)


class AsyncSinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.create = async_to_streamed_response_wrapper(
            sinkholes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sinkholes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sinkholes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sinkholes.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sinkholes.get,
        )

    @cached_property
    def ingresses(self) -> AsyncIngressesResourceWithStreamingResponse:
        return AsyncIngressesResourceWithStreamingResponse(self._sinkholes.ingresses)
