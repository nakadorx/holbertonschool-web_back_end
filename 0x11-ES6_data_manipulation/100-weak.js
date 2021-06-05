export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const acc = weakMap.get(endpoint) + 1;
    weakMap.set(endpoint, acc);
  } else {
    weakMap.set(endpoint, 1);
  }
  if (weakMap.get(endpoint) >= 5) throw new Error('Endpoint load is high');
}
