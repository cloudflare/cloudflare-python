# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pages.projects.deployments import RollbackPagesDeploymentRollbackDeploymentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRollbacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_pages_deployment_rollback_deployment(self, client: Cloudflare) -> None:
        rollback = client.pages.projects.deployments.rollbacks.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pages_deployment_rollback_deployment(self, client: Cloudflare) -> None:
        response = client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = response.parse()
        assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pages_deployment_rollback_deployment(self, client: Cloudflare) -> None:
        with client.pages.projects.deployments.rollbacks.with_streaming_response.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = response.parse()
            assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pages_deployment_rollback_deployment(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )


class TestAsyncRollbacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_pages_deployment_rollback_deployment(self, async_client: AsyncCloudflare) -> None:
        rollback = await async_client.pages.projects.deployments.rollbacks.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pages_deployment_rollback_deployment(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollback = await response.parse()
        assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pages_deployment_rollback_deployment(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.deployments.rollbacks.with_streaming_response.pages_deployment_rollback_deployment(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollback = await response.parse()
            assert_matches_type(RollbackPagesDeploymentRollbackDeploymentResponse, rollback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pages_deployment_rollback_deployment(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.pages.projects.deployments.rollbacks.with_raw_response.pages_deployment_rollback_deployment(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )
