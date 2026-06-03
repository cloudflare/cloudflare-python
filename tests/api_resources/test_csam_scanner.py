# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.csam_scanner import CsamScannerGetResponse, CsamScannerEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCsamScanner:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        csam_scanner = client.csam_scanner.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        csam_scanner = client.csam_scanner.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="csam_scanner",
            value={
                "email": "user@example.com",
                "enabled": True,
                "resend_email": True,
                "sources": {"source1": True},
            },
        )
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.csam_scanner.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csam_scanner = response.parse()
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.csam_scanner.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csam_scanner = response.parse()
            assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.csam_scanner.with_raw_response.edit(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        csam_scanner = client.csam_scanner.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.csam_scanner.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csam_scanner = response.parse()
        assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.csam_scanner.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csam_scanner = response.parse()
            assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.csam_scanner.with_raw_response.get(
                zone_id="",
            )


class TestAsyncCsamScanner:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        csam_scanner = await async_client.csam_scanner.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        csam_scanner = await async_client.csam_scanner.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="csam_scanner",
            value={
                "email": "user@example.com",
                "enabled": True,
                "resend_email": True,
                "sources": {"source1": True},
            },
        )
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.csam_scanner.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csam_scanner = await response.parse()
        assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.csam_scanner.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csam_scanner = await response.parse()
            assert_matches_type(Optional[CsamScannerEditResponse], csam_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.csam_scanner.with_raw_response.edit(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        csam_scanner = await async_client.csam_scanner.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.csam_scanner.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        csam_scanner = await response.parse()
        assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.csam_scanner.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            csam_scanner = await response.parse()
            assert_matches_type(Optional[CsamScannerGetResponse], csam_scanner, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.csam_scanner.with_raw_response.get(
                zone_id="",
            )
