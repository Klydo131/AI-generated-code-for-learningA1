#!/usr/bin/env python3
"""
Optimistic Future Research Tool - Example Usage
================================================
Example scripts demonstrating different ways to use the
Optimistic Future Research Tool.
"""

from optimistic_future_research_tool import OptimisticFutureResearchTool
import time
from datetime import datetime


def example_1_single_category():
    """Example 1: Research a single category."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Single Category Research - AI")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research AI category
    research = tool.research_category('AI', num_keywords=3, depth=5)

    # Save results
    tool.save_research(research)
    tool.save_all_to_json()

    print("\n✅ AI research complete!")
    print(f"📁 Check {tool.output_dir}/ for results")


def example_2_adventist_culture():
    """Example 2: Deep dive into Adventist Culture."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Adventist Culture Deep Dive")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research Adventist Culture with more depth
    research = tool.research_category('Adventist Culture', num_keywords=5, depth=7)

    # Generate insights
    insights = tool.generate_optimistic_insights(research)

    print("\n💡 Optimistic Article Ideas:")
    for i, insight in enumerate(insights[:5], 1):
        print(f"  {i}. {insight}")

    # Save
    tool.save_research(research)

    print("\n✅ Adventist Culture research complete!")


def example_3_healthcare_innovation():
    """Example 3: Healthcare and Innovation together."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Healthcare + Innovation Research")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research both categories
    healthcare = tool.research_category('Health Care', num_keywords=3, depth=5)
    time.sleep(3)
    innovation = tool.research_category('Innovation', num_keywords=3, depth=5)

    # Save both
    tool.save_research(healthcare)
    tool.save_research(innovation)
    tool.save_all_to_json('healthcare_innovation_combined.json')

    print("\n✅ Healthcare and Innovation research complete!")
    print(f"📊 Total sources: {healthcare['num_sources'] + innovation['num_sources']}")


def example_4_comprehensive_research():
    """Example 4: Comprehensive research across all categories."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Comprehensive All-Category Research")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research all categories
    all_research = tool.research_all_categories(num_keywords=2, depth=4)

    # Save individual reports
    for research in all_research:
        tool.save_research(research)

    # Generate and save comprehensive report
    comp_report = tool.generate_comprehensive_report()
    import os
    report_path = os.path.join(tool.output_dir,
                              f"comprehensive_report_{datetime.now().strftime('%Y%m%d')}.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(comp_report)

    tool.save_all_to_json()

    print("\n✅ Comprehensive research complete!")
    print(f"📄 Categories researched: {len(all_research)}")
    print(f"📁 Comprehensive report: {report_path}")


def example_5_quick_daily_research():
    """Example 5: Quick daily research routine."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Quick Daily Research Routine")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Quick research with minimal keywords
    print("\n⚡ Running quick daily scan...")

    categories_to_research = ['AI', 'Health Care']

    for category in categories_to_research:
        print(f"\n🔍 Researching: {category}")
        research = tool.research_category(category, num_keywords=2, depth=3)
        tool.save_research(research)
        time.sleep(2)

    tool.save_all_to_json(f"daily_brief_{datetime.now().strftime('%Y%m%d')}.json")

    print("\n✅ Daily research complete!")
    print("Perfect for morning inspiration!")


def example_6_custom_analysis():
    """Example 6: Custom analysis workflow."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Custom Analysis Workflow")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research a category
    print("\n📚 Researching Innovation category...")
    research = tool.research_category('Innovation', num_keywords=3, depth=5)

    # Analyze results
    print(f"\n📊 Analysis Results:")
    print(f"   Category: {research['category']}")
    print(f"   Description: {research['description']}")
    print(f"   Keywords Used: {len(research['keywords_searched'])}")
    print(f"   Unique Sources: {research['num_sources']}")
    print(f"   Articles Scraped: {len(research['articles'])}")

    # Show top sources
    print(f"\n🌟 Top 5 Sources:")
    for i, result in enumerate(research['search_results'][:5], 1):
        print(f"\n   {i}. {result['title'][:60]}...")
        print(f"      Query: {result['query'][:50]}...")

    # Generate insights
    insights = tool.generate_optimistic_insights(research)
    print(f"\n💡 Content Ideas:")
    for i, insight in enumerate(insights[:3], 1):
        print(f"   {i}. {insight}")

    # Save
    tool.save_research(research)

    print("\n✅ Custom analysis complete!")


