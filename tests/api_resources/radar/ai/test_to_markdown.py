# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.radar.ai import ToMarkdownCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToMarkdown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        to_markdown = client.radar.ai.to_markdown.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        to_markdown = client.radar.ai.to_markdown.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(SyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.radar.ai.to_markdown.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        to_markdown = response.parse()
        assert_matches_type(SyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.radar.ai.to_markdown.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            to_markdown = response.parse()
            assert_matches_type(SyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.radar.ai.to_markdown.with_raw_response.create(
                account_id="",
            )


class TestAsyncToMarkdown:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        to_markdown = await async_client.radar.ai.to_markdown.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        to_markdown = await async_client.radar.ai.to_markdown.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(AsyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.to_markdown.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        to_markdown = await response.parse()
        assert_matches_type(AsyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.to_markdown.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            to_markdown = await response.parse()
            assert_matches_type(AsyncSinglePage[ToMarkdownCreateResponse], to_markdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.radar.ai.to_markdown.with_raw_response.create(
                account_id="",
            )
