# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workflows.instances import StatusEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        status = client.workflows.instances.status.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        )
        assert_matches_type(StatusEditResponse, status, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.workflows.instances.status.with_raw_response.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusEditResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.workflows.instances.status.with_streaming_response.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusEditResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.instances.status.with_raw_response.edit(
                instance_id="x",
                account_id="",
                workflow_name="x",
                status="resume",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.instances.status.with_raw_response.edit(
                instance_id="x",
                account_id="account_id",
                workflow_name="",
                status="resume",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.workflows.instances.status.with_raw_response.edit(
                instance_id="",
                account_id="account_id",
                workflow_name="x",
                status="resume",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        status = await async_client.workflows.instances.status.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        )
        assert_matches_type(StatusEditResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.instances.status.with_raw_response.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusEditResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.instances.status.with_streaming_response.edit(
            instance_id="x",
            account_id="account_id",
            workflow_name="x",
            status="resume",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusEditResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.instances.status.with_raw_response.edit(
                instance_id="x",
                account_id="",
                workflow_name="x",
                status="resume",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.instances.status.with_raw_response.edit(
                instance_id="x",
                account_id="account_id",
                workflow_name="",
                status="resume",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.workflows.instances.status.with_raw_response.edit(
                instance_id="",
                account_id="account_id",
                workflow_name="x",
                status="resume",
            )
