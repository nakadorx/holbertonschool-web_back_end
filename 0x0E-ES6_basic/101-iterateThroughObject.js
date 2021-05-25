export default function iterateThroughObject(reportWithIterator) {
  const listt = [];
  for (const index of reportWithIterator) listt.push(index);
  return listt.join(' | ');
}
