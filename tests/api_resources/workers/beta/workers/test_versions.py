# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
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
                    "base_path": "/docs/",
                    "html_handling": "auto-trailing-slash",
                    "not_found_handling": "404-page",
                    "run_worker_first": True,
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
            cache_options={
                "enabled": True,
                "cross_version_cache": True,
            },
            compatibility_date="2021-01-01T00:00:00Z",
            compatibility_flags=["nodejs_compat"],
            containers=[{"class_name": "MyDurableObject"}],
            exports={
                "Admin": {
                    "type": "worker",
                    "cache": {"enabled": True},
                    "state": "created",
                },
                "Counter": {
                    "storage": "sqlite",
                    "type": "durable-object",
                    "container": "my-container",
                    "state": "created",
                },
                "OldCounter": {
                    "renamed_to": "Counter",
                    "state": "renamed",
                    "type": "durable-object",
                },
                "default": {
                    "type": "worker",
                    "cache": {"enabled": False},
                    "state": "created",
                },
            },
            limits={
                "cpu_ms": 50,
                "subrequests": 1000,
            },
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
            package_dependencies=[
                {
                    "installed_version": "4.17.22",
                    "name": "lodash",
                    "package_json_version": "^4.17.21",
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_profile(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = client.workers.beta.workers.versions.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        )
        assert version.is_closed
        assert version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_profile_with_all_params(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = client.workers.beta.workers.versions.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
            actor_id="actor_id",
            namespace_id="namespace_id",
            profile_type="cpu",
        )
        assert version.is_closed
        assert version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_profile(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = client.workers.beta.workers.versions.with_raw_response.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        )

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert version.json() == {"foo": "bar"}
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_profile(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.workers.beta.workers.versions.with_streaming_response.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        ) as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, StreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_profile(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
                duration_ms=1000,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
                duration_ms=1000,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
                duration_ms=1000,
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
                    "base_path": "/docs/",
                    "html_handling": "auto-trailing-slash",
                    "not_found_handling": "404-page",
                    "run_worker_first": True,
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
            cache_options={
                "enabled": True,
                "cross_version_cache": True,
            },
            compatibility_date="2021-01-01T00:00:00Z",
            compatibility_flags=["nodejs_compat"],
            containers=[{"class_name": "MyDurableObject"}],
            exports={
                "Admin": {
                    "type": "worker",
                    "cache": {"enabled": True},
                    "state": "created",
                },
                "Counter": {
                    "storage": "sqlite",
                    "type": "durable-object",
                    "container": "my-container",
                    "state": "created",
                },
                "OldCounter": {
                    "renamed_to": "Counter",
                    "state": "renamed",
                    "type": "durable-object",
                },
                "default": {
                    "type": "worker",
                    "cache": {"enabled": False},
                    "state": "created",
                },
            },
            limits={
                "cpu_ms": 50,
                "subrequests": 1000,
            },
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
            package_dependencies=[
                {
                    "installed_version": "4.17.22",
                    "name": "lodash",
                    "package_json_version": "^4.17.21",
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_profile(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = await async_client.workers.beta.workers.versions.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        )
        assert version.is_closed
        assert await version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_profile_with_all_params(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = await async_client.workers.beta.workers.versions.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
            actor_id="actor_id",
            namespace_id="namespace_id",
            profile_type="cpu",
        )
        assert version.is_closed
        assert await version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_profile(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = await async_client.workers.beta.workers.versions.with_raw_response.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        )

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await version.json() == {"foo": "bar"}
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_profile(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.post(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/workers/worker_id/versions/version_id/profile"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.workers.beta.workers.versions.with_streaming_response.profile(
            version_id="version_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            worker_id="worker_id",
            duration_ms=1000,
        ) as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_profile(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="version_id",
                account_id="",
                worker_id="worker_id",
                duration_ms=1000,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="version_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="",
                duration_ms=1000,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workers.beta.workers.versions.with_raw_response.profile(
                version_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                worker_id="worker_id",
                duration_ms=1000,
            )
