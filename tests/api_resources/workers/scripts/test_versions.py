# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.scripts.version_get_response import VersionGetResponse
from cloudflare.types.workers.scripts.version_list_response import VersionListResponse
from cloudflare.types.workers.scripts.version_create_response import VersionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "annotations": {
                    "workers_message": "Fixed worker code.",
                    "workers_tag": "string",
                },
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "compatibility_date": "2023-07-25",
                "compatibility_flags": ["string", "string", "string"],
                "keep_bindings": ["string", "string", "string"],
                "main_module": "worker.js",
                "usage_model": "standard",
            },
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.create(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VersionListResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionListResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.list(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        version = client.workers.scripts.versions.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.versions.with_raw_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.versions.with_streaming_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.workers.scripts.versions.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "annotations": {
                    "workers_message": "Fixed worker code.",
                    "workers_tag": "string",
                },
                "bindings": [
                    {
                        "name": "MY_ENV_VAR",
                        "text": "my_data",
                        "type": "plain_text",
                    }
                ],
                "compatibility_date": "2023-07-25",
                "compatibility_flags": ["string", "string", "string"],
                "keep_bindings": ["string", "string", "string"],
                "main_module": "worker.js",
                "usage_model": "standard",
            },
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.create(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.create(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VersionListResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionListResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.list(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.list(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.workers.scripts.versions.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.versions.with_raw_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.versions.with_streaming_response.get(
            "bcf48806-b317-4351-9ee7-36e7d557d4de",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionGetResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                "bcf48806-b317-4351-9ee7-36e7d557d4de",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.workers.scripts.versions.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )
