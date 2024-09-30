# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreenshot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        screenshot = client.url_scanner.screenshot.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert screenshot.is_closed
        assert screenshot.json() == {"foo": "bar"}
        assert cast(Any, screenshot.is_closed) is True
        assert isinstance(screenshot, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        screenshot = client.url_scanner.screenshot.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            resolution="desktop",
        )
        assert screenshot.is_closed
        assert screenshot.json() == {"foo": "bar"}
        assert cast(Any, screenshot.is_closed) is True
        assert isinstance(screenshot, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        screenshot = client.url_scanner.screenshot.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert screenshot.is_closed is True
        assert screenshot.http_request.headers.get("X-Stainless-Lang") == "python"
        assert screenshot.json() == {"foo": "bar"}
        assert isinstance(screenshot, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.url_scanner.screenshot.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as screenshot:
            assert not screenshot.is_closed
            assert screenshot.http_request.headers.get("X-Stainless-Lang") == "python"

            assert screenshot.json() == {"foo": "bar"}
            assert cast(Any, screenshot.is_closed) is True
            assert isinstance(screenshot, StreamedBinaryAPIResponse)

        assert cast(Any, screenshot.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.screenshot.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.screenshot.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )


class TestAsyncScreenshot:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        screenshot = await async_client.url_scanner.screenshot.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )
        assert screenshot.is_closed
        assert await screenshot.json() == {"foo": "bar"}
        assert cast(Any, screenshot.is_closed) is True
        assert isinstance(screenshot, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        screenshot = await async_client.url_scanner.screenshot.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
            resolution="desktop",
        )
        assert screenshot.is_closed
        assert await screenshot.json() == {"foo": "bar"}
        assert cast(Any, screenshot.is_closed) is True
        assert isinstance(screenshot, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        screenshot = await async_client.url_scanner.screenshot.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        )

        assert screenshot.is_closed is True
        assert screenshot.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await screenshot.json() == {"foo": "bar"}
        assert isinstance(screenshot, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/accountId/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.url_scanner.screenshot.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="accountId",
        ) as screenshot:
            assert not screenshot.is_closed
            assert screenshot.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await screenshot.json() == {"foo": "bar"}
            assert cast(Any, screenshot.is_closed) is True
            assert isinstance(screenshot, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, screenshot.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.screenshot.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.screenshot.with_raw_response.get(
                scan_id="",
                account_id="accountId",
            )
