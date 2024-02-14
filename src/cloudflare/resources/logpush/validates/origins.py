# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.logpush.validates import (
    OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse,
    origin_post_accounts_account_identifier_logpush_validate_origin_params,
)

__all__ = ["Origins", "AsyncOrigins"]


class Origins(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginsWithRawResponse:
        return OriginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginsWithStreamingResponse:
        return OriginsWithStreamingResponse(self)

    def post_accounts_account_identifier_logpush_validate_origin(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        logpull_options: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse]:
        """
        Validates logpull origin with logpull_options.

        Args:
          account_or_zone_id: Identifier

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/validate/origin",
            body=maybe_transform(
                {"logpull_options": logpull_options},
                origin_post_accounts_account_identifier_logpush_validate_origin_params.OriginPostAccountsAccountIdentifierLogpushValidateOriginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse]],
                ResultWrapper[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse],
            ),
        )


class AsyncOrigins(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginsWithRawResponse:
        return AsyncOriginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginsWithStreamingResponse:
        return AsyncOriginsWithStreamingResponse(self)

    async def post_accounts_account_identifier_logpush_validate_origin(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        logpull_options: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse]:
        """
        Validates logpull origin with logpull_options.

        Args:
          account_or_zone_id: Identifier

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/validate/origin",
            body=maybe_transform(
                {"logpull_options": logpull_options},
                origin_post_accounts_account_identifier_logpush_validate_origin_params.OriginPostAccountsAccountIdentifierLogpushValidateOriginParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse]],
                ResultWrapper[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse],
            ),
        )


class OriginsWithRawResponse:
    def __init__(self, origins: Origins) -> None:
        self._origins = origins

        self.post_accounts_account_identifier_logpush_validate_origin = to_raw_response_wrapper(
            origins.post_accounts_account_identifier_logpush_validate_origin,
        )


class AsyncOriginsWithRawResponse:
    def __init__(self, origins: AsyncOrigins) -> None:
        self._origins = origins

        self.post_accounts_account_identifier_logpush_validate_origin = async_to_raw_response_wrapper(
            origins.post_accounts_account_identifier_logpush_validate_origin,
        )


class OriginsWithStreamingResponse:
    def __init__(self, origins: Origins) -> None:
        self._origins = origins

        self.post_accounts_account_identifier_logpush_validate_origin = to_streamed_response_wrapper(
            origins.post_accounts_account_identifier_logpush_validate_origin,
        )


class AsyncOriginsWithStreamingResponse:
    def __init__(self, origins: AsyncOrigins) -> None:
        self._origins = origins

        self.post_accounts_account_identifier_logpush_validate_origin = async_to_streamed_response_wrapper(
            origins.post_accounts_account_identifier_logpush_validate_origin,
        )
