from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# -------- Sorting Algorithms -------- #

def bubble_sort(arr):
    a = arr.copy()
    start = time.time()

    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return time.time() - start


def merge_sort(arr):
    start = time.time()

    def merge_sort_recursive(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = merge_sort_recursive(a[:mid])
        right = merge_sort_recursive(a[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    merge_sort_recursive(arr.copy())
    return time.time() - start


def quick_sort(arr):
    start = time.time()

    def quick_sort_recursive(a):
        if len(a) <= 1:
            return a
        pivot = a[len(a) // 2]
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

    quick_sort_recursive(arr.copy())
    return time.time() - start


# -------- Routes -------- #

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sort', methods=['POST'])
def sort():
    try:
        input_numbers = request.json['numbers']
        data = [int(x.strip()) for x in input_numbers.split(',')]
    except:
        return jsonify({"error": "Invalid input! Use format: 5,2,9,1"})

    results = {
        "bubble": bubble_sort(data),
        "merge": merge_sort(data),
        "quick": quick_sort(data)
    }

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)