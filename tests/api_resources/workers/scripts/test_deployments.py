# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.scripts import (
    DeploymentGetResponse,
    DeploymentCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        )
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
            force=True,
            annotations={"workers_message": "Deploy bug fix."},
        )
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                strategy="percentage",
                versions=[
                    {
                        "percentage": 100,
                        "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.deployments.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                strategy="percentage",
                versions=[
                    {
                        "percentage": 100,
                        "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.deployments.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        )
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
            force=True,
            annotations={"workers_message": "Deploy bug fix."},
        )
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Optional[DeploymentCreateResponse], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                strategy="percentage",
                versions=[
                    {
                        "percentage": 100,
                        "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                strategy="percentage",
                versions=[
                    {
                        "percentage": 100,
                        "version_id": "bcf48806-b317-4351-9ee7-36e7d557d4de",
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(Optional[DeploymentGetResponse], deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
