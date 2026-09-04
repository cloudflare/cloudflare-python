# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pages.projects.deployments import TailCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tail = client.pages.projects.deployments.tails.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        tail = client.pages.projects.deployments.tails.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            filters=[{"outcome": "bar"}],
        )
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pages.projects.deployments.tails.with_raw_response.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pages.projects.deployments.tails.with_streaming_response.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(TailCreateResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tail = client.pages.projects.deployments.tails.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, tail, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pages.projects.deployments.tails.with_raw_response.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(object, tail, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pages.projects.deployments.tails.with_streaming_response.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(object, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                deployment_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tail_id` but received ''"):
            client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.pages.projects.deployments.tails.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.pages.projects.deployments.tails.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            filters=[{"outcome": "bar"}],
        )
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.deployments.tails.with_raw_response.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(TailCreateResponse, tail, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.deployments.tails.with_streaming_response.create(
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(TailCreateResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.create(
                deployment_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.pages.projects.deployments.tails.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, tail, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.deployments.tails.with_raw_response.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(object, tail, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.deployments.tails.with_streaming_response.delete(
            tail_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
            deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(object, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                project_name="this-is-my-project-01",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deployment_id` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                deployment_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tail_id` but received ''"):
            await async_client.pages.projects.deployments.tails.with_raw_response.delete(
                tail_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
                deployment_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
