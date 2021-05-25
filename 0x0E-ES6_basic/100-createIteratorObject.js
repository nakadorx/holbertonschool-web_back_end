export default function createIteratorObject(report) {
  let listt = [];

  listt = {
    *[Symbol.listt]() {
      for (const value of Object.values(report.allEmployees)) {
        for (const i of value) {
          yield i;
        }
      }
    },
  };

  return listt;
}
