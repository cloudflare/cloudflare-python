# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

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
from cloudflare.types.url_scanner import (
    ScanGetResponse,
    ScanHARResponse,
    ScanListResponse,
    ScanBulkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.create(
            account_id="account_id",
            url="https://www.example.com",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.create(
            account_id="account_id",
            url="https://www.example.com",
            customagent="customagent",
            custom_headers={"foo": "string"},
            referer="referer",
            screenshots_resolutions=["desktop"],
            visibility="Public",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.create(
            account_id="account_id",
            url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.create(
            account_id="account_id",
            url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(str, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.create(
                account_id="",
                url="https://www.example.com",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.list(
            account_id="account_id",
        )
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.list(
            account_id="account_id",
            q="q",
            size=100,
        )
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanListResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.bulk_create(
            account_id="account_id",
        )
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.bulk_create(
            account_id="account_id",
            body=[
                {
                    "url": "https://www.example.com",
                    "customagent": "customagent",
                    "custom_headers": {"foo": "string"},
                    "referer": "referer",
                    "screenshots_resolutions": ["desktop"],
                    "visibility": "Public",
                }
            ],
        )
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.bulk_create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.bulk_create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.bulk_create(
                account_id="",
            )

    @parametrize
    def test_method_dom(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    def test_raw_response_dom(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    def test_streaming_response_dom(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(str, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_dom(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.dom(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.dom(
                scan_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanGetResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.get(
                scan_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_har(self, client: Cloudflare) -> None:
        scan = client.url_scanner.scans.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ScanHARResponse, scan, path=["response"])

    @parametrize
    def test_raw_response_har(self, client: Cloudflare) -> None:
        response = client.url_scanner.scans.with_raw_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = response.parse()
        assert_matches_type(ScanHARResponse, scan, path=["response"])

    @parametrize
    def test_streaming_response_har(self, client: Cloudflare) -> None:
        with client.url_scanner.scans.with_streaming_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = response.parse()
            assert_matches_type(ScanHARResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_har(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.har(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.har(
                scan_id="",
                account_id="account_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert scan.is_closed
        assert scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_screenshot_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            resolution="desktop",
        )
        assert scan.is_closed
        assert scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_screenshot(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scan = client.url_scanner.scans.with_raw_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert scan.is_closed is True
        assert scan.http_request.headers.get("X-Stainless-Lang") == "python"
        assert scan.json() == {"foo": "bar"}
        assert isinstance(scan, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_screenshot(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.url_scanner.scans.with_streaming_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as scan:
            assert not scan.is_closed
            assert scan.http_request.headers.get("X-Stainless-Lang") == "python"

            assert scan.json() == {"foo": "bar"}
            assert cast(Any, scan.is_closed) is True
            assert isinstance(scan, StreamedBinaryAPIResponse)

        assert cast(Any, scan.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_screenshot(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="",
                account_id="account_id",
            )


class TestAsyncScans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.create(
            account_id="account_id",
            url="https://www.example.com",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.create(
            account_id="account_id",
            url="https://www.example.com",
            customagent="customagent",
            custom_headers={"foo": "string"},
            referer="referer",
            screenshots_resolutions=["desktop"],
            visibility="Public",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.create(
            account_id="account_id",
            url="https://www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.create(
            account_id="account_id",
            url="https://www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(str, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.create(
                account_id="",
                url="https://www.example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.list(
            account_id="account_id",
        )
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.list(
            account_id="account_id",
            q="q",
            size=100,
        )
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanListResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanListResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.bulk_create(
            account_id="account_id",
        )
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.bulk_create(
            account_id="account_id",
            body=[
                {
                    "url": "https://www.example.com",
                    "customagent": "customagent",
                    "custom_headers": {"foo": "string"},
                    "referer": "referer",
                    "screenshots_resolutions": ["desktop"],
                    "visibility": "Public",
                }
            ],
        )
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.bulk_create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.bulk_create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanBulkCreateResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.bulk_create(
                account_id="",
            )

    @parametrize
    async def test_method_dom(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    async def test_raw_response_dom(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(str, scan, path=["response"])

    @parametrize
    async def test_streaming_response_dom(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.dom(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(str, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_dom(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.dom(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.dom(
                scan_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanGetResponse, scan, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.get(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanGetResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.get(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.get(
                scan_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_har(self, async_client: AsyncCloudflare) -> None:
        scan = await async_client.url_scanner.scans.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ScanHARResponse, scan, path=["response"])

    @parametrize
    async def test_raw_response_har(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.scans.with_raw_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scan = await response.parse()
        assert_matches_type(ScanHARResponse, scan, path=["response"])

    @parametrize
    async def test_streaming_response_har(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.scans.with_streaming_response.har(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scan = await response.parse()
            assert_matches_type(ScanHARResponse, scan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_har(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.har(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.har(
                scan_id="",
                account_id="account_id",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = await async_client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert scan.is_closed
        assert await scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_screenshot_with_all_params(
        self, async_client: AsyncCloudflare, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        scan = await async_client.url_scanner.scans.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            resolution="desktop",
        )
        assert scan.is_closed
        assert await scan.json() == {"foo": "bar"}
        assert cast(Any, scan.is_closed) is True
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_screenshot(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        scan = await async_client.url_scanner.scans.with_raw_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert scan.is_closed is True
        assert scan.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await scan.json() == {"foo": "bar"}
        assert isinstance(scan, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_screenshot(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/account_id/urlscanner/v2/screenshots/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e.png").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.url_scanner.scans.with_streaming_response.screenshot(
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as scan:
            assert not scan.is_closed
            assert scan.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await scan.json() == {"foo": "bar"}
            assert cast(Any, scan.is_closed) is True
            assert isinstance(scan, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, scan.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_screenshot(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `scan_id` but received ''"):
            await async_client.url_scanner.scans.with_raw_response.screenshot(
                scan_id="",
                account_id="account_id",
            )
