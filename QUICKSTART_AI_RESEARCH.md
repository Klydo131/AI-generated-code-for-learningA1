# Quick Start Guide - AI Research Tool

Get started with the AI Research Tool in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements_ai_research.txt
```

Or install manually:
```bash
pip install requests beautifulsoup4 lxml html5lib
```

## Step 2: Run Your First Research

### Option A: Interactive Mode (Recommended for beginners)

```bash
python3 AI_Research_Tool.py
```

Then select option 1 and enter a topic like "ChatGPT"

### Option B: Quick Example

```bash
python3 example_usage.py
```

Choose example 1 for a simple demonstration.

### Option C: Direct Python Code

Create a file `my_research.py`:

```python
from AI_Research_Tool import AIResearchTool

tool = AIResearchTool()
research = tool.research_topic("Artificial Intelligence", depth=5)
tool.save_to_markdown(research)
tool.save_to_json()
```

Run it:
```bash
python3 my_research.py
```

## Step 3: Check Your Results

All output files are saved in `research_output/` directory:

```bash
ls research_output/
```

You'll see:
- `.md` files - Ready for Medium blog posts!
- `.json` files - Complete research data

## Step 4: Daily Automation

For daily Medium updates, use the automation script:

```bash
# Research 3 trending topics
python3 daily_ai_research.py

# Research 5 topics with deeper analysis
python3 daily_ai_research.py --topics 5 --depth 7

# Research custom topics
python3 daily_ai_research.py --custom "GPT-4,AI Ethics,Robotics"
```

## Common Commands

| Command | Description |
|---------|-------------|
| `python3 AI_Research_Tool.py` | Interactive menu |
| `python3 daily_ai_research.py` | Daily digest (3 topics) |
| `python3 example_usage.py` | See examples |
| `python3 daily_ai_research.py --help` | Show all options |

## Next Steps

1. Read the full documentation: `AI_Research_Tool_README.md`
2. Customize trending topics in `AI_Research_Tool.py:86`
3. Set up daily automation (see README)
4. Start writing your Medium blogs!

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'requests'`
**Solution**: Install dependencies (Step 1 above)

**Problem**: No results found
**Solution**: Try different search terms or increase depth

**Problem**: Files not saving
**Solution**: Check permissions in current directory

## Tips for Medium Bloggers

1. Run `daily_ai_research.py` every morning
2. Review generated markdown files
3. Pick the most interesting topic
4. Expand the outline with your insights
5. Publish to Medium!

## File Overview

- `AI_Research_Tool.py` - Main tool (interactive)
- `daily_ai_research.py` - Automation script
- `example_usage.py` - Example demonstrations
- `requirements_ai_research.txt` - Dependencies
- `AI_Research_Tool_README.md` - Full documentation
- `research_output/` - All generated files

---

**Ready to research? Start with:** `python3 AI_Research_Tool.py`
