#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


CHECK_SCHEMA_VERSION = "0.2.2"

REMEDIATION_MAP = {
    "android_project_detected": {
        "priority": 0,
        "files": [],
        "action": "Point the doctor at the actual Android project root that contains the target app module.",
    },
    "android_manifest_found": {
        "priority": 0,
        "files": ["app/src/main/AndroidManifest.xml"],
        "action": "Make sure the target project includes the Android manifest under the app module or adjust the project root.",
    },
    "app_gradle_found": {
        "priority": 0,
        "files": ["app/build.gradle", "app/build.gradle.kts"],
        "action": "Make sure the target project exposes the app-level Gradle file under the expected module path.",
    },
    "hero_aar_present": {
        "priority": 1,
        "files": ["app/libs/HeroUSDK.aar"],
        "action": "Copy the official HeroUSDK.aar into the app libs directory or the project path scanned by the doctor.",
    },
    "herosdkcfg_present": {
        "priority": 1,
        "files": ["app/src/main/assets/herosdkcfg.xml"],
        "action": "Add herosdkcfg.xml to the app assets directory and keep it under source control.",
    },
    "herosdkcfg_has_product_placeholders": {
        "priority": 1,
        "files": ["app/src/main/assets/herosdkcfg.xml"],
        "action": "Populate herosdkcfg.xml with the expected USDK keys or placeholders so AI and integrators know what must be filled later.",
    },
    "manifest_install_location_auto": {
        "priority": 1,
        "files": ["app/src/main/AndroidManifest.xml"],
        "action": "Set android:installLocation=\"auto\" on the manifest root if the packaging path requires it.",
    },
    "manifest_application_name_present": {
        "priority": 1,
        "files": ["app/src/main/AndroidManifest.xml"],
        "action": "Declare the owning Application class in AndroidManifest.xml so USDK can attach through the intended application entry point.",
    },
    "gradle_flatdir_present": {
        "priority": 1,
        "files": ["app/build.gradle", "app/build.gradle.kts"],
        "action": "Add a flatDir libs repository or switch to the provider-approved artifact resolution path for HeroUSDK.",
    },
    "gradle_herousdk_dependency_present": {
        "priority": 1,
        "files": ["app/build.gradle", "app/build.gradle.kts"],
        "action": "Add the HeroUSDK dependency declaration to the app module dependencies block.",
    },
    "gradle_sdk_variant_detected": {
        "priority": 1,
        "files": ["app/build.gradle", "app/build.gradle.kts"],
        "action": "Make the SDK variant explicit by aligning the project to either the legacy android/support path or the androidx path.",
    },
    "application_extends_sdkapplication": {
        "priority": 1,
        "files": ["Application class", "app/src/main/AndroidManifest.xml"],
        "action": "Update the owning Application class to extend SdkApplication and wire that class through the manifest.",
    },
    "splash_extends_sdksplashactivity": {
        "priority": 1,
        "files": ["Splash or launch activity"],
        "action": "Attach USDK splash integration by making the launch splash activity extend SdkSplashActivity.",
    },
    "protocol_listener_present": {
        "priority": 2,
        "files": ["Splash or launch activity"],
        "action": "If you use SDK-hosted consent UI, set an IProtocolListener before calling init.",
    },
    "agree_protocol_present": {
        "priority": 2,
        "files": ["Splash or launch activity", "consent flow owner"],
        "action": "If you use self-hosted consent UI, call setAgreeProtocol after the user accepts the protocol.",
    },
    "runtime_protocol_gate_present": {
        "priority": 1,
        "files": ["Splash or launch activity", "consent flow owner"],
        "action": "Make init happen only after protocol consent, either through setProtocolListener or through setAgreeProtocol in your own consent flow.",
    },
    "init_call_present": {
        "priority": 1,
        "files": ["Splash or launch activity", "integration wrapper"],
        "action": "Add the HeroSdk init call to the runtime chain after protocol consent.",
    },
    "login_call_present": {
        "priority": 1,
        "files": ["Login entry point", "main game activity"],
        "action": "Add a HeroSdk login call at the chosen login entry point.",
    },
    "enter_game_call_present": {
        "priority": 1,
        "files": ["Role entry point", "main game activity"],
        "action": "Upload role data with enterGame after login succeeds and real role data is available.",
    },
    "create_new_role_call_present": {
        "priority": 1,
        "files": ["Role creation flow owner", "main game activity"],
        "action": "Add createNewRole at the real role-creation event instead of startup or unrelated UI.",
    },
    "role_level_up_call_present": {
        "priority": 1,
        "files": ["Role level-up flow owner", "main game activity"],
        "action": "Add roleLevelUp at the real role-upgrade event instead of startup or unrelated UI.",
    },
    "pay_call_present": {
        "priority": 1,
        "files": ["Purchase flow owner"],
        "action": "Add the HeroSdk pay call to the real purchase flow with OrderInfo and RoleInfo.",
    },
    "kick_listener_present": {
        "priority": 1,
        "files": ["Account or session owner"],
        "action": "Register setKickListener before runtime entry points so forced offline or anti-addiction kick events can be handled in the game flow.",
    },
    "logout_call_present": {
        "priority": 2,
        "files": ["Account or session owner"],
        "action": "Wire logout handling so the game can return to the correct post-logout state.",
    },
    "exit_call_present": {
        "priority": 2,
        "files": ["Exit flow owner"],
        "action": "Wire the USDK exit call into the game exit path after checking whether the channel owns the exit dialog.",
    },
    "lifecycle_oncreate_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onCreate into HeroSdk.",
    },
    "lifecycle_onnewintent_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onNewIntent into HeroSdk.",
    },
    "lifecycle_onstart_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onStart into HeroSdk.",
    },
    "lifecycle_onresume_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onResume into HeroSdk.",
    },
    "lifecycle_onpause_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onPause into HeroSdk.",
    },
    "lifecycle_onstop_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onStop into HeroSdk.",
    },
    "lifecycle_onrestart_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onRestart into HeroSdk.",
    },
    "lifecycle_ondestroy_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onDestroy into HeroSdk.",
    },
    "lifecycle_onactivityresult_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onActivityResult into HeroSdk.",
    },
    "lifecycle_onrequestpermissionsresult_forwarded": {
        "priority": 2,
        "files": ["Main activity or integration wrapper"],
        "action": "Forward Activity onRequestPermissionsResult into HeroSdk.",
    },
}


