#!/usr/bin/env python3
"""
AI Research Tool for Blog Content Generation
=============================================
This tool helps research AI topics from the internet and generates
content ideas for blog posts, particularly for Medium.

Features:
- Search for trending AI topics
- Scrape articles and news
- Generate content summaries
- Export to multiple formats
- Daily automation support
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time
import re
from urllib.parse import quote_plus, urljoin
import os


class AIResearchTool:
    """Main class for AI topic research and content generation."""

    def __init__(self, output_dir: str = "research_output"):
        """
        Initialize the AI Research Tool.

        Args:
            output_dir: Directory to save research outputs
        """
        self.output_dir = output_dir
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def search_ai_topics(self, query: str, num_results: int = 10) -> List[Dict]:
        """
        Search for AI-related topics using DuckDuckGo (no API key required).

        Args:
            query: Search query
            num_results: Number of results to return

        Returns:
            List of search results with titles, URLs, and snippets
        """
        print(f"\n🔍 Searching for: {query}")
        results = []

        try:
            # Using DuckDuckGo HTML search (no API key needed)
            search_url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
            response = self.session.get(search_url, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                search_results = soup.find_all('div', class_='result')

                for idx, result in enumerate(search_results[:num_results]):
                    try:
                        title_elem = result.find('a', class_='result__a')
                        snippet_elem = result.find('a', class_='result__snippet')

                        if title_elem:
                            title = title_elem.get_text(strip=True)
                            url = title_elem.get('href', '')
                            snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""

                            results.append({
                                'title': title,
                                'url': url,
                                'snippet': snippet,
                                'query': query,
                                'timestamp': datetime.now().isoformat()
                            })
                            print(f"  ✓ Found: {title[:60]}...")
                    except Exception as e:
                        print(f"  ⚠ Error parsing result {idx}: {e}")
                        continue
        except Exception as e:
            print(f"  ✗ Search error: {e}")

        return results

    def scrape_article(self, url: str) -> Optional[Dict]:
        """
        Scrape content from a given URL.

        Args:
            url: URL to scrape

        Returns:
            Dictionary with article content or None if failed
        """
        try:
            print(f"\n📄 Scraping: {url[:60]}...")
            response = self.session.get(url, timeout=15)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Remove script and style elements
                for script in soup(['script', 'style', 'nav', 'footer', 'header']):
                    script.decompose()

                # Try to find the main content
                article_content = None

                # Common article containers
                for selector in ['article', 'main', '.article-content', '.post-content',
                                '.entry-content', '#content']:
                    content = soup.select_one(selector)
                    if content:
                        article_content = content
                        break

                if not article_content:
                    article_content = soup.find('body')

                # Extract text
                paragraphs = article_content.find_all('p') if article_content else []
                text_content = ' '.join([p.get_text(strip=True) for p in paragraphs])

                # Get title
                title = soup.find('title')
                title_text = title.get_text(strip=True) if title else "No title"

                # Get meta description
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                description = meta_desc.get('content', '') if meta_desc else ""

                article_data = {
                    'url': url,
                    'title': title_text,
                    'description': description,
                    'content': text_content[:2000],  # First 2000 chars
                    'word_count': len(text_content.split()),
                    'scraped_at': datetime.now().isoformat()
                }

                print(f"  ✓ Scraped successfully ({article_data['word_count']} words)")
                return article_data
        except Exception as e:
            print(f"  ✗ Scraping error: {e}")

        return None

    def get_trending_ai_topics(self) -> List[str]:
        """
        Get a list of currently trending AI topics.

        Returns:
            List of trending AI topics
        """
        return [
            "ChatGPT",
            "Large Language Models",
            "GPT-4",
            "Generative AI",
            "AI Ethics",
            "Machine Learning",
            "Deep Learning",
            "Neural Networks",
            "AI Agents",
            "Computer Vision",
            "Natural Language Processing",
            "AI in Healthcare",
            "AI Regulation",
            "OpenAI",
            "Google Gemini",
            "Claude AI",
            "AI Coding Tools",
            "Autonomous AI",
            "Transformer Models",
            "AI Safety"
        ]

    def research_topic(self, topic: str, depth: int = 5) -> Dict:
        """
        Conduct deep research on a specific AI topic.

        Args:
            topic: The AI topic to research
            depth: Number of sources to investigate

        Returns:
            Comprehensive research data
        """
        print(f"\n{'='*60}")
        print(f"RESEARCHING: {topic}")
        print(f"{'='*60}")

        # Search for the topic
        search_results = self.search_ai_topics(f"{topic} AI artificial intelligence", num_results=depth)

        # Scrape articles (limit to avoid overwhelming)
        articles = []
        for i, result in enumerate(search_results[:3]):  # Scrape top 3 results
            time.sleep(2)  # Be polite to servers
            article = self.scrape_article(result['url'])
            if article:
                articles.append(article)

        research_data = {
            'topic': topic,
            'search_results': search_results,
            'articles': articles,
            'num_sources': len(search_results),
            'researched_at': datetime.now().isoformat()
        }

        self.results.append(research_data)
        return research_data

    def generate_blog_ideas(self, research_data: Dict) -> List[str]:
        """
        Generate blog post ideas based on research data.

        Args:
            research_data: Research results

        Returns:
            List of blog post ideas
        """
        topic = research_data['topic']

        blog_ideas = [
            f"Understanding {topic}: A Beginner's Guide",
            f"The Future of {topic} in 2025",
            f"How {topic} is Transforming Industries",
            f"5 Things You Need to Know About {topic}",
            f"{topic}: Opportunities and Challenges",
            f"A Deep Dive into {topic}",
            f"The Ethics of {topic}",
            f"Real-World Applications of {topic}",
            f"{topic} vs Traditional Approaches: A Comparison",
            f"Getting Started with {topic}: A Practical Guide"
        ]

        return blog_ideas

    def create_content_outline(self, topic: str, research_data: Dict) -> str:
        """
        Create a blog post outline based on research.

        Args:
            topic: The topic
            research_data: Research results

        Returns:
            Markdown formatted outline
        """
        outline = f"""# {topic}: A Comprehensive Guide

