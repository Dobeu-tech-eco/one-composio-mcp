from one_composio_mcp.config import BridgeConfig, ProfileConfig
from one_composio_mcp.profiles import resolve_session_options


def test_resolve_session_options_maps_aliases():
    cfg = BridgeConfig(
        api_key="ak_test",
        user_id="user-1",
        default_profile="phase1_cloud",
        profiles={
            "phase1_cloud": ProfileConfig(
                toolkits=["googledrive", "outlook"],
                connected_accounts={
                    "googledrive": "gdrive_work",
                    "outlook": "outlook_work",
                },
            )
        },
        connected_account_aliases={
            "gdrive_work": "ca_gdrive",
            "outlook_work": "ca_outlook",
        },
    )
    opts = resolve_session_options(cfg, "phase1_cloud")
    assert opts["toolkits"] == ["googledrive", "outlook"]
    assert opts["connected_accounts"] == {
        "googledrive": "ca_gdrive",
        "outlook": "ca_outlook",
    }
