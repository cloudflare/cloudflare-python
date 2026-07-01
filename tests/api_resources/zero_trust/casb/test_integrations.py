# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.casb import (
    IntegrationGetResponse,
    IntegrationPauseResponse,
    IntegrationCreateResponse,
    IntegrationResumeResponse,
    IntegrationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        )
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
            auth_method="service_account",
            dlp_profiles=["e91a2360-da51-4fdf-9711-bcdecd462614"],
            permissions=["https://www.googleapis.com/auth/drive.readonly"],
            use_cases=["casb", "ces"],
        )
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.create(
                account_id="",
                application="GOOGLE_WORKSPACE",
                credentials={"admin_email": "bar"},
                name="My Google Workspace",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "access_token": "bar",
                "refresh_token": "bar",
            },
            dlp_profiles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
            permissions=["x"],
            use_cases=["casb"],
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.update(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.update(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="application",
            direction="asc",
            dlp_enabled=True,
            order="application",
            page=0,
            page_size=0,
            search="search",
            status="Healthy",
            use_cases="use_cases",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(object, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert integration is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert integration is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert integration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.delete(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.delete(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationGetResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.get(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.get(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_pause(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_pause(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_pause(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pause(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.pause(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.pause(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_resume(self, client: Cloudflare) -> None:
        integration = client.zero_trust.casb.integrations.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_resume(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.integrations.with_raw_response.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_resume(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.integrations.with_streaming_response.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resume(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.resume(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.casb.integrations.with_raw_response.resume(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        )
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
            auth_method="service_account",
            dlp_profiles=["e91a2360-da51-4fdf-9711-bcdecd462614"],
            permissions=["https://www.googleapis.com/auth/drive.readonly"],
            use_cases=["casb", "ces"],
        )
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="GOOGLE_WORKSPACE",
            credentials={"admin_email": "bar"},
            name="My Google Workspace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationCreateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.create(
                account_id="",
                application="GOOGLE_WORKSPACE",
                credentials={"admin_email": "bar"},
                name="My Google Workspace",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            credentials={
                "access_token": "bar",
                "refresh_token": "bar",
            },
            dlp_profiles=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="x",
            permissions=["x"],
            use_cases=["casb"],
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.update(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.update(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.update(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            application="application",
            direction="asc",
            dlp_enabled=True,
            order="application",
            page=0,
            page_size=0,
            search="search",
            status="Healthy",
            use_cases="use_cases",
        )
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(object, integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(object, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert integration is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert integration is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.delete(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert integration is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.delete(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.delete(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationGetResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.get(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationGetResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.get(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.get(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_pause(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.pause(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationPauseResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pause(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.pause(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.pause(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_resume(self, async_client: AsyncCloudflare) -> None:
        integration = await async_client.zero_trust.casb.integrations.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.integrations.with_raw_response.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.integrations.with_streaming_response.resume(
            id="id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationResumeResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resume(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.resume(
                id="id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.casb.integrations.with_raw_response.resume(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
