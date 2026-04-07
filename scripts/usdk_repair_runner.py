#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


RUNNER_SCHEMA_VERSION = "0.1.0"

PHASES = [
    {
        "id": "project_shape",
        "title": "Project Shape",
        "checks": [
            "android_project_detected",
            "android_manifest_found",
            "app_gradle_found",
        ],
    },
    {
        "id": "resources_and_variant",
        "title": "Resources And Variant",
        "checks": [
            "hero_aar_present",
            "herosdkcfg_present",
            "herosdkcfg_has_product_placeholders",
            "gradle_flatdir_present",
            "gradle_herousdk_dependency_present",
            "gradle_sdk_variant_detected",
        ],
    },
    {
        "id": "app_entry",
        "title": "Application And Splash Entry",
        "checks": [
            "manifest_application_name_present",
            "application_extends_sdkapplication",
            "splash_extends_sdksplashactivity",
        ],
    },
    {
        "id": "consent_and_runtime",
        "title": "Consent And Runtime Chain",
        "checks": [
            "protocol_listener_present",
            "agree_protocol_present",
            "runtime_protocol_gate_present",
            "init_call_present",
            "login_call_present",
            "enter_game_call_present",
            "pay_call_present",
            "logout_call_present",
            "exit_call_present",
        ],
    },
    {
        "id": "lifecycle",
        "title": "Lifecycle Forwarding",
        "checks": [
            "lifecycle_oncreate_forwarded",
            "lifecycle_onnewintent_forwarded",
            "lifecycle_onstart_forwarded",
            "lifecycle_onresume_forwarded",
            "lifecycle_onpause_forwarded",
            "lifecycle_onstop_forwarded",
            "lifecycle_onrestart_forwarded",
            "lifecycle_ondestroy_forwarded",
            "lifecycle_onactivityresult_forwarded",
            "lifecycle_onrequestpermissionsresult_forwarded",
        ],
    },
]

TEMPLATE_MAP = {
    "application_extends_sdkapplication": [
        "skill/usdk-android-integration/references/templates/application_java.md",
    ],
    "manifest_application_name_present": [
        "skill/usdk-android-integration/references/templates/application_java.md",
    ],
    "splash_extends_sdksplashactivity": [
        "skill/usdk-android-integration/references/templates/splash_activity_java.md",
    ],
    "protocol_listener_present": [
        "skill/usdk-android-integration/references/templates/splash_activity_java.md",
    ],
    "agree_protocol_present": [
        "skill/usdk-android-integration/references/templates/splash_activity_java.md",
    ],
    "runtime_protocol_gate_present": [
        "skill/usdk-android-integration/references/templates/splash_activity_java.md",
    ],
    "init_call_present": [
        "skill/usdk-android-integration/references/templates/splash_activity_java.md",
    ],
    "login_call_present": [
        "skill/usdk-android-integration/references/templates/runtime_chain_java.md",
    ],
    "enter_game_call_present": [
        "skill/usdk-android-integration/references/templates/runtime_chain_java.md",
    ],
    "pay_call_present": [
        "skill/usdk-android-integration/references/templates/runtime_chain_java.md",
    ],
    "logout_call_present": [
        "skill/usdk-android-integration/references/templates/runtime_chain_java.md",
    ],
    "exit_call_present": [
        "skill/usdk-android-integration/references/templates/runtime_chain_java.md",
    ],
    "lifecycle_oncreate_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onnewintent_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onstart_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onresume_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onpause_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onstop_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onrestart_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_ondestroy_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onactivityresult_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "lifecycle_onrequestpermissionsresult_forwarded": [
        "skill/usdk-android-integration/references/templates/activity_lifecycle_forwarding_java.md",
    ],
    "gradle_flatdir_present": [
        "skill/usdk-android-integration/references/templates/gradle_androidx.md",
        "skill/usdk-android-integration/references/templates/gradle_legacy_android.md",
    ],
    "gradle_herousdk_dependency_present": [
        "skill/usdk-android-integration/references/templates/gradle_androidx.md",
        "skill/usdk-android-integration/references/templates/gradle_legacy_android.md",
    ],
    "gradle_sdk_variant_detected": [
        "skill/usdk-android-integration/references/templates/gradle_androidx.md",
        "skill/usdk-android-integration/references/templates/gradle_legacy_android.md",
    ],
}


def load_doctor_result(project_root: Path, doctor_result_path: Path | None):
    if doctor_result_path:
        return json.loads(doctor_result_path.read_text(encoding="utf-8"))

    script_path = Path(__file__).with_name("usdk_doctor.py")
    cmd = [sys.executable, str(script_path), "--project-root", str(project_root)]
    completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(completed.stdout)