def example_7_focused_ai_healthcare():
    """Example 7: Focused AI + Healthcare intersection."""
    print("\n" + "="*70)
    print("EXAMPLE 7: AI + Healthcare Intersection")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Research both with focus on intersection
    print("\n🤖 Researching AI...")
    ai_research = tool.research_category('AI', num_keywords=3, depth=5)

    time.sleep(3)

    print("\n⚕️  Researching Healthcare...")
    healthcare_research = tool.research_category('Health Care', num_keywords=3, depth=5)

    # Create custom combined report
    import os
    combined_report = f"""# 🌟 AI + Healthcare: Optimistic Future Perspectives

**Research Date:** {datetime.now().strftime('%Y-%m-%d')}

## Overview

This research explores the optimistic intersection of Artificial Intelligence
and Healthcare, highlighting breakthrough innovations and positive developments.

---

## AI Research Summary

**Sources Found:** {ai_research['num_sources']}
**Articles Analyzed:** {len(ai_research['articles'])}

### Top AI Findings:
"""

    for i, result in enumerate(ai_research['search_results'][:3], 1):
        combined_report += f"\n{i}. {result['title']}\n"

    combined_report += f"""

---

## Healthcare Research Summary

**Sources Found:** {healthcare_research['num_sources']}
**Articles Analyzed:** {len(healthcare_research['articles'])}

### Top Healthcare Findings:
"""

    for i, result in enumerate(healthcare_research['search_results'][:3], 1):
        combined_report += f"\n{i}. {result['title']}\n"

    combined_report += """

---

## Intersection Opportunities

1. AI-powered diagnostic tools
2. Personalized medicine through machine learning
3. Predictive healthcare analytics
4. Robot-assisted surgery
5. AI-driven drug discovery

---

*Research powered by Optimistic Future Research Tool*
"""

    # Save combined report
    report_path = os.path.join(tool.output_dir,
                              f"ai_healthcare_intersection_{datetime.now().strftime('%Y%m%d')}.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(combined_report)

    print(f"\n✅ Intersection research complete!")
    print(f"📄 Combined report: {report_path}")


def example_8_weekly_content_planner():
    """Example 8: Weekly content planning."""
    print("\n" + "="*70)
    print("EXAMPLE 8: Weekly Optimistic Content Planner")
    print("="*70)

    tool = OptimisticFutureResearchTool()

    # Define weekly schedule
    weekly_plan = {
        'Monday': 'AI',
        'Tuesday': 'Adventist Culture',
        'Wednesday': 'Health Care',
        'Thursday': 'Innovation',
        'Friday': 'All Categories Summary'
    }

    print("\n📅 Weekly Content Plan:\n")

    researched_data = []

    for day, category in weekly_plan.items():
        if category == 'All Categories Summary':
            print(f"\n{day}: {category}")
            print("   (Will generate comprehensive summary)")
        else:
            print(f"\n{day}: {category}")
            research = tool.research_category(category, num_keywords=2, depth=3)
            researched_data.append(research)

            # Get top idea
            insights = tool.generate_optimistic_insights(research)
            print(f"   💡 Featured idea: {insights[0]}")

            # Save
            tool.save_research(research, f"week_{day.lower()}_{category.replace(' ', '_').lower()}.md")

            time.sleep(2)

    # Generate weekly summary
    import os
    weekly_summary = f"""# 🌟 Weekly Optimistic Research Summary

**Week of:** {datetime.now().strftime('%Y-%m-%d')}

## Monday - Friday Research Overview

"""

    for i, (day, category) in enumerate(list(weekly_plan.items())[:-1]):
        research = researched_data[i]
        weekly_summary += f"""
### {day}: {category}

- **Sources:** {research['num_sources']}
- **Articles:** {len(research['articles'])}
- **Top Finding:** {research['search_results'][0]['title'] if research['search_results'] else 'N/A'}

"""

    summary_path = os.path.join(tool.output_dir,
                               f"weekly_summary_{datetime.now().strftime('%Y%m%d')}.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(weekly_summary)

    tool.save_all_to_json('weekly_research.json')

    print(f"\n✅ Weekly planning complete!")
    print(f"📄 Summary: {summary_path}")


def interactive_menu():
    """Interactive menu to choose examples."""
    examples = {
        '1': ("Single Category - AI", example_1_single_category),
        '2': ("Adventist Culture Deep Dive", example_2_adventist_culture),
        '3': ("Healthcare + Innovation", example_3_healthcare_innovation),
        '4': ("Comprehensive Research", example_4_comprehensive_research),
        '5': ("Quick Daily Research", example_5_quick_daily_research),
        '6': ("Custom Analysis", example_6_custom_analysis),
        '7': ("AI + Healthcare Intersection", example_7_focused_ai_healthcare),
        '8': ("Weekly Content Planner", example_8_weekly_content_planner),
    }

    while True:
        print("\n" + "="*70)
        print("OPTIMISTIC FUTURE RESEARCH TOOL - EXAMPLES")
        print("="*70)
        print("\nChoose an example to run:\n")

        for key, (name, _) in examples.items():
            print(f"  {key}. {name}")

        print("\n  q. Quit")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == 'q':
            print("\n✨ Goodbye! Keep researching hope!")
            break

        if choice in examples:
            name, func = examples[choice]
            print(f"\n▶ Running: {name}\n")
            try:
                func()
            except Exception as e:
                print(f"\n❌ Error: {e}")
                import traceback
                traceback.print_exc()

            input("\n[Press Enter to return to menu...]")
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║   Optimistic Future Research Tool - Examples                  ║
    ║   Learn Through Practical Examples                            ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    interactive_menu()
