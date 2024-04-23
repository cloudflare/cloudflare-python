# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Mapping, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
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
from ...._base_client import (
    make_request_options,
)
from ....types.workers.scripts import version_create_params
from ....types.workers.scripts.version_get_response import VersionGetResponse
from ....types.workers.scripts.version_list_response import VersionListResponse
from ....types.workers.scripts.version_create_response import VersionCreateResponse

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self)

    def create(
        self,
        script_name: str,
        *,
        account_id: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: version_create_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionCreateResponse]:
        """
        Upload a Worker Version without deploying to Cloudflare's network.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module`.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions",
            body=maybe_transform(body, version_create_params.VersionCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionCreateResponse]], ResultWrapper[VersionCreateResponse]),
        )

    def list(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionListResponse]:
        """List of Worker Versions.

        The first version in the list is the latest version.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionListResponse]], ResultWrapper[VersionListResponse]),
        )

    def get(
        self,
        version_id: str,
        *,
        account_id: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionGetResponse]:
        """
        Get Version Detail

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionGetResponse]], ResultWrapper[VersionGetResponse]),
        )


class AsyncVersions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self)

    async def create(
        self,
        script_name: str,
        *,
        account_id: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: version_create_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionCreateResponse]:
        """
        Upload a Worker Version without deploying to Cloudflare's network.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module`.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions",
            body=await async_maybe_transform(body, version_create_params.VersionCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionCreateResponse]], ResultWrapper[VersionCreateResponse]),
        )

    async def list(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionListResponse]:
        """List of Worker Versions.

        The first version in the list is the latest version.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionListResponse]], ResultWrapper[VersionListResponse]),
        )

    async def get(
        self,
        version_id: str,
        *,
        account_id: str,
        script_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VersionGetResponse]:
        """
        Get Version Detail

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[VersionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[VersionGetResponse]], ResultWrapper[VersionGetResponse]),
        )


class VersionsWithRawResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.get = to_raw_response_wrapper(
            versions.get,
        )


class AsyncVersionsWithRawResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.get = async_to_raw_response_wrapper(
            versions.get,
        )


class VersionsWithStreamingResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.get = to_streamed_response_wrapper(
            versions.get,
        )


class AsyncVersionsWithStreamingResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            versions.get,
        )
