# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.page_shield import Script, ScriptGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        script = client.page_shield.scripts.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Script], script, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        script = client.page_shield.scripts.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            exclude_cdn_cgi=True,
            exclude_duplicates=True,
            exclude_urls="blog.cloudflare.com,www.example",
            export="csv",
            hosts="blog.cloudflare.com,www.example*,*cloudflare.com",
            order_by="first_seen_at",
            page="2",
            page_url="example.com/page,*/checkout,example.com/*,*checkout*",
            per_page=100,
            prioritize_malicious=True,
            status="active,inactive",
            urls="blog.cloudflare.com,www.example",
        )
        assert_matches_type(SyncSinglePage[Script], script, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.page_shield.scripts.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(SyncSinglePage[Script], script, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.page_shield.scripts.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(SyncSinglePage[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shield.scripts.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        script = client.page_shield.scripts.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.page_shield.scripts.with_raw_response.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.page_shield.scripts.with_streaming_response.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.page_shield.scripts.with_raw_response.get(
                script_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            client.page_shield.scripts.with_raw_response.get(
                script_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncScripts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        script = await async_client.page_shield.scripts.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        script = await async_client.page_shield.scripts.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            exclude_cdn_cgi=True,
            exclude_duplicates=True,
            exclude_urls="blog.cloudflare.com,www.example",
            export="csv",
            hosts="blog.cloudflare.com,www.example*,*cloudflare.com",
            order_by="first_seen_at",
            page="2",
            page_url="example.com/page,*/checkout,example.com/*,*checkout*",
            per_page=100,
            prioritize_malicious=True,
            status="active,inactive",
            urls="blog.cloudflare.com,www.example",
        )
        assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_shield.scripts.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_shield.scripts.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(AsyncSinglePage[Script], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shield.scripts.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        script = await async_client.page_shield.scripts.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.page_shield.scripts.with_raw_response.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.page_shield.scripts.with_streaming_response.get(
            script_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(Optional[ScriptGetResponse], script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.page_shield.scripts.with_raw_response.get(
                script_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_id` but received ''"):
            await async_client.page_shield.scripts.with_raw_response.get(
                script_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
