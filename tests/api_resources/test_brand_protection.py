# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.brand_protection import BrandProtectionSubmitResponse, BrandProtectionURLInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrandProtection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit(self, client: Cloudflare) -> None:
        brand_protection = client.brand_protection.submit(
            account_id="x",
        )
        assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Cloudflare) -> None:
        response = client.brand_protection.with_raw_response.submit(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_protection = response.parse()
        assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Cloudflare) -> None:
        with client.brand_protection.with_streaming_response.submit(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_protection = response.parse()
            assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.with_raw_response.submit(
                account_id="",
            )

    @parametrize
    def test_method_url_info(self, client: Cloudflare) -> None:
        brand_protection = client.brand_protection.url_info(
            account_id="x",
        )
        assert_matches_type(SyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

    @parametrize
    def test_raw_response_url_info(self, client: Cloudflare) -> None:
        response = client.brand_protection.with_raw_response.url_info(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_protection = response.parse()
        assert_matches_type(SyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

    @parametrize
    def test_streaming_response_url_info(self, client: Cloudflare) -> None:
        with client.brand_protection.with_streaming_response.url_info(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_protection = response.parse()
            assert_matches_type(SyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_url_info(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.with_raw_response.url_info(
                account_id="",
            )


class TestAsyncBrandProtection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_submit(self, async_client: AsyncCloudflare) -> None:
        brand_protection = await async_client.brand_protection.submit(
            account_id="x",
        )
        assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.with_raw_response.submit(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_protection = await response.parse()
        assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.with_streaming_response.submit(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_protection = await response.parse()
            assert_matches_type(BrandProtectionSubmitResponse, brand_protection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.with_raw_response.submit(
                account_id="",
            )

    @parametrize
    async def test_method_url_info(self, async_client: AsyncCloudflare) -> None:
        brand_protection = await async_client.brand_protection.url_info(
            account_id="x",
        )
        assert_matches_type(AsyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

    @parametrize
    async def test_raw_response_url_info(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.with_raw_response.url_info(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_protection = await response.parse()
        assert_matches_type(AsyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

    @parametrize
    async def test_streaming_response_url_info(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.with_streaming_response.url_info(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_protection = await response.parse()
            assert_matches_type(AsyncSinglePage[BrandProtectionURLInfoResponse], brand_protection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_url_info(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.with_raw_response.url_info(
                account_id="",
            )
