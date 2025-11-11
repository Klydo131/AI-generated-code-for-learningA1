#!/usr/bin/env python3
"""
Quick test of the Optimistic Future Research Tool
This performs a minimal test to verify functionality
"""

from optimistic_future_research_tool import OptimisticFutureResearchTool

def main():
    print("="*70)
    print("QUICK TEST - Optimistic Future Research Tool")
    print("="*70)

    # Initialize
    tool = OptimisticFutureResearchTool()

    # Show available categories
    print("\n📚 Available Categories:")
    for i, (category, data) in enumerate(tool.TOPIC_CATEGORIES.items(), 1):
        print(f"  {i}. {category}")
        print(f"     {data['description']}")
        print(f"     Keywords: {len(data['keywords'])} available")
        print()

    # Perform a quick test search
    print("\n🔍 Performing test search...")
    print("Testing with: 'AI future innovation breakthrough'")

    results = tool.search_topic('AI future innovation breakthrough', num_results=3)

    if results:
        print(f"\n✅ Search successful! Found {len(results)} results:")
        for i, result in enumerate(results, 1):
            print(f"\n  {i}. {result['title'][:60]}...")
            if result['snippet']:
                print(f"     {result['snippet'][:100]}...")
    else:
        print("\n⚠ No results found (this is normal in some environments)")

    # Show category info
    print("\n" + "="*70)
    print("📊 Tool Statistics:")
    print(f"  Categories: {len(tool.TOPIC_CATEGORIES)}")
    print(f"  Total Keywords: {sum(len(cat['keywords']) for cat in tool.TOPIC_CATEGORIES.values())}")
    print(f"  Output Directory: {tool.output_dir}")
    print("="*70)

    print("\n✅ Quick test complete!")
    print("\n💡 Next steps:")
    print("  1. Run: python optimistic_future_research_tool.py")
    print("  2. Or: python optimistic_research_examples.py")
    print("  3. Read: OPTIMISTIC_RESEARCH_README.md")

if __name__ == "__main__":
    main()
