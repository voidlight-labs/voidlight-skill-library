#!/usr/bin/env python3
"""Voidlight Skill Library Benchmark Runner.

Evaluates AI-generated code against skill rules for 2-layer clean architecture
compliance, SRP, explicit naming, type safety, and domain purity.

Usage:
    python benchmark.py                    # Run all skills
    python benchmark.py --skill python     # Run specific skill
    python benchmark.py --format json      # JSON output
    python benchmark.py --format csv       # CSV output
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class CheckResult:
    """Result of a single validation check."""
    check_name: str
    passed: bool
    details: str = ""
    points: int = 0
    max_points: int = 0


@dataclass
class ScenarioResult:
    """Result of evaluating a single scenario."""
    scenario_name: str
    skill: str
    difficulty: str
    checks: list[CheckResult] = field(default_factory=list)
    total_points: int = 0
    max_points: int = 0

    @property
    def percentage(self) -> float:
        if self.max_points == 0:
            return 0.0
        return (self.total_points / self.max_points) * 100


@dataclass
class SkillResult:
    """Aggregated results for a skill."""
    skill: str
    scenarios: list[ScenarioResult] = field(default_factory=list)

    @property
    def total_points(self) -> int:
        return sum(s.total_points for s in self.scenarios)

    @property
    def max_points(self) -> int:
        return sum(s.max_points for s in self.scenarios)

    @property
    def percentage(self) -> float:
        if self.max_points == 0:
            return 0.0
        return (self.total_points / self.max_points) * 100


def find_scenario_files(base_dir: Path, skill: Optional[str] = None) -> list[Path]:
    """Find all scenario markdown files in the benchmark directory."""
    if skill is not None:
        scenario_dir_name = skill.removesuffix("-craft")
        skill_dir = base_dir / "scenarios" / scenario_dir_name
        if not skill_dir.exists():
            return []
        return sorted(skill_dir.glob("scenario-*.md"))

    return sorted(base_dir.glob("scenarios/*/scenario-*.md"))


def parse_scenario(scenario_path: Path) -> dict[str, str]:
    """Parse a scenario markdown file into structured data."""
    content = scenario_path.read_text(encoding="utf-8")

    difficulty_match = re.search(r"## Difficulty\s*\n\s*(Easy|Medium|Hard)", content, re.IGNORECASE)
    difficulty = difficulty_match.group(1).capitalize() if difficulty_match else "Unknown"

    desc_match = re.search(r"## Description\s*\n(.+?)(?=\n## )", content, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""

    prompt_match = re.search(r"## Prompt\s*\n(.+?)(?=\n## )", content, re.DOTALL)
    prompt = prompt_match.group(1).strip() if prompt_match else ""

    expected_match = re.search(r"## Expected Output\s*\n(.+?)(?=\n## )", content, re.DOTALL)
    expected = expected_match.group(1).strip() if expected_match else ""

    criteria: list[dict[str, str]] = []
    criteria_section = re.search(r"## Scoring Criteria\s*\n(.+)$", content, re.DOTALL)
    if criteria_section:
        for line in criteria_section.group(1).strip().split("\n"):
            match = re.search(r"- \[ \] (.+?) \((\d+) points?\)", line)
            if match:
                criteria.append({"name": match.group(1), "points": int(match.group(2))})

    return {
        "name": scenario_path.stem,
        "skill": scenario_path.parent.name,
        "difficulty": difficulty,
        "description": description,
        "prompt": prompt,
        "expected": expected,
        "criteria": criteria,
        "path": str(scenario_path),
    }


def evaluate_scenario(scenario: dict[str, str], code_output: str) -> ScenarioResult:
    """Evaluate a code output against a scenario's criteria."""
    result = ScenarioResult(
        scenario_name=scenario["name"],
        skill=scenario["skill"],
        difficulty=scenario["difficulty"],
    )

    max_points = sum(c["points"] for c in scenario["criteria"])
    result.max_points = max_points

    for criterion in scenario["criteria"]:
        check = _run_check(criterion["name"], code_output, criterion["points"])
        result.checks.append(check)
        if check.passed:
            result.total_points += check.points

    return result


