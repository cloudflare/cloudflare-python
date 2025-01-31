# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.hostnames.settings import (
    Setting,
    TLSGetResponse,
    TLSDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTLS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        tls = client.hostnames.settings.tls.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        )
        assert_matches_type(Optional[Setting], tls, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.hostnames.settings.tls.with_raw_response.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = response.parse()
        assert_matches_type(Optional[Setting], tls, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.hostnames.settings.tls.with_streaming_response.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = response.parse()
            assert_matches_type(Optional[Setting], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.hostnames.settings.tls.with_raw_response.update(
                hostname="app.example.com",
                zone_id="",
                setting_id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            client.hostnames.settings.tls.with_raw_response.update(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                setting_id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tls = client.hostnames.settings.tls.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        )
        assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.hostnames.settings.tls.with_raw_response.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = response.parse()
        assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.hostnames.settings.tls.with_streaming_response.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = response.parse()
            assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.hostnames.settings.tls.with_raw_response.delete(
                hostname="app.example.com",
                zone_id="",
                setting_id="ciphers",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            client.hostnames.settings.tls.with_raw_response.delete(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                setting_id="ciphers",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tls = client.hostnames.settings.tls.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[TLSGetResponse], tls, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.hostnames.settings.tls.with_raw_response.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = response.parse()
        assert_matches_type(SyncSinglePage[TLSGetResponse], tls, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.hostnames.settings.tls.with_streaming_response.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = response.parse()
            assert_matches_type(SyncSinglePage[TLSGetResponse], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.hostnames.settings.tls.with_raw_response.get(
                setting_id="ciphers",
                zone_id="",
            )


class TestAsyncTLS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        tls = await async_client.hostnames.settings.tls.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        )
        assert_matches_type(Optional[Setting], tls, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hostnames.settings.tls.with_raw_response.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = await response.parse()
        assert_matches_type(Optional[Setting], tls, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hostnames.settings.tls.with_streaming_response.update(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = await response.parse()
            assert_matches_type(Optional[Setting], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.hostnames.settings.tls.with_raw_response.update(
                hostname="app.example.com",
                zone_id="",
                setting_id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            await async_client.hostnames.settings.tls.with_raw_response.update(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                setting_id="ciphers",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"],
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tls = await async_client.hostnames.settings.tls.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        )
        assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hostnames.settings.tls.with_raw_response.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = await response.parse()
        assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hostnames.settings.tls.with_streaming_response.delete(
            hostname="app.example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            setting_id="ciphers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = await response.parse()
            assert_matches_type(Optional[TLSDeleteResponse], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.hostnames.settings.tls.with_raw_response.delete(
                hostname="app.example.com",
                zone_id="",
                setting_id="ciphers",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hostname` but received ''"):
            await async_client.hostnames.settings.tls.with_raw_response.delete(
                hostname="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                setting_id="ciphers",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tls = await async_client.hostnames.settings.tls.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[TLSGetResponse], tls, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.hostnames.settings.tls.with_raw_response.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = await response.parse()
        assert_matches_type(AsyncSinglePage[TLSGetResponse], tls, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.hostnames.settings.tls.with_streaming_response.get(
            setting_id="ciphers",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = await response.parse()
            assert_matches_type(AsyncSinglePage[TLSGetResponse], tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.hostnames.settings.tls.with_raw_response.get(
                setting_id="ciphers",
                zone_id="",
            )