## Introduction
- Brief overview of {topic}
- Why {topic} matters today
- What readers will learn

## Background and Context
- History and evolution of {topic}
- Key developments and milestones
- Current state of {topic}

## Key Concepts and Technologies
"""

        # Add insights from search results
        if research_data['search_results']:
            outline += "\n### Important Points:\n"
            for i, result in enumerate(research_data['search_results'][:5], 1):
                outline += f"{i}. {result['title']}\n"

        outline += """
## Applications and Use Cases
- Industry applications
- Real-world examples
- Case studies

## Challenges and Considerations
- Current limitations
- Ethical considerations
- Future challenges

## Future Outlook
- Emerging trends
- Predictions and possibilities
- What to watch for

## Conclusion
- Key takeaways
- Final thoughts
- Call to action

## Resources
"""

        # Add sources
        if research_data['search_results']:
            outline += "\n### Sources:\n"
            for result in research_data['search_results']:
                outline += f"- [{result['title']}]({result['url']})\n"

        outline += f"\n---\n*Research conducted on {datetime.now().strftime('%Y-%m-%d')}*\n"

        return outline

    def save_to_json(self, filename: Optional[str] = None) -> str:
        """Save research results to JSON file."""
        if not filename:
            filename = f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Saved to: {filepath}")
        return filepath

    def save_to_markdown(self, research_data: Dict, filename: Optional[str] = None) -> str:
        """Save research as a markdown file."""
        if not filename:
            topic_slug = re.sub(r'[^a-z0-9]+', '_', research_data['topic'].lower())
            filename = f"research_{topic_slug}_{datetime.now().strftime('%Y%m%d')}.md"

        filepath = os.path.join(self.output_dir, filename)

        content = f"# {research_data['topic']} - Research Report\n\n"
        content += f"*Research Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
        content += "---\n\n"

        content += "## Blog Post Ideas\n\n"
        for i, idea in enumerate(self.generate_blog_ideas(research_data), 1):
            content += f"{i}. {idea}\n"

        content += "\n## Content Outline\n\n"
        content += self.create_content_outline(research_data['topic'], research_data)

        content += "\n\n## Search Results Summary\n\n"
        for i, result in enumerate(research_data['search_results'], 1):
            content += f"### {i}. {result['title']}\n"
            content += f"**URL:** {result['url']}\n\n"
            if result['snippet']:
                content += f"{result['snippet']}\n\n"
            content += "---\n\n"

        if research_data['articles']:
            content += "\n## Detailed Article Analysis\n\n"
            for i, article in enumerate(research_data['articles'], 1):
                content += f"### Article {i}: {article['title']}\n\n"
                content += f"**Word Count:** {article['word_count']}\n\n"
                content += f"**Description:** {article['description']}\n\n"
                content += f"**Content Preview:**\n{article['content'][:500]}...\n\n"
                content += "---\n\n"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"📝 Saved markdown to: {filepath}")
        return filepath

    def daily_ai_digest(self, num_topics: int = 3) -> Dict:
        """
        Create a daily digest of AI topics.

        Args:
            num_topics: Number of topics to research

        Returns:
            Digest data
        """
        print("\n" + "="*60)
        print("DAILY AI RESEARCH DIGEST")
        print("="*60)

        trending_topics = self.get_trending_ai_topics()[:num_topics]
        digest = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'topics': []
        }

        for topic in trending_topics:
            research = self.research_topic(topic, depth=5)
            digest['topics'].append(research)

            # Save individual markdown file
            self.save_to_markdown(research)

            time.sleep(3)  # Be polite to servers

        # Save complete digest
        self.save_to_json(f"daily_digest_{datetime.now().strftime('%Y%m%d')}.json")

        return digest

    def generate_summary_report(self) -> str:
        """Generate a summary report of all research."""
        report = f"# AI Research Summary Report\n\n"
        report += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
        report += f"**Total Topics Researched:** {len(self.results)}\n\n"

        report += "## Topics Covered:\n\n"
        for i, result in enumerate(self.results, 1):
            report += f"{i}. **{result['topic']}** - {result['num_sources']} sources\n"

        report += "\n## Quick Stats:\n\n"
        total_sources = sum(r['num_sources'] for r in self.results)
        total_articles = sum(len(r['articles']) for r in self.results)

        report += f"- Total Sources Found: {total_sources}\n"
        report += f"- Total Articles Scraped: {total_articles}\n"

        return report


def main():
    """Main function to demonstrate the AI Research Tool."""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         AI Research Tool for Blog Content                 ║
    ║              Medium Daily Updates                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    # Initialize the tool
    tool = AIResearchTool()

    while True:
        print("\n" + "="*60)
        print("MENU:")
        print("1. Research a specific AI topic")
        print("2. Daily AI digest (3 topics)")
        print("3. Research multiple topics")
        print("4. Generate summary report")
        print("5. Exit")
        print("="*60)

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            topic = input("\nEnter AI topic to research: ").strip()
            if topic:
                research = tool.research_topic(topic, depth=7)
                tool.save_to_markdown(research)
                tool.save_to_json()

                print("\n✅ Research complete!")
                print(f"📊 Found {len(research['search_results'])} sources")
                print(f"📄 Scraped {len(research['articles'])} articles")

        elif choice == '2':
            digest = tool.daily_ai_digest(num_topics=3)
            print(f"\n✅ Daily digest complete! Researched {len(digest['topics'])} topics")

        elif choice == '3':
            topics_input = input("\nEnter topics separated by commas: ").strip()
            topics = [t.strip() for t in topics_input.split(',') if t.strip()]

            for topic in topics:
                research = tool.research_topic(topic, depth=5)
                tool.save_to_markdown(research)
                time.sleep(2)

            tool.save_to_json()
            print(f"\n✅ Researched {len(topics)} topics!")

        elif choice == '4':
            if tool.results:
                report = tool.generate_summary_report()
                print("\n" + report)

                # Save report
                report_file = os.path.join(tool.output_dir,
                                          f"summary_{datetime.now().strftime('%Y%m%d')}.md")
                with open(report_file, 'w') as f:
                    f.write(report)
                print(f"\n💾 Report saved to: {report_file}")
            else:
                print("\n⚠ No research data available. Please research some topics first.")

        elif choice == '5':
            print("\n👋 Thank you for using AI Research Tool!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
