# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.ssls import VerificationUpdateResponse, VerificationSSLVerificationSSLVerificationDetailsResponse

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssls import verification_update_params
from cloudflare.types.ssls import verification_ssl_verification_ssl_verification_details_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        verification = client.ssls.verifications.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.ssls.verifications.with_raw_response.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.ssls.verifications.with_streaming_response.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.verifications.with_raw_response.update(
                "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
                zone_id="",
                validation_method="txt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.ssls.verifications.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                validation_method="txt",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_ssl_verification_ssl_verification_details(self, client: Cloudflare) -> None:
        verification = client.ssls.verifications.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_ssl_verification_ssl_verification_details_with_all_params(self, client: Cloudflare) -> None:
        verification = client.ssls.verifications.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            retry=True,
        )
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ssl_verification_ssl_verification_details(self, client: Cloudflare) -> None:
        response = client.ssls.verifications.with_raw_response.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ssl_verification_ssl_verification_details(self, client: Cloudflare) -> None:
        with client.ssls.verifications.with_streaming_response.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(
                Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ssl_verification_ssl_verification_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.verifications.with_raw_response.ssl_verification_ssl_verification_details(
                "",
            )


class TestAsyncVerifications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        verification = await async_client.ssls.verifications.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        )
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.verifications.with_raw_response.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssls.verifications.with_streaming_response.update(
            "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            validation_method="txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationUpdateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.verifications.with_raw_response.update(
                "a77f8bd7-3b47-46b4-a6f1-75cf98109948",
                zone_id="",
                validation_method="txt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.ssls.verifications.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                validation_method="txt",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ssl_verification_ssl_verification_details(self, async_client: AsyncCloudflare) -> None:
        verification = await async_client.ssls.verifications.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ssl_verification_ssl_verification_details_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        verification = await async_client.ssls.verifications.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            retry=True,
        )
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ssl_verification_ssl_verification_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.verifications.with_raw_response.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(
            Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ssl_verification_ssl_verification_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.ssls.verifications.with_streaming_response.ssl_verification_ssl_verification_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(
                Optional[VerificationSSLVerificationSSLVerificationDetailsResponse], verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ssl_verification_ssl_verification_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.verifications.with_raw_response.ssl_verification_ssl_verification_details(
                "",
            )
