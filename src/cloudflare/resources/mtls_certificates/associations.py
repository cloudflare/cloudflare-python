# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.mtls_certificates import AssociationListResponse

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Associations", "AsyncAssociations"]


class Associations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssociationsWithRawResponse:
        return AssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssociationsWithStreamingResponse:
        return AssociationsWithStreamingResponse(self)

    def list(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssociationListResponse]:
        """
        Lists all active associations between the certificate and Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssociationListResponse]], ResultWrapper[AssociationListResponse]),
        )


class AsyncAssociations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssociationsWithRawResponse:
        return AsyncAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssociationsWithStreamingResponse:
        return AsyncAssociationsWithStreamingResponse(self)

    async def list(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AssociationListResponse]:
        """
        Lists all active associations between the certificate and Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AssociationListResponse]], ResultWrapper[AssociationListResponse]),
        )


class AssociationsWithRawResponse:
    def __init__(self, associations: Associations) -> None:
        self._associations = associations

        self.list = to_raw_response_wrapper(
            associations.list,
        )


class AsyncAssociationsWithRawResponse:
    def __init__(self, associations: AsyncAssociations) -> None:
        self._associations = associations

        self.list = async_to_raw_response_wrapper(
            associations.list,
        )


class AssociationsWithStreamingResponse:
    def __init__(self, associations: Associations) -> None:
        self._associations = associations

        self.list = to_streamed_response_wrapper(
            associations.list,
        )


class AsyncAssociationsWithStreamingResponse:
    def __init__(self, associations: AsyncAssociations) -> None:
        self._associations = associations

        self.list = async_to_streamed_response_wrapper(
            associations.list,
        )
