export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw new Error('Position outside range');
  const bf = new ArrayBuffer(length);
  const lists = new DataView(bf, 0);
  lists.setInt8(position, value);
  return lists;
}
