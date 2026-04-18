#!/usr/bin/env python3
"""
awesome-android-cli -- Browse awesome-android-customization from terminal
"""
import json, subprocess, sys, argparse, os
from urllib.request import urlopen

TOOLS_JSON = "https://raw.githubusercontent.com/OutrageousStorm/awesome-android-customization/main/tools.json"

def fetch_tools():
    try:
        with urlopen(TOOLS_JSON, timeout=5) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"Error fetching tools: {e}")
        return []

def search(query, tools):
    results = []
    q = query.lower()
    for tool in tools:
        if q in tool.get('name', '').lower() or q in tool.get('description', '').lower():
            results.append(tool)
    return results

def show_tool(tool):
    print(f"\n{'='*60}")
    print(f"{tool.get('name', 'Unknown')}")
    print(f"{'='*60}")
    print(f"Category: {tool.get('category', 'N/A')}")
    print(f"Description: {tool.get('description', 'N/A')}")
    if tool.get('link'):
        print(f"Link: {tool['link']}")
    if tool.get('rating'):
        print(f"Rating: {'⭐' * tool.get('rating', 0)}")
    print()

def main():
    parser = argparse.ArgumentParser(description="awesome-android-customization CLI")
    subparsers = parser.add_subparsers(dest='command')

    sp_search = subparsers.add_parser('search', help='Search tools')
    sp_search.add_argument('query', help='Search term')
    sp_search.add_argument('-c', '--category', help='Filter by category')

    sp_show = subparsers.add_parser('show', help='Show tool details')
    sp_show.add_argument('name', help='Tool name')

    sp_list = subparsers.add_parser('list', help='List all tools')
    sp_list.add_argument('-c', '--category', help='Filter by category')

    args = parser.parse_args()

    print("Loading awesome-android tools...")
    tools = fetch_tools()
    print(f"Found {len(tools)} tools\n")

    if not args.command:
        parser.print_help()
        return

    if args.command == 'search':
        results = search(args.query, tools)
        if not results:
            print(f"No tools matching '{args.query}'")
        for tool in results:
            print(f"  {tool.get('name'):<30} {tool.get('description', '')[:50]}")

    elif args.command == 'show':
        matches = search(args.name, tools)
        if matches:
            show_tool(matches[0])
        else:
            print(f"Tool not found: {args.name}")

    elif args.command == 'list':
        for tool in sorted(tools, key=lambda t: t.get('name', '')):
            if args.category and args.category.lower() not in tool.get('category', '').lower():
                continue
            print(f"  {tool.get('name'):<30} [{tool.get('category', 'other')}]")

if __name__ == "__main__":
    main()
