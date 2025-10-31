# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.iam import sso_create_params, sso_update_params
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.iam.sso_get_response import SSOGetResponse
from ...types.iam.sso_list_response import SSOListResponse
from ...types.iam.sso_create_response import SSOCreateResponse
from ...types.iam.sso_delete_response import SSODeleteResponse
from ...types.iam.sso_update_response import SSOUpdateResponse
from ...types.iam.sso_begin_verification_response import SSOBeginVerificationResponse

__all__ = ["SSOResource", "AsyncSSOResource"]


class SSOResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSOResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SSOResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSOResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SSOResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        email_domain: str,
        begin_verification: bool | Omit = omit,
        use_fedramp_language: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOCreateResponse]:
        """
        Initialize new SSO connector

        Args:
          account_id: Account identifier tag.

          email_domain: Email domain of the new SSO connector

          begin_verification: Begin the verification process after creation

          use_fedramp_language: Controls the display of FedRAMP language to the user during SSO login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/sso_connectors",
            body=maybe_transform(
                {
                    "email_domain": email_domain,
                    "begin_verification": begin_verification,
                    "use_fedramp_language": use_fedramp_language,
                },
                sso_create_params.SSOCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOCreateResponse]], ResultWrapper[SSOCreateResponse]),
        )

    def update(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        enabled: bool | Omit = omit,
        use_fedramp_language: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOUpdateResponse]:
        """
        Update SSO connector state

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          enabled: SSO Connector enabled state

          use_fedramp_language: Controls the display of FedRAMP language to the user during SSO login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return self._patch(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "use_fedramp_language": use_fedramp_language,
                },
                sso_update_params.SSOUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOUpdateResponse]], ResultWrapper[SSOUpdateResponse]),
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
    ) -> SyncSinglePage[SSOListResponse]:
        """
        Get all SSO connectors

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/sso_connectors",
            page=SyncSinglePage[SSOListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SSOListResponse,
        )

    def delete(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSODeleteResponse]:
        """
        Delete SSO connector

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return self._delete(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSODeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSODeleteResponse]], ResultWrapper[SSODeleteResponse]),
        )

    def begin_verification(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOBeginVerificationResponse:
        """
        Begin SSO connector verification

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return self._post(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOBeginVerificationResponse,
        )

    def get(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOGetResponse]:
        """
        Get single SSO connector

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return self._get(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOGetResponse]], ResultWrapper[SSOGetResponse]),
        )


class AsyncSSOResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSOResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSOResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSOResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSSOResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        email_domain: str,
        begin_verification: bool | Omit = omit,
        use_fedramp_language: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOCreateResponse]:
        """
        Initialize new SSO connector

        Args:
          account_id: Account identifier tag.

          email_domain: Email domain of the new SSO connector

          begin_verification: Begin the verification process after creation

          use_fedramp_language: Controls the display of FedRAMP language to the user during SSO login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/sso_connectors",
            body=await async_maybe_transform(
                {
                    "email_domain": email_domain,
                    "begin_verification": begin_verification,
                    "use_fedramp_language": use_fedramp_language,
                },
                sso_create_params.SSOCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOCreateResponse]], ResultWrapper[SSOCreateResponse]),
        )

    async def update(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        enabled: bool | Omit = omit,
        use_fedramp_language: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOUpdateResponse]:
        """
        Update SSO connector state

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          enabled: SSO Connector enabled state

          use_fedramp_language: Controls the display of FedRAMP language to the user during SSO login

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "use_fedramp_language": use_fedramp_language,
                },
                sso_update_params.SSOUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOUpdateResponse]], ResultWrapper[SSOUpdateResponse]),
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
    ) -> AsyncPaginator[SSOListResponse, AsyncSinglePage[SSOListResponse]]:
        """
        Get all SSO connectors

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/sso_connectors",
            page=AsyncSinglePage[SSOListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SSOListResponse,
        )

    async def delete(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSODeleteResponse]:
        """
        Delete SSO connector

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSODeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSODeleteResponse]], ResultWrapper[SSODeleteResponse]),
        )

    async def begin_verification(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSOBeginVerificationResponse:
        """
        Begin SSO connector verification

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return await self._post(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOBeginVerificationResponse,
        )

    async def get(
        self,
        sso_connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SSOGetResponse]:
        """
        Get single SSO connector

        Args:
          account_id: Account identifier tag.

          sso_connector_id: SSO Connector identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sso_connector_id:
            raise ValueError(f"Expected a non-empty value for `sso_connector_id` but received {sso_connector_id!r}")
        return await self._get(
            f"/accounts/{account_id}/sso_connectors/{sso_connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSOGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSOGetResponse]], ResultWrapper[SSOGetResponse]),
        )


class SSOResourceWithRawResponse:
    def __init__(self, sso: SSOResource) -> None:
        self._sso = sso

        self.create = to_raw_response_wrapper(
            sso.create,
        )
        self.update = to_raw_response_wrapper(
            sso.update,
        )
        self.list = to_raw_response_wrapper(
            sso.list,
        )
        self.delete = to_raw_response_wrapper(
            sso.delete,
        )
        self.begin_verification = to_raw_response_wrapper(
            sso.begin_verification,
        )
        self.get = to_raw_response_wrapper(
            sso.get,
        )


class AsyncSSOResourceWithRawResponse:
    def __init__(self, sso: AsyncSSOResource) -> None:
        self._sso = sso

        self.create = async_to_raw_response_wrapper(
            sso.create,
        )
        self.update = async_to_raw_response_wrapper(
            sso.update,
        )
        self.list = async_to_raw_response_wrapper(
            sso.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sso.delete,
        )
        self.begin_verification = async_to_raw_response_wrapper(
            sso.begin_verification,
        )
        self.get = async_to_raw_response_wrapper(
            sso.get,
        )


class SSOResourceWithStreamingResponse:
    def __init__(self, sso: SSOResource) -> None:
        self._sso = sso

        self.create = to_streamed_response_wrapper(
            sso.create,
        )
        self.update = to_streamed_response_wrapper(
            sso.update,
        )
        self.list = to_streamed_response_wrapper(
            sso.list,
        )
        self.delete = to_streamed_response_wrapper(
            sso.delete,
        )
        self.begin_verification = to_streamed_response_wrapper(
            sso.begin_verification,
        )
        self.get = to_streamed_response_wrapper(
            sso.get,
        )


class AsyncSSOResourceWithStreamingResponse:
    def __init__(self, sso: AsyncSSOResource) -> None:
        self._sso = sso

        self.create = async_to_streamed_response_wrapper(
            sso.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sso.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sso.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sso.delete,
        )
        self.begin_verification = async_to_streamed_response_wrapper(
            sso.begin_verification,
        )
        self.get = async_to_streamed_response_wrapper(
            sso.get,
        )
