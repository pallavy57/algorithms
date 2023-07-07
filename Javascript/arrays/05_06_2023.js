function getMinEle(arr) {
    var baseIndex = arr[0]
    var baseIndexx = 0
    for (let index = 1; index < arr.length; index++) {
        if (arr[index] < baseIndex) {
            baseIndex = arr[index]
            baseIndexx = index
        }

    }
    return baseIndexx
}

function checkifsortedrotated(arr) {
    const minEle = getMinEle(arr)
    var flag = false
    var flag2 = false
    for (let index = 0; index < minEle; index++) {
        if (arr[index] < arr[index + 1]) {
            flag = true
        }
    }

    for (let index2 = minEle; index2 < arr.length; index2++) {
        if (arr[index2] < arr[index2 + 1]) {
            flag2 = true
        }
    }

    if (flag && flag2 && arr[arr.length - 1] < arr[minEle - 1]) {
        return true
    } else {
        return false
    }

}




array = [3, 4, 5, 2, 1]
console.log(checkifsortedrotated(array))