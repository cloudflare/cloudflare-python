# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones.settings import CipherGetResponse, CipherEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCiphers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        cipher = client.zones.settings.ciphers.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )
        assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zones.settings.ciphers.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cipher = response.parse()
        assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zones.settings.ciphers.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cipher = response.parse()
            assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.ciphers.with_raw_response.edit(
                zone_id="",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        cipher = client.zones.settings.ciphers.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.settings.ciphers.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cipher = response.parse()
        assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.settings.ciphers.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cipher = response.parse()
            assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.settings.ciphers.with_raw_response.get(
                zone_id="",
            )


class TestAsyncCiphers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        cipher = await async_client.zones.settings.ciphers.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )
        assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.ciphers.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cipher = await response.parse()
        assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.ciphers.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cipher = await response.parse()
            assert_matches_type(Optional[CipherEditResponse], cipher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.ciphers.with_raw_response.edit(
                zone_id="",
                value=["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        cipher = await async_client.zones.settings.ciphers.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.settings.ciphers.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cipher = await response.parse()
        assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.settings.ciphers.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cipher = await response.parse()
            assert_matches_type(Optional[CipherGetResponse], cipher, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.settings.ciphers.with_raw_response.get(
                zone_id="",
            )
