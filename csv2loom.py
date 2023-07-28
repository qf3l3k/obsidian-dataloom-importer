import csv
import json
import uuid
import time
import argparse
import os


def csv_to_json(csv_file):
    print(f"Reading CSV file: {csv_file}")
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)
        data = list(reader)

    print("Translating to LOOM format...")
    model = {
        "columns": [],
        "headerRows": [{"id": str(uuid.uuid4())}],
        "bodyRows": [],
        "headerCells": [],
        "bodyCells": [],
        "footerRows": [{"id": str(uuid.uuid4()) for _ in range(2)}],
        "footerCells": [],
        "filterRules": []
    }

    for i, column in enumerate(columns):
        column_id = str(uuid.uuid4())
        model["columns"].append({
            "id": column_id,
            "sortDir": "default",
            "isVisible": True,
            "width": "140px",
            "type": "text",
            "currencyType": "USD",
            "dateFormat": "mm/dd/yyyy",
            "shouldWrapOverflow": True,
            "tags": [],
            "calculationType": "none",
            "aspectRatio": "unset",
            "horizontalPadding": "unset",
            "verticalPadding": "unset"
        })
        model["headerCells"].append({
            "id": str(uuid.uuid4()),
            "columnId": column_id,
            "rowId": model["headerRows"][0]["id"],
            "markdown": column
        })

    for i, row in enumerate(data):
        row_id = str(uuid.uuid4())
        model["bodyRows"].append({
            "id": row_id,
            "index": i,
            "creationTime": int(time.time() * 1000),
            "lastEditedTime": int(time.time() * 1000)
        })
        for j, cell in enumerate(row):
            model["bodyCells"].append({
                "id": str(uuid.uuid4()),
                "isExternalLink": False,
                "columnId": model["columns"][j]["id"],
                "rowId": row_id,
                "dateTime": None,
                "markdown": cell,
                "tagIds": []
            })

    for i, row_id in enumerate(model["footerRows"]):
        for column in model["columns"]:
            model["footerCells"].append({
                "id": str(uuid.uuid4()),
                "columnId": column["id"],
                "rowId": row_id["id"]
            })

    print("Translation complete.")
    return {"model": model, "pluginVersion": "8.0.0"}


def main():
    parser = argparse.ArgumentParser(description='Convert a CSV file to a LOOM file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input CSV file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output JSON file')
    args = parser.parse_args()

    json_data = csv_to_json(args.input)

    # Check if output file has extension
    filename, file_extension = os.path.splitext(args.output)

    # If not, add .loom extension
    if file_extension == "":
        filename += ".loom"
    else:
        filename += file_extension

    print(f"Writing to output file: {filename}")
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Operation completed successfully.")


if __name__ == "__main__":
    main()
