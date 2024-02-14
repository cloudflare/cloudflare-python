# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.intels import DomainDomainIntelligenceGetDomainDetailsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intels import domain_domain_intelligence_get_domain_details_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_domain_intelligence_get_domain_details(self, client: Cloudflare) -> None:
        domain = client.intels.domains.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_domain_intelligence_get_domain_details_with_all_params(self, client: Cloudflare) -> None:
        domain = client.intels.domains.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domain="string",
        )
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_domain_intelligence_get_domain_details(self, client: Cloudflare) -> None:
        response = client.intels.domains.with_raw_response.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_domain_intelligence_get_domain_details(self, client: Cloudflare) -> None:
        with client.intels.domains.with_streaming_response.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_domain_intelligence_get_domain_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intels.domains.with_raw_response.domain_intelligence_get_domain_details(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_domain_intelligence_get_domain_details(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.intels.domains.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_domain_intelligence_get_domain_details_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        domain = await async_client.intels.domains.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domain="string",
        )
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_domain_intelligence_get_domain_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intels.domains.with_raw_response.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_domain_intelligence_get_domain_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.intels.domains.with_streaming_response.domain_intelligence_get_domain_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDomainIntelligenceGetDomainDetailsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_domain_intelligence_get_domain_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intels.domains.with_raw_response.domain_intelligence_get_domain_details(
                "",
            )
