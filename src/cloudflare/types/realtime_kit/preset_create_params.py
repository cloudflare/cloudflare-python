# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PresetCreateParams",
    "Config",
    "ConfigMaxVideoStreams",
    "ConfigMedia",
    "ConfigMediaScreenshare",
    "ConfigMediaVideo",
    "ConfigMediaAudio",
    "UI",
    "UIDesignTokens",
    "UIDesignTokensColors",
    "UIDesignTokensColorsBackground",
    "UIDesignTokensColorsBrand",
    "Permissions",
    "PermissionsChat",
    "PermissionsChatPrivate",
    "PermissionsChatPublic",
    "PermissionsConnectedMeetings",
    "PermissionsMedia",
    "PermissionsMediaAudio",
    "PermissionsMediaScreenshare",
    "PermissionsMediaVideo",
    "PermissionsPlugins",
    "PermissionsPluginsConfig",
    "PermissionsPluginsConfigUnionMember1",
    "PermissionsPolls",
]


class PresetCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    config: Required[Config]

    name: Required[str]
    """Name of the preset"""

    ui: Required[UI]

    permissions: Permissions


class ConfigMaxVideoStreams(TypedDict, total=False):
    """Maximum number of streams that are visible on a device"""

    desktop: Required[int]
    """Maximum number of video streams visible on desktop devices"""

    mobile: Required[int]
    """Maximum number of streams visible on mobile devices"""


class ConfigMediaScreenshare(TypedDict, total=False):
    """Configuration options for participant screen shares"""

    frame_rate: Required[int]
    """Frame rate of screen share"""

    quality: Required[Literal["hd", "vga", "qvga"]]
    """Quality of screen share"""


class ConfigMediaVideo(TypedDict, total=False):
    """Configuration options for participant videos"""

    frame_rate: Required[int]
    """Frame rate of participants' video"""

    quality: Required[Literal["hd", "vga", "qvga"]]
    """Video quality of participants"""


class ConfigMediaAudio(TypedDict, total=False):
    """Control options for Audio quality."""

    enable_high_bitrate: bool
    """Enable High Quality Audio for your meetings"""

    enable_stereo: bool
    """Enable Stereo for your meetings"""


class ConfigMedia(TypedDict, total=False):
    """Media configuration options. eg: Video quality"""

    screenshare: Required[ConfigMediaScreenshare]
    """Configuration options for participant screen shares"""

    video: Required[ConfigMediaVideo]
    """Configuration options for participant videos"""

    audio: ConfigMediaAudio
    """Control options for Audio quality."""


class Config(TypedDict, total=False):
    max_screenshare_count: Required[int]
    """Maximum number of screen shares that can be active at a given time"""

    max_video_streams: Required[ConfigMaxVideoStreams]
    """Maximum number of streams that are visible on a device"""

    media: Required[ConfigMedia]
    """Media configuration options. eg: Video quality"""

    view_type: Required[Literal["GROUP_CALL", "WEBINAR", "AUDIO_ROOM"]]
    """Type of the meeting"""


class UIDesignTokensColorsBackground(TypedDict, total=False):
    _1000: Required[Annotated[str, PropertyInfo(alias="1000")]]

    _600: Required[Annotated[str, PropertyInfo(alias="600")]]

    _700: Required[Annotated[str, PropertyInfo(alias="700")]]

    _800: Required[Annotated[str, PropertyInfo(alias="800")]]

    _900: Required[Annotated[str, PropertyInfo(alias="900")]]


class UIDesignTokensColorsBrand(TypedDict, total=False):
    _300: Required[Annotated[str, PropertyInfo(alias="300")]]

    _400: Required[Annotated[str, PropertyInfo(alias="400")]]

    _500: Required[Annotated[str, PropertyInfo(alias="500")]]

    _600: Required[Annotated[str, PropertyInfo(alias="600")]]

    _700: Required[Annotated[str, PropertyInfo(alias="700")]]


class UIDesignTokensColors(TypedDict, total=False):
    background: Required[UIDesignTokensColorsBackground]

    brand: Required[UIDesignTokensColorsBrand]

    danger: Required[str]

    success: Required[str]

    text: Required[str]

    text_on_brand: Required[str]

    video_bg: Required[str]

    warning: Required[str]


