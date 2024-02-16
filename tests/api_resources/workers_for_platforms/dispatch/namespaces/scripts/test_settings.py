# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import SettingUpdateResponse, SettingGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import setting_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        setting = client.workers_for_platforms.dispatch.namespaces.scripts.settings.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={},
            success=True,
        )
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        setting = client.workers_for_platforms.dispatch.namespaces.scripts.settings.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={
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
            success=True,
        )
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={},
            success=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={},
            success=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingUpdateResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.workers_for_platforms.dispatch.namespaces.scripts.settings.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
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
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={},
            success=True,
        )
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={
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
            success=True,
        )
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingUpdateResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            errors=[
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
            messages=[
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
            result={},
            success=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingUpdateResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
                errors=[
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
                messages=[
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
                result={},
                success=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingGetResponse, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
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
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
