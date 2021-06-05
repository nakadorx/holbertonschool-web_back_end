export default function getStudentsByLocation(arr, city) {
  return arr.filter((ct) => ct.location === city);
}
