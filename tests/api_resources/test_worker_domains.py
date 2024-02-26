# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import WorkerDomainGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkerDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        worker_domain = client.worker_domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert worker_domain is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.worker_domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker_domain = response.parse()
        assert worker_domain is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.worker_domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker_domain = response.parse()
            assert worker_domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        worker_domain = client.worker_domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.worker_domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker_domain = response.parse()
        assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.worker_domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker_domain = response.parse()
            assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkerDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        worker_domain = await async_client.worker_domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert worker_domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.worker_domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker_domain = await response.parse()
        assert worker_domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.worker_domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker_domain = await response.parse()
            assert worker_domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        worker_domain = await async_client.worker_domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.worker_domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker_domain = await response.parse()
        assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.worker_domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker_domain = await response.parse()
            assert_matches_type(WorkerDomainGetResponse, worker_domain, path=["response"])

        assert cast(Any, response.is_closed) is True
