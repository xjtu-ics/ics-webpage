import json
import argparse
from datetime import datetime, timedelta

# 生成单个事件
def generate_single_event(title, start_time_str, end_time_str, teacher, location, theme):
    event = {
        "title": title,
        "start": start_time_str,
        "end": end_time_str,
        "extendedProps": {
            "teacher": teacher,
            "theme": theme,
            "pptLink": "",
            "location": location
        }
    }
    return event

# 生成课程事件的函数
def generate_course_events(start_date, end_date, location, weeks):
    events = []
    start_date_1 = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_1 = datetime(2025, 4, 30)
    start_date_2 = datetime(2025, 5, 1)
    end_date_2 = datetime.strptime(end_date, '%Y-%m-%d')
    weeks = [i - 1 for i in weeks]
    # 2025年5月1日之前的课程
    current_date = start_date_1
    while current_date <= end_date_1:
        if current_date.weekday() in weeks:  # 1 代表周二，3 代表周四
            event = {
                "title": "Lecture",
                "start": current_date.replace(hour=19, minute=40).strftime("%Y-%m-%dT%H:%M:%S"),
                "end": current_date.replace(hour=21, minute=30).strftime("%Y-%m-%dT%H:%M:%S"),
                "extendedProps": {
                    "teacher": "",
                    "theme": "",
                    "pptLink": "",
                    "location": location,
                }
            }
            events.append(event)
        current_date += timedelta(days=1)

    # 2025年5月1日之后的课程
    current_date = start_date_2
    while current_date <= end_date_2:
        if current_date.weekday() in weeks:  # 1 代表周二，3 代表周四
            event = {
                "title": "Lecture",
                "start": current_date.replace(hour=19, minute=10).strftime("%Y-%m-%dT%H:%M:%S"),
                "end": current_date.replace(hour=21, minute=0).strftime("%Y-%m-%dT%H:%M:%S"),
                "extendedProps": {
                    "teacher": "",
                    "theme": "",
                    "pptLink": "",
                    "location": location,
                }
            }
            events.append(event)
        current_date += timedelta(days=1)

    return events

def main():
    parser = argparse.ArgumentParser(description='Generate and add lecture events to a JSON file')

    # 添加 --mode 参数
    parser.add_argument('--mode', choices=['g', 'a'], required=True,
                        help='Mode: "g" for generating events by week, "a" for adding a single event')

    # 添加目标 JSON 文件路径参数
    parser.add_argument('--json', type=str, help='Path to the target JSON file')

    # 根据 --mode 的值添加不同的参数组
    group_g = parser.add_argument_group('Mode "g" arguments')
    group_a = parser.add_argument_group('Mode "a" arguments')

    group_g.add_argument('--start_date', type=str, help='Start date (YYYY-MM-DD)')
    group_g.add_argument('--end_date', type=str, help='End date (YYYY-MM-DD)')
    group_g.add_argument('--location', type=str, help='Location of the events')
    group_g.add_argument('--weeks', nargs='+', type=int, help='List of week numbers')

    group_a.add_argument('--title', type=str, help='Title of the event')
    group_a.add_argument('--start_time', type=str, help='Start time (YYYY-MM-DDTHH:MM:SS)')
    group_a.add_argument('--end_time', type=str, help='End time (YYYY-MM-DDTHH:MM:SS)')
    group_a.add_argument('--teacher', type=str, help='Teacher of the event')
    group_a.add_argument('--loc', type=str, help='Location of the event')
    group_a.add_argument('--theme', type=str, help='Theme of the event')

    args = parser.parse_args()
    existing_events = []
    try:
        # 尝试读取现有的 JSON 文件内容
        if args.mode == 'a':
            with open(args.json, 'r', encoding='utf-8') as f:
                existing_events = json.load(f)
    except FileNotFoundError:
        # 如果文件不存在，初始化一个空列表
        existing_events = []
    except json.JSONDecodeError:
        # 如果文件内容不是有效的 JSON 格式，初始化一个空列表
        existing_events = []

    if args.mode == 'g':
        if not all([args.start_date, args.end_date, args.location, args.weeks]):
            parser.error('For mode "g", --start_date, --end_date, --location and --weeks are required.')
        new_events = generate_course_events(args.start_date, args.end_date, args.location, args.weeks)
        existing_events.extend(new_events)
    elif args.mode == 'a':
        if not all([args.title, args.start_time, args.end_time, args.teacher, args.location, args.theme]):
            parser.error('For mode "a", --title, --start_time, --end_time, --teacher, --location and --theme are required.')
        new_event = generate_single_event(args.title, args.start_time, args.end_time, args.teacher, args.location,
                                          args.theme)
        existing_events.append(new_event)

    # 将更新后的事件列表写回 JSON 文件
    with open(args.json, 'w', encoding='utf-8') as f:
        json.dump(existing_events, f, ensure_ascii=False, indent=4)

    print(f"Events have been successfully updated in {args.json}")

if __name__ == "__main__":
    main()