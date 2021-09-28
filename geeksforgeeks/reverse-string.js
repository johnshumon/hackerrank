
function reverse_str(str) {
    // String sanity check
    if(!str || str.length < 2) {
        return;
    }

    // Take empty array revArray
    const reverseStrArr = [];
    const length = str.length - 1;

    // Loop through the entire string
    for(let i = length; i >= 0; i--) {
        reverseStrArr.push(str[i]);
    }

    // Join the array elements
    return reverseStrArr.join('');
}
