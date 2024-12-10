# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.workflows import (
    WorkflowGetResponse,
    WorkflowListResponse,
    WorkflowUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        workflow = client.workflows.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workflows.with_raw_response.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workflows.with_streaming_response.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.with_raw_response.update(
                workflow_name="x",
                account_id="",
                class_name="x",
                script_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.update(
                workflow_name="",
                account_id="account_id",
                class_name="x",
                script_name="x",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        workflow = client.workflows.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        workflow = client.workflows.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workflows.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workflows.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        workflow = client.workflows.get(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workflows.with_raw_response.get(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workflows.with_streaming_response.get(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.with_raw_response.get(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.get(
                workflow_name="",
                account_id="account_id",
            )


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        workflow = await async_client.workflows.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.with_raw_response.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.with_streaming_response.update(
            workflow_name="x",
            account_id="account_id",
            class_name="x",
            script_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.with_raw_response.update(
                workflow_name="x",
                account_id="",
                class_name="x",
                script_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.update(
                workflow_name="",
                account_id="account_id",
                class_name="x",
                script_name="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        workflow = await async_client.workflows.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        workflow = await async_client.workflows.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[WorkflowListResponse], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        workflow = await async_client.workflows.get(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.with_raw_response.get(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.with_streaming_response.get(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.with_raw_response.get(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.get(
                workflow_name="",
                account_id="account_id",
            )
