# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.magics.ipsec_tunnels import PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["PskGenerates", "AsyncPskGenerates"]


class PskGenerates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PskGeneratesWithRawResponse:
        return PskGeneratesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PskGeneratesWithStreamingResponse:
        return PskGeneratesWithStreamingResponse(self)

    def magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse],
                ResultWrapper[PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse],
            ),
        )


class AsyncPskGenerates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPskGeneratesWithRawResponse:
        return AsyncPskGeneratesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPskGeneratesWithStreamingResponse:
        return AsyncPskGeneratesWithStreamingResponse(self)

    async def magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse:
        """
        Generates a Pre Shared Key for a specific IPsec tunnel used in the IKE session.
        Use `?validate_only=true` as an optional query parameter to only run validation
        without persisting changes. After a PSK is generated, the PSK is immediately
        persisted to Cloudflare's edge and cannot be retrieved later. Note the PSK in a
        safe place.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/ipsec_tunnels/{tunnel_identifier}/psk_generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse],
                ResultWrapper[PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse],
            ),
        )


class PskGeneratesWithRawResponse:
    def __init__(self, psk_generates: PskGenerates) -> None:
        self._psk_generates = psk_generates

        self.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels = to_raw_response_wrapper(
            psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels,
        )


class AsyncPskGeneratesWithRawResponse:
    def __init__(self, psk_generates: AsyncPskGenerates) -> None:
        self._psk_generates = psk_generates

        self.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels = async_to_raw_response_wrapper(
            psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels,
        )


class PskGeneratesWithStreamingResponse:
    def __init__(self, psk_generates: PskGenerates) -> None:
        self._psk_generates = psk_generates

        self.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels = to_streamed_response_wrapper(
            psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels,
        )


class AsyncPskGeneratesWithStreamingResponse:
    def __init__(self, psk_generates: AsyncPskGenerates) -> None:
        self._psk_generates = psk_generates

        self.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels = async_to_streamed_response_wrapper(
            psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels,
        )
