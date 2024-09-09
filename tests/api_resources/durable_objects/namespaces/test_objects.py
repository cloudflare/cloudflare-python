# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from cloudflare.types.durable_objects.namespaces import DurableObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        object_ = client.durable_objects.namespaces.objects.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        object_ = client.durable_objects.namespaces.objects.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="AAAAANuhDN7SjacTnSVsDu3WW1Lvst6dxJGTjRY5BhxPXdf6L6uTcpd_NVtjhn11OUYRsVEykxoUwF-JQU4dn6QylZSKTOJuG0indrdn_MlHpMRtsxgXjs-RPdHYIVm3odE_uvEQ_dTQGFm8oikZMohns34DLBgrQpc",
            limit=10,
        )
        assert_matches_type(SyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.durable_objects.namespaces.objects.with_raw_response.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.durable_objects.namespaces.objects.with_streaming_response.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncCursorLimitPagination[DurableObject], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.durable_objects.namespaces.objects.with_raw_response.list(
                id="5fd1cafff895419c8bcc647fc64ab8f0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.durable_objects.namespaces.objects.with_raw_response.list(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.durable_objects.namespaces.objects.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        object_ = await async_client.durable_objects.namespaces.objects.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="AAAAANuhDN7SjacTnSVsDu3WW1Lvst6dxJGTjRY5BhxPXdf6L6uTcpd_NVtjhn11OUYRsVEykxoUwF-JQU4dn6QylZSKTOJuG0indrdn_MlHpMRtsxgXjs-RPdHYIVm3odE_uvEQ_dTQGFm8oikZMohns34DLBgrQpc",
            limit=10,
        )
        assert_matches_type(AsyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.durable_objects.namespaces.objects.with_raw_response.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncCursorLimitPagination[DurableObject], object_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.durable_objects.namespaces.objects.with_streaming_response.list(
            id="5fd1cafff895419c8bcc647fc64ab8f0",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncCursorLimitPagination[DurableObject], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.durable_objects.namespaces.objects.with_raw_response.list(
                id="5fd1cafff895419c8bcc647fc64ab8f0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.durable_objects.namespaces.objects.with_raw_response.list(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