def phase_for_check(check_id: str):
    for phase in PHASES:
        if check_id in phase["checks"]:
            return phase["id"], phase["title"]
    return "other", "Other"


def unique_items(items):
    seen = set()
    ordered = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def build_phase_plan(doctor_result):
    repairs = doctor_result.get("prioritized_repairs", [])
    phase_buckets = []
    for phase in PHASES:
        phase_repairs = []
        for repair in repairs:
            phase_id, _ = phase_for_check(repair["check_id"])
            if phase_id != phase["id"]:
                continue
            phase_repairs.append({
                "check_id": repair["check_id"],
                "priority": repair["priority"],
                "status": repair["status"],
                "action": repair["action"],
                "files": repair["files"],
                "templates": TEMPLATE_MAP.get(repair["check_id"], []),
            })
        if phase_repairs:
            phase_buckets.append({
                "phase_id": phase["id"],
                "title": phase["title"],
                "repairs": phase_repairs,
                "edit_scope": unique_items(
                    file for repair in phase_repairs for file in repair["files"]
                ),
                "template_scope": unique_items(
                    template for repair in phase_repairs for template in repair["templates"]
                ),
            })
    return phase_buckets


def build_runner_result(doctor_result):
    status = doctor_result["summary"]["status"]
    phase_plan = build_phase_plan(doctor_result)
    assumptions = []

    if doctor_result.get("detected_sdk_variant") == "androidx":
        assumptions.append("Use AndroidX-oriented Gradle templates unless the target project proves otherwise.")
    elif doctor_result.get("detected_sdk_variant") == "android":
        assumptions.append("Use legacy support-oriented Gradle templates unless the target project is being migrated.")

    if any(
        repair["check_id"] in {"protocol_listener_present", "runtime_protocol_gate_present", "init_call_present"}
        for phase in phase_plan
        for repair in phase["repairs"]
    ):
        assumptions.append("Choose one consent path before wiring init: SDK-hosted or self-hosted.")

    if status == "blocked_on_project_shape":
        summary = "Do not edit code yet. Fix project targeting first."
    elif status == "blocked_on_manual_inputs":
        summary = "Static engineering checks are clear. Remaining work is provider-side manual input and runtime verification."
    else:
        summary = "Use the phased repair plan to clear the remaining static integration issues."

    return {
        "runner_schema_version": RUNNER_SCHEMA_VERSION,
        "project_root": doctor_result["project_root"],
        "project_type": doctor_result["project_type"],
        "doctor_summary": doctor_result["summary"],
        "summary": summary,
        "phase_plan": phase_plan,
        "manual_inputs": doctor_result.get("missing_manual_inputs", []),
        "assumptions": assumptions,
        "source_doctor_checks": len(doctor_result.get("checks", [])),
    }


def format_markdown(result):
    lines = []
    lines.append("# USDK Repair Plan")
    lines.append("")
    lines.append(f"- Project root: `{result['project_root']}`")
    lines.append(f"- Project type: `{result['project_type']}`")
    lines.append(f"- Doctor status: `{result['doctor_summary']['status']}`")
    lines.append("")
    lines.append(result["summary"])
    lines.append("")

    if result["phase_plan"]:
        lines.append("## Phases")
        lines.append("")
        for phase in result["phase_plan"]:
            lines.append(f"### {phase['title']}")
            lines.append("")
            lines.append("Edit scope:")
            for item in phase["edit_scope"]:
                lines.append(f"- `{item}`")
            if phase["template_scope"]:
                lines.append("Templates:")
                for item in phase["template_scope"]:
                    lines.append(f"- `{item}`")
            lines.append("Repairs:")
            for repair in phase["repairs"]:
                lines.append(f"- `{repair['check_id']}`: {repair['action']}")
            lines.append("")

    if result["manual_inputs"]:
        lines.append("## Manual Inputs")
        lines.append("")
        for item in result["manual_inputs"]:
            lines.append(f"- `{item}`")
        lines.append("")

    if result["assumptions"]:
        lines.append("## Assumptions")
        lines.append("")
        for item in result["assumptions"]:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Generate a phased USDK repair plan from doctor results.")
    parser.add_argument("--project-root", default=".", help="Target project root.")
    parser.add_argument("--doctor-result", help="Optional path to a saved doctor JSON result.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", help="Output format.")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    doctor_result_path = Path(args.doctor_result).resolve() if args.doctor_result else None
    doctor_result = load_doctor_result(project_root, doctor_result_path)
    runner_result = build_runner_result(doctor_result)

    if args.format == "markdown":
        print(format_markdown(runner_result))
    else:
        print(json.dumps(runner_result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
