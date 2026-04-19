# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import (
    EnvironmentEditResponse,
    EnvironmentListResponse,
    EnvironmentCreateResponse,
    EnvironmentDeleteResponse,
    EnvironmentUpdateResponse,
    EnvironmentRollbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        environment = client.zones.environments.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.create(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        environment = client.zones.environments.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.update(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        environment = client.zones.environments.list(
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        environment = client.zones.environments.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.delete(
                environment_id="environment_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.zones.environments.with_raw_response.delete(
                environment_id="",
                zone_id="zone_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        environment = client.zones.environments.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.edit(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    def test_method_rollback(self, client: Cloudflare) -> None:
        environment = client.zones.environments.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_rollback(self, client: Cloudflare) -> None:
        response = client.zones.environments.with_raw_response.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_rollback(self, client: Cloudflare) -> None:
        with client.zones.environments.with_streaming_response.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rollback(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.environments.with_raw_response.rollback(
                environment_id="environment_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            client.zones.environments.with_raw_response.rollback(
                environment_id="",
                zone_id="zone_id",
            )


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.create(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.create(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.update(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentUpdateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.update(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.list(
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.list(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.list(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.delete(
            environment_id="environment_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentDeleteResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.delete(
                environment_id="environment_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.zones.environments.with_raw_response.delete(
                environment_id="",
                zone_id="zone_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )
        assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.edit(
            zone_id="zone_id",
            environments=[
                {
                    "expression": "expression",
                    "locked_on_deployment": True,
                    "name": "name",
                    "position": {},
                    "ref": "ref",
                    "version": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentEditResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.edit(
                zone_id="",
                environments=[
                    {
                        "expression": "expression",
                        "locked_on_deployment": True,
                        "name": "name",
                        "position": {},
                        "ref": "ref",
                        "version": 0,
                    }
                ],
            )

    @parametrize
    async def test_method_rollback(self, async_client: AsyncCloudflare) -> None:
        environment = await async_client.zones.environments.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        )
        assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_rollback(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.environments.with_raw_response.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_rollback(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.environments.with_streaming_response.rollback(
            environment_id="environment_id",
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRollbackResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rollback(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.environments.with_raw_response.rollback(
                environment_id="environment_id",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_id` but received ''"):
            await async_client.zones.environments.with_raw_response.rollback(
                environment_id="",
                zone_id="zone_id",
            )