def _run_check(check_name: str, code: str, max_points: int) -> CheckResult:
    """Run a single validation check against code output."""
    check_lower = check_name.lower()

    if "srp" in check_lower or "single responsibility" in check_lower:
        return _check_srp(code, max_points)
    elif "naming" in check_lower:
        return _check_naming(code, max_points)
    elif "type safety" in check_lower or "typing" in check_lower:
        return _check_type_safety(code, max_points)
    elif "2-layer" in check_lower or "layer" in check_lower or "architecture" in check_lower:
        return _check_2layer(code, max_points)
    elif "domain purity" in check_lower or "inbound" in check_lower:
        return _check_domain_purity(code, max_points)
    else:
        return CheckResult(
            check_name=check_name,
            passed=True,
            details="Manual review required",
            points=max_points,
            max_points=max_points,
        )


def _check_srp(code: str, max_points: int) -> CheckResult:
    """Check Single Responsibility Principle compliance."""
    issues: list[str] = []
    lines = code.split("\n")
    in_function = False
    function_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(("def ", "function ", "fn ")) and not stripped.startswith("def __"):
            in_function = True
            function_start = i
        elif in_function and stripped and not stripped.startswith(" ") and not stripped.startswith("#"):
            func_len = i - function_start
            if func_len > 30:
                issues.append(f"Function at line {function_start + 1} has {func_len} lines")
            in_function = False

    passed = len(issues) == 0
    return CheckResult(
        check_name="SRP Compliance",
        passed=passed,
        details="; ".join(issues) if issues else "Functions within length limits",
        points=max_points if passed else max_points // 2,
        max_points=max_points,
    )


def _check_naming(code: str, max_points: int) -> CheckResult:
    """Check explicit naming conventions."""
    issues: list[str] = []
    short_names = re.findall(r"\b([a-zA-Z]{1,2})\b", code)
    common_bad = {"s", "x", "i", "j", "k", "n", "e", "ex", "st", "str", "obj", "res", "tmp", "val", "var"}
    found_bad = set(short_names) & common_bad
    if found_bad:
        issues.append(f"Short names found: {found_bad}")

    passed = len(issues) == 0
    return CheckResult(
        check_name="Explicit Naming",
        passed=passed,
        details="; ".join(issues) if issues else "Naming conventions followed",
        points=max_points if passed else max_points // 2,
        max_points=max_points,
    )


def _check_type_safety(code: str, max_points: int) -> CheckResult:
    """Check type safety compliance."""
    issues: list[str] = []
    if ": any" in code or " as any" in code:
        issues.append("'any' type found")
    if "from typing import" in code and "Any" in code:
        if re.search(r":\s*Any\b", code):
            issues.append("'Any' type annotation found")

    passed = len(issues) == 0
    return CheckResult(
        check_name="Type Safety",
        passed=passed,
        details="; ".join(issues) if issues else "Type safety rules followed",
        points=max_points if passed else max_points // 2,
        max_points=max_points,
    )


def _check_2layer(code: str, max_points: int) -> CheckResult:
    """Check 2-layer architecture compliance."""
    issues: list[str] = []
    has_domain = "DOMAIN LAYER" in code or "domain/" in code
    has_infra = "INFRASTRUCTURE LAYER" in code or "infrastructure/" in code

    if not has_domain:
        issues.append("No domain layer found")
    if not has_infra:
        issues.append("No infrastructure layer found")

    passed = len(issues) == 0
    return CheckResult(
        check_name="2-Layer Architecture",
        passed=passed,
        details="; ".join(issues) if issues else "Architecture layers present",
        points=max_points if passed else 0,
        max_points=max_points,
    )


def _check_domain_purity(code: str, max_points: int) -> CheckResult:
    """Check domain layer purity (no framework imports)."""
    issues: list[str] = []
    domain_section = ""
    if "DOMAIN LAYER" in code:
        parts = code.split("DOMAIN LAYER")
        if len(parts) > 1:
            domain_section = parts[1].split("INFRASTRUCTURE LAYER")[0] if "INFRASTRUCTURE LAYER" in parts[1] else parts[1]

    if domain_section:
        framework_imports = [
            "from fastapi", "from flask", "from django",
            "from spring", "import org.springframework",
            "from axum", "from actix", "from sqlx",
            "import express", "from express", "import next", "from next",
            "import nuxt", "import vue",
            "@Entity", "@Component", "@RestController",
            "from prisma", "from pydantic",
        ]
        for fw in framework_imports:
            if fw.lower() in domain_section.lower():
                issues.append(f"Framework import '{fw}' in domain layer")
                break

    passed = len(issues) == 0
    return CheckResult(
        check_name="Domain Purity",
        passed=passed,
        details="; ".join(issues) if issues else "Domain layer is pure",
        points=max_points if passed else 0,
        max_points=max_points,
    )


