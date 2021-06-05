export default function getStudentIdsSum(arr) {
  return arr.reduce((a, d) => a + d.id, 0);
}
