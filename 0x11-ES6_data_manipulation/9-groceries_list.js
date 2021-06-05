export default function groceriesList() {
  const groc = new Map();
  const arr = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  for (const x of arr) groc.set(x[0], x[1]);
  return groc;
}
