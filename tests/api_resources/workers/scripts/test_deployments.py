# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.scripts import (
    DeploymentGetResponse,
    DeploymentListResponse,
    DeploymentCreateResponse,
    DeploymentDeleteResponse,
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
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            force=True,
            annotations={"workers_message": "Deploy bug fix."},
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

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
                        "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                        "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentListResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.deployments.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        deployment = client.workers.scripts.deployments.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.deployments.with_raw_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.deployments.with_streaming_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            force=True,
            annotations={"workers_message": "Deploy bug fix."},
        )
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            strategy="percentage",
            versions=[
                {
                    "percentage": 100,
                    "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentCreateResponse, deployment, path=["response"])

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
                        "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
                        "version_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentListResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentListResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.delete(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentDeleteResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.delete(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        deployment = await async_client.workers.scripts.deployments.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.deployments.with_raw_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.deployments.with_streaming_response.get(
            deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentGetResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.workers.scripts.deployments.with_raw_response.get(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )
