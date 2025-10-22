#!/usr/bin/env python3
"""
AI Research Tool - Example Usage Scripts
=========================================
This file contains example code snippets showing different ways
to use the AI Research Tool for blog content generation.
"""

from AI_Research_Tool import AIResearchTool
from datetime import datetime
import time


def example_1_simple_research():
    """Example 1: Research a single topic."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Simple Topic Research")
    print("="*60)

    tool = AIResearchTool()

    # Research ChatGPT
    research = tool.research_topic("ChatGPT", depth=5)

    # Save results
    tool.save_to_markdown(research)
    tool.save_to_json()

    print("\n✅ Research complete! Check research_output/ directory")


def example_2_multiple_topics():
    """Example 2: Research multiple topics at once."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Multiple Topics Research")
    print("="*60)

    tool = AIResearchTool()

    topics = [
        "Artificial General Intelligence",
        "AI Safety",
        "Large Language Models"
    ]

    for topic in topics:
        research = tool.research_topic(topic, depth=5)
        tool.save_to_markdown(research)
        time.sleep(2)  # Be polite to servers

    tool.save_to_json("multi_topic_research.json")

    print(f"\n✅ Researched {len(topics)} topics!")


def example_3_daily_digest():
    """Example 3: Generate a daily digest."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Daily Digest")
    print("="*60)

    tool = AIResearchTool()

    # Generate digest for 3 trending topics
    digest = tool.daily_ai_digest(num_topics=3)

    print(f"\n✅ Daily digest complete!")
    print(f"📊 Topics researched: {len(digest['topics'])}")
    print(f"📁 Files saved in: research_output/")


def example_4_custom_workflow():
    """Example 4: Custom workflow for Medium bloggers."""
    print("\n" + "="*60)
    print("EXAMPLE 4: Custom Medium Blog Workflow")
    print("="*60)

    tool = AIResearchTool()

    # Step 1: Research a topic
    topic = "AI Ethics in 2025"
    print(f"\n📚 Step 1: Researching '{topic}'...")
    research = tool.research_topic(topic, depth=7)

    # Step 2: Generate blog ideas
    print("\n💡 Step 2: Generating blog post ideas...")
    ideas = tool.generate_blog_ideas(research)
    print("\nBlog Post Ideas:")
    for i, idea in enumerate(ideas[:5], 1):
        print(f"  {i}. {idea}")

    # Step 3: Create outline
    print("\n📝 Step 3: Creating content outline...")
    outline = tool.create_content_outline(topic, research)

    # Step 4: Save everything
    print("\n💾 Step 4: Saving results...")
    tool.save_to_markdown(research)
    tool.save_to_json()

    print("\n✅ Workflow complete! Ready to write your Medium article!")


def example_5_trending_topics():
    """Example 5: Work with trending topics."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Trending Topics")
    print("="*60)

    tool = AIResearchTool()

    # Get trending topics
    trending = tool.get_trending_ai_topics()

    print(f"\n📈 Current Trending AI Topics ({len(trending)} total):\n")
    for i, topic in enumerate(trending[:10], 1):
        print(f"  {i}. {topic}")

    # Research top 2 trending topics
    print("\n🔍 Researching top 2 trending topics...\n")
    for topic in trending[:2]:
        research = tool.research_topic(topic, depth=3)
        tool.save_to_markdown(research)
        time.sleep(2)

    print("\n✅ Trending topics researched!")


def example_6_content_analysis():
    """Example 6: Analyze and summarize content."""
    print("\n" + "="*60)
    print("EXAMPLE 6: Content Analysis")
    print("="*60)

    tool = AIResearchTool()

    # Research a topic
    research = tool.research_topic("Generative AI", depth=5)

    # Analyze results
    print(f"\n📊 Research Analysis:")
    print(f"  Topic: {research['topic']}")
    print(f"  Sources Found: {research['num_sources']}")
    print(f"  Articles Scraped: {len(research['articles'])}")
    print(f"  Research Date: {research['researched_at']}")

    # Show source titles
    print(f"\n📰 Top Sources:")
    for i, result in enumerate(research['search_results'][:5], 1):
        print(f"  {i}. {result['title'][:60]}...")

    # Save
    tool.save_to_markdown(research)

    print("\n✅ Analysis complete!")


