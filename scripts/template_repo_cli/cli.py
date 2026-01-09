"""Command-line interface for template repository creation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from scripts.template_repo_cli.core.collector import FileCollector
from scripts.template_repo_cli.core.github import GitHubClient
from scripts.template_repo_cli.core.packager import TemplatePackager
from scripts.template_repo_cli.core.selector import ExerciseSelector


def get_repo_root() -> Path:
    """Get repository root directory."""
    # Assume we're running from repository root
    return Path.cwd()


def create_command(args: argparse.Namespace) -> int:
    """Handle create command.
    
    Args:
        args: Parsed command-line arguments.
        
    Returns:
        Exit code (0 for success).
    """
    repo_root = get_repo_root()
    
    if args.verbose:
        print(f"Repository root: {repo_root}")
    
    # Initialize components
    selector = ExerciseSelector(repo_root)
    collector = FileCollector(repo_root)
    packager = TemplatePackager(repo_root)
    github = GitHubClient(dry_run=args.dry_run)
    
    # Select exercises
    exercises = []
    
    try:
        if args.notebooks:
            # Select by specific notebooks or patterns
            for pattern in args.notebooks:
                if "*" in pattern or "?" in pattern or "[" in pattern:
                    exercises.extend(selector.select_by_pattern(pattern))
                else:
                    exercises.extend(selector.select_by_notebooks([pattern]))
        elif args.construct and args.type:
            # Select by construct AND type
            exercises = selector.select_by_construct_and_type(args.construct, args.type)
        elif args.construct:
            # Select by construct only
            exercises = selector.select_by_construct(args.construct)
        elif args.type:
            # Select by type only
            exercises = selector.select_by_type(args.type)
        else:
            print("Error: Must specify --construct, --type, or --notebooks", file=sys.stderr)
            return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    if not exercises:
        print("No exercises found matching criteria", file=sys.stderr)
        return 1
    
    if args.verbose:
        print(f"Selected {len(exercises)} exercises: {', '.join(exercises)}")
    
    # Collect files
    try:
        files = collector.collect_multiple(exercises)
    except FileNotFoundError as e:
        print(f"Error collecting files: {e}", file=sys.stderr)
        return 1
    
    # Create workspace
    workspace = packager.create_workspace()
    if args.verbose:
        print(f"Created workspace: {workspace}")
    
    try:
        # Copy files
        packager.copy_exercise_files(workspace, files, include_solutions=True)
        packager.copy_template_base_files(workspace)
        
        # Generate README
        template_name = args.name or f"{args.repo_name} Exercises"
        packager.generate_readme(workspace, template_name, exercises)
        
        # Validate package
        if not packager.validate_package(workspace):
            print("Error: Package validation failed", file=sys.stderr)
            packager.cleanup(workspace)
            return 1
        
        if args.verbose:
            print("Package validated successfully")
        
        # Create GitHub repository (if not dry-run)
        if not args.dry_run:
            if not github.check_gh_installed():
                print(
                    "Error: gh CLI not installed. "
                    "Please install it from https://cli.github.com/",
                    file=sys.stderr,
                )
                packager.cleanup(workspace)
                return 1
            
            if not github.check_authentication():
                print(
                    "Error: Not authenticated with GitHub. "
                    "Run 'gh auth login' first.",
                    file=sys.stderr,
                )
                packager.cleanup(workspace)
                return 1
            
            # Create repository
            result = github.create_repository(args.repo_name, workspace, push=False)
            
            if result["success"]:
                print(f"✓ Created repository: {args.repo_name}")
            else:
                print(f"Error creating repository: {result.get('error')}", file=sys.stderr)
                packager.cleanup(workspace)
                return 1
        else:
            print(f"[DRY RUN] Would create repository: {args.repo_name}")
            print(f"[DRY RUN] Workspace: {workspace}")
            print(f"[DRY RUN] Exercises: {', '.join(exercises)}")
        
        # Cleanup (unless output-dir specified)
        if not args.output_dir:
            packager.cleanup(workspace)
        else:
            # Copy to output directory instead of cleaning up
            import shutil
            output_path = Path(args.output_dir)
            try:
                if output_path.exists():
                    shutil.rmtree(output_path)
                shutil.copytree(workspace, output_path)
            except Exception as copy_error:
                print(f"Error saving output to {output_path}: {copy_error}", file=sys.stderr)
                print(f"Workspace preserved at: {workspace}", file=sys.stderr)
                return 1
            packager.cleanup(workspace)
            print(f"Output saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        packager.cleanup(workspace)
        return 1
    
    return 0


def list_command(args: argparse.Namespace) -> int:
    """Handle list command.
    
    Args:
        args: Parsed command-line arguments.
        
    Returns:
        Exit code (0 for success).
    """
    repo_root = get_repo_root()
    selector = ExerciseSelector(repo_root)
    
    # Get exercises based on filters
    if args.construct:
        exercises = selector.select_by_construct([args.construct])
    else:
        # List all exercises
        exercises = selector._get_all_notebooks()
    
    # Print exercises
    if args.format == "json":
        import json
        print(json.dumps(exercises, indent=2))
    elif args.format == "table":
        print(f"{'Exercise ID':<40}")
        print("-" * 40)
        for ex in exercises:
            print(f"{ex:<40}")
    else:  # list format
        for ex in exercises:
            print(ex)
    
    return 0


def validate_command(args: argparse.Namespace) -> int:
    """Handle validate command.
    
    Args:
        args: Parsed command-line arguments.
        
    Returns:
        Exit code (0 for success).
    """
    repo_root = get_repo_root()
    selector = ExerciseSelector(repo_root)
    collector = FileCollector(repo_root)
    
    # Select exercises
    try:
        if args.construct and args.type:
            exercises = selector.select_by_construct_and_type(args.construct, args.type)
        elif args.construct:
            exercises = selector.select_by_construct(args.construct)
        elif args.type:
            exercises = selector.select_by_type(args.type)
        else:
            print("Error: Must specify --construct or --type", file=sys.stderr)
            return 1
    except ValueError as e:
        print(f"Validation error: {e}", file=sys.stderr)
        return 1
    
    if not exercises:
        print("No exercises found matching criteria")
        return 0
    
    # Validate files exist
    print(f"Found {len(exercises)} exercises:")
    missing_files = []
    
    for ex in exercises:
        try:
            collector.collect_files(ex)
            print(f"  ✓ {ex}")
        except FileNotFoundError as e:
            print(f"  ✗ {ex}: {e}")
            missing_files.append(ex)
    
    if missing_files:
        print(f"\n{len(missing_files)} exercises have missing files")
        return 1
    
    print("\nAll exercises validated successfully")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Main entry point.
    
    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).
        
    Returns:
        Exit code.
    """
    parser = argparse.ArgumentParser(
        description="Create GitHub template repositories from exercise subsets"
    )
    
    # Global options
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build and validate without executing gh commands",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed progress"
    )
    parser.add_argument(
        "--output-dir", type=str, help="Local output directory (default: temp)"
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create template repository")
    create_parser.add_argument(
        "--construct", nargs="+", help="One or more constructs"
    )
    create_parser.add_argument("--type", nargs="+", help="One or more exercise types")
    create_parser.add_argument(
        "--notebooks", nargs="+", help="Specific notebook patterns"
    )
    create_parser.add_argument(
        "--name", type=str, help="Template repository name/description"
    )
    create_parser.add_argument(
        "--repo-name", type=str, required=True, help="GitHub repository name (slug)"
    )
    create_parser.add_argument(
        "--private", action="store_true", help="Create as private repository"
    )
    create_parser.add_argument(
        "--org", type=str, help="Create in organization (default: user account)"
    )
    
    # List command
    list_parser = subparsers.add_parser("list", help="List available exercises")
    list_parser.add_argument("--construct", type=str, help="Filter by construct")
    list_parser.add_argument("--type", type=str, help="Filter by type")
    list_parser.add_argument(
        "--format",
        choices=["table", "json", "list"],
        default="list",
        help="Output format",
    )
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate selection")
    validate_parser.add_argument("--construct", nargs="+", help="Filter by construct")
    validate_parser.add_argument("--type", nargs="+", help="Filter by type")
    
    # Parse arguments
    args = parser.parse_args(argv)
    
    # Execute command
    if args.command == "create":
        return create_command(args)
    elif args.command == "list":
        return list_command(args)
    elif args.command == "validate":
        return validate_command(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
