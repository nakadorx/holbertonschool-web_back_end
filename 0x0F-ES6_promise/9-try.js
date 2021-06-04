export default function guardrail(mathFunction) {
  const lists = [];

  try {
    lists.push(mathFunction());
  } catch (err) {
    lists.push(err.toString());
  } finally {
    lists.push("Guardrail was processed");
  }
  return lists;
}
