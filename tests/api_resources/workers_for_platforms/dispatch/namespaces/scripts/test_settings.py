# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import SettingsItem

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.workers_for_platforms.dispatch.namespaces.scripts.settings.edit(
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
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        setting = client.workers_for_platforms.dispatch.namespaces.scripts.settings.edit(
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
                "logpush": False,
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
            },
            success=True,
        )
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.edit(
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
            assert_matches_type(SettingsItem, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
            client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
        assert_matches_type(SettingsItem, setting, path=["response"])

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
        assert_matches_type(SettingsItem, setting, path=["response"])

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
            assert_matches_type(SettingsItem, setting, path=["response"])

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
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.edit(
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
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.edit(
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
                "logpush": False,
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
            },
            success=True,
        )
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
        setting = await response.parse()
        assert_matches_type(SettingsItem, setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_streaming_response.edit(
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
            assert_matches_type(SettingsItem, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.settings.with_raw_response.edit(
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
        assert_matches_type(SettingsItem, setting, path=["response"])

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
        assert_matches_type(SettingsItem, setting, path=["response"])

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
            assert_matches_type(SettingsItem, setting, path=["response"])

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
