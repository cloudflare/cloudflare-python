# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.brand_protection.v2 import (
    LogoGetResponse,
    LogoCreateResponse,
    LogoDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        logo = client.brand_protection.v2.logos.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        )
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        logo = client.brand_protection.v2.logos.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
            search_lookback=True,
        )
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.brand_protection.v2.logos.with_raw_response.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.brand_protection.v2.logos.with_streaming_response.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert_matches_type(LogoCreateResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.v2.logos.with_raw_response.create(
                account_id="",
                image_data="x",
                similarity_threshold=0,
                tag="x",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        logo = client.brand_protection.v2.logos.delete(
            query_id="x",
            account_id="x",
        )
        assert_matches_type(LogoDeleteResponse, logo, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.brand_protection.v2.logos.with_raw_response.delete(
            query_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert_matches_type(LogoDeleteResponse, logo, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.brand_protection.v2.logos.with_streaming_response.delete(
            query_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert_matches_type(LogoDeleteResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.v2.logos.with_raw_response.delete(
                query_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            client.brand_protection.v2.logos.with_raw_response.delete(
                query_id="",
                account_id="x",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        logo = client.brand_protection.v2.logos.get(
            account_id="x",
        )
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        logo = client.brand_protection.v2.logos.get(
            account_id="x",
            id="id",
            download="download",
        )
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.brand_protection.v2.logos.with_raw_response.get(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = response.parse()
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.brand_protection.v2.logos.with_streaming_response.get(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = response.parse()
            assert_matches_type(LogoGetResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.v2.logos.with_raw_response.get(
                account_id="",
            )


class TestAsyncLogos:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        logo = await async_client.brand_protection.v2.logos.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        )
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        logo = await async_client.brand_protection.v2.logos.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
            search_lookback=True,
        )
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.v2.logos.with_raw_response.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert_matches_type(LogoCreateResponse, logo, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.v2.logos.with_streaming_response.create(
            account_id="x",
            image_data="x",
            similarity_threshold=0,
            tag="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert_matches_type(LogoCreateResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.v2.logos.with_raw_response.create(
                account_id="",
                image_data="x",
                similarity_threshold=0,
                tag="x",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        logo = await async_client.brand_protection.v2.logos.delete(
            query_id="x",
            account_id="x",
        )
        assert_matches_type(LogoDeleteResponse, logo, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.v2.logos.with_raw_response.delete(
            query_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert_matches_type(LogoDeleteResponse, logo, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.v2.logos.with_streaming_response.delete(
            query_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert_matches_type(LogoDeleteResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.v2.logos.with_raw_response.delete(
                query_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `query_id` but received ''"):
            await async_client.brand_protection.v2.logos.with_raw_response.delete(
                query_id="",
                account_id="x",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        logo = await async_client.brand_protection.v2.logos.get(
            account_id="x",
        )
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        logo = await async_client.brand_protection.v2.logos.get(
            account_id="x",
            id="id",
            download="download",
        )
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.v2.logos.with_raw_response.get(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        logo = await response.parse()
        assert_matches_type(LogoGetResponse, logo, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.v2.logos.with_streaming_response.get(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            logo = await response.parse()
            assert_matches_type(LogoGetResponse, logo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.v2.logos.with_raw_response.get(
                account_id="",
            )
