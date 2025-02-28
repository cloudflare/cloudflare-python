# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.workers.scripts import (
    VersionGetResponse,
    VersionListResponse,
    VersionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.js",
                "annotations": {
                    "workers_message": "Fixed worker code.",
                    "workers_tag": "workers/tag",
                },
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "type": "ai",
                    }
                ],
                "compatibility_date": "2021-01-01",
                "compatibility_flags": ["nodejs_compat"],
                "keep_bindings": ["string"],
                "usage_model": "standard",
            },
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                metadata={"main_module": "worker.js"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                metadata={"main_module": "worker.js"},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deployable=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(SyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncV4PagePagination[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.js",
                "annotations": {
                    "workers_message": "Fixed worker code.",
                    "workers_tag": "workers/tag",
                },
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "type": "ai",
                    }
                ],
                "compatibility_date": "2021-01-01",
                "compatibility_flags": ["nodejs_compat"],
                "keep_bindings": ["string"],
                "usage_model": "standard",
            },
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={"main_module": "worker.js"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                metadata={"main_module": "worker.js"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                metadata={"main_module": "worker.js"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deployable=True,
            page=0,
            per_page=0,
        )
        assert_matches_type(AsyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncV4PagePagination[VersionListResponse], version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncV4PagePagination[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.list(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.list(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.get(
            version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                version_id="bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )
