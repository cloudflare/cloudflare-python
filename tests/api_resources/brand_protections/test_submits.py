# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.brand_protections import (
    SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_phishing_url_scanner_submit_suspicious_url_for_scanning(self, client: Cloudflare) -> None:
        submit = client.brand_protections.submits.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_phishing_url_scanner_submit_suspicious_url_for_scanning_with_all_params(
        self, client: Cloudflare
    ) -> None:
        submit = client.brand_protections.submits.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://www.cloudflare.com",
        )
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_phishing_url_scanner_submit_suspicious_url_for_scanning(self, client: Cloudflare) -> None:
        response = (
            client.brand_protections.submits.with_raw_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = response.parse()
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_phishing_url_scanner_submit_suspicious_url_for_scanning(
        self, client: Cloudflare
    ) -> None:
        with client.brand_protections.submits.with_streaming_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = response.parse()
            assert_matches_type(
                SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_phishing_url_scanner_submit_suspicious_url_for_scanning(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protections.submits.with_raw_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
                "",
            )


class TestAsyncSubmits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_phishing_url_scanner_submit_suspicious_url_for_scanning(
        self, async_client: AsyncCloudflare
    ) -> None:
        submit = await async_client.brand_protections.submits.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_phishing_url_scanner_submit_suspicious_url_for_scanning_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        submit = await async_client.brand_protections.submits.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://www.cloudflare.com",
        )
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_phishing_url_scanner_submit_suspicious_url_for_scanning(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.brand_protections.submits.with_raw_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submit = await response.parse()
        assert_matches_type(SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_phishing_url_scanner_submit_suspicious_url_for_scanning(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.brand_protections.submits.with_streaming_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submit = await response.parse()
            assert_matches_type(
                SubmitPhishingURLScannerSubmitSuspiciousURLForScanningResponse, submit, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_phishing_url_scanner_submit_suspicious_url_for_scanning(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protections.submits.with_raw_response.phishing_url_scanner_submit_suspicious_url_for_scanning(
                "",
            )