class UIDesignTokens(TypedDict, total=False):
    border_radius: Required[Literal["rounded"]]

    border_width: Required[Literal["thin"]]

    colors: Required[UIDesignTokensColors]

    logo: Required[str]

    spacing_base: Required[float]

    theme: Required[Literal["dark"]]


class UI(TypedDict, total=False):
    design_tokens: Required[UIDesignTokens]

    config_diff: object


class PermissionsChatPrivate(TypedDict, total=False):
    can_receive: Required[bool]

    can_send: Required[bool]

    files: Required[bool]

    text: Required[bool]


class PermissionsChatPublic(TypedDict, total=False):
    can_send: Required[bool]
    """Can send messages in general"""

    files: Required[bool]
    """Can send file messages"""

    text: Required[bool]
    """Can send text messages"""


class PermissionsChat(TypedDict, total=False):
    """Chat permissions"""

    private: Required[PermissionsChatPrivate]

    public: Required[PermissionsChatPublic]


class PermissionsConnectedMeetings(TypedDict, total=False):
    can_alter_connected_meetings: Required[bool]

    can_switch_connected_meetings: Required[bool]

    can_switch_to_parent_meeting: Required[bool]


class PermissionsMediaAudio(TypedDict, total=False):
    """Audio permissions"""

    can_produce: Required[Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]]
    """Can produce audio"""


class PermissionsMediaScreenshare(TypedDict, total=False):
    """Screenshare permissions"""

    can_produce: Required[Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]]
    """Can produce screen share video"""


class PermissionsMediaVideo(TypedDict, total=False):
    """Video permissions"""

    can_produce: Required[Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]]
    """Can produce video"""


class PermissionsMedia(TypedDict, total=False):
    """Media permissions"""

    audio: Required[PermissionsMediaAudio]
    """Audio permissions"""

    screenshare: Required[PermissionsMediaScreenshare]
    """Screenshare permissions"""

    video: Required[PermissionsMediaVideo]
    """Video permissions"""


class PermissionsPluginsConfigUnionMember1(TypedDict, total=False):
    access_control: Required[Literal["FULL_ACCESS", "VIEW_ONLY"]]

    handles_view_only: Required[bool]


PermissionsPluginsConfig: TypeAlias = Union[str, PermissionsPluginsConfigUnionMember1]


class PermissionsPlugins(TypedDict, total=False):
    """Plugin permissions"""

    can_close: Required[bool]
    """Can close plugins that are already open"""

    can_edit_config: Required[bool]
    """Can edit plugin config"""

    can_start: Required[bool]
    """Can start plugins"""

    config: Required[PermissionsPluginsConfig]


class PermissionsPolls(TypedDict, total=False):
    """Poll permissions"""

    can_create: Required[bool]
    """Can create polls"""

    can_view: Required[bool]
    """Can view polls"""

    can_vote: Required[bool]
    """Can vote on polls"""


class Permissions(TypedDict, total=False):
    accept_waiting_requests: Required[bool]
    """Whether this participant can accept waiting requests"""

    can_accept_production_requests: Required[bool]

    can_change_participant_permissions: Required[bool]

    can_edit_display_name: Required[bool]

    can_livestream: Required[bool]

    can_record: Required[bool]

    can_spotlight: Required[bool]

    chat: Required[PermissionsChat]
    """Chat permissions"""

    connected_meetings: Required[PermissionsConnectedMeetings]

    disable_participant_audio: Required[bool]

    disable_participant_screensharing: Required[bool]

    disable_participant_video: Required[bool]

    hidden_participant: Required[bool]
    """Whether this participant is visible to others or not"""

    kick_participant: Required[bool]

    media: Required[PermissionsMedia]
    """Media permissions"""

    pin_participant: Required[bool]

    plugins: Required[PermissionsPlugins]
    """Plugin permissions"""

    polls: Required[PermissionsPolls]
    """Poll permissions"""

    recorder_type: Required[Literal["RECORDER", "LIVESTREAMER", "NONE"]]
    """Type of the recording peer"""

    show_participant_list: Required[bool]

    waiting_room_type: Required[Literal["SKIP", "ON_PRIVILEGED_USER_ENTRY", "SKIP_ON_ACCEPT"]]
    """Waiting room type"""

    is_recorder: bool
