function addCommas(number) {
    if (typeof number !== 'number') return `${number} is not a num!`;
    const numArr = Array.from(String(number));
    let negRemoved = false;
    let decimalRemoved = null;
    // handle negatives
    if (numArr[0] === '-') {
        numArr.shift()
        negRemoved = true;
    }

    // handle decimals
    for (let i = 0; i < numArr.length; i++) {
        if (numArr[i] === '.') {
            decimalRemoved = numArr.splice(i, numArr.length - i)
        }
    }

    let posistionsFromRight = 0
    for (let i = numArr.length - 1; i >= 0; i--) {
        posistionsFromRight++;
        if (numArr[i] === '.') {
            decimalRemoved = numArr.splice(i,)
        }
        if (posistionsFromRight % 3 === 0 && i !== 0) {
            numArr.splice(i, 0, ',')
        }
    }

    if (negRemoved) numArr.unshift('-')
    if (decimalRemoved) {
        const joinedArr = numArr.concat(decimalRemoved)
        return joinedArr.join('')
    } 
    return numArr.join('')
}

module.exports = addCommas;