# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.workflows import VersionGetResponse, VersionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.workflows.versions.list(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        version = client.workflows.versions.list(
            workflow_name="x",
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workflows.versions.with_raw_response.list(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workflows.versions.with_streaming_response.list(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.versions.with_raw_response.list(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.versions.with_raw_response.list(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.workflows.versions.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workflows.versions.with_raw_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workflows.versions.with_streaming_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workflows.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                workflow_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                workflow_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workflows.versions.with_raw_response.get(
                version_id="",
                account_id="account_id",
                workflow_name="x",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workflows.versions.list(
            workflow_name="x",
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workflows.versions.list(
            workflow_name="x",
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.versions.with_raw_response.list(
            workflow_name="x",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.versions.with_streaming_response.list(
            workflow_name="x",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.versions.with_raw_response.list(
                workflow_name="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.versions.with_raw_response.list(
                workflow_name="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workflows.versions.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        )
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workflows.versions.with_raw_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionGetResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workflows.versions.with_streaming_response.get(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            workflow_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionGetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workflows.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                workflow_name="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.versions.with_raw_response.get(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                workflow_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workflows.versions.with_raw_response.get(
                version_id="",
                account_id="account_id",
                workflow_name="x",
            )
