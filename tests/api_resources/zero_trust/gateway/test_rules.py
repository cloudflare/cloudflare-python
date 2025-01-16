# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.gateway import (
    GatewayRule,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            expiration={
                "expires_at": parse_datetime("2014-01-01T05:20:20Z"),
                "duration": 10,
                "expired": False,
            },
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {"foo": "string"},
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "copy": "enabled",
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "download": "enabled",
                    "dp": False,
                    "du": False,
                    "keyboard": "enabled",
                    "paste": "enabled",
                    "printing": "enabled",
                    "upload": "enabled",
                    "version": "v1",
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2.2.2.2",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "ignore_cname_category_matches": True,
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "msg",
                    "support_url": "support_url",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "quarantine": {"file_types": ["exe"]},
                "resolve_dns_internally": {
                    "fallback": "none",
                    "view_id": "view_id",
                },
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "pass_through"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.create(
                account_id="",
                action="on",
                name="block bad websites",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            expiration={
                "expires_at": parse_datetime("2014-01-01T05:20:20Z"),
                "duration": 10,
                "expired": False,
            },
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {"foo": "string"},
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "copy": "enabled",
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "download": "enabled",
                    "dp": False,
                    "du": False,
                    "keyboard": "enabled",
                    "paste": "enabled",
                    "printing": "enabled",
                    "upload": "enabled",
                    "version": "v1",
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2.2.2.2",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "ignore_cname_category_matches": True,
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "msg",
                    "support_url": "support_url",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "quarantine": {"file_types": ["exe"]},
                "resolve_dns_internally": {
                    "fallback": "none",
                    "view_id": "view_id",
                },
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "pass_through"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                action="on",
                name="block bad websites",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.update(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                action="on",
                name="block bad websites",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[GatewayRule], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[GatewayRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncSinglePage[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(object, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.delete(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.get(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.get(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_reset_expiration(self, client: Cloudflare) -> None:
        rule = client.zero_trust.gateway.rules.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_raw_response_reset_expiration(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_reset_expiration(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.rules.with_streaming_response.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_expiration(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            expiration={
                "expires_at": parse_datetime("2014-01-01T05:20:20Z"),
                "duration": 10,
                "expired": False,
            },
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {"foo": "string"},
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "copy": "enabled",
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "download": "enabled",
                    "dp": False,
                    "du": False,
                    "keyboard": "enabled",
                    "paste": "enabled",
                    "printing": "enabled",
                    "upload": "enabled",
                    "version": "v1",
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2.2.2.2",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "ignore_cname_category_matches": True,
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "msg",
                    "support_url": "support_url",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "quarantine": {"file_types": ["exe"]},
                "resolve_dns_internally": {
                    "fallback": "none",
                    "view_id": "view_id",
                },
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "pass_through"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.create(
                account_id="",
                action="on",
                name="block bad websites",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
            description="Block bad websites based on their host name.",
            device_posture='any(device_posture.checks.passed[*] in {"1308749e-fcfb-4ebc-b051-fe022b632644"})',
            enabled=True,
            expiration={
                "expires_at": parse_datetime("2014-01-01T05:20:20Z"),
                "duration": 10,
                "expired": False,
            },
            filters=["http"],
            identity='any(identity.groups.name[*] in {"finance"})',
            precedence=0,
            rule_settings={
                "add_headers": {"foo": "string"},
                "allow_child_bypass": False,
                "audit_ssh": {"command_logging": False},
                "biso_admin_controls": {
                    "copy": "enabled",
                    "dcp": False,
                    "dd": False,
                    "dk": False,
                    "download": "enabled",
                    "dp": False,
                    "du": False,
                    "keyboard": "enabled",
                    "paste": "enabled",
                    "printing": "enabled",
                    "upload": "enabled",
                    "version": "v1",
                },
                "block_page_enabled": True,
                "block_reason": "This website is a security risk",
                "bypass_parent_rule": False,
                "check_session": {
                    "duration": "300s",
                    "enforce": True,
                },
                "dns_resolvers": {
                    "ipv4": [
                        {
                            "ip": "2.2.2.2",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                    "ipv6": [
                        {
                            "ip": "2001:DB8::",
                            "port": 5053,
                            "route_through_private_network": True,
                            "vnet_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                        }
                    ],
                },
                "egress": {
                    "ipv4": "192.0.2.2",
                    "ipv4_fallback": "192.0.2.3",
                    "ipv6": "2001:DB8::/64",
                },
                "ignore_cname_category_matches": True,
                "insecure_disable_dnssec_validation": False,
                "ip_categories": True,
                "ip_indicator_feeds": True,
                "l4override": {
                    "ip": "1.1.1.1",
                    "port": 0,
                },
                "notification_settings": {
                    "enabled": True,
                    "msg": "msg",
                    "support_url": "support_url",
                },
                "override_host": "example.com",
                "override_ips": ["1.1.1.1", "2.2.2.2"],
                "payload_log": {"enabled": True},
                "quarantine": {"file_types": ["exe"]},
                "resolve_dns_internally": {
                    "fallback": "none",
                    "view_id": "view_id",
                },
                "resolve_dns_through_cloudflare": True,
                "untrusted_cert": {"action": "pass_through"},
            },
            schedule={
                "fri": "08:00-12:30,13:30-17:00",
                "mon": "08:00-12:30,13:30-17:00",
                "sat": "08:00-12:30,13:30-17:00",
                "sun": "08:00-12:30,13:30-17:00",
                "thu": "08:00-12:30,13:30-17:00",
                "time_zone": "America/New York",
                "tue": "08:00-12:30,13:30-17:00",
                "wed": "08:00-12:30,13:30-17:00",
            },
            traffic='http.request.uri matches ".*a/partial/uri.*" and http.request.host in $01302951-49f9-47c9-a400-0297e60b6a10',
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            action="on",
            name="block bad websites",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                action="on",
                name="block bad websites",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.update(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                action="on",
                name="block bad websites",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncSinglePage[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(object, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.delete(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.get(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.get(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_reset_expiration(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.gateway.rules.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_reset_expiration(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[GatewayRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_reset_expiration(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.rules.with_streaming_response.reset_expiration(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[GatewayRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_expiration(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.gateway.rules.with_raw_response.reset_expiration(
                rule_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
