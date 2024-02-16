# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import (
    SubdomainWorkerSubdomainGetSubdomainResponse,
    SubdomainWorkerSubdomainCreateSubdomainResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubdomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_subdomain_create_subdomain(self, client: Cloudflare) -> None:
        subdomain = client.workers.subdomains.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        )
        assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_subdomain_create_subdomain(self, client: Cloudflare) -> None:
        response = client.workers.subdomains.with_raw_response.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_subdomain_create_subdomain(self, client: Cloudflare) -> None:
        with client.workers.subdomains.with_streaming_response.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_subdomain_create_subdomain(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.subdomains.with_raw_response.worker_subdomain_create_subdomain(
                "",
                body="{'subdomain': 'example-subdomain'}",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_subdomain_get_subdomain(self, client: Cloudflare) -> None:
        subdomain = client.workers.subdomains.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_subdomain_get_subdomain(self, client: Cloudflare) -> None:
        response = client.workers.subdomains.with_raw_response.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_subdomain_get_subdomain(self, client: Cloudflare) -> None:
        with client.workers.subdomains.with_streaming_response.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_subdomain_get_subdomain(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.subdomains.with_raw_response.worker_subdomain_get_subdomain(
                "",
            )


class TestAsyncSubdomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_subdomain_create_subdomain(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.workers.subdomains.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        )
        assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_subdomain_create_subdomain(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.subdomains.with_raw_response.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_subdomain_create_subdomain(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.subdomains.with_streaming_response.worker_subdomain_create_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="{'subdomain': 'example-subdomain'}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(SubdomainWorkerSubdomainCreateSubdomainResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_subdomain_create_subdomain(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.subdomains.with_raw_response.worker_subdomain_create_subdomain(
                "",
                body="{'subdomain': 'example-subdomain'}",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_subdomain_get_subdomain(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.workers.subdomains.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_subdomain_get_subdomain(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.subdomains.with_raw_response.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_subdomain_get_subdomain(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.subdomains.with_streaming_response.worker_subdomain_get_subdomain(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(SubdomainWorkerSubdomainGetSubdomainResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_subdomain_get_subdomain(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.subdomains.with_raw_response.worker_subdomain_get_subdomain(
                "",
            )
