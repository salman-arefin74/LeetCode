var titleToNumber = function(columnTitle) {
  let out = 0, len = columnTitle.length;
  for (pos = 0; pos < len; pos++) {
    out += (columnTitle.charCodeAt(pos) - 64) * Math.pow(26, len - pos - 1);
  }
  return out;
};