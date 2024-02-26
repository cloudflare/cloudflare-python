# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.worker_scripts import SettingGetResponse, SettingEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.worker_scripts.settings.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        setting = client.worker_scripts.settings.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings={
                "errors": [
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                ],
                "messages": [
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                ],
                "result": {
                    "bindings": [{"type": "kv_namespace"}, {"type": "kv_namespace"}, {"type": "kv_namespace"}],
                    "compatibility_date": "2022-04-05",
                    "compatibility_flags": [
                        "formdata_parser_supports_files",
                        "formdata_parser_supports_files",
                        "formdata_parser_supports_files",
                    ],
                    "logpush": False,
                    "migrations": {
                        "new_tag": "v2",
                        "old_tag": "v1",
                        "deleted_classes": ["string", "string", "string"],
                        "new_classes": ["string", "string", "string"],
                        "renamed_classes": [
                            {
                                "from": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "to": "string",
                            },
                        ],
                        "transferred_classes": [
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                        ],
                    },
                    "placement": {"mode": "smart"},
                    "tags": ["my-tag", "my-tag", "my-tag"],
                    "tail_consumers": [
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                    ],
                    "usage_model": "unbound",
                },
                "success": True,
            },
        )
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.worker_scripts.settings.with_raw_response.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.worker_scripts.settings.with_streaming_response.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingEditResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.worker_scripts.settings.with_raw_response.edit(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.worker_scripts.settings.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.worker_scripts.settings.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.worker_scripts.settings.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.worker_scripts.settings.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingGetResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.worker_scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.worker_scripts.settings.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.worker_scripts.settings.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.worker_scripts.settings.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            settings={
                "errors": [
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                ],
                "messages": [
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                    {
                        "code": 1000,
                        "message": "string",
                    },
                ],
                "result": {
                    "bindings": [{"type": "kv_namespace"}, {"type": "kv_namespace"}, {"type": "kv_namespace"}],
                    "compatibility_date": "2022-04-05",
                    "compatibility_flags": [
                        "formdata_parser_supports_files",
                        "formdata_parser_supports_files",
                        "formdata_parser_supports_files",
                    ],
                    "logpush": False,
                    "migrations": {
                        "new_tag": "v2",
                        "old_tag": "v1",
                        "deleted_classes": ["string", "string", "string"],
                        "new_classes": ["string", "string", "string"],
                        "renamed_classes": [
                            {
                                "from": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "to": "string",
                            },
                        ],
                        "transferred_classes": [
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                            {
                                "from": "string",
                                "from_script": "string",
                                "to": "string",
                            },
                        ],
                    },
                    "placement": {"mode": "smart"},
                    "tags": ["my-tag", "my-tag", "my-tag"],
                    "tail_consumers": [
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                        {
                            "environment": "production",
                            "namespace": "my-namespace",
                            "service": "my-log-consumer",
                        },
                    ],
                    "usage_model": "unbound",
                },
                "success": True,
            },
        )
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.worker_scripts.settings.with_raw_response.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingEditResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.worker_scripts.settings.with_streaming_response.edit(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingEditResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.worker_scripts.settings.with_raw_response.edit(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.worker_scripts.settings.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.worker_scripts.settings.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.worker_scripts.settings.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.worker_scripts.settings.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingGetResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.worker_scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.worker_scripts.settings.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
