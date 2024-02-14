# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.brand_protections import URLInfoPhishingURLInformationGetResultsForAURLScanResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.brand_protections import url_info_phishing_url_information_get_results_for_a_url_scan_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLInfos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_phishing_url_information_get_results_for_a_url_scan(self, client: Cloudflare) -> None:
        url_info = client.brand_protections.url_infos.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_phishing_url_information_get_results_for_a_url_scan_with_all_params(
        self, client: Cloudflare
    ) -> None:
        url_info = client.brand_protections.url_infos.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="string",
            url_id_param={"url_id": 0},
        )
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_phishing_url_information_get_results_for_a_url_scan(self, client: Cloudflare) -> None:
        response = (
            client.brand_protections.url_infos.with_raw_response.phishing_url_information_get_results_for_a_url_scan(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_info = response.parse()
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_phishing_url_information_get_results_for_a_url_scan(self, client: Cloudflare) -> None:
        with client.brand_protections.url_infos.with_streaming_response.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_info = response.parse()
            assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_phishing_url_information_get_results_for_a_url_scan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protections.url_infos.with_raw_response.phishing_url_information_get_results_for_a_url_scan(
                "",
            )


class TestAsyncURLInfos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_phishing_url_information_get_results_for_a_url_scan(
        self, async_client: AsyncCloudflare
    ) -> None:
        url_info = await async_client.brand_protections.url_infos.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_phishing_url_information_get_results_for_a_url_scan_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        url_info = await async_client.brand_protections.url_infos.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="string",
            url_id_param={"url_id": 0},
        )
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_phishing_url_information_get_results_for_a_url_scan(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.brand_protections.url_infos.with_raw_response.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_info = await response.parse()
        assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_phishing_url_information_get_results_for_a_url_scan(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.brand_protections.url_infos.with_streaming_response.phishing_url_information_get_results_for_a_url_scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_info = await response.parse()
            assert_matches_type(URLInfoPhishingURLInformationGetResultsForAURLScanResponse, url_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_phishing_url_information_get_results_for_a_url_scan(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protections.url_infos.with_raw_response.phishing_url_information_get_results_for_a_url_scan(
                "",
            )
