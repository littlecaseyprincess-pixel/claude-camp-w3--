import json
import pandas as pd


def main():
    df = pd.read_csv("students.csv")

    total_students = len(df)
    country_counts = df["country"].value_counts().to_dict()
    completion_rate = (df["bet_status"] == "completed").mean()
    completion_rate = round(completion_rate, 2)

    report = {
        "total_students": total_students,
        "country_counts": country_counts,
        "completion_rate": completion_rate
    }

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)

    print("统计完成，结果已保存到 report.json")


if __name__ == "__main__":
    main()