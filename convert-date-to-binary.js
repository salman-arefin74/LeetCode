var convertDateToBinary = function(date) {
    let dateParts = date.split('-');
    let year = Number(dateParts[0]).toString(2);
    let month = Number(dateParts[1]).toString(2);
    let day = Number(dateParts[2]).toString(2);

    return year + '-' + month + '-' + day;
};
