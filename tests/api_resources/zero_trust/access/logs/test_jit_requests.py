# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access.logs import (
    JitRequestGetResponse,
    JitRequestListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJitRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        jit_request = client.zero_trust.access.logs.jit_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        jit_request = client.zero_trust.access.logs.jit_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=1000,
            search="search",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="PENDING",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.logs.jit_requests.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jit_request = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.logs.jit_requests.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jit_request = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.logs.jit_requests.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        jit_request = client.zero_trust.access.logs.jit_requests.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.logs.jit_requests.with_raw_response.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jit_request = response.parse()
        assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.logs.jit_requests.with_streaming_response.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jit_request = response.parse()
            assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.logs.jit_requests.with_raw_response.get(
                knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knock_request_id` but received ''"):
            client.zero_trust.access.logs.jit_requests.with_raw_response.get(
                knock_request_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncJitRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        jit_request = await async_client.zero_trust.access.logs.jit_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        jit_request = await async_client.zero_trust.access.logs.jit_requests.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=1000,
            search="search",
            since=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="PENDING",
            until=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.logs.jit_requests.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jit_request = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.logs.jit_requests.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jit_request = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[JitRequestListResponse], jit_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.logs.jit_requests.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        jit_request = await async_client.zero_trust.access.logs.jit_requests.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.logs.jit_requests.with_raw_response.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jit_request = await response.parse()
        assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.logs.jit_requests.with_streaming_response.get(
            knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jit_request = await response.parse()
            assert_matches_type(Optional[JitRequestGetResponse], jit_request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.logs.jit_requests.with_raw_response.get(
                knock_request_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knock_request_id` but received ''"):
            await async_client.zero_trust.access.logs.jit_requests.with_raw_response.get(
                knock_request_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