def example_7_weekly_planning():
    """Example 7: Weekly content planning."""
    print("\n" + "="*60)
    print("EXAMPLE 7: Weekly Content Planning")
    print("="*60)

    tool = AIResearchTool()

    # Define weekly topics (Monday - Friday)
    weekly_topics = {
        'Monday': 'ChatGPT and Large Language Models',
        'Tuesday': 'AI in Healthcare',
        'Wednesday': 'Computer Vision Applications',
        'Thursday': 'AI Ethics and Regulation',
        'Friday': 'Future of AI - 2025 Predictions'
    }

    print(f"\n📅 Planning content for the week:\n")

    for day, topic in weekly_topics.items():
        print(f"\n{day}: {topic}")
        research = tool.research_topic(topic, depth=4)
        ideas = tool.generate_blog_ideas(research)
        print(f"  Top idea: {ideas[0]}")
        tool.save_to_markdown(research, f"week_plan_{day.lower()}_{datetime.now().strftime('%Y%m%d')}.md")
        time.sleep(2)

    tool.save_to_json("weekly_planning.json")

    print("\n✅ Weekly content plan complete!")
    print("📁 Check research_output/ for daily outlines")


def example_8_quick_ideas():
    """Example 8: Quick blog ideas without full research."""
    print("\n" + "="*60)
    print("EXAMPLE 8: Quick Blog Ideas")
    print("="*60)

    tool = AIResearchTool()

    topics = ["Neural Networks", "AI Agents", "Transformer Models"]

    print("\n💡 Quick Blog Post Ideas:\n")

    for topic in topics:
        print(f"\n{topic}:")
        # Create mock research data for idea generation
        research_data = {'topic': topic, 'search_results': [], 'articles': []}
        ideas = tool.generate_blog_ideas(research_data)

        # Show top 3 ideas
        for i, idea in enumerate(ideas[:3], 1):
            print(f"  {i}. {idea}")

    print("\n✅ Ideas generated! Pick one and do full research.")


def run_all_examples():
    """Run all examples sequentially."""
    examples = [
        ("Simple Research", example_1_simple_research),
        ("Multiple Topics", example_2_multiple_topics),
        ("Daily Digest", example_3_daily_digest),
        ("Custom Workflow", example_4_custom_workflow),
        ("Trending Topics", example_5_trending_topics),
        ("Content Analysis", example_6_content_analysis),
        ("Weekly Planning", example_7_weekly_planning),
        ("Quick Ideas", example_8_quick_ideas),
    ]

    print("\n" + "="*60)
    print("AI RESEARCH TOOL - EXAMPLE DEMONSTRATIONS")
    print("="*60)

    for i, (name, func) in enumerate(examples, 1):
        print(f"\n\n{'#'*60}")
        print(f"Running Example {i}/{len(examples)}: {name}")
        print(f"{'#'*60}")

        try:
            func()
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")

        if i < len(examples):
            input("\n[Press Enter to continue to next example...]")

    print("\n\n" + "="*60)
    print("ALL EXAMPLES COMPLETED!")
    print("="*60)
    print("\nCheck the research_output/ directory for all generated files.")


def interactive_menu():
    """Interactive menu to choose which example to run."""
    examples = {
        '1': ("Simple Research", example_1_simple_research),
        '2': ("Multiple Topics", example_2_multiple_topics),
        '3': ("Daily Digest", example_3_daily_digest),
        '4': ("Custom Workflow", example_4_custom_workflow),
        '5': ("Trending Topics", example_5_trending_topics),
        '6': ("Content Analysis", example_6_content_analysis),
        '7': ("Weekly Planning", example_7_weekly_planning),
        '8': ("Quick Ideas", example_8_quick_ideas),
        'all': ("All Examples", run_all_examples),
    }

    while True:
        print("\n" + "="*60)
        print("AI RESEARCH TOOL - EXAMPLE MENU")
        print("="*60)
        print("\nChoose an example to run:\n")

        for key, (name, _) in examples.items():
            if key != 'all':
                print(f"  {key}. {name}")

        print(f"\n  all. Run All Examples")
        print(f"  q. Quit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == 'q':
            print("\n👋 Goodbye!")
            break

        if choice in examples:
            name, func = examples[choice]
            print(f"\n▶ Running: {name}")
            try:
                func()
            except Exception as e:
                print(f"\n❌ Error: {e}")

            if choice == 'all':
                break

            input("\n[Press Enter to return to menu...]")
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         AI Research Tool - Example Usage                  ║
    ║              Learn by Example                             ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    interactive_menu()
