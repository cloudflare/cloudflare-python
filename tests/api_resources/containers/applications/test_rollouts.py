# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.containers.applications import RolloutCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRollouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rollout = client.containers.applications.rollouts.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        )
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rollout = client.containers.applications.rollouts.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "command": ["myapp", "--default-option"],
                "entrypoint": ["/bin/bash"],
                "environment_variables": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "image": "image",
                "instance_type": "lite",
                "observability": {"logs": {"enabled": True}},
            },
            kind="full_auto",
            percentage=0,
            step_percentage=5,
            steps=[
                {
                    "description": "description",
                    "step_size": {"percentage": 0},
                }
            ],
        )
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.containers.applications.rollouts.with_raw_response.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollout = response.parse()
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.containers.applications.rollouts.with_streaming_response.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollout = response.parse()
            assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.applications.rollouts.with_raw_response.create(
                application_id="application_id",
                account_id="",
                description="description",
                strategy="rolling",
                target_configuration={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.containers.applications.rollouts.with_raw_response.create(
                application_id="",
                account_id="account-123",
                description="description",
                strategy="rolling",
                target_configuration={},
            )


class TestAsyncRollouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rollout = await async_client.containers.applications.rollouts.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        )
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rollout = await async_client.containers.applications.rollouts.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={
                "authorized_keys": [
                    {
                        "public_key": "public_key",
                        "name": "name",
                    }
                ],
                "command": ["myapp", "--default-option"],
                "entrypoint": ["/bin/bash"],
                "environment_variables": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "image": "image",
                "instance_type": "lite",
                "observability": {"logs": {"enabled": True}},
            },
            kind="full_auto",
            percentage=0,
            step_percentage=5,
            steps=[
                {
                    "description": "description",
                    "step_size": {"percentage": 0},
                }
            ],
        )
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.applications.rollouts.with_raw_response.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rollout = await response.parse()
        assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.applications.rollouts.with_streaming_response.create(
            application_id="application_id",
            account_id="account-123",
            description="description",
            strategy="rolling",
            target_configuration={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rollout = await response.parse()
            assert_matches_type(RolloutCreateResponse, rollout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.applications.rollouts.with_raw_response.create(
                application_id="application_id",
                account_id="",
                description="description",
                strategy="rolling",
                target_configuration={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.containers.applications.rollouts.with_raw_response.create(
                application_id="",
                account_id="account-123",
                description="description",
                strategy="rolling",
                target_configuration={},
            )
