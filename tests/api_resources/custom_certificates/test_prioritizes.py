# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.custom_certificates import (
    PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrioritizes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(self, client: Cloudflare) -> None:
        prioritize = client.custom_certificates.prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )
        assert_matches_type(
            Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(self, client: Cloudflare) -> None:
        response = client.custom_certificates.prioritizes.with_raw_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prioritize = response.parse()
        assert_matches_type(
            Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(self, client: Cloudflare) -> None:
        with client.custom_certificates.prioritizes.with_streaming_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prioritize = response.parse()
            assert_matches_type(
                Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_certificates.prioritizes.with_raw_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
                "",
                certificates=[{}, {}],
            )


class TestAsyncPrioritizes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        prioritize = (
            await async_client.custom_certificates.prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
                "023e105f4ecef8ad9ca31a8372d0c353",
                certificates=[{}, {}],
            )
        )
        assert_matches_type(
            Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.custom_certificates.prioritizes.with_raw_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prioritize = await response.parse()
        assert_matches_type(
            Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.custom_certificates.prioritizes.with_streaming_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prioritize = await response.parse()
            assert_matches_type(
                Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse], prioritize, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_certificates.prioritizes.with_raw_response.custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
                "",
                certificates=[{}, {}],
            )
