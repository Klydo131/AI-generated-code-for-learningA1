#!/bin/bash
# Launcher script for Optimistic Future Research Tool

clear
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║   Optimistic Future Research Tool - Launcher                  ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Choose how to run the tool:"
echo ""
echo "  1. Interactive Research Tool (Main App)"
echo "  2. Example Demonstrations"
echo "  3. Quick Test"
echo "  4. Exit"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Starting Interactive Research Tool..."
        echo ""
        python3 optimistic_future_research_tool.py
        ;;
    2)
        echo ""
        echo "Starting Examples..."
        echo ""
        python3 optimistic_research_examples.py
        ;;
    3)
        echo ""
        echo "Running Quick Test..."
        echo ""
        python3 quick_test.py
        ;;
    4)
        echo ""
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo ""
        echo "Invalid choice. Please run again and choose 1-4."
        exit 1
        ;;
esac
