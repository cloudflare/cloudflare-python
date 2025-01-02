# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai import FinetuneListResponse, FinetuneCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinetunes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        finetune = client.ai.finetunes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        )
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        finetune = client.ai.finetunes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
            description="description",
            public=True,
        )
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai.finetunes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetune = response.parse()
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai.finetunes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetune = response.parse()
            assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.finetunes.with_raw_response.create(
                account_id="",
                model="model",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        finetune = client.ai.finetunes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FinetuneListResponse, finetune, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai.finetunes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetune = response.parse()
        assert_matches_type(FinetuneListResponse, finetune, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai.finetunes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetune = response.parse()
            assert_matches_type(FinetuneListResponse, finetune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.finetunes.with_raw_response.list(
                account_id="",
            )


class TestAsyncFinetunes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        finetune = await async_client.ai.finetunes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        )
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finetune = await async_client.ai.finetunes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
            description="description",
            public=True,
        )
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.finetunes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetune = await response.parse()
        assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.finetunes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            model="model",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetune = await response.parse()
            assert_matches_type(FinetuneCreateResponse, finetune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.finetunes.with_raw_response.create(
                account_id="",
                model="model",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        finetune = await async_client.ai.finetunes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FinetuneListResponse, finetune, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.finetunes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finetune = await response.parse()
        assert_matches_type(FinetuneListResponse, finetune, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.finetunes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finetune = await response.parse()
            assert_matches_type(FinetuneListResponse, finetune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.finetunes.with_raw_response.list(
                account_id="",
            )
