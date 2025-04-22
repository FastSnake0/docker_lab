import sys
import collections

def main():
    text = sys.stdin.read()
    words = text.lower().split()
    freq = collections.Counter(words)
    for word, count in freq.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()