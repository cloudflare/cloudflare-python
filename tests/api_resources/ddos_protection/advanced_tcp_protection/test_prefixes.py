# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ddos_protection.advanced_tcp_protection import (
    PrefixListResponse,
    PrefixCreateResponse,
    PrefixBulkCreateResponse,
    PrefixBulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        prefix = client.ddos_protection.advanced_tcp_protection.prefixes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        )
        assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.create(
                account_id="",
                comment="comment",
                excluded=True,
                prefix="192.0.2.0/24",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        prefix = client.ddos_protection.advanced_tcp_protection.prefixes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        prefix = client.ddos_protection.advanced_tcp_protection.prefixes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="direction",
            order="order",
            page=0,
            per_page=0,
        )
        assert_matches_type(SyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        prefix = client.ddos_protection.advanced_tcp_protection.prefixes.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        )
        assert_matches_type(SyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(SyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(SyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_create(
                account_id="",
                body=[
                    {
                        "comment": "comment",
                        "excluded": True,
                        "prefix": "192.0.2.0/24",
                    }
                ],
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        prefix = client.ddos_protection.advanced_tcp_protection.prefixes.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_delete(
                account_id="",
            )


class TestAsyncPrefixes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.ddos_protection.advanced_tcp_protection.prefixes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        )
        assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="comment",
            excluded=True,
            prefix="192.0.2.0/24",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[PrefixCreateResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.create(
                account_id="",
                comment="comment",
                excluded=True,
                prefix="192.0.2.0/24",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.ddos_protection.advanced_tcp_protection.prefixes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.ddos_protection.advanced_tcp_protection.prefixes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="direction",
            order="order",
            page=0,
            per_page=0,
        )
        assert_matches_type(AsyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[PrefixListResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.ddos_protection.advanced_tcp_protection.prefixes.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        )
        assert_matches_type(AsyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(AsyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.bulk_create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "comment": "comment",
                    "excluded": True,
                    "prefix": "192.0.2.0/24",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(AsyncSinglePage[PrefixBulkCreateResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_create(
                account_id="",
                body=[
                    {
                        "comment": "comment",
                        "excluded": True,
                        "prefix": "192.0.2.0/24",
                    }
                ],
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.ddos_protection.advanced_tcp_protection.prefixes.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ddos_protection.advanced_tcp_protection.prefixes.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(PrefixBulkDeleteResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ddos_protection.advanced_tcp_protection.prefixes.with_raw_response.bulk_delete(
                account_id="",
            )
