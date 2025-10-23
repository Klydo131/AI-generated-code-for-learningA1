#!/usr/bin/env python3
"""
Daily AI Research Automation Script
====================================
This script automates the daily research process for AI topics.
Perfect for scheduling with cron or Task Scheduler for daily Medium blog updates.

Usage:
    python daily_ai_research.py [options]

Options:
    --topics N          Number of topics to research (default: 3)
    --depth N           Depth of research per topic (default: 5)
    --custom TOPICS     Comma-separated custom topics
    --schedule          Run on schedule (requires schedule library)
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

# Import the AI Research Tool
try:
    from AI_Research_Tool import AIResearchTool
except ImportError:
    print("Error: Could not import AI_Research_Tool")
    print("Make sure AI_Research_Tool.py is in the same directory")
    sys.exit(1)


def run_daily_research(num_topics=3, depth=5, custom_topics=None):
    """
    Run the daily research routine.

    Args:
        num_topics: Number of topics to research
        depth: Research depth per topic
        custom_topics: List of custom topics (or None for trending)
    """
    print("="*70)
    print(f"DAILY AI RESEARCH - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)

    # Initialize tool
    tool = AIResearchTool(output_dir="research_output")

    if custom_topics:
        # Research custom topics
        print(f"\n📋 Researching {len(custom_topics)} custom topics...")
        for topic in custom_topics:
            print(f"\n{'='*70}")
            research = tool.research_topic(topic.strip(), depth=depth)
            tool.save_to_markdown(research)
            print(f"✅ Completed: {topic}")

        tool.save_to_json(f"custom_research_{datetime.now().strftime('%Y%m%d')}.json")
    else:
        # Run daily digest with trending topics
        print(f"\n📊 Running daily digest for {num_topics} trending topics...")
        digest = tool.daily_ai_digest(num_topics=num_topics)

    # Generate summary report
    print("\n" + "="*70)
    print("GENERATING SUMMARY REPORT")
    print("="*70)

    summary = tool.generate_summary_report()
    print(summary)

    # Save summary
    summary_file = Path(tool.output_dir) / f"summary_{datetime.now().strftime('%Y%m%d')}.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"\n💾 Summary saved to: {summary_file}")

    # Display completion message
    print("\n" + "="*70)
    print("✅ DAILY RESEARCH COMPLETE!")
    print("="*70)
    print(f"\n📁 Check your research_output/ directory for results")
    print(f"📝 Markdown files ready for Medium blog posts")
    print(f"🎯 Next steps: Review, edit, and publish!")
    print("\n")


def scheduled_job():
    """Run as a scheduled job."""
    try:
        run_daily_research(num_topics=3, depth=5)
    except Exception as e:
        print(f"❌ Error during scheduled research: {e}")
        # Log error to file
        error_log = Path("research_output") / "error_log.txt"
        with open(error_log, 'a') as f:
            f.write(f"{datetime.now()}: {e}\n")


def run_on_schedule(schedule_time="09:00"):
    """
    Run research on a daily schedule.

    Args:
        schedule_time: Time to run (HH:MM format)
    """
    try:
        import schedule
        import time
    except ImportError:
        print("❌ Error: 'schedule' library not installed")
        print("Install it with: pip install schedule")
        sys.exit(1)

    print(f"⏰ Scheduling daily research for {schedule_time}")
    print("Press Ctrl+C to stop\n")

    schedule.every().day.at(schedule_time).do(scheduled_job)

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n\n⏹️ Scheduler stopped")


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Daily AI Research Tool for Medium Blog Content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run daily digest with 3 topics
  python daily_ai_research.py

  # Research 5 topics with depth 7
  python daily_ai_research.py --topics 5 --depth 7

  # Research custom topics
  python daily_ai_research.py --custom "GPT-4,AI Ethics,Robotics"

  # Run on schedule (daily at 9 AM)
  python daily_ai_research.py --schedule --time 09:00
        """
    )

    parser.add_argument(
        '--topics',
        type=int,
        default=3,
        help='Number of topics to research (default: 3)'
    )

    parser.add_argument(
        '--depth',
        type=int,
        default=5,
        help='Research depth per topic (default: 5)'
    )

    parser.add_argument(
        '--custom',
        type=str,
        help='Comma-separated list of custom topics to research'
    )

    parser.add_argument(
        '--schedule',
        action='store_true',
        help='Run on a daily schedule'
    )

    parser.add_argument(
        '--time',
        type=str,
        default='09:00',
        help='Time to run scheduled job (HH:MM format, default: 09:00)'
    )

    args = parser.parse_args()

    # Parse custom topics if provided
    custom_topics = None
    if args.custom:
        custom_topics = [t.strip() for t in args.custom.split(',')]

    # Run based on arguments
    if args.schedule:
        run_on_schedule(args.time)
    else:
        run_daily_research(
            num_topics=args.topics,
            depth=args.depth,
            custom_topics=custom_topics
        )


if __name__ == "__main__":
    main()
