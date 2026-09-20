"""Calculate an average grade from command-line scores."""

import argparse


def average_grade(scores: list[float]) -> float:
    if not scores:
        raise ValueError("at least one score is required")
    if any(score < 0 or score > 100 for score in scores):
        raise ValueError("scores must be between 0 and 100")
    return sum(scores) / len(scores)


def letter_grade(average: float) -> str:
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate a student's average grade")
    parser.add_argument("scores", nargs="+", type=float, help="scores from 0 to 100")
    args = parser.parse_args()

    try:
        average = average_grade(args.scores)
    except ValueError as exc:
        parser.error(str(exc))

    print(f"Average: {average:.1f} | Grade: {letter_grade(average)}")


if __name__ == "__main__":
    main()
