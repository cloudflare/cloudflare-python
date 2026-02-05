# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.workers.beta.workers import (
    Version,
    VersionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deploy=True,
            annotations={
                "workers_message": "Fixed bug.",
                "workers_tag": "v1.0.1",
            },
            assets={
                "config": {
                    "html_handling": "auto-trailing-slash",
                    "not_found_handling": "404-page",
                    "run_worker_first": ["string"],
                },
                "jwt": "jwt",
            },
            bindings=[
                {
                    "name": "MY_ENV_VAR",
                    "text": "my_data",
                    "type": "plain_text",
                }
            ],
            compatibility_date="2021-01-01",
            compatibility_flags=["nodejs_compat"],
            limits={"cpu_ms": 50},
            main_module="index.js",
            migrations={
                "deleted_classes": ["string"],
                "new_classes": ["string"],
                "new_sqlite_classes": ["string"],
                "new_tag": "v2",
                "old_tag": "v1",
                "renamed_classes": [
                    {
                        "from": "from",
                        "to": "to",
                    }
                ],
                "transferred_classes": [
                    {
                        "from": "from",
                        "from_script": "from_script",
                        "to": "to",
                    }
                ],
            },
            modules=[
                {
                    "content_base64": "ZXhwb3J0IGRlZmF1bHQgewogIGFzeW5jIGZldGNoKHJlcXVlc3QsIGVudiwgY3R4KSB7CiAgICByZXR1cm4gbmV3IFJlc3BvbnNlKCdIZWxsbyBXb3JsZCEnKQogIH0KfQ==",
                    "content_type": "application/javascript+module",
                    "name": "index.js",
                }
            ],
            placement={"mode": "smart"},
            usage_model="standard",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.versions.with_raw_response.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.versions.with_streaming_response.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Version, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.create(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.create(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.versions.with_raw_response.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.versions.with_streaming_response.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Version], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.list(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.list(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )
        assert_matches_type(VersionDeleteResponse, version, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.versions.with_raw_response.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionDeleteResponse, version, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.versions.with_streaming_response.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionDeleteResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.beta.workers.versions.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            include="modules",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.beta.workers.versions.with_raw_response.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.beta.workers.versions.with_streaming_response.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Version, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.get(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.get(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.get(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deploy=True,
            annotations={
                "workers_message": "Fixed bug.",
                "workers_tag": "v1.0.1",
            },
            assets={
                "config": {
                    "html_handling": "auto-trailing-slash",
                    "not_found_handling": "404-page",
                    "run_worker_first": ["string"],
                },
                "jwt": "jwt",
            },
            bindings=[
                {
                    "name": "MY_ENV_VAR",
                    "text": "my_data",
                    "type": "plain_text",
                }
            ],
            compatibility_date="2021-01-01",
            compatibility_flags=["nodejs_compat"],
            limits={"cpu_ms": 50},
            main_module="index.js",
            migrations={
                "deleted_classes": ["string"],
                "new_classes": ["string"],
                "new_sqlite_classes": ["string"],
                "new_tag": "v2",
                "old_tag": "v1",
                "renamed_classes": [
                    {
                        "from": "from",
                        "to": "to",
                    }
                ],
                "transferred_classes": [
                    {
                        "from": "from",
                        "from_script": "from_script",
                        "to": "to",
                    }
                ],
            },
            modules=[
                {
                    "content_base64": "ZXhwb3J0IGRlZmF1bHQgewogIGFzeW5jIGZldGNoKHJlcXVlc3QsIGVudiwgY3R4KSB7CiAgICByZXR1cm4gbmV3IFJlc3BvbnNlKCdIZWxsbyBXb3JsZCEnKQogIH0KfQ==",
                    "content_type": "application/javascript+module",
                    "name": "index.js",
                }
            ],
            placement={"mode": "smart"},
            usage_model="standard",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.versions.with_raw_response.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.versions.with_streaming_response.create(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Version, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.create(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.create(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.versions.with_raw_response.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Version], version, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.versions.with_streaming_response.list(
            worker_id="worker_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Version], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.list(
                worker_id="worker_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.list(
                worker_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )
        assert_matches_type(VersionDeleteResponse, version, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.versions.with_raw_response.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionDeleteResponse, version, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.versions.with_streaming_response.delete(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionDeleteResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.delete(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.beta.workers.versions.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            include="modules",
        )
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.beta.workers.versions.with_raw_response.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Version, version, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.beta.workers.versions.with_streaming_response.get(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Version, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.get(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.get(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.get(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
            )
