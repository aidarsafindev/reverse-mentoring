"""
Планировщик сессий обратного менторства.

Генерирует расписание на месяц: кто кого учит и какой теме.
"""

import random

# Команда
TEAM = {
    "juniors": [
        {"name": "Анна", "topics": ["Docker", "gRPC", "AI-ассистенты"]},
        {"name": "Борис", "topics": ["Kubernetes", "GitOps", "eBPF"]},
        {"name": "Виктор", "topics": ["ClickHouse", "Grafana", "Python"]},
    ],
    "leads": [
        {"name": "Дмитрий", "interests": ["контейнеризация", "мониторинг"]},
        {"name": "Елена", "interests": ["интеграции", "базы данных"]},
    ],
}

WEEKS = ["Неделя 1", "Неделя 2", "Неделя 3", "Неделя 4"]


def generate_schedule():
    """Генерирует расписание на месяц."""
    schedule = []

    for week in WEEKS:
        junior = random.choice(TEAM["juniors"])
        lead = random.choice(TEAM["leads"])

        # Выбираем тему которая интересна лиду
        matching_topics = [
            t for t in junior["topics"]
            if any(interest in t.lower() for interest in lead["interests"])
        ]
        topic = random.choice(matching_topics) if matching_topics else random.choice(junior["topics"])

        schedule.append({
            "week": week,
            "junior": junior["name"],
            "lead": lead["name"],
            "topic": topic,
            "duration": "30 минут",
            "format": "демонстрация + практика",
        })

    return schedule


def print_schedule(schedule):
    """Выводит расписание."""
    print("=" * 70)
    print("РАСПИСАНИЕ ОБРАТНОГО МЕНТОРСТВА НА МЕСЯЦ")
    print("=" * 70)
    for session in schedule:
        print(f"\n{session['week']}:")
        print(f"  Ментор: {session['junior']} (junior)")
        print(f"  Ученик: {session['lead']} (тимлид)")
        print(f"  Тема: {session['topic']}")
        print(f"  Формат: {session['format']}, {session['duration']}")


if __name__ == "__main__":
    schedule = generate_schedule()
    print_schedule(schedule)
