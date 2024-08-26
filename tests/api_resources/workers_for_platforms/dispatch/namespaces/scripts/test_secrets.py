# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import SecretUpdateResponse, SecretListResponse

from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts import secret_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        secret = client.workers_for_platforms.dispatch.namespaces.scripts.secrets.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        secret = client.workers_for_platforms.dispatch.namespaces.scripts.secrets.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            name="MY_SECRET",
            text="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            type="secret_text",
        )
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        secret = response.parse()
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            secret = response.parse()
            assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="this-is_my_script-01",
              account_id="",
              dispatch_namespace="my-dispatch-namespace",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="this-is_my_script-01",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="my-dispatch-namespace",
          )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        secret = client.workers_for_platforms.dispatch.namespaces.scripts.secrets.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(SyncSinglePage[SecretListResponse], secret, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        secret = response.parse()
        assert_matches_type(SyncSinglePage[SecretListResponse], secret, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            secret = response.parse()
            assert_matches_type(SyncSinglePage[SecretListResponse], secret, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="this-is_my_script-01",
              account_id="",
              dispatch_namespace="my-dispatch-namespace",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="this-is_my_script-01",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
          client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="my-dispatch-namespace",
          )
class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            name="MY_SECRET",
            text="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            type="secret_text",
        )
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        secret = await response.parse()
        assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_streaming_response.update(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            secret = await response.parse()
            assert_matches_type(Optional[SecretUpdateResponse], secret, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="this-is_my_script-01",
              account_id="",
              dispatch_namespace="my-dispatch-namespace",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="this-is_my_script-01",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.update(
              script_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="my-dispatch-namespace",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(AsyncSinglePage[SecretListResponse], secret, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        secret = await response.parse()
        assert_matches_type(AsyncSinglePage[SecretListResponse], secret, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_streaming_response.list(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            secret = await response.parse()
            assert_matches_type(AsyncSinglePage[SecretListResponse], secret, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="this-is_my_script-01",
              account_id="",
              dispatch_namespace="my-dispatch-namespace",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="this-is_my_script-01",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
          await async_client.workers_for_platforms.dispatch.namespaces.scripts.secrets.with_raw_response.list(
              script_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
              dispatch_namespace="my-dispatch-namespace",
          )