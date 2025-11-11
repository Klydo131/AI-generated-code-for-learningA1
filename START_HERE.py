#!/usr/bin/env python3
"""
START HERE - Optimistic Future Research Tool Launcher
======================================================
Easy launcher for the Optimistic Future Research Tool
"""

import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name != 'nt' else 'cls')

def main():
    clear_screen()

    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║   Optimistic Future Research Tool - START HERE               ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    print("Welcome! Choose how you want to use the research tool:")
    print()
    print("  1. 🚀 Launch Interactive Research Tool (RECOMMENDED)")
    print("       - Research AI, Adventist Culture, Health Care, or Innovation")
    print("       - Full menu with all features")
    print()
    print("  2. 📚 View Example Demonstrations")
    print("       - See 8 different usage examples")
    print("       - Learn how to use the tool effectively")
    print()
    print("  3. ⚡ Run Quick Test")
    print("       - Verify the tool is working")
    print("       - See all available categories and keywords")
    print()
    print("  4. 📖 Open Documentation")
    print("       - Read the complete README")
    print()
    print("  5. ❌ Exit")
    print()

    try:
        choice = input("Enter your choice (1-5): ").strip()
        print()

        if choice == '1':
            print("🚀 Launching Interactive Research Tool...")
            print("=" * 70)
            print()
            import optimistic_future_research_tool
            optimistic_future_research_tool.main()

        elif choice == '2':
            print("📚 Launching Example Demonstrations...")
            print("=" * 70)
            print()
            import optimistic_research_examples
            optimistic_research_examples.interactive_menu()

        elif choice == '3':
            print("⚡ Running Quick Test...")
            print("=" * 70)
            print()
            import quick_test
            quick_test.main()

        elif choice == '4':
            print("📖 Opening Documentation...")
            print()
            readme_path = "OPTIMISTIC_RESEARCH_README.md"
            if os.path.exists(readme_path):
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Show first 50 lines
                    lines = content.split('\n')
                    for line in lines[:50]:
                        print(line)
                    print()
                    print(f"... (showing first 50 lines of {len(lines)} total)")
                    print(f"\nFull documentation: {readme_path}")
            else:
                print("❌ README file not found")

        elif choice == '5':
            print("✨ Thank you for using Optimistic Future Research Tool!")
            print("🌟 Keep researching hope!")
            sys.exit(0)

        else:
            print("❌ Invalid choice. Please run the script again and choose 1-5.")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n✨ Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        print()
        print("Troubleshooting:")
        print("  1. Make sure you're in the correct directory")
        print("  2. Install dependencies: pip install requests beautifulsoup4")
        print("  3. Check that all tool files are present")
        sys.exit(1)

if __name__ == "__main__":
    main()