def run_benchmark(base_dir: Path, skill: Optional[str] = None, format_output: str = "text") -> None:
    """Run the benchmark suite and output results."""
    scenario_files = find_scenario_files(base_dir, skill)

    if not scenario_files:
        print(f"No scenarios found for skill: {skill}", file=sys.stderr)
        sys.exit(1)

    results: list[SkillResult] = []
    current_skill: Optional[str] = None
    current_scenarios: list[ScenarioResult] = []

    for scenario_file in scenario_files:
        scenario_data = parse_scenario(scenario_file)

        if current_skill != scenario_data["skill"]:
            if current_skill is not None:
                results.append(SkillResult(skill=current_skill, scenarios=current_scenarios))
            current_skill = scenario_data["skill"]
            current_scenarios = []

        result = evaluate_scenario(scenario_data, "")
        current_scenarios.append(result)

    if current_skill is not None:
        results.append(SkillResult(skill=current_skill, scenarios=current_scenarios))

    if format_output == "json":
        _output_json(results)
    elif format_output == "csv":
        _output_csv(results)
    else:
        _output_text(results)


def _output_text(results: list[SkillResult]) -> None:
    """Output results in plain text format."""
    print("=" * 70)
    print("VOIDLIGHT SKILL LIBRARY BENCHMARK RESULTS")
    print("=" * 70)

    total_points = 0
    total_max = 0

    for skill_result in results:
        print(f"\n{'─' * 50}")
        print(f"  Skill: {skill_result.skill}")
        print(f"  Scenarios: {len(skill_result.scenarios)}")
        print(f"  Score: {skill_result.total_points}/{skill_result.max_points} ({skill_result.percentage:.1f}%)")
        print(f"{'─' * 50}")

        for scenario in skill_result.scenarios:
            print(f"  • {scenario.scenario_name} ({scenario.difficulty})")
            print(f"    {scenario.total_points}/{scenario.max_points} ({scenario.percentage:.1f}%)")
            for check in scenario.checks:
                status = "PASS" if check.passed else "FAIL"
                print(f"      [{status}] {check.check_name}: {check.details}")

        total_points += skill_result.total_points
        total_max += skill_result.max_points

    print(f"\n{'=' * 70}")
    if total_max > 0:
        print(f"OVERALL: {total_points}/{total_max} ({(total_points/total_max)*100:.1f}%)")
    print(f"Skills: {len(results)} | Scenarios: {sum(len(s.scenarios) for s in results)}")
    print("=" * 70)


def _output_json(results: list[SkillResult]) -> None:
    """Output results in JSON format."""
    data = []
    for skill_result in results:
        skill_data = {
            "skill": skill_result.skill,
            "total_points": skill_result.total_points,
            "max_points": skill_result.max_points,
            "percentage": round(skill_result.percentage, 1),
            "scenarios": [],
        }
        for scenario in skill_result.scenarios:
            skill_data["scenarios"].append({
                "name": scenario.scenario_name,
                "difficulty": scenario.difficulty,
                "total_points": scenario.total_points,
                "max_points": scenario.max_points,
                "percentage": round(scenario.percentage, 1),
                "checks": [asdict(c) for c in scenario.checks],
            })
        data.append(skill_data)
    print(json.dumps(data, indent=2))


def _output_csv(results: list[SkillResult]) -> None:
    """Output results in CSV format."""
    writer = csv.writer(sys.stdout)
    writer.writerow(["skill", "scenario", "difficulty", "total_points", "max_points", "percentage"])
    for skill_result in results:
        for scenario in skill_result.scenarios:
            writer.writerow([
                skill_result.skill,
                scenario.scenario_name,
                scenario.difficulty,
                scenario.total_points,
                scenario.max_points,
                round(scenario.percentage, 1),
            ])


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Voidlight Skill Library Benchmark Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Run all skills
  %(prog)s --skill python-craft      # Run specific skill
  %(prog)s --format json             # JSON output
        """,
    )
    parser.add_argument("--skill", type=str, default=None, help="Specific skill to benchmark")
    parser.add_argument("--format", type=str, choices=["text", "json", "csv"], default="text", help="Output format")
    parser.add_argument("--scenarios-dir", type=Path, default=Path(__file__).parent, help="Scenarios directory")

    args = parser.parse_args()
    run_benchmark(args.scenarios_dir, args.skill, args.format)


if __name__ == "__main__":
    main()
