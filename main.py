import os

LINE = "This morning the neighbor's orange cat, usually far too aloof for anyone, fell asleep on my flip-flops, so I left for work wearing one blue sandal and one green one."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

def verify():
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    assert text.strip(), "entry.txt is empty"
    assert len(text) <= 200, "entry.txt exceeds 200 characters"

if __name__ == "__main__":
    main()
    verify()
