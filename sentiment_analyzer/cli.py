import argparse
import json
from pathlib import Path

from sentiment_analyzer.analyzer import StudentTextSentimentAnalyzer


def main():
    parser = argparse.ArgumentParser(
        description="Student Text Sentiment Analyzer"
    )
    parser.add_argument(
        "--text",
        type=str,
        help="Text to analyze (wrap in quotes)"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Path to a UTF-8 text file to analyze"
    )
    parser.add_argument(
        "--json-out",
        type=str,
        help="Optional path to save result as JSON"
    )

    args = parser.parse_args()

    # 입력 검증
    if (args.text is None) == (args.file is None):
        print("Error: use exactly one of --text or --file")
        return

    # 텍스트 읽기
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")
    else:
        text = args.text

    analyzer = StudentTextSentimentAnalyzer()
    result = analyzer.analyze(text)

    # 콘솔 출력
    print(f"Label: {result['label']}")
    print(f"Score: {result['score']:.4f}")

    # JSON 저장 옵션
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(result, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"Saved JSON to {args.json_out}")


if __name__ == "__main__":
    main()
