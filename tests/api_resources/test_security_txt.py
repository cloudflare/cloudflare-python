# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.security_txt import (
    SecurityTXTGetResponse,
    SecurityTXTDeleteResponse,
    SecurityTXTUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecurityTXT:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        security_txt = client.security_txt.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        security_txt = client.security_txt.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            acknowledgments=["https://example.com/hall-of-fame.html"],
            canonical=["https://www.example.com/.well-known/security.txt"],
            contact=["mailto:security@example.com", "tel:+1-201-555-0123", "https://example.com/security-contact.html"],
            enabled=True,
            encryption=[
                "https://example.com/pgp-key.txt",
                "dns:5d2d37ab76d47d36._openpgpkey.example.com?type=OPENPGPKEY",
                "openpgp4fpr:5f2de5521c63a801ab59ccb603d49de44b29100f",
            ],
            expires=parse_datetime("2019-12-27T18:11:19.117Z"),
            hiring=["https://example.com/jobs.html"],
            policy=["https://example.com/disclosure-policy.html"],
            preferred_languages="en, es, fr",
        )
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.security_txt.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = response.parse()
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.security_txt.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = response.parse()
            assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.security_txt.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        security_txt = client.security_txt.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.security_txt.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = response.parse()
        assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.security_txt.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = response.parse()
            assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.security_txt.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        security_txt = client.security_txt.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.security_txt.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = response.parse()
        assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.security_txt.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = response.parse()
            assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.security_txt.with_raw_response.get(
                zone_id="",
            )


class TestAsyncSecurityTXT:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        security_txt = await async_client.security_txt.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        security_txt = await async_client.security_txt.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            acknowledgments=["https://example.com/hall-of-fame.html"],
            canonical=["https://www.example.com/.well-known/security.txt"],
            contact=["mailto:security@example.com", "tel:+1-201-555-0123", "https://example.com/security-contact.html"],
            enabled=True,
            encryption=[
                "https://example.com/pgp-key.txt",
                "dns:5d2d37ab76d47d36._openpgpkey.example.com?type=OPENPGPKEY",
                "openpgp4fpr:5f2de5521c63a801ab59ccb603d49de44b29100f",
            ],
            expires=parse_datetime("2019-12-27T18:11:19.117Z"),
            hiring=["https://example.com/jobs.html"],
            policy=["https://example.com/disclosure-policy.html"],
            preferred_languages="en, es, fr",
        )
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_txt.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = await response.parse()
        assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_txt.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = await response.parse()
            assert_matches_type(SecurityTXTUpdateResponse, security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.security_txt.with_raw_response.update(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        security_txt = await async_client.security_txt.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_txt.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = await response.parse()
        assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_txt.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = await response.parse()
            assert_matches_type(SecurityTXTDeleteResponse, security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.security_txt.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        security_txt = await async_client.security_txt.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_txt.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        security_txt = await response.parse()
        assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_txt.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            security_txt = await response.parse()
            assert_matches_type(Optional[SecurityTXTGetResponse], security_txt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.security_txt.with_raw_response.get(
                zone_id="",
            )
