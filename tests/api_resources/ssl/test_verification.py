# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssl import (
    VerificationGetResponse,
    VerificationEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        verification = client.ssl.verification.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        )
        assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.ssl.verification.with_raw_response.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.ssl.verification.with_streaming_response.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.verification.with_raw_response.edit(
                certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
                zone_id="",
                validation_method="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssl.verification.with_raw_response.edit(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                validation_method="http",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        verification = client.ssl.verification.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        verification = client.ssl.verification.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            retry=True,
        )
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.ssl.verification.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.ssl.verification.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.verification.with_raw_response.get(
                zone_id="",
            )


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        verification = await async_client.ssl.verification.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        )
        assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.verification.with_raw_response.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.verification.with_streaming_response.edit(
            certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(Optional[VerificationEditResponse], verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.verification.with_raw_response.edit(
                certificate_pack_id="a77f8bd7-3b47-46b4-a6f1-75cf98109948",
                zone_id="",
                validation_method="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssl.verification.with_raw_response.edit(
                certificate_pack_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                validation_method="http",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        verification = await async_client.ssl.verification.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        verification = await async_client.ssl.verification.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            retry=True,
        )
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.verification.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.verification.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(Optional[VerificationGetResponse], verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.verification.with_raw_response.get(
                zone_id="",
            )
