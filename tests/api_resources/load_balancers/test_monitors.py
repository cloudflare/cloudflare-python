# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.load_balancers import (
    MonitorCreateResponse,
    MonitorUpdateResponse,
    MonitorListResponse,
    MonitorDeleteResponse,
    MonitorGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers import monitor_create_params
from cloudflare.types.load_balancers import monitor_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.create(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.update(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
                expected_codes="2xx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.with_streaming_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.delete(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        monitor = client.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorGetResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.get(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.load_balancers.monitors.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncMonitors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorCreateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.create(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.update(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
                expected_codes="2xx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Optional[MonitorListResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.with_streaming_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.delete(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorGetResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.get(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.load_balancers.monitors.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
