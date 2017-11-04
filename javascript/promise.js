'use strict';

// Promiseで遅延して取得される関数の結果を使って (((1 + 2) * 3) - 4) = 5 を求める

// const f1 = () => new Promise((resolve, reject) => {
//   setTimeout(() => resolve(1), 1000);
// });


async function f1() {
  setTimeout(() => 1, 10000);

}

const f2 = () => new Promise((resolve, reject) => {
  setTimeout(() => resolve(2), 1000);
});

const f3 = () => new Promise((resolve, reject) => {
  setTimeout(() => resolve(3), 1000);
});

const f4 = () => new Promise((resolve, reject) => {
  setTimeout(() => resolve(4), 1000);
});

// 合成する関数の実装
const getAnswer = async () => (await f1() + await f2()) * await f3() - await f4();

getAnswer().then((a) => console.log(a)).catch((e) => console.error(e)); // 5
