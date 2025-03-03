# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.types.browser_rendering import (
    BrowserRenderingScrapeResponse,
    BrowserRenderingSnapshotResponse,
    BrowserRenderingScreenshotResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrowserRendering:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_content(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.content(
            account_id="accountId",
        )
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    def test_method_content_with_all_params(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.content(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    def test_raw_response_content(self, client: Cloudflare) -> None:
        response = client.browser_rendering.with_raw_response.content(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = response.parse()
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    def test_streaming_response_content(self, client: Cloudflare) -> None:
        with client.browser_rendering.with_streaming_response.content(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = response.parse()
            assert_matches_type(str, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_content(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.with_raw_response.content(
                account_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pdf(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        browser_rendering = client.browser_rendering.pdf(
            account_id="accountId",
        )
        assert browser_rendering.is_closed
        assert browser_rendering.json() == {"foo": "bar"}
        assert cast(Any, browser_rendering.is_closed) is True
        assert isinstance(browser_rendering, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_pdf_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        browser_rendering = client.browser_rendering.pdf(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert browser_rendering.is_closed
        assert browser_rendering.json() == {"foo": "bar"}
        assert cast(Any, browser_rendering.is_closed) is True
        assert isinstance(browser_rendering, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_pdf(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        browser_rendering = client.browser_rendering.with_raw_response.pdf(
            account_id="accountId",
        )

        assert browser_rendering.is_closed is True
        assert browser_rendering.http_request.headers.get("X-Stainless-Lang") == "python"
        assert browser_rendering.json() == {"foo": "bar"}
        assert isinstance(browser_rendering, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_pdf(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.browser_rendering.with_streaming_response.pdf(
            account_id="accountId",
        ) as browser_rendering:
            assert not browser_rendering.is_closed
            assert browser_rendering.http_request.headers.get("X-Stainless-Lang") == "python"

            assert browser_rendering.json() == {"foo": "bar"}
            assert cast(Any, browser_rendering.is_closed) is True
            assert isinstance(browser_rendering, StreamedBinaryAPIResponse)

        assert cast(Any, browser_rendering.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_pdf(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.with_raw_response.pdf(
                account_id="",
            )

    @parametrize
    def test_method_scrape(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        )
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    def test_method_scrape_with_all_params(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    def test_raw_response_scrape(self, client: Cloudflare) -> None:
        response = client.browser_rendering.with_raw_response.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = response.parse()
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    def test_streaming_response_scrape(self, client: Cloudflare) -> None:
        with client.browser_rendering.with_streaming_response.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = response.parse()
            assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_scrape(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.with_raw_response.scrape(
                account_id="",
                elements=[{"selector": "selector"}],
            )

    @parametrize
    def test_method_screenshot(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.screenshot(
            account_id="accountId",
        )
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    def test_method_screenshot_with_all_params(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.screenshot(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            screenshot_options={
                "capture_beyond_viewport": True,
                "clip": {
                    "height": 0,
                    "width": 0,
                    "x": 0,
                    "y": 0,
                    "scale": 0,
                },
                "encoding": "binary",
                "from_surface": True,
                "full_page": True,
                "omit_background": True,
                "optimize_for_speed": True,
                "quality": 0,
                "type": "png",
            },
            scroll_page=True,
            selector="selector",
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    def test_raw_response_screenshot(self, client: Cloudflare) -> None:
        response = client.browser_rendering.with_raw_response.screenshot(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = response.parse()
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    def test_streaming_response_screenshot(self, client: Cloudflare) -> None:
        with client.browser_rendering.with_streaming_response.screenshot(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = response.parse()
            assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_screenshot(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.with_raw_response.screenshot(
                account_id="",
            )

    @parametrize
    def test_method_snapshot(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.snapshot(
            account_id="accountId",
        )
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    def test_method_snapshot_with_all_params(self, client: Cloudflare) -> None:
        browser_rendering = client.browser_rendering.snapshot(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    def test_raw_response_snapshot(self, client: Cloudflare) -> None:
        response = client.browser_rendering.with_raw_response.snapshot(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = response.parse()
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    def test_streaming_response_snapshot(self, client: Cloudflare) -> None:
        with client.browser_rendering.with_streaming_response.snapshot(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = response.parse()
            assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_snapshot(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.browser_rendering.with_raw_response.snapshot(
                account_id="",
            )


class TestAsyncBrowserRendering:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_content(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.content(
            account_id="accountId",
        )
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    async def test_method_content_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.content(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    async def test_raw_response_content(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.with_raw_response.content(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = await response.parse()
        assert_matches_type(str, browser_rendering, path=["response"])

    @parametrize
    async def test_streaming_response_content(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.with_streaming_response.content(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = await response.parse()
            assert_matches_type(str, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_content(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.with_raw_response.content(
                account_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pdf(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        browser_rendering = await async_client.browser_rendering.pdf(
            account_id="accountId",
        )
        assert browser_rendering.is_closed
        assert await browser_rendering.json() == {"foo": "bar"}
        assert cast(Any, browser_rendering.is_closed) is True
        assert isinstance(browser_rendering, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_pdf_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        browser_rendering = await async_client.browser_rendering.pdf(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert browser_rendering.is_closed
        assert await browser_rendering.json() == {"foo": "bar"}
        assert cast(Any, browser_rendering.is_closed) is True
        assert isinstance(browser_rendering, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_pdf(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        browser_rendering = await async_client.browser_rendering.with_raw_response.pdf(
            account_id="accountId",
        )

        assert browser_rendering.is_closed is True
        assert browser_rendering.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await browser_rendering.json() == {"foo": "bar"}
        assert isinstance(browser_rendering, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_pdf(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post("/accounts/accountId/browser-rendering/pdf").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.browser_rendering.with_streaming_response.pdf(
            account_id="accountId",
        ) as browser_rendering:
            assert not browser_rendering.is_closed
            assert browser_rendering.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await browser_rendering.json() == {"foo": "bar"}
            assert cast(Any, browser_rendering.is_closed) is True
            assert isinstance(browser_rendering, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, browser_rendering.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_pdf(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.with_raw_response.pdf(
                account_id="",
            )

    @parametrize
    async def test_method_scrape(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        )
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.with_raw_response.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = await response.parse()
        assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.with_streaming_response.scrape(
            account_id="accountId",
            elements=[{"selector": "selector"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = await response.parse()
            assert_matches_type(BrowserRenderingScrapeResponse, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_scrape(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.with_raw_response.scrape(
                account_id="",
                elements=[{"selector": "selector"}],
            )

    @parametrize
    async def test_method_screenshot(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.screenshot(
            account_id="accountId",
        )
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.screenshot(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            screenshot_options={
                "capture_beyond_viewport": True,
                "clip": {
                    "height": 0,
                    "width": 0,
                    "x": 0,
                    "y": 0,
                    "scale": 0,
                },
                "encoding": "binary",
                "from_surface": True,
                "full_page": True,
                "omit_background": True,
                "optimize_for_speed": True,
                "quality": 0,
                "type": "png",
            },
            scroll_page=True,
            selector="selector",
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.with_raw_response.screenshot(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = await response.parse()
        assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.with_streaming_response.screenshot(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = await response.parse()
            assert_matches_type(BrowserRenderingScreenshotResponse, browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_screenshot(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.with_raw_response.screenshot(
                account_id="",
            )

    @parametrize
    async def test_method_snapshot(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.snapshot(
            account_id="accountId",
        )
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    async def test_method_snapshot_with_all_params(self, async_client: AsyncCloudflare) -> None:
        browser_rendering = await async_client.browser_rendering.snapshot(
            account_id="accountId",
            cache_ttl=86400,
            add_script_tag=[
                {
                    "id": "id",
                    "content": "content",
                    "type": "type",
                    "url": "url",
                }
            ],
            add_style_tag=[
                {
                    "content": "content",
                    "url": "url",
                }
            ],
            allow_request_pattern=["string"],
            allow_resource_types=["document"],
            authenticate={
                "password": "x",
                "username": "x",
            },
            best_attempt=True,
            cookies=[
                {
                    "name": "name",
                    "value": "value",
                    "domain": "domain",
                    "expires": 0,
                    "http_only": True,
                    "partition_key": "partitionKey",
                    "path": "path",
                    "priority": "Low",
                    "same_party": True,
                    "same_site": "Strict",
                    "secure": True,
                    "source_port": 0,
                    "source_scheme": "Unset",
                    "url": "url",
                }
            ],
            emulate_media_type="emulateMediaType",
            goto_options={
                "referer": "referer",
                "referrer_policy": "referrerPolicy",
                "timeout": 60000,
                "wait_until": "load",
            },
            html="x",
            reject_request_pattern=["string"],
            reject_resource_types=["document"],
            set_extra_http_headers={"foo": "string"},
            set_java_script_enabled=True,
            url="https://example.com",
            user_agent="userAgent",
            viewport={
                "height": 0,
                "width": 0,
                "device_scale_factor": 0,
                "has_touch": True,
                "is_landscape": True,
                "is_mobile": True,
            },
            wait_for_selector={
                "selector": "selector",
                "hidden": True,
                "timeout": 60000,
                "visible": True,
            },
            wait_for_timeout=60000,
        )
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    async def test_raw_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.browser_rendering.with_raw_response.snapshot(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        browser_rendering = await response.parse()
        assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

    @parametrize
    async def test_streaming_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        async with async_client.browser_rendering.with_streaming_response.snapshot(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            browser_rendering = await response.parse()
            assert_matches_type(Optional[BrowserRenderingSnapshotResponse], browser_rendering, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_snapshot(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.browser_rendering.with_raw_response.snapshot(
                account_id="",
            )
