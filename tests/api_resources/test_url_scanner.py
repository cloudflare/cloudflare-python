# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.url_scanner import URLScannerScanResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.url_scanner import url_scanner_scan_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLScanner:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_scan(self, client: Cloudflare) -> None:
        url_scanner = client.url_scanner.scan(
            account_id="accountId",
        )
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    def test_method_scan_with_all_params(self, client: Cloudflare) -> None:
        url_scanner = client.url_scanner.scan(
            account_id="accountId",
            account_scans=True,
            asn="13335",
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            hash="hash",
            hostname="example.com",
            ip="1.1.1.1",
            is_malicious=True,
            limit=100,
            next_cursor="next_cursor",
            page_asn="page_asn",
            page_hostname="page_hostname",
            page_ip="page_ip",
            page_path="page_path",
            page_url="page_url",
            path="/samples/subresource-integrity/",
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="https://example.com/?hello",
        )
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    def test_raw_response_scan(self, client: Cloudflare) -> None:
        response = client.url_scanner.with_raw_response.scan(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_scanner = response.parse()
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    def test_streaming_response_scan(self, client: Cloudflare) -> None:
        with client.url_scanner.with_streaming_response.scan(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_scanner = response.parse()
            assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_scan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.url_scanner.with_raw_response.scan(
                account_id="",
            )


class TestAsyncURLScanner:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_scan(self, async_client: AsyncCloudflare) -> None:
        url_scanner = await async_client.url_scanner.scan(
            account_id="accountId",
        )
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    async def test_method_scan_with_all_params(self, async_client: AsyncCloudflare) -> None:
        url_scanner = await async_client.url_scanner.scan(
            account_id="accountId",
            account_scans=True,
            asn="13335",
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            hash="hash",
            hostname="example.com",
            ip="1.1.1.1",
            is_malicious=True,
            limit=100,
            next_cursor="next_cursor",
            page_asn="page_asn",
            page_hostname="page_hostname",
            page_ip="page_ip",
            page_path="page_path",
            page_url="page_url",
            path="/samples/subresource-integrity/",
            scan_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            url="https://example.com/?hello",
        )
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_scanner.with_raw_response.scan(
            account_id="accountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_scanner = await response.parse()
        assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_scanner.with_streaming_response.scan(
            account_id="accountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_scanner = await response.parse()
            assert_matches_type(URLScannerScanResponse, url_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_scan(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.url_scanner.with_raw_response.scan(
                account_id="",
            )
