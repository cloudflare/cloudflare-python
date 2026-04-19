# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2_data_catalog import (
    R2DataCatalogGetResponse,
    R2DataCatalogListResponse,
    R2DataCatalogEnableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestR2DataCatalog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        r2_data_catalog = client.r2_data_catalog.list(
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.with_raw_response.list(
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = response.parse()
        assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.with_streaming_response.list(
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = response.parse()
            assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_disable(self, client: Cloudflare) -> None:
        r2_data_catalog = client.r2_data_catalog.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert r2_data_catalog is None

    @parametrize
    def test_raw_response_disable(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.with_raw_response.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = response.parse()
        assert r2_data_catalog is None

    @parametrize
    def test_streaming_response_disable(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.with_streaming_response.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = response.parse()
            assert r2_data_catalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.with_raw_response.disable(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.with_raw_response.disable(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )

    @parametrize
    def test_method_enable(self, client: Cloudflare) -> None:
        r2_data_catalog = client.r2_data_catalog.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.with_raw_response.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = response.parse()
        assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.with_streaming_response.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = response.parse()
            assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.with_raw_response.enable(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.with_raw_response.enable(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        r2_data_catalog = client.r2_data_catalog.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.with_raw_response.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = response.parse()
        assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.with_streaming_response.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = response.parse()
            assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.with_raw_response.get(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.with_raw_response.get(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )


class TestAsyncR2DataCatalog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        r2_data_catalog = await async_client.r2_data_catalog.list(
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.with_raw_response.list(
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = await response.parse()
        assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.with_streaming_response.list(
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = await response.parse()
            assert_matches_type(Optional[R2DataCatalogListResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncCloudflare) -> None:
        r2_data_catalog = await async_client.r2_data_catalog.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert r2_data_catalog is None

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.with_raw_response.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = await response.parse()
        assert r2_data_catalog is None

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.with_streaming_response.disable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = await response.parse()
            assert r2_data_catalog is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.disable(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.disable(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncCloudflare) -> None:
        r2_data_catalog = await async_client.r2_data_catalog.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.with_raw_response.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = await response.parse()
        assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.with_streaming_response.enable(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = await response.parse()
            assert_matches_type(Optional[R2DataCatalogEnableResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.enable(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.enable(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        r2_data_catalog = await async_client.r2_data_catalog.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.with_raw_response.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        r2_data_catalog = await response.parse()
        assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.with_streaming_response.get(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            r2_data_catalog = await response.parse()
            assert_matches_type(Optional[R2DataCatalogGetResponse], r2_data_catalog, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.get(
                bucket_name="my-data-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.with_raw_response.get(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
            )
