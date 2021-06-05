export default function updateUniqueItems(map) {
  if (map.constructor !== Map) throw new Error('Cannot process');
  for (const pair of map) {
    const val = pair[1];
    const key = pair[0];
    if (val === 1) map.set(key, 100);
  }
  return map;
}
