# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.ssls import AnalyzeAnalyzeCertificateAnalyzeCertificateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssls import analyze_analyze_certificate_analyze_certificate_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalyzes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_analyze_certificate_analyze_certificate(self, client: Cloudflare) -> None:
        analyze = client.ssls.analyzes.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_analyze_certificate_analyze_certificate_with_all_params(self, client: Cloudflare) -> None:
        analyze = client.ssls.analyzes.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            bundle_method="ubiquitous",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDtTCCAp2gAwIBAgIJAMHAwfXZ5/PWMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV\nBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX\naWRnaXRzIFB0eSBMdGQwHhcNMTYwODI0MTY0MzAxWhcNMTYxMTIyMTY0MzAxWjBF\nMQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50\nZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\nCgKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmGdtcGbg/1\nCGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKnabIRuGvB\nKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpidtnKX/a+5\n0GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+pyFxIXjbEI\ndZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pEewooaeO2\nizNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABo4GnMIGkMB0GA1UdDgQWBBT/LbE4\n9rWf288N6sJA5BRb6FJIGDB1BgNVHSMEbjBsgBT/LbE49rWf288N6sJA5BRb6FJI\nGKFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUtU3RhdGUxITAfBgNV\nBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAMHAwfXZ5/PWMAwGA1UdEwQF\nMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAHHFwl0tH0quUYZYO0dZYt4R7SJ0pCm2\n2satiyzHl4OnXcHDpekAo7/a09c6Lz6AU83cKy/+x3/djYHXWba7HpEu0dR3ugQP\nMlr4zrhd9xKZ0KZKiYmtJH+ak4OM4L3FbT0owUZPyjLSlhMtJVcoRp5CJsjAMBUG\nSvD8RX+T01wzox/Qb+lnnNnOlaWpqu8eoOenybxKp1a9ULzIVvN/LAcc+14vioFq\n2swRWtmocBAs8QR9n4uvbpiYvS8eYueDCWMM4fvFfBhaDZ3N9IbtySh3SpFdQDhw\nYbjM2rxXiyLGxB4Bol7QTv4zHif7Zt89FReT/NBy4rzaskDJY5L6xmY=\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_analyze_certificate_analyze_certificate(self, client: Cloudflare) -> None:
        response = client.ssls.analyzes.with_raw_response.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyze = response.parse()
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_analyze_certificate_analyze_certificate(self, client: Cloudflare) -> None:
        with client.ssls.analyzes.with_streaming_response.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyze = response.parse()
            assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_analyze_certificate_analyze_certificate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.analyzes.with_raw_response.analyze_certificate_analyze_certificate(
                "",
            )


class TestAsyncAnalyzes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_analyze_certificate_analyze_certificate(self, async_client: AsyncCloudflare) -> None:
        analyze = await async_client.ssls.analyzes.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_analyze_certificate_analyze_certificate_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        analyze = await async_client.ssls.analyzes.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            bundle_method="ubiquitous",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDtTCCAp2gAwIBAgIJAMHAwfXZ5/PWMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV\nBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX\naWRnaXRzIFB0eSBMdGQwHhcNMTYwODI0MTY0MzAxWhcNMTYxMTIyMTY0MzAxWjBF\nMQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50\nZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB\nCgKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmGdtcGbg/1\nCGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKnabIRuGvB\nKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpidtnKX/a+5\n0GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+pyFxIXjbEI\ndZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pEewooaeO2\nizNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABo4GnMIGkMB0GA1UdDgQWBBT/LbE4\n9rWf288N6sJA5BRb6FJIGDB1BgNVHSMEbjBsgBT/LbE49rWf288N6sJA5BRb6FJI\nGKFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUtU3RhdGUxITAfBgNV\nBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAMHAwfXZ5/PWMAwGA1UdEwQF\nMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAHHFwl0tH0quUYZYO0dZYt4R7SJ0pCm2\n2satiyzHl4OnXcHDpekAo7/a09c6Lz6AU83cKy/+x3/djYHXWba7HpEu0dR3ugQP\nMlr4zrhd9xKZ0KZKiYmtJH+ak4OM4L3FbT0owUZPyjLSlhMtJVcoRp5CJsjAMBUG\nSvD8RX+T01wzox/Qb+lnnNnOlaWpqu8eoOenybxKp1a9ULzIVvN/LAcc+14vioFq\n2swRWtmocBAs8QR9n4uvbpiYvS8eYueDCWMM4fvFfBhaDZ3N9IbtySh3SpFdQDhw\nYbjM2rxXiyLGxB4Bol7QTv4zHif7Zt89FReT/NBy4rzaskDJY5L6xmY=\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_analyze_certificate_analyze_certificate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssls.analyzes.with_raw_response.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyze = await response.parse()
        assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_analyze_certificate_analyze_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.ssls.analyzes.with_streaming_response.analyze_certificate_analyze_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyze = await response.parse()
            assert_matches_type(AnalyzeAnalyzeCertificateAnalyzeCertificateResponse, analyze, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_analyze_certificate_analyze_certificate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.analyzes.with_raw_response.analyze_certificate_analyze_certificate(
                "",
            )
