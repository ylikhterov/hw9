import argparse
import json
from typing import Any, Dict, List, Tuple, Union, Final

def add(args: argparse.Namespace) -> None:
    with open('todo.json', 'r') as f:
        data: List[Dict[str, Union[str, bool]]] = json.load(f)
    data.append({'title': args.title, 'description': args.description, 'done': False})
    with open('todo.json', 'w') as f:
        json.dump(data, f)

def show(args: argparse.Namespace) -> None:
    with open('todo.json', 'r') as f:
        data: List[Dict[str, Union[str, bool]]] = json.load(f)
    for i in range(min(args.count, len(data))):
        print(f"{i+1}. {data[i]['title']}: {data[i]['description']}")

def done(args: argparse.Namespace) -> None:
    with open('todo.json', 'r') as f:
        data: List[Dict[str, Union[str, bool]]] = json.load(f)
    data[args.index-1]['done'] = True
    with open('todo.json', 'w') as f:
        json.dump(data, f)

def find(args: argparse.Namespace) -> None:
    with open('todo.json', 'r') as f:
        data: List[Dict[str, Union[str, bool]]] = json.load(f)
    for i in range(len(data)):
        if args.text in data[i]['title'] or args.text in data[i]['description']:
            print(f"{i+1}. {data[i]['title']}: {data[i]['description']}")

def main() -> None:

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Todo list manager')

    #parser.add_argument('command', choices=['add', 'show', 'done', 'find'], help='Command to execute')
    subparsers: argparse._SubParsersAction = parser.add_subparsers()

    add_parser: argparse.ArgumentParser = subparsers.add_parser('add', help='Add a new todo item')
    add_parser.add_argument('title', help='Title of the todo item')
    add_parser.add_argument('description', help='Description of the todo item')
    add_parser.set_defaults(func=add)

    show_parser: argparse.ArgumentParser = subparsers.add_parser('show', help='Show the todo list')
    show_parser.add_argument('count', type=int, default=5, nargs='?', help='Number of items to show')
    show_parser.set_defaults(func=show)

    done_parser: argparse.ArgumentParser = subparsers.add_parser('done', help='Mark a todo item as done')
    done_parser.add_argument('index', type=int, help='Index of the todo item to mark as done')
    done_parser.set_defaults(func=done)

    find_parser: argparse.ArgumentParser = subparsers.add_parser('find', help='Find a todo item by text')
    find_parser.add_argument('text', help='Text to search for')
    find_parser.set_defaults(func=find)

    args: argparse.Namespace = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()