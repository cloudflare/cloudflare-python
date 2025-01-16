# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.managed_transforms import (
    ManagedTransformEditResponse,
    ManagedTransformListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagedTransforms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        managed_transform = client.managed_transforms.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.managed_transforms.with_raw_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = response.parse()
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.managed_transforms.with_streaming_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = response.parse()
            assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_transforms.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        managed_transform = client.managed_transforms.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert managed_transform is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.managed_transforms.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = response.parse()
        assert managed_transform is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.managed_transforms.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = response.parse()
            assert managed_transform is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_transforms.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        managed_transform = client.managed_transforms.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        )
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.managed_transforms.with_raw_response.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = response.parse()
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.managed_transforms.with_streaming_response.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = response.parse()
            assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_transforms.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[
                    {
                        "id": "add_bot_protection_headers",
                        "enabled": True,
                    }
                ],
                managed_response_headers=[
                    {
                        "id": "add_security_headers",
                        "enabled": True,
                    }
                ],
            )


class TestAsyncManagedTransforms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        managed_transform = await async_client.managed_transforms.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_transforms.with_raw_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = await response.parse()
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_transforms.with_streaming_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = await response.parse()
            assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_transforms.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        managed_transform = await async_client.managed_transforms.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert managed_transform is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_transforms.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = await response.parse()
        assert managed_transform is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_transforms.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = await response.parse()
            assert managed_transform is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_transforms.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        managed_transform = await async_client.managed_transforms.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        )
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_transforms.with_raw_response.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = await response.parse()
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_transforms.with_streaming_response.edit(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            managed_request_headers=[
                {
                    "id": "add_bot_protection_headers",
                    "enabled": True,
                }
            ],
            managed_response_headers=[
                {
                    "id": "add_security_headers",
                    "enabled": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = await response.parse()
            assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_transforms.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[
                    {
                        "id": "add_bot_protection_headers",
                        "enabled": True,
                    }
                ],
                managed_response_headers=[
                    {
                        "id": "add_security_headers",
                        "enabled": True,
                    }
                ],
            )
