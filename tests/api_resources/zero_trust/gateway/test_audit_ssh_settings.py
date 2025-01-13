# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.gateway import GatewaySettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditSSHSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.zero_trust.gateway.audit_ssh_settings.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.audit_ssh_settings.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.audit_ssh_settings.with_raw_response.update(
                account_id="",
                public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.zero_trust.gateway.audit_ssh_settings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.audit_ssh_settings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.audit_ssh_settings.with_raw_response.get(
                account_id="",
            )

    @parametrize
    def test_method_rotate_seed(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.zero_trust.gateway.audit_ssh_settings.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_raw_response_rotate_seed(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.audit_ssh_settings.with_raw_response.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    def test_streaming_response_rotate_seed(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate_seed(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.audit_ssh_settings.with_raw_response.rotate_seed(
                account_id="",
            )


class TestAsyncAuditSSHSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.zero_trust.gateway.audit_ssh_settings.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = await response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.update(
            account_id="699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = await response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.update(
                account_id="",
                public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.zero_trust.gateway.audit_ssh_settings.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = await response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.get(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = await response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.get(
                account_id="",
            )

    @parametrize
    async def test_method_rotate_seed(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.zero_trust.gateway.audit_ssh_settings.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_raw_response_rotate_seed(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = await response.parse()
        assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

    @parametrize
    async def test_streaming_response_rotate_seed(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.audit_ssh_settings.with_streaming_response.rotate_seed(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = await response.parse()
            assert_matches_type(Optional[GatewaySettings], audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate_seed(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.audit_ssh_settings.with_raw_response.rotate_seed(
                account_id="",
            )
