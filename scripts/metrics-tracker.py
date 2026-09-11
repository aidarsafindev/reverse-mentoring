"""
Трекер метрик обратного менторства.

Позволяет записывать сессии и считать метрики эффективности.
"""

import csv
import os
from datetime import datetime

METRICS_FILE = "metrics/template.csv"


def init_metrics_file():
    """Создаёт файл метрик если его нет."""
    if not os.path.exists(METRICS_FILE):
        os.makedirs(os.path.dirname(METRICS_FILE), exist_ok=True)
        with open(METRICS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date", "junior", "lead", "topic",
                "status", "implemented", "savings_hours",
                "lead_satisfaction", "junior_satisfaction",
            ])


def add_session(
    junior: str,
    lead: str,
    topic: str,
    status: str,
    implemented: bool = False,
    savings_hours: float = 0,
    lead_satisfaction: int = 0,
    junior_satisfaction: int = 0,
):
    """Добавляет запись о сессии."""
    init_metrics_file()
    with open(METRICS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            junior,
            lead,
            topic,
            status,
            "yes" if implemented else "no",
            savings_hours,
            lead_satisfaction,
            junior_satisfaction,
        ])
    print(f"Сессия записана: {junior} -> {lead}, тема: {topic}")


def print_metrics():
    """Выводит сводку метрик."""
    if not os.path.exists(METRICS_FILE):
        print("Нет данных. Добавьте сессии через add_session().")
        return

    with open(METRICS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("Нет данных.")
        return

    total = len(rows)
    implemented = sum(1 for r in rows if r["implemented"] == "yes")
    savings = sum(float(r["savings_hours"] or 0) for r in rows)
    lead_sat = [int(r["lead_satisfaction"]) for r in rows if r["lead_satisfaction"]]
    junior_sat = [int(r["junior_satisfaction"]) for r in rows if r["junior_satisfaction"]]

    print("=" * 60)
    print("МЕТРИКИ ОБРАТНОГО МЕНТОРСТВА")
    print("=" * 60)
    print(f"Всего сессий: {total}")
    print(f"Внедрено идей: {implemented} ({implemented * 100 // total}%)")
    print(f"Экономия: {savings} часов")
    if lead_sat:
        print(f"Удовлетворённость тимлидов: {sum(lead_sat) / len(lead_sat):.1f}/5")
    if junior_sat:
        print(f"Удовлетворённость джунов: {sum(junior_sat) / len(junior_sat):.1f}/5")


if __name__ == "__main__":
    add_session(
        junior="Анна",
        lead="Дмитрий",
        topic="Docker для тестовых сред",
        status="implemented",
        implemented=True,
        savings_hours=300,
        lead_satisfaction=5,
        junior_satisfaction=5,
    )
    print_metrics()
