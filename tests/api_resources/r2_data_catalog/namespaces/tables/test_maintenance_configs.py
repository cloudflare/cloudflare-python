# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2_data_catalog.namespaces.tables import (
    MaintenanceConfigGetResponse,
    MaintenanceConfigUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMaintenanceConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        maintenance_config = client.r2_data_catalog.namespaces.tables.maintenance_configs.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        maintenance_config = client.r2_data_catalog.namespaces.tables.maintenance_configs.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
            compaction={
                "state": "enabled",
                "target_size_mb": "256",
            },
        )
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance_config = response.parse()
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.namespaces.tables.maintenance_configs.with_streaming_response.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance_config = response.parse()
            assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_name` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        maintenance_config = client.r2_data_catalog.namespaces.tables.maintenance_configs.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )
        assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance_config = response.parse()
        assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.namespaces.tables.maintenance_configs.with_streaming_response.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance_config = response.parse()
            assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_name` but received ''"):
            client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )


class TestAsyncMaintenanceConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        maintenance_config = await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        maintenance_config = await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
            compaction={
                "state": "enabled",
                "target_size_mb": "256",
            },
        )
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance_config = await response.parse()
        assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_streaming_response.update(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance_config = await response.parse()
            assert_matches_type(Optional[MaintenanceConfigUpdateResponse], maintenance_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_name` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.update(
                table_name="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        maintenance_config = await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )
        assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        maintenance_config = await response.parse()
        assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_streaming_response.get(
            table_name="my_table",
            account_id="0123456789abcdef0123456789abcdef",
            bucket_name="my-data-bucket",
            namespace="my_namespace%1Fsub_namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            maintenance_config = await response.parse()
            assert_matches_type(Optional[MaintenanceConfigGetResponse], maintenance_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="",
                namespace="my_namespace%1Fsub_namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="my_table",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_name` but received ''"):
            await async_client.r2_data_catalog.namespaces.tables.maintenance_configs.with_raw_response.get(
                table_name="",
                account_id="0123456789abcdef0123456789abcdef",
                bucket_name="my-data-bucket",
                namespace="my_namespace%1Fsub_namespace",
            )
