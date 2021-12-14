#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  const myList = [];
  for (let i = len; i >= 0; i--) {
    myList.push(list[i]);
  }
  return (myList);
};