def make_check(check_id, level, status, message, evidence=None):
    item = {
        "id": check_id,
        "level": level,
        "status": status,
        "message": message,
    }
    if evidence:
        item["evidence"] = evidence
    return item


def attach_remediation(check):
    remediation = REMEDIATION_MAP.get(check["id"])
    if remediation and check["status"] in {"failed", "warning"}:
        check["remediation"] = remediation
    return check


def read_text(path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def find_files(root, names):
    found = []
    for name in names:
        found.extend(root.rglob(name))
    return found


def first_existing(paths):
    for path in paths:
        if path.exists():
            return path
    return None


def search_any(root, patterns, suffixes=None):
    matches = []
    suffixes = suffixes or {".java", ".kt", ".gradle", ".kts", ".xml"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in suffixes:
            continue
        text = read_text(path)
        for pattern in patterns:
            if re.search(pattern, text):
                matches.append(str(path.relative_to(root)))
                break
    return sorted(set(matches))


def detect_project_type(manifest_path, gradle_path):
    if manifest_path and gradle_path:
        return "android_native"
    if manifest_path or gradle_path:
        return "android_export_shell"
    return "unknown"


def detect_sdk_variant(gradle_text):
    uses_androidx = bool(re.search(r"androidx\.", gradle_text))
    uses_support = bool(re.search(r"android-support-v4\.jar|com\.android\.support", gradle_text))

    if uses_androidx and uses_support:
        return "mixed"
    if uses_androidx:
        return "androidx"
    if uses_support:
        return "android"
    return "unknown"


def detect_settings_repo_mode(settings_text):
    if "RepositoriesMode.FAIL_ON_PROJECT_REPOS" in settings_text:
        return "fail_on_project_repos"
    if "RepositoriesMode.PREFER_SETTINGS" in settings_text:
        return "prefer_settings"
    return "unknown"


def extract_application_name(manifest_text):
    match = re.search(r"<application\b[^>]*android:name\s*=\s*[\"']([^\"']+)[\"']", manifest_text)
    return match.group(1) if match else None


def build_suggested_next_steps(checks):
    failed_ids = {check["id"] for check in checks if check["status"] == "failed"}
    warning_ids = {check["id"] for check in checks if check["status"] == "warning"}
    steps = []

    if "android_project_detected" in failed_ids:
        steps.append("Point the doctor at a real Android project root that contains an app module or manifest.")
    if {"hero_aar_present", "herosdkcfg_present"} & failed_ids:
        steps.append("Import official USDK resources first so the project has HeroUSDK.aar and herosdkcfg.xml.")
    if {"gradle_herousdk_dependency_present", "gradle_flatdir_present"} & failed_ids:
        steps.append("Wire USDK into the app Gradle file, including local libs lookup and the HeroUSDK dependency.")
    if {"application_extends_sdkapplication", "manifest_application_name_present"} & failed_ids:
        steps.append("Connect the project Application class to SdkApplication and point AndroidManifest.xml at it.")
    if "splash_extends_sdksplashactivity" in failed_ids:
        steps.append("Attach USDK splash integration by making the launch splash activity extend SdkSplashActivity.")
    runtime_failures = {
        "init_call_present",
        "login_call_present",
        "enter_game_call_present",
        "create_new_role_call_present",
        "role_level_up_call_present",
        "pay_call_present",
        "kick_listener_present",
        "logout_call_present",
        "exit_call_present",
    }
    if runtime_failures & failed_ids:
        steps.append("Implement the required runtime chain: protocol handling, init, login, enterGame, pay, logout/exit.")
    lifecycle_failures = {check["id"] for check in checks if check["id"].startswith("lifecycle_") and check["status"] == "failed"}
    if lifecycle_failures:
        steps.append("Forward the required Activity lifecycle callbacks into HeroSdk before treating the integration as complete.")
    if "runtime_protocol_gate_present" in failed_ids or "runtime_protocol_gate_present" in warning_ids:
        steps.append("Make sure init only happens after protocol consent or after explicitly calling setAgreeProtocol for self-hosted consent.")

    steps.append("Provide real provider-side values for product, payment, and protocol configuration.")
    steps.append("Re-run usdk_doctor.py after each integration pass.")
    return steps


def build_prioritized_repairs(checks):
    repairs = []
    seen = set()
    for check in checks:
        remediation = check.get("remediation")
        if not remediation:
            continue
        key = (check["id"], check["status"])
        if key in seen:
            continue
        seen.add(key)
        repairs.append({
            "check_id": check["id"],
            "status": check["status"],
            "priority": remediation["priority"],
            "action": remediation["action"],
            "files": remediation["files"],
        })
    repairs.sort(key=lambda item: (item["priority"], item["check_id"]))
    return repairs


def main():
    parser = argparse.ArgumentParser(description="Static USDK integration doctor for Android projects.")
    parser.add_argument("--project-root", default=".", help="Target project root.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    checks = []

    manifest_candidates = find_files(root, ["AndroidManifest.xml"])
    gradle_candidates = find_files(root, ["build.gradle", "build.gradle.kts"])
    settings_candidates = find_files(root, ["settings.gradle", "settings.gradle.kts"])
    herosdkcfg_candidates = find_files(root, ["herosdkcfg.xml"])
    aar_candidates = find_files(root, ["HeroUSDK.aar"])

    manifest_path = first_existing([
        root / "app" / "src" / "main" / "AndroidManifest.xml",
        root / "src" / "main" / "AndroidManifest.xml",
    ]) or (manifest_candidates[0] if manifest_candidates else None)

    gradle_path = first_existing([
        root / "app" / "build.gradle",
        root / "app" / "build.gradle.kts",
    ]) or (gradle_candidates[0] if gradle_candidates else None)

    settings_path = first_existing([
        root / "settings.gradle",
        root / "settings.gradle.kts",
    ]) or (settings_candidates[0] if settings_candidates else None)

    manifest_text = read_text(manifest_path) if manifest_path else ""
    gradle_text = read_text(gradle_path) if gradle_path else ""
    settings_text = read_text(settings_path) if settings_path else ""
    project_type = detect_project_type(manifest_path, gradle_path)
    sdk_variant = detect_sdk_variant(gradle_text)
    settings_repo_mode = detect_settings_repo_mode(settings_text)

    if project_type == "unknown":
        checks.append(attach_remediation(make_check(
            "android_project_detected",
            "required",
            "failed",
            "No Android manifest or app build file was found under the target root.",
        )))
    else:
        checks.append(attach_remediation(make_check(
            "android_project_detected",
            "required",
            "passed",
            f"Detected Android project shape: {project_type}.",
        )))

    if manifest_path:
        checks.append(attach_remediation(make_check(
            "android_manifest_found",
            "required",
            "passed",
            "AndroidManifest.xml detected.",
            str(manifest_path.relative_to(root)),
        )))
    else:
        checks.append(attach_remediation(make_check(
            "android_manifest_found",
            "required",
            "failed",
            "AndroidManifest.xml not found.",
        )))

    if gradle_path:
        checks.append(attach_remediation(make_check(
            "app_gradle_found",
            "required",
            "passed",
            "App-level Gradle file detected.",
            str(gradle_path.relative_to(root)),
        )))
    else:
        checks.append(attach_remediation(make_check(
            "app_gradle_found",
            "required",
            "failed",
            "App-level Gradle file not found.",
        )))

    if aar_candidates:
        checks.append(attach_remediation(make_check(
            "hero_aar_present",
            "required",
            "passed",
            "HeroUSDK.aar found.",
            str(aar_candidates[0].relative_to(root)),
        )))
    else:
        checks.append(attach_remediation(make_check(
            "hero_aar_present",
            "required",
            "failed",
            "HeroUSDK.aar not found under project root.",
        )))

    if herosdkcfg_candidates:
        cfg_path = herosdkcfg_candidates[0]
        cfg_text = read_text(cfg_path)
        checks.append(attach_remediation(make_check(
            "herosdkcfg_present",
            "required",
            "passed",
            "herosdkcfg.xml found.",
            str(cfg_path.relative_to(root)),
        )))
        if "_hu_pid_" in cfg_text and "_hu_pk_" in cfg_text:
            checks.append(attach_remediation(make_check(
                "herosdkcfg_has_product_placeholders",
                "required",
                "passed",
                "herosdkcfg.xml contains product placeholders.",
            )))
        else:
            checks.append(attach_remediation(make_check(
                "herosdkcfg_has_product_placeholders",
                "required",
                "warning",
                "herosdkcfg.xml exists but expected placeholders were not detected.",
            )))
    else:
        checks.append(attach_remediation(make_check(
            "herosdkcfg_present",
            "required",
            "failed",
            "herosdkcfg.xml not found.",
        )))
        checks.append(attach_remediation(make_check(
            "herosdkcfg_has_product_placeholders",
            "required",
            "failed",
            "Cannot validate product placeholders because herosdkcfg.xml is missing.",
        )))

    if manifest_text:
        if 'android:installLocation="auto"' in manifest_text or "android:installLocation='auto'" in manifest_text:
            checks.append(attach_remediation(make_check(
                "manifest_install_location_auto",
                "required",
                "passed",
                "Manifest installLocation is set to auto.",
            )))
        else:
            checks.append(attach_remediation(make_check(
                "manifest_install_location_auto",
                "required",
                "warning",
                "Manifest installLocation=auto was not detected.",
            )))

        if re.search(r"<application\b", manifest_text):
            checks.append(attach_remediation(make_check(
                "manifest_application_declared",
                "required",
                "passed",
                "Manifest contains an application node.",
            )))
        else:
            checks.append(attach_remediation(make_check(
                "manifest_application_declared",
                "required",
                "failed",
                "Manifest application node was not detected.",
            )))

        application_name = extract_application_name(manifest_text)
        if application_name:
            checks.append(attach_remediation(make_check(
                "manifest_application_name_present",
                "required",
                "passed",
                "Manifest declares android:name on the application node.",
                application_name,
            )))
        else:
            checks.append(attach_remediation(make_check(
                "manifest_application_name_present",
                "required",
                "warning",
                "Manifest application android:name was not detected.",
            )))
    else:
        checks.append(attach_remediation(make_check(
            "manifest_install_location_auto",
            "required",
            "failed",
            "Manifest not available for installLocation validation.",
        )))
        checks.append(attach_remediation(make_check(
            "manifest_application_declared",
            "required",
            "failed",
            "Manifest not available for application node validation.",
        )))
        checks.append(attach_remediation(make_check(
            "manifest_application_name_present",
            "required",
            "failed",
            "Manifest not available for application name validation.",
        )))

    if gradle_text:
        gradle_flatdir_present = bool(re.search(r"flatDir\s*\{[\s\S]*dirs\s+['\"]libs['\"]", gradle_text))
        settings_flatdir_present = bool(re.search(r"flatDir\s*\{[\s\S]*dirs\s+[\"']?\$\{rootDir\}/app/libs[\"']?", settings_text))
        if settings_repo_mode in {"fail_on_project_repos", "prefer_settings"}:
            flatdir_ok = settings_flatdir_present
            flatdir_message = "Settings-level flatDir libs repository detected." if flatdir_ok else "Settings-level flatDir libs repository was not detected."
        else:
            flatdir_ok = gradle_flatdir_present or settings_flatdir_present
            flatdir_message = "Gradle flatDir libs repository detected." if flatdir_ok else "Gradle flatDir libs repository was not detected."

        if flatdir_ok:
            checks.append(attach_remediation(make_check(
                "gradle_flatdir_present",
                "required",
                "passed",
                flatdir_message,
            )))
        else:
            checks.append(attach_remediation(make_check(
                "gradle_flatdir_present",
                "required",
                "warning",
                flatdir_message,
            )))

        if re.search(r"HeroUSDK", gradle_text):
            checks.append(attach_remediation(make_check(
                "gradle_herousdk_dependency_present",
                "required",
                "passed",
                "Gradle mentions the HeroUSDK dependency.",
            )))
        else:
            checks.append(attach_remediation(make_check(
                "gradle_herousdk_dependency_present",
                "required",
                "failed",
                "Gradle does not appear to include a HeroUSDK dependency.",
            )))

        if sdk_variant == "androidx":
            checks.append(attach_remediation(make_check(
                "gradle_sdk_variant_detected",
                "required",
                "passed",
                "Gradle indicates the androidx USDK variant.",
                sdk_variant,
            )))
        elif sdk_variant == "android":
            checks.append(attach_remediation(make_check(
                "gradle_sdk_variant_detected",
                "required",
                "passed",
                "Gradle indicates the legacy android/support USDK variant.",
                sdk_variant,
            )))
        elif sdk_variant == "mixed":
            checks.append(attach_remediation(make_check(
                "gradle_sdk_variant_detected",
                "required",
                "warning",
                "Gradle appears to mix AndroidX and legacy support references.",
                sdk_variant,
            )))
        else:
            checks.append(attach_remediation(make_check(
                "gradle_sdk_variant_detected",
                "required",
                "warning",
                "Could not infer whether the project expects the android or androidx USDK variant.",
                sdk_variant,
            )))
    else:
        checks.append(attach_remediation(make_check(
            "gradle_flatdir_present",
            "required",
            "failed",
            "Gradle file not available for local libs repository validation.",
        )))
        checks.append(attach_remediation(make_check(
            "gradle_herousdk_dependency_present",
            "required",
            "failed",
            "Gradle file not available for HeroUSDK dependency validation.",
        )))
        checks.append(attach_remediation(make_check(
            "gradle_sdk_variant_detected",
            "required",
            "failed",
            "Gradle file not available for sdk variant detection.",
        )))

    code_checks = {
        "application_extends_sdkapplication": ("required", r"extends\s+(?:com\.herosdk\.)?SdkApplication", "SdkApplication inheritance"),
        "splash_extends_sdksplashactivity": ("required", r"extends\s+(?:com\.herosdk\.)?SdkSplashActivity", "SdkSplashActivity inheritance"),
        "protocol_listener_present": ("advisory", r"setProtocolListener\s*\(", "setProtocolListener"),
        "agree_protocol_present": ("advisory", r"setAgreeProtocol\s*\(", "setAgreeProtocol"),
        "init_call_present": (r"\.init\s*\(", "HeroSdk init"),
        "login_call_present": (r"\.login\s*\(", "HeroSdk login"),
        "enter_game_call_present": (r"\.enterGame\s*\(", "HeroSdk enterGame"),
        "create_new_role_call_present": (r"\.createNewRole\s*\(", "HeroSdk createNewRole"),
        "role_level_up_call_present": (r"\.roleLevelUp\s*\(", "HeroSdk roleLevelUp"),
        "pay_call_present": (r"\.pay\s*\(", "HeroSdk pay"),
        "kick_listener_present": (r"\.setKickListener\s*\(", "HeroSdk setKickListener"),
        "logout_call_present": (r"\.logout\s*\(", "HeroSdk logout"),
        "exit_call_present": (r"\.exit\s*\(", "HeroSdk exit"),
        "lifecycle_oncreate_forwarded": (r"\.onCreate\s*\(", "HeroSdk onCreate"),
        "lifecycle_onnewintent_forwarded": (r"\.onNewIntent\s*\(", "HeroSdk onNewIntent"),
        "lifecycle_onstart_forwarded": (r"\.onStart\s*\(", "HeroSdk onStart"),
        "lifecycle_onresume_forwarded": (r"\.onResume\s*\(", "HeroSdk onResume"),
        "lifecycle_onpause_forwarded": (r"\.onPause\s*\(", "HeroSdk onPause"),
        "lifecycle_onstop_forwarded": (r"\.onStop\s*\(", "HeroSdk onStop"),
        "lifecycle_onrestart_forwarded": (r"\.onRestart\s*\(", "HeroSdk onRestart"),
        "lifecycle_ondestroy_forwarded": (r"\.onDestroy\s*\(", "HeroSdk onDestroy"),
        "lifecycle_onactivityresult_forwarded": (r"\.onActivityResult\s*\(", "HeroSdk onActivityResult"),
        "lifecycle_onrequestpermissionsresult_forwarded": (r"\.onRequestPermissionsResult\s*\(", "HeroSdk onRequestPermissionsResult"),
    }

    matched_code_checks = {}
    normalized_code_checks = {}
    for check_id, value in code_checks.items():
        if len(value) == 3:
            normalized_code_checks[check_id] = value
        else:
            normalized_code_checks[check_id] = ("required", value[0], value[1])

    for check_id, (level, pattern, label) in normalized_code_checks.items():
        matches = search_any(root, [pattern])
        matched_code_checks[check_id] = matches
        status = "passed" if matches else "failed"
        message = f"Detected {label}." if matches else f"{label} was not detected."
        checks.append(attach_remediation(make_check(check_id, level, status, message, matches[:5] if matches else None)))

    has_protocol_gate = bool(
        matched_code_checks["protocol_listener_present"] or matched_code_checks["agree_protocol_present"]
    )
    if matched_code_checks["init_call_present"] and has_protocol_gate:
        checks.append(attach_remediation(make_check(
            "runtime_protocol_gate_present",
            "required",
            "passed",
            "Detected both init and a protocol consent gate marker.",
        )))
    elif matched_code_checks["init_call_present"]:
        checks.append(attach_remediation(make_check(
            "runtime_protocol_gate_present",
            "required",
            "warning",
            "Init was detected without a visible protocol consent gate marker.",
        )))
    else:
        checks.append(attach_remediation(make_check(
            "runtime_protocol_gate_present",
            "required",
            "failed",
            "Cannot validate protocol gating because init was not detected.",
        )))

    missing_manual_inputs = [
        "product_id",
        "product_key",
        "sdk_variant",
        "protocol_popup_mode",
        "payment_callback_url",
        "payment_callback_key",
    ]

    required_failed = [check for check in checks if check["level"] == "required" and check["status"] == "failed"]
    required_warning = [check for check in checks if check["level"] == "required" and check["status"] == "warning"]

    if project_type == "unknown":
        overall_status = "blocked_on_project_shape"
    elif required_failed:
        overall_status = "integration_partially_detected"
    elif missing_manual_inputs:
        overall_status = "blocked_on_manual_inputs"
    elif required_warning:
        overall_status = "ready_for_manual_inputs"
    else:
        overall_status = "integration_verified_static"

    result = {
        "check_schema_version": CHECK_SCHEMA_VERSION,
        "project_root": str(root),
        "project_type": project_type,
        "detected_sdk_variant": sdk_variant,
        "summary": {
            "status": overall_status,
            "required_failed_count": len(required_failed),
            "required_warning_count": len(required_warning),
            "check_count": len(checks),
        },
        "checks": checks,
        "prioritized_repairs": build_prioritized_repairs(checks),
        "missing_manual_inputs": missing_manual_inputs,
        "suggested_next_steps": build_suggested_next_steps(checks),
    }

    if args.pretty:
        print(json.dumps(result, ensure_ascii=True, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    main()
