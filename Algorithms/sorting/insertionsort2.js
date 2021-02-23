//Problem:
//https://www.hackerrank.com/challenges/insertionsort2/
//score: 30


//--------------------------------------------------------------
//Solution:
function insertionSort2(n, arr) {
    let i = 1;
    while (i < n) {
        let x = arr[i]
        let j = i - 1
        while (j >= 0 && arr[j] > x) {
            arr[j + 1] = arr[j]
            j--
        }
        arr[j + 1] = x
        i++
        console.log(...arr)
    }
}


